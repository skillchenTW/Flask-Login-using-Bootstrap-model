

Login Form Using Bootstrap Modal using Python Flask jquery Ajax password hash and session

install psycopg2 https://pypi.org/project/psycopg2/
Psycopg is the most popular PostgreSQL database adapter for the Python programming language.
(venv) PS C:\flaskmyproject> pip install psycopg2

CREATE TABLE admin_login (
	id serial PRIMARY KEY,
	admin_name VARCHAR ( 150 ) NOT NULL,
	admin_password VARCHAR ( 150 ) NOT NULL
);

INSERT INTO
    admin_login(admin_name,admin_password)
VALUES
('admin', '123456');