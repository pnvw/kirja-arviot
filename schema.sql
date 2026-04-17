CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
);

CREATE TABLE items (
    id INTEGER PRIMARY KEY,
    book_name TEXT,
    writer TEXT,
    review TEXT,
    rating INTEGER,
    user_id INTEGER REFERENCES users
);