-- A planet in a specific game

CREATE TABLE planets ( 
  planet_id INTEGER AUTO_INCREMENT PRIMARY KEY,
  game_id INTEGER NOT NULL,
  name VARCHAR(200) NOT NULL,
  x_location INTEGER NOT NULL,
  y_location INTEGER NOT NULL,
  -- Later add, e.g. resources, ownership, 
  FOREIGN KEY (game_id) REFERENCES games (game_id) ON DELETE CASCADE
) ENGINE=InnoDB;