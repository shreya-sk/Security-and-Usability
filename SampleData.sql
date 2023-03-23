begin transaction;

INSERT INTO ContactType VALUES (1, 'email');
INSERT INTO ContactType VALUES (2, 'phone');
INSERT INTO ContactType VALUES (3, 'social');

INSERT INTO UserAccount VALUES ('james.smith', '2KK8oykkvp', 1,0);
INSERT INTO ContactMethod VALUES (1, 1, 'james.smith87@testing.com.au');
INSERT INTO ContactMethod VALUES (1, 2, '0498855580');

INSERT INTO UserAccount VALUES ('robert.jones', 'yA3Z6cYV5', 2,0);
INSERT INTO ContactMethod VALUES (2, 1, 'robert.jones81@test.com');
INSERT INTO ContactMethod VALUES (2, 2, '0446029367');

INSERT INTO UserAccount VALUES ('william.johnson', 'M8jL283RI', 3,0);
INSERT INTO ContactMethod VALUES (3, 1, 'william.johnson87@example.net.au');
INSERT INTO ContactMethod VALUES (3, 2, '0420784051');

INSERT INTO UserAccount VALUES ('michael.miller', 'I81jK2L9O', 4,0);
INSERT INTO ContactMethod VALUES (4, 1, 'michael.miller80@example.com');
INSERT INTO ContactMethod VALUES (4, 2, '0424167024');


INSERT INTO UserProfile VALUES (1, 'James', 'Smith');
INSERT INTO UserProfile VALUES (2 , 'Robert', 'Jones');
INSERT INTO UserProfile VALUES (3, 'William', 'Johnson');
INSERT INTO UserProfile VALUES (4, 'Michael', 'Miller');

INSERT INTO Friends VALUES ('james.smith',   'Robert', 'Jones');
INSERT INTO Friends VALUES ('james.smith',   'William', 'Johnson');
INSERT INTO Friends VALUES ('james.smith',    'Michael', 'Miller');

INSERT INTO Friends VALUES ('robert.jones',  'William', 'Johnson');
INSERT INTO Friends VALUES ('robert.jones','Michael', 'Miller');
INSERT INTO Friends VALUES ('robert.jones', 'James', 'Smith');


INSERT INTO Friends VALUES ('michael.miller', 'Robert', 'Jones');
INSERT INTO Friends VALUES ('michael.miller', 'James', 'Smith');


INSERT INTO Friends VALUES ('william.johnson', 'Robert', 'Jones');
INSERT INTO Friends VALUES ('william.johnson',  'James', 'Smith');

commit;

-- 
--
-- drop schema if exists messenger cascade;
-- create schema messenger;
-- set search_path to 'messenger';
--
-- DROP TABLE IF EXISTS UserAccount CASCADE;
-- DROP TABLE IF EXISTS ContactType CASCADE;
-- DROP TABLE IF EXISTS ContactMethod CASCADE;
-- DROP TABLE IF EXISTS UserProfile CASCADE;
-- DROP TABLE IF EXISTS Friends CASCADE;
--
-- CREATE TABLE UserAccount (
--     username VARCHAR(50) PRIMARY KEY,
--     password VARCHAR(72) NOT NULL,
--     isSuper boolean DEFAULT FALSE
-- );
--
-- CREATE TABLE ContactType(
--     contact_type_id SERIAL PRIMARY KEY,
--     contact_type_name VARCHAR(50)
-- );
--
-- CREATE TABLE ContactMethod(
--     username varchar(50) references UserAccount(username),
--     contact_type_id INTEGER REFERENCES ContactType(contact_type_id),
--     contact_type_value VARCHAR(100),
--     PRIMARY KEY(username, contact_type_id, contact_type_value)
-- );
--
-- CREATE TABLE UserProfile (
--     username varchar(50) UNIQUE REFERENCES UserAccount (username),
-- 	user_id INTEGER PRIMARY KEY,
-- 	first_name varchar(50),
--     last_name varchar(50),
--     bio text
--
-- );
--
--
-- CREATE TABLE Friends (
--     username varchar(50) UNIQUE NOT NULL REFERENCES UserAccount (username),
--     friend_id INTEGER NOT NULL REFERENCES UserProfile (user_id),
--     friend_fname varchar(50) references UserProfile(first_name),
--     friend_lname varchar(50) references UserProfile(last_name),
--     PRIMARY KEY (friend_id)
-- );
--
--
--
-- -- create or replace function messenger.addFriend(
-- -- 	location text,
-- -- 	songdescription text,
-- -- 	title varchar(250),
-- -- 	songlength int,
-- -- 	songgenre text,
-- --     er int)
-- -- RETURNS int AS
-- -- $BODY$
-- --     SELECT -1;
-- -- $BODY$
-- -- LANGUAGE sql;
--
--
-- CREATE OR REPLACE FUNCTION messenger.storeSecurePassword(
--     username VARCHAR(50),
--     password VARCHAR(100))
-- RETURNS void AS
-- $$
--     DECLARE
--         -- you would have any variables declared here
--     BEGIN
-- 		INSERT INTO messenger.UserAccount (username, password) VALUES
--   			(lower(username), public.crypt(password, public.gen_salt('bf', 8)));
--     END;
-- $$
-- LANGUAGE plpgsql;
