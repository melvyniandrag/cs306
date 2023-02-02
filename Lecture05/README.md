# Lecture 05

## Some useful sqlite3 scripts
A variety of sql scripts that do interesting things.
1. AlterTable.sql - Add a not null column to an existing table. Make sure to provide a DEFAULT value!
2.  RowIDTables.sql - Show that an INTEGER PRIMARY KEY is aliased to the row id of the table. Any other primary key ( e.g. TEXT, INT, FLOAT ) will have a rowid that is distinct from the PRIMARY KEY. Run the script and see that the table with INTEGER PRIMARY KEY has row id == primary key, and the values are 100 and 200. The other table has row ids 1, 2.
3. WeekThreeTables.sql - Show that sqlite3 database columns do not strictly enforce the type. In other words, if you have an INTEGER column you can still insert TEXT into that column. If you have a TEXT column, you can still insert a FLOAT value. CRazy isn't it? Run the script and have a look.
4. affinity_types.sql - Just like the previous script, this script shows that sql does not enforce the column type. You can insert any value into any column. If that's the case - then what's the point of having typed columns anyway?!?! More on that later.
5. Strict.sql - Despite what we just showed in the above two scripts, sqlite3 ( version 3.37+ ) does support STRICT typing - if you're into that sort of thing. Run this script and see that it fails because the values you try to insert do not match the type of the column.

The typing of columns is very interesting and [there is a great write up about it on the sqlite website](https://www.sqlite.org/datatype3.html).

## sqlite3 and C++

This folder contains a short c++ program that uses sqlite3 as a library. Up until now we've been using sqlite3 interactively with the sqlite3 shell, or by passing it SQL scripts. This little program shows you that you can use sqlite3 easily in other languages.
