from flask import Flask, render_template, request
import pyshorteners
   
app = Flask(__name__)
   
@app.route('/')
def home():
    return render_template('home.html')
   
@app.route('/', methods=['POST'])
def shorten_link():
    link = request.form['link']
    srt = pyshorteners.Shortener()
    x = srt.tinyurl.short(link)
    return render_template('result.html', short_link=x)
   
if __name__ == '__main__':
    app.run(debug=True)
