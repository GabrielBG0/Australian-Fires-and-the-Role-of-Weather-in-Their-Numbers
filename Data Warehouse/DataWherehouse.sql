CREATE TABLE IF NOT EXISTS date
(
 id     serial PRIMARY KEY,
 day    integer NOT NULL,
 month  integer NOT NULL,
 year   integer NOT NULL,
 season integer NOT NULL
);


CREATE TABLE IF NOT EXISTS location
(
 id        serial PRIMARY KEY,
 city      varchar(50) NOT NULL,
 latitude  decimal(10,6) NOT NULL,
 longitude decimal(9,6) NOT NULL
);

CREATE TABLE IF NOT EXISTS fires
(
 id         serial NOT NULL,
 dateId     integer NOT NULL,
 locationId integer NOT NULL,
 brightness decimal(4,1) NOT NULL,
 confidence integer NOT NULL,
 dayNight   char(1) NOT NULL,
 longitude  decimal(10,6) NOT NULL,
 latitude   decimal(9,6) NOT NULL,
 CONSTRAINT PK_fires PRIMARY KEY ( id, dateId, locationId ),
 CONSTRAINT FK_28 FOREIGN KEY ( dateId ) REFERENCES date ( id ),
 CONSTRAINT FK_31 FOREIGN KEY ( locationId ) REFERENCES location ( id )
);

CREATE INDEX fkIdx_29 ON fires
(
 dateId
);

CREATE INDEX fkIdx_32 ON fires
(
 locationId
);


CREATE TABLE IF NOT EXISTS weather
(
 id            serial NOT NULL,
 dateId        integer NOT NULL,
 locationId    integer NOT NULL,
 mimTemp       decimal(3,1) NOT NULL,
 maxTemp       decimal(3,1) NOT NULL,
 rainfall      decimal(2,1) NOT NULL,
 windGustDir   char(3) NOT NULL,
 windGustSpeed integer NOT NULL,
 CONSTRAINT PK_weather PRIMARY KEY ( id, dateId, locationId ),
 CONSTRAINT FK_59 FOREIGN KEY ( dateId ) REFERENCES date ( id ),
 CONSTRAINT FK_62 FOREIGN KEY ( locationId ) REFERENCES location ( id )
);

CREATE INDEX fkIdx_60 ON weather
(
 dateId
);

CREATE INDEX fkIdx_63 ON weather
(
 locationId
);


CREATE TABLE IF NOT EXISTS weatherChange
(
 id                serial NOT NULL,
 dateId            integer NOT NULL,
 temperatureChange decimal(2,1) NOT NULL,
 standardDeviation decimal(2,1) NOT NULL,
 CONSTRAINT PK_weatherchange PRIMARY KEY ( id, dateId ),
 CONSTRAINT FK_53 FOREIGN KEY ( dateId ) REFERENCES date ( id )
);

CREATE INDEX fkIdx_54 ON weatherChange
(
 dateId
);