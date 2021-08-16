"""
Flask Application
Author: Shilpaj Bhalerao
Date: Aug 15, 2021
"""
# Third-Party Imports
from flask import Flask, render_template, request


# Crate instance of flask for the app
application = Flask(__name__)

# Subscribers Information
subscribers = []


@application.route('/')
def home():
    """
    Logic for the Home page
    """
    # Point the app to the HTML file containing website
    return render_template("index.html", title="Shilpaj")


@application.route('/about')
def about():
    """
    Logic for the About Page
    """
    data = []
    with open('about.txt', 'r') as file:
        for row in file:
            data.append(row.split('\n'))
    return render_template("about.html", data=data)


@application.route('/subscribe')
def subscribe():
    """
    Logic for the Subscribe Page
    """
    return render_template("subscribe.html")


@application.route('/form', methods=["POST"])
def form():
    """
    Logic for the form page which can only appear after subscription details are provided
    """
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")

    if not first_name or not last_name or not email:
        error_statement = "All Form Fields Required..."
        return render_template("subscribe.html",
                               error_statement=error_statement,
                               first_name=first_name,
                               last_name=last_name,
                               email=email)

    subscribers.append(f"{first_name} {last_name} | {email}")
    return render_template("form.html", first_name=first_name, subscribers=subscribers)


if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8880, debug=True)
