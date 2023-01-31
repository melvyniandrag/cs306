-- note this requires sqlite 3.37 or higher
create table rules(
	a INT,
	b INTEGER,
	c REAL,
	d TEXT,
	e BLOB, 
	f ANY
) Strict ;

insert into rules values(1, 1, 1.0, "hello", "hello", "hello");
insert into rules values("hello", 1, 1.0, "hello", "hello", "hello");

