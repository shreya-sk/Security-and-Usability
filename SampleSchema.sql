drop schema if exists messenger cascade;
create schema messenger;
set search_path to 'messenger';

DROP TABLE IF EXISTS UserAccount CASCADE;
DROP TABLE IF EXISTS ContactType CASCADE;
DROP TABLE IF EXISTS ContactMethod CASCADE;
DROP TABLE IF EXISTS UserProfile CASCADE;
DROP TABLE IF EXISTS Friends CASCADE;

CREATE TABLE UserAccount (
    username VARCHAR(50) unique,
    password VARCHAR(50) NOT NULL,
	user_id integer PRIMARY KEY,
    admin integer DEFAULT 0
   
);

CREATE TABLE ContactType(
    contact_type_id SERIAL PRIMARY KEY,
    contact_type_name VARCHAR(50)
);

CREATE TABLE ContactMethod(
    user_id integer references UserAccount(user_id),
    contact_type_id INTEGER REFERENCES ContactType(contact_type_id),
    contact_type_value VARCHAR(100),
    PRIMARY KEY(user_id, contact_type_id, contact_type_value)
);

CREATE TABLE UserProfile (
     user_id integer UNIQUE PRIMARY KEY NOT NULL REFERENCES UserAccount (user_id),
     first_name varchar(50) UNIQUE,
     last_name varchar(50) UNIQUE,
     bio text

 );


CREATE TABLE Friends (
     username varchar(50) NOT NULL REFERENCES UserAccount(username),
    --  friend_id INTEGER PRIMARY KEY,
     friend_fname varchar(50) references UserProfile(first_name),
     friend_lname varchar(50) references UserProfile(last_name)

 );



-- create or replace function messenger.addFriend(
-- 	location text,
-- 	songdescription text,
-- 	title varchar(250),
-- 	songlength int,
-- 	songgenre text,
--     er int)
-- RETURNS int AS
-- $BODY$
--     SELECT -1;
-- $BODY$
-- LANGUAGE sql;


CREATE OR REPLACE FUNCTION messenger.AddUser(
    username VARCHAR(50),
    password VARCHAR(50),
	 user_id integer,
    admin integer DEFAULT 0
   
    )
RETURNS void AS
$$
    DECLARE
        -- you would have any variables declared here
    BEGIN
    
		INSERT INTO messenger.UserAccount (username, password, user_id, admin) VALUES
        
  			(lower(username), HASHBYTES('SHA2_512', Password), user_id,admin );
    END;
$$
	

LANGUAGE plpgsql;

