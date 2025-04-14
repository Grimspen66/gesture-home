DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS settings;
DROP TABLE IF EXISTS appliance;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE settings (
    user_id INTEGER PRIMARY KEY,
    appliances SET NOT NULL
)

CREATE TABLE appliance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    appliance_name TEXT NOT NULL,
    gesture TEXT NOT NULL
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
);