import psycopg2
from configparser import ConfigParser
import json
import cherrypy
from random import randrange

#connect database from file
# create a parser
parser = ConfigParser()
# read config file
parser.read('database.ini')

# get section, default to postgresql
db = {}
if parser.has_section('postgresql'):
    params = parser.items('postgresql')
    for param in params:
        db[param[0]] = param[1]
    print(db)
else:
    raise Exception('Section {0} not found in the {1} file'.format('postgresql', 'database.ini'))

#establishing connection
# connection = psycopg2.connect(database='post', user='postgres',
#                               password='postgres', host='localhost', port='5432')

connection = psycopg2.connect(**db)

#creating cursor object
cursor = connection.cursor()

#print(f'The connection used by cursor is {cursor.connection}')

# user_input = 11
# post_id = 12
# post_title = 'UK PM resigns'
# post_desc = 'Streak of resignations causes BoJo to resign.'
# #execute insert sql statement
# insrt_stmt = f'insert into post values (%s, %s, %s);'
# insrt_data = (post_id, post_title, post_desc)
# cursor.execute(insrt_stmt, insrt_data)
#
# #commit inserted data into the database
# connection.commit()

#execute select sql query
# sql_query = f'delete from post where post_id = {user_input};'
# sql_query = 'select * from post;'
# cursor.execute(sql_query)
# connection.commit()

#retrieve data after executing the query
# query_output = cursor.fetchall()
#
# print(f'The {cursor.rowcount} rows are returned.')
#
# print(f'The output of query : {sql_query} is ')
#
# for i in range(0, len(query_output)):
#     print(query_output[i])

def convert_to_json(list):
    out = {}
    for index, item in enumerate(list):
        out[index]=item
    return out

BASE_URL = "https://127.0.0.1/"
API_TOKEN = None

# Cherrypy server
class TestServer():
    @cherrypy.expose
    def index(self):
        # templateLoader = jinja2.FileSystemLoader(searchpath="./")
        # templateEnv = jinja2.Environment(loader=templateLoader)
        # TEMPLATE_FILE = "index.html"
        # template = templateEnv.get_template(TEMPLATE_FILE)
        # outputText = template.render()  # this is where to put args to the template renderer
        # return outputText
        return '<html><body>Welcome to FB server.</body></html>'

    @cherrypy.expose
    def get_post(self, id):
        try:
            sql_query = f'select * from post where post_id={id};'
            cursor.execute(sql_query)
            output = cursor.fetchall()
            output = convert_to_json(output)
            return json.dumps(output)
        except Exception as e:
            return cherrypy.HTTPError(e, str(e))

    @cherrypy.expose
    def post_data(self, post):
        # paramss = cherrypy.request.params['post']
        # print(post)
        try:
            post = cherrypy.request.params['post']
            post = json.loads(post)
            post_id = int(post['id'])
            title = post['title']
            description = post['description']
            insrt_stmt = f'insert into post values (%s, %s, %s);'
            insrt_data = (post_id, title, description)
            cursor.execute(insrt_stmt, insrt_data)
            connection.commit()
            # raise Exception("le aye error")
            # cherrypy.response.headers['status_code'] = 200
            # cherrypy.response.headers['status_message'] = 'OK'
            return json.dumps({'response': '200', 'Number of Insertions': cursor.rowcount,
                               'Database Acknoledgement': cursor.statusmessage})
        except Exception as e:
            connection.rollback()
            return cherrypy.HTTPError(e, str(e))

    @cherrypy.expose
    def get_posts(self):
        try:
            sql_query = f'select * from post;'
            cursor.execute(sql_query)
            output = cursor.fetchall()
            output = convert_to_json(output)
            return json.dumps(output)
        except Exception as e:
            return cherrypy.HTTPError(e, str(e))

    @cherrypy.expose
    def delete_post(self, id):
        try:
            sql_query = "delete from post where post_id = %s"
            cursor.execute(sql_query, (id,))
            connection.commit()
            return json.dumps({'response': '200', 'message':'Post deleted successfully.'})
        except Exception as e:
            return cherrypy.HTTPError(e, str(e))

    @cherrypy.expose
    def delete_all(self):
        try:
            sql_query = 'Truncate post;'
            rows = cursor.execute(sql_query)
            if rows is None:
                raise Exception("Operation failed.")
            return json.dumps({'response': 200, 'Result': rows})
        except Exception as e:
            return json.dumps({'response': str(e)})

    def authenticate_me(self):
        try:
            header = cherrypy.request.headers
            if header['Token'] == '123456abcd':
                API_TOKEN = randrange(1000)
                return json.dumps({'response': 200, 'Authentication': header, 'Api Token': API_TOKEN})
            else:
                raise Exception('Http 401 Auth token is invalid.')
        except Exception as e:
            return json.dumps({'response': str(e)})


# cherrypy.config.update({'server.socket_host': '127.0.0.1', 'server.socket_port': 8089})
# cherrypy.quickstart(TestServer(), '/')

#close cursor and connection
# cursor.close()
# connection.close()

if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host':'0.0.0.0','server.socket_port': 8080})
    cherrypy.quickstart(TestServer(), '/')
