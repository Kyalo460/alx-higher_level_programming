-- Creates a table if it doesn't exist
CREATE TABLE IF NOT EXISTS unique_id (
    id INT UNIQUE,
    name VARCHAR(256)
);
