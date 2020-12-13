from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_scrape"
mongo = PyMongo(app)


@app.route('/')
def Query():
    mars_dict = mongo.db.mars_info.find_one()
    return render_template("index.html", mars_dict=mars_dict)


@app.route('/scrape')
def Scrape():
    mars_info = mongo.db.mars_info
    mars_data = scrape_mars.scrape()
    mars_info.update({}, mars_data, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run() # host ='127.0.0.1', port ='5000'