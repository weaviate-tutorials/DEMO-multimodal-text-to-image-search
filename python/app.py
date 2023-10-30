from flask import Flask, render_template, request, redirect, url_for
from utils import client, search_query


app=Flask(__name__)

show_more = False
show_more_button_text = "Show More"


@app.route("/", methods =["GET","POST"])
def home():

    

    if request.method == "POST":
        #Retrieve query from html form
        query = request.form.get("search_query")

        #Get results from db query
        results = search_query(query)

        return render_template('search_page.html', results = results, show_more = show_more, show_more_button_text = show_more_button_text, logo = None)
    
    else:
        #Load inital page
        return render_template('search_page.html', results = None, show_more = show_more, show_more_button_text = show_more_button_text, logo = None)





    
if __name__ == "__main__":
    app.run()