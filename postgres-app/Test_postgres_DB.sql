DROP TABLE IF EXISTS emp cascade;
DROP TABLE IF EXISTS dept cascade;
/*
create table post(post_id INT primary key, title VARCHAR, description VARCHAR);
create table userrr(user_id INT primary key, name VARCHAR, post_id INT, constraint fk foreign key(post_id) references post(post_id));
Insert into post values (1, 'Russia and Ukraine', 'The war is aggravting and becoming bad.'), (2, 'Japanese PM assasinated', 'Shock and mourning in India and Japan.'), (3, 'India clinches t20', 'England loses to India in second t20.'), (4, 'Taiwan under threat', 'China plans to capture or re-unite.');
Insert into userrr values (100, 'Zelensky', 1), (200, 'Putin', 1), (300, 'Biden', 3), (400, 'Xinping', 4);
*/

create table emp (emp_id VARCHAR primary key NOT NULL, emp_name VARCHAR, proj_id VARCHAR);
create table proj (proj_id VARCHAR primary key NOT NULL, proj_name VARCHAR, proj_title VARCHAR);
create table works (emp_id VARCHAR NOT NULL, proj_id VARCHAR NOT NULL, duration INT, primary key(emp_id, proj_id));

