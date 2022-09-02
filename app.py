from operator import methodcaller
from flask import Flask , render_template , request
import marks as m

app = Flask(__name__)

@app.route("/",methods = ["GET","POST"])
def hello():
    mks = 0
    if request.method == "POST":
        hrs = request.form["hrs"]
        marks_p = m.marks_prediction(int(hrs))
        mks = marks_p


    return render_template("index.html",my_marks = mks)
if __name__ == "__main__":
    app.run(debug=1)



# @app.route("/sub",methods = ["POST"])
# def submit():
#     # html -> .py
#     if(request.method == "POST"):
#         name = request.form["username"]
#     # py -> html 
#     return render_template("sub.html",n = name)
