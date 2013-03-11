Photographic Validation of Satellite Forecasting Models for Extreme Weather Events
===
This script downloads images for a prototype of a website for the study of
current auroras.

    # Set your credentials
    export FLICKR_KEY=12345abcde...

    # Create schema
    sqlite3 aurora.db < schema.sql

    # Download
    ./run

    # Generate csv
    sqlite3 aurora.db -csv -header 'SELECT * FROM aurora;'

Test the parser

    nosetests2
