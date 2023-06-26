-- SQL to initialize the database

-- CREATE DATABASE openai;
-- \c openai;

DROP TABLE IF EXISTS completion;
CREATE TABLE completion (
  id SERIAL PRIMARY KEY,
  timestamp TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  completion_model TEXT NOT NULL,
  completion_prompt TEXT NOT NULL,
  completion_temperature REAL NOT NULL,
  completion_result TEXT NOT NULL
);
