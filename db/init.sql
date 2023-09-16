-- SQL to initialize the database

CREATE TABLE IF NOT EXISTS completion (
  id SERIAL PRIMARY KEY,
  timestamp TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  completion_model TEXT NOT NULL,
  completion_prompt TEXT NOT NULL,
  completion_temperature REAL NOT NULL,
  completion_result JSONB NOT NULL
);
