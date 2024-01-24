DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes( 
  quaketime timestamp with time zone,
  latitude float,
  longitude float,
  quakedepth float,
  magnitude float,
  magType text,
  id text,
  place text
);
