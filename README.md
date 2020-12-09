# ETL_Project

Team Members:
    - Taylor Greenhut
    - Michael Ejike
    - Roberto Clavijo
    - Brandon Wiley
    - Dev Patel

In our second group project, we were given the task to scrape the following information from all quotes listed on the website  http://quotes.toscrape.com/:
    - quote text
    - quote tags
    - author name
    - author Details
        - born
        - description

To scrape the data, we created functions that would be called upon to run in our app to go through every quote, grab all quote information requested, then click on the author's link and grab the information requested for the author.  Once scraped, we stored all information into a MongoDB database.

In Postgres, we created 3 tables to hold our information and use to link to our Flask API:
    - Quotes & Quote/Author Relation
    - Author Info
    - Quote/Tag Relation

Using our Flask API, we created a site that contained 3 routes that contained specific information jsonified:
    - ("/"):
        - Homepage to list the routes available.
    - ("/quotes"):
        - Quote info in a json list containing the text, author name, and tags of each
        - total number of quotes.
    - ("/top10tags"):
        - Json list of the tag name and the total number of quotes with the tag of the top 10 tags used on the website.