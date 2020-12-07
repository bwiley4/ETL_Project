# Import Dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# Connect to Postgres Database
# NEED TO INPUT CORRECT CONNECTION STRING
engine = create_engine("<postgres connection string>")
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save References To Each Table
# NEED TO INSERT CORRECT TABLE NAMES
Quotes = Base.classes.<insert_table_name>
Authors = Base.classes.<insert_table_name>
Tags = Base.classes.<insert_table_name>
session = Session(engine)

# Create Flask App
app = Flask(__name__)

# Quotes Route
# NEED TO EDIT THE QUERY WITH CORRECT TABLE/COLUMN NAMES
@app.route("/quotes")
def get_quotes():
    quote_data = {}
    quote_results = session.query(Quotes.quote).all()
    data['total_number'] = results.rowcount
    quotes = []
    for x in quote_results:
        quote = {}
        quote['text'] = x.text
        quote['author name'] = x.author_name
        quote['tags'] = x.tags
        quotes.append(quote)
    quote_data['quotes'] = quotes
    return jsonify(quote_data)

# Top 10 Tags Route
# NEED TO EDIT THE QUERY WITH CORRECT TABLE/COLUMN NAMES
# NEED TO LOOK OVER COUNT SECTION TO SEE IF THIS EVEN WORKS
@app.route("/top10tags")
def get_top_ten():
    tag_data = {}
    tag_results = session.query(Tags.tag)\
        .group_by(Tag.tag).order_by(Tag.count(*) desc)\
        .limit(10)
    for y in tag_results:
        tags = {}
        tags['tag'] = y.tag
        tags['quote count'] = y.count(*)
        tag_data.append(tags)
    return jsonify(result)

if __name__ == '__main__':
    app.run()