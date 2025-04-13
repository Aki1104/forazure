from flask import Flask, render_template_string

app = Flask(__name__)

with open("index.html", "r") as f:
    html_template = f.read()

@app.route('/')
def home():
    return render_template_string(html_template)

if __name__ == '__main__':
    app.run(debug=True)
