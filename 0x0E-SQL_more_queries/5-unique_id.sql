-- Creates a table if it doesn't exist
CREATE TABLE IF NOT EXISTS unique_id (
    id INT Default 1 UNIQUE,
    name VARCHAR(256)
);
