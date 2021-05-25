CREATE TABLE IF NOT EXISTS date
(
 id     integer PRIMARY KEY AUTOINCREMENT,
 day    integer NOT NULL,
 month  integer NOT NULL,
 year   integer NOT NULL,
 season integer NOT NULL
);


CREATE TABLE IF NOT EXISTS location
(
 id        integer PRIMARY KEY AUTOINCREMENT,
 city      varchar(50) NOT NULL,
 latitude  decimal(10,6) NOT NULL,
 longitude decimal(9,6) NOT NULL,
 CONSTRAINT PK_location PRIMARY KEY ( "id" )
);

CREATE TABLE IF NOT EXISTS fires
(
 dataId     integer NOT NULL,
 locationId integer NOT NULL,
 brightness decimal(4,1) NOT NULL,
 confidence integer NOT NULL,
 dayNight   char(1) NOT NULL,
 longitude  decimal(10,6) NOT NULL,
 latitude   decimal(9,6) NOT NULL,
 CONSTRAINT PK_fires PRIMARY KEY ( dataId, locationId ),
 CONSTRAINT FK_28 FOREIGN KEY ( dataId ) REFERENCES data ( "id" ),
 CONSTRAINT FK_31 FOREIGN KEY ( locationId ) REFERENCES location ( "id" )
);

CREATE INDEX fkIdx_29 ON fires
(
 dataId
);

CREATE INDEX fkIdx_32 ON fires
(
 locationId
);


CREATE TABLE IF NOT EXISTS weather
(
 dataId        integer NOT NULL,
 locationId    integer NOT NULL,
 mimTemp       decimal(3,1) NOT NULL,
 maxTemp       decimal(3,1) NOT NULL,
 rainfall      decimal(2,1) NOT NULL,
 windGustDir   char(3) NOT NULL,
 windGustSpeed integer NOT NULL,
 CONSTRAINT PK_weather PRIMARY KEY ( dataId, locationId ),
 CONSTRAINT FK_59 FOREIGN KEY ( dataId ) REFERENCES data ( "id" ),
 CONSTRAINT FK_62 FOREIGN KEY ( locationId ) REFERENCES location ( "id" )
);

CREATE INDEX fkIdx_60 ON weather
(
 dataId
);

CREATE INDEX fkIdx_63 ON weather
(
 locationId
);


CREATE TABLE IF NOT EXISTS weatherChange
(
 dataId            integer NOT NULL,
 temperatureChange decimal(2,1) NOT NULL,
 standardDeviation decimal(2,1) NOT NULL,
 CONSTRAINT PK_weatherchange PRIMARY KEY ( dataId ),
 CONSTRAINT FK_53 FOREIGN KEY ( dataId ) REFERENCES data ( "id" )
);

CREATE INDEX fkIdx_54 ON weatherChange
(
 dataId
);