create table if not exists entries (
  id integer primary key autoincrement,
  title text not null,
  author text not null,
  text text not null
);

create table if not exists users(
  id integer primary key autoincrement unique ,
  login text not null,
  pass text not null,
  role varchar not null
);