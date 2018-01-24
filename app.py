from flask import Flask
from flask import render_template
from models import Comment


app = Flask(__name__)

@app.route("/")
def index():

   return "WElcome"


    
@app.route("/Comments")
def Comments():

    table=CommentTable(Comments)

    return render_template ("index.html" table=table)