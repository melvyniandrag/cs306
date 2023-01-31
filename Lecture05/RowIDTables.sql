CREATE TABLE test(
	a INTEGER PRIMARY KEY,
	b TEXT
);

insert into test values (100, "one hundred");
insert into test values (200, "two hundred");

SELECT rowid, * FROM test;

CREATE TABLE test2(
	a INTEGER,
	b TEXT
);

insert into test2 values (100, "one hundred");
insert into test2 values (200, "two hundred");

SELECT ROWID, * FROM TEST2;

CREATE TABLE test3(
      a TEXT PRIMARY KEY,
      b TEXT
);

insert into test3 values ( "a", "b");
insert into test3 values ( "A", "B");

select rowid, * from test3;

