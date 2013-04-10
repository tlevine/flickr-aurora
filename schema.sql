CREATE TABLE photo (
  -- Page
  group_id TEXT NOT NULL,
  page INTEGER,
  within_page INTEGER,

  -- Standard response
  id TEXT NOT NULL,
  owner TEXT NOT NULL,
  title TEXT NOT NULL,
  dateadded DATETIME NOT NULL,

  -- Special fields
  datetaken DATETIME,
  description TEXT NOT NULL,
  url_sq TEXT NOT NULL,
  url_l TEXT NOT NULL,
  longitude REAL,
  latitude REAL,

  -- This one is always null.
  -- dateuploaded DATETIME,

  UNIQUE(group_id, page, within_page)
);

CREATE VIEW aurora AS SELECT
  url_l AS 'url',
  'http://www.flickr.com/photos/' || owner || '/' || id AS 'photostream_url',
  'http://www.flickr.com/people/' || owner AS 'owner_url',
  datetaken,
  dateadded,
--dateuploaded,
  title,
  description,
  longitude,
  latitude
FROM photo;
