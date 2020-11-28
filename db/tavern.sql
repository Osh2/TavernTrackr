DROP TABLE IF EXISTS rooms; 
DROP TABLE IF EXISTS guests;
DROP TABLE IF EXISTS weapons;

CREATE TABLE weapons(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    stats VARCHAR(255)
);

CREATE TABLE guests(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    type VARCHAR(255),
    race VARCHAR(255),
    weapon_id INT REFERENCES weapons(id)
);

CREATE TABLE rooms(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    capacity INT,
    guest_id INT REFERENCES guests(id)
);

