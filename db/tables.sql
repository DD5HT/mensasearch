CREATE TABLE kind (
    name TEXT NOT NULL PRIMARY KEY
);

CREATE TABLE meal (
    id INTEGER NOT NULL,
    description TEXT NOT NULL,
    kind TEXT NOT NULL,
    FOREIGN KEY (kind) REFERENCES kind(name),
    PRIMARY KEY (id, kind)
);

CREATE TABLE mensa (
    id INTEGER NOT NULL PRIMARY KEY,
    name TEXT NOT NULL,
    location_lo REAL NOT NULL DEFAULT 0.0,
    location_la REAL NOT NULL DEFAULT 0.0
);

CREATE TABLE food_lable (
    name TEXT NOT NULL PRIMARY KEY,
    icon BLOB
);

CREATE TABLE allergy_lable (
    lable TEXT NOT NULL PRIMARY KEY,
    description TEXT NOT NULL
);

CREATE TABLE ingredient_lable (
    lable INTEGER NOT NULL,
    description TEXT NOT NULL
);

CREATE TABLE meal_contains_ingredient (
    meal INTEGER NOT NULL,
    ingredient INTEGER NOT NULL,
    FOREIGN KEY (meal) REFERENCES meal(id),
    FOREIGN KEY (ingredient) REFERENCES ingredient(lable),
    PRIMARY KEY (meal, ingredient)
);

CREATE TABLE meal_has_lable (
    meal INTEGER NOT NULL,
    lable INTEGER NOT NULL,
    since TEXT DEFAULT CURRENT_TIME,
    FOREIGN KEY (meal) REFERENCES meal(id),
    FOREIGN KEY (lable) REFERENCES food_lable(lable),
    PRIMARY KEY (meal, lable)
);

CREATE TABLE mensa_has_meal (
    meal INTEGER NOT NULL,
    mensa INTEGER NOT NULL,
    available TEXT DEFAULT CURRENT_TIME,
    price_student INTEGER NOT NULL,
    price_employe INTEGER NOT NULL,
    price_guest INTEGER NOT NULL,
    FOREIGN KEY (meal) REFERENCES meal(id),
    FOREIGN KEY (mensa) REFERENCES mensa(id),
    PRIMARY KEY (mensa, meal, available)
);
