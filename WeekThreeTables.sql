--CREATE TABLE experiment(
--	a int,
--	b smallint,
--	c text,
--	d char(5),
--	e varchar(10),
--	f text,
--	g blob
--);

-- READ THIS!
-- https://www.sqlite.org/datatype3.html

CREATE TABLE small_experiment(
	a int,
	b text
);

insert into small_experiment values (x'61', x'61');
insert into small_experiment values (1.66e-9, 1.66e-9);
insert into small_experiment values ("123", "123");
insert into small_experiment values (999, 999);
insert into small_experiment values (9223372036854775807,9223372036854775807);
insert into small_experiment values (9223372036854775808,9223372036854775808);
insert into small_experiment values (1.7976931348623157e+308, 1.7976931348623157e+308);
insert into small_experiment values (1.7976931348623157e+3000, 1.7976931348623157e+3000);

-- interesting stuff! This is the smallest normalized double precision float.
-- but sqlite can go lower!
insert into small_experiment values (2.2251e-308,2.2251e-308);

-- See ! we went lower.
insert into small_experiment values (2.2251e-320, 2.2251e-320);

-- and now THIS is the smallest normalized positive double precision float.
insert into small_experiment values (4.9e-324, 4.9e-324);

--and we cannot go smaller than that.
insert into small_experiment values (4.9e-325, 4.9e-325);

--See, all of these are zeros.
insert into small_experiment values (2.2251e-330, 2.2251e-330);
insert into small_experiment values (2.2251e-335, 2.2251e-335);
insert into small_experiment values (2.2251e-340, 2.2251e-340);
insert into small_experiment values (2.2251e-345, 2.2251e-345);

select typeof(a), typeof(b)
from small_experiment;

select * from small_experiment;

drop table small_experiment;
