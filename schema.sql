CREATE TABLE photo (
  -- Page
  page INTEGER,
  within_page INTEGER,

  -- Standard response
  id TEXT NOT NULL,
  owner TEXT NOT NULL,
  title TEXT NOT NULL,
  dateadded DATETIME NOT NULL,

  -- Special fields
  date_upload DATETIME NOT NULL,
  date_taken DATETIME NOT NULL,
  description TEXT NOT NULL,
  url_l TEXT NOT NULL,
  longitude REAL NOT NULL,
  latitude REAL NOT NULL,
  UNIQUE(page, within_page)
);

CREATE VIEW aurora AS SELECT
  url_l AS 'url',
  'http://www.flickr.com/photos/' || owner || '/' || id AS 'photostream_url'
  'http://www.flickr.com/people/' || owner AS 'owner_url'
  date_taken,
  date_upload,
  dateadded AS date_added,
  title,
  description,
  longitude,
  latitude
FROM photo;
