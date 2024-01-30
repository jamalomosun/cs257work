DROP TABLE IF EXISTS population;
CREATE TABLE population(
  quaketime timestamp with time zone,
  latitude float,
  longitude float,
  quakedepth float,
  magnitude float,
  magType text,
  id text,
  place text
