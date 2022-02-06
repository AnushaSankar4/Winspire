from flask import Flask, render_template
from db import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inspiringwomen/<specialization>',methods=['GET'])
def inspiringWomen(specialization):
    print(specialization)
    return get_inspiring_women_in_category(specialization)

if __name__ == '__main__':
  app.run(debug=True)