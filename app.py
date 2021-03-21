from flask import Flask, render_template, request
import goal

app = Flask(__name__)

templateData = {
    'title': "Carolina Hurricanes"
}

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        goal.activate_experience()
        print("Hello")
    return render_template("index.html", **templateData)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
