-- A particular user playing in a particular game 

-- Basically a join table with extra information about the relationship.

-- For the foreign keys, we use ON DELETE CASCADE to simplify dropping a
-- game, although this introduces some risk of accidental deletion.

CREATE TABLE players (
  game_id INTEGER NOT NULL,
  user_id INTEGER NOT NULL,
  -- Maybe add name in game 
  -- Add timestamps for when last moved and the like
  -- Possibly add some info about the current range of what they can see
  FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
  FOREIGN KEY (game_id) REFERENCES games(game_id) ON DELETE CASCADE,
  PRIMARY KEY (game_id, user_id)
) ENGINE=InnoDB;
