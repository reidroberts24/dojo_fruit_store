#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    form_data = request.form
    print(request.form)
    total = int(form_data.get('strawberry', 0)) + int(form_data.get('raspberry', 0)) + int(form_data.get('apple', 0))
    first = form_data.get('first_name') + " "
    last = form_data.get('last_name')
    print(f"Charging {first + last} for {total} fruits.")
    return render_template("checkout.html", data=form_data, total=total)

# you can notice in the terminal that when you hit refresh it keeps charging the customer again and again

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    