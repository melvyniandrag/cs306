CREATE TABLE tab(
	a INT
);

insert into tab values ( 100 );

-- this will not work. The default value in sqlite is null.
-- There is currently one row in the table. This will cause a null to be put in col
-- b for the currently existing row.

-- alter table tab add column b int NOT NULL;

-- To deal with the above issue, we will also add a default value
alter table tab add column b int NOT NULL DEFAULT 0;
