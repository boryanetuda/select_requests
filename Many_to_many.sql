create table if not exists Artist (
	id serial primary key,
	name varchar (40) not null
);
	
create table if not exists Album (
	id serial primary key,
	name varchar (40) not null,
	year_date int
);

create table if not exists ArtistAlbum (
	id serial primary key,
	Artist_id int not null references Artist(id),
	Album_id int not null references Album(id)
);

create table if not exists Track (
	id serial primary key,
	name varchar (40) not null,
	length real check (length > 0),
	album_id int references Album(id)
);

create table if not exists Compilation (
	id serial primary key,
	name varchar (40) not null,
	year_date int not null
);

create table if not exists TrackCompilation (
	id serial primary key,
	Track_id int not null references Track(id),
	Compilation_id int not null references Compilation(id)
);

create table if not exists Genre (
	id serial primary key,
	name varchar (40) not null
);

create table if not exists ArtistGenre (
	id serial primary key,
	Artist_id int not null references Artist(id),
	Genre_id int not null references Genre(id)
);