drop table if exists calposts;
	create table calposts (
		cid integer primary key autoincrement,
		calname text not null,
		calcontent text not null

);

