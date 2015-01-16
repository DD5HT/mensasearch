CREATE TABLE price
(
    id INTEGER PRIMARY KEY ASC,
    price_student DECIMAL(1,2) NOT NULL UNIQUE CHECK ( price_student > 0 ),
    price_worker DECIMAL(1,2) NOT NULL UNIQUE CHECK ( price_worker > 0 ),
    price_visitor DECIMAL(1,2) NOT NULL UNIQUE CHECK ( price_visitor > 0 )
);

CREATE TABLE meal_type
(
    name VARCHAR(64) PRIMARY KEY
);

CREATE TABLE city
(
    name VARCHAR(64) PRIMARY KEY
);

CREATE TABLE meal
(
    name VARCHAR(64) PRIMARY KEY,
    mtype VARCHAR(64) NOT NULL,
    FOREIGN KEY(mtype) REFERENCES meal_type(name)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE mensa
(
    name VARCHAR(64) NOT NULL,
    city VARCHAR(64) NOT NULL,
    location_latitude REAL,
    location_longitude REAL,
    FOREIGN KEY(city) REFERENCES city(name)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    PRIMARY KEY(name, city)
);

CREATE TABLE meal_mensa
(
    meal VARCHAR(64) NOT NULL,
    mensa VARCHAR(64) NOT NULL,
    city VARCHAR(64) NOT NULL, 
    FOREIGN KEY(meal) REFERENCES meal(name)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY(mensa, city) REFERENCES mensa(name, city)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    PRIMARY KEY(meal, mensa, city)
);

CREATE TABLE available
(
    meal INTEGER NOT NULL,
    mensa INTEGER NOT NULL,
    price INTEGER NOT NULL,
    city VARCHAR(64) NOT NULL, 
    avail_time DATETIME NOT NULL,
    FOREIGN KEY(meal, mensa, city) REFERENCES meal_mensa(meal, mensa, city)
    FOREIGN KEY(price) REFERENCES price(id),
    PRIMARY KEY(meal, mensa, city, avail_time)
);
