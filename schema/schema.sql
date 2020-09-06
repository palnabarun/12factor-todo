-- create the table task if it does not exist
CREATE TABLE IF NOT EXISTS task (
    id serial,
    description text,
    completed boolean
);

-- set default for completed column
ALTER TABLE task ALTER COLUMN completed SET DEFAULT false;
