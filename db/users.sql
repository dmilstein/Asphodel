-- The actual, real-world users.  A single user can play in many games over time.
CREATE TABLE users (
  user_id INTEGER AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(64) NOT NULL,
  password VARCHAR(64) NOT NULL,
  email VARCHAR(128) NOT NULL
) ENGINE=InnoDB;
