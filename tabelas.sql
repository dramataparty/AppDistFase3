PRAGMA foreign_keys = ON;
CREATE TABLE legs (
id INTEGER PRIMARY KEY,
dep_IATA TEXT,
arr_IATA TEXT,
dep_datetime TEXT,
arr_datetime TEXT,
duration_min numeric(2),
airline_codes TEXT,
FOREIGN KEY(dep_IATA) REFERENCES locations(IATA) ON DELETE CASCADE,
FOREIGN KEY(arr_IATA) REFERENCES locations(IATA) ON DELETE CASCADE
);

create table airlines(
    code TEXT(2) primary key,
    name TEXT
);

create table weather(
    id INTEGER PRIMARY KEY,
    date TEXT,
    location TEXT,
    condition TEXT,
    mintemp_c TEXT,
    maxtemp_c TEXT,
);

create table locations(
    id INTEGER PRIMARY KEY,
    name TEXT,
    IATA TEXT,
    wea_name text
);

create table roundtrips(
    id INTEGER PRIMARY KEY,
    cost numeric,
    IATA TEXT,
    wea_name text,
    id_leg0 text,
    id_leg1 text
    FOREIGN KEY id_leg0 REFERENCES legs(id) ON DELETE CASCADE,
    FOREIGN KEY id_leg1 REFERENCES legs(id) ON DELETE CASCADE
);


