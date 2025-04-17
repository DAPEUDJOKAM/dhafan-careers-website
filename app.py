from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Frontend Engineer',
        'location': 'Remote',
        'salary': 'Rp. 10,000,000'
    },
    {
        'id': 2,
        'title': 'Backend Engineer',
        'location': 'Bandung, Indonesia',
        'salary': 'Rp. 10,000,000'
    },
    {
        'id': 3,
        'title': 'Video Editing',
        'location': 'Remote',
        'salary': 'Rp. 10,000,000'
    }
]

@app.route("/")
def hello_dhafan():
    return render_template('home.html' , 
                           jobs=JOBS , 
                           company_name= 'Dhafan')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")