from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(my_data):
    with open('database.txt', mode='a') as database:
        email = my_data["email"]
        subject = my_data["subject"]
        message = my_data["message"]
        file = database.write(f'\n{email}, {subject}, {message}')


def write_to_csv(my_data):
    with open('database.csv', mode='a', newline='') as database2:
        email = my_data["email"]
        subject = my_data["subject"]
        message = my_data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            my_data = request.form.to_dict()
            write_to_csv(my_data)
            return redirect('/thankyou.html')
        except:
            return 'Is not safe for the Database'
    else:
        return 'Something went wrong'

