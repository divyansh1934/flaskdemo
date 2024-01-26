from flask import Flask, render_template,request,redirect,url_for
# request is used to know weather request is get or post
# dersrender template is a function which is used by flask to display our html content, add informations(which we have left in form of placeholders) in web browser
# redirect is used to send from one user to another url
# url_for is use to retuen the url of that webpage

# create simple flask application

app=Flask(__name__)

# for app routing

@app.route('/',methods=['GET'])  #  '/' denotes url of homepage
def welcome():
    return "<h1> Hello welcome to my channel</h1>"

@app.route('/index',methods=["GET"])
def index():
    return "<h2> Hello how are yu </h2>"


@app.route('/success/<int:score>')  # by default it will take 'GET'
def success(score):
    return "the person has passed the exam and he got: " + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "the person has failed the exam and he got: " + str(score)

@app.route('/calculate',methods=['GET','POST'])
def calculate():
    if request.method=='GET':
        return render_template('calculate.html')   # whenever we use render_template , remember that any html file will be under the templates folder.
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])

        average_marks=(maths+science+history)/3
        result=""
        if average_marks>=50:
            result="success"   
        else:
            result="fail"

        # return redirect(url_for(result,score=average_marks))  # so basically url_for is generating url of result, which in either success or fail , so basically it is generating there url.
        return render_template('result.html', results=average_marks)



if __name__=="__main__":
    app.run(debug=True)

