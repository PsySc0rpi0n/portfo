"""Build an html server"""
import csv
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/<string:page_name>')
def load_html_page(page_name):
    """Load any page"""
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    """Submit form page"""
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Something wrong happened'
    else:
        return  'Something went wrong. Try again!'

def write_data(data):
    """Write data to database"""
    with open('database.dat', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}, {subject}, {message}')

def write_csv(data):
    """Write data to database"""
    with open('database.csv', mode='a', newline='') as databasecsv:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(databasecsv, delimiter=',', quotechar='$', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
