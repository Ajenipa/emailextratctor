from flask import Flask,request,render_template,url_for
import re
email_regex = re.compile(r'[\w\.-]+@[\w\.-]+')
phone_num = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
url_https_regex = re.compile(r'https?://www\.?\w+\.\w+')
url_regex =re.compile(r'http?://www\.?\w+\.\w+')
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/process', methods = ["GET", "POST"])
def process():
    if request.method == "POST":
        choice = request.form['task']
        if choice == "email":
            rawtext = request.form['rawtext']
            results = email_regex.findall(rawtext)
            num_of_results=len(results)
            return render_template('index.html', results=results, num_of_results=num_of_results)
        elif choice == "phone":
            rawtext = request.form['rawtext']
            results = phone_num.findall(rawtext)
            num_of_results=len(results)
            return render_template('index.html', results=results, num_of_results=num_of_results)
        elif choice == "url":
            rawtext = request.form['rawtext']
            results = url_regex.findall(rawtext)
            num_of_results = len(results)
            return render_template('index.html', results=results, num_of_results=num_of_results)
        elif choice == "urls":
            rawtext = request.form['rawtext']
            results = url_https_regex.findall(rawtext)
            num_of_results = len(results)
            return render_template('index.html', results=results, num_of_results=num_of_results)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug = True)