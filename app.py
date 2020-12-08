# Import Dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# Connect to Postgres Database
# NEED TO INPUT CORRECT CONNECTION STRING
# connection_string = f"postgres:postgres@localhost:5432/quotes_db"
# engine = create_engine(f'postgresql://{connection_string}')

engine = create_engine("postgresql://postgres:postgres@localhost:5432/quotes_db")
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save References To Each Table
# NEED TO INSERT CORRECT TABLE NAMES
# Quotes = Base.classes.quotes
# Authors = Base.classes.author
# Tags = Base.classes.tags
session = Session(engine)

# Create Flask App
app = Flask(__name__)

# Functions to help get specific quote data
def quote_tags(quote_id):
    all_tags = []
    tags_result = engine.execute(f'select tag  from tags where quote_id= {quote_id}')
    for tr in tags_result:
        all_tags.append(tr.tag)
    return all_tags


@app.route("/")
def welcome():
    home_message = {"Available Routes":    
        ["/quotes",
        "/top10tags"]}
    return home_message



# Quotes Route
@app.route("/quotes")
def get_quotes():
    quote_data = {}
    quote_results = engine.execute('''select id, author_name, text
    from quotes q inner join author a on q.author_name = a.name
    order by id''')
    quote_data['total_number'] = quote_results.rowcount
    quotes = []
    for x in quote_results:
        quote = {}
        quote['text'] = x.text
        quote['author name'] = x.author_name
        tags = quote_tags(x.id)
        quote['tags'] = tags
        quotes.append(quote)
    quote_data['quotes'] = quotes
    return jsonify(quote_data)

# Top 10 Tags Route
@app.route("/top10tags")
def get_top_ten():
    tag_data = {}
    tag_results = engine.execute(
         '''SELECT tag, COUNT(tag)AS tag_frequency
            FROM tags
            GROUP BY tag
            ORDER BY COUNT(tag) DESC
            Limit 10''')
    tag_list = []
    for y in tag_results:
        tags = {}
        tags['tag'] = y.tag
        tags['tag count'] = y.tag_frequency
        tag_list.append(tags)
    tag_data['Top 10 Tags'] = tag_list
    return jsonify(tag_data)

if __name__ == '__main__':
    app.run()