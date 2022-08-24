-- DROP TABLE IF EXISTS emp cascade;
-- DROP TABLE IF EXISTS dept cascade;

DROP TABLE IF EXISTS post cascade;
DROP TABLE IF EXISTS users_fb_clone cascade;


create table users_fb_clone(user_id INT primary key, name VARCHAR);
Insert into users_fb_clone values (100, 'Zelensky'), (200, 'Putin'), (300, 'Biden'), (400, 'Xinping');
create table post(post_id INT primary key, title VARCHAR, description VARCHAR, user_id INT, constraint fk foreign key(user_id) references users_fb_clone(user_id));
Insert into post values (1, 'Russia and Ukraine', 'The war is aggravting and becoming bad.', 200), (2, 'Japanese PM assasinated', 'Shock and mourning in India and Japan.', 300), (3, 'India clinches t20', 'England loses to India in second t20.', 200), (4, 'Taiwan under threat', 'China plans to capture or re-unite.', 400);


-- create table emp (emp_id VARCHAR primary key NOT NULL, emp_name VARCHAR, proj_id VARCHAR);
-- create table proj (proj_id VARCHAR primary key NOT NULL, proj_name VARCHAR, proj_title VARCHAR);
-- create table works (emp_id VARCHAR NOT NULL, proj_id VARCHAR NOT NULL, duration INT, primary key(emp_id, proj_id));
