from flask import Flask,request,render_template,redirect,flash  
                                          
app = Flask(__name__)                     
app.secret_key = 'KeepItSecretKeepItSafe'                                         
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result',methods=['POST','GET'])
def result():
    name=request.form['user_name']
    if len(request.form['comment'])==0 or len(request.form['user_name'])==0:
        flash('These field cannot be left blank ')
    if len(request.form['comment'])>120:
        flash('Comments cannot be more than 120 characters')

    
        
    return render_template('result.html',context={
        "name":request.form['user_name'],
        "where":request.form['where'],
        "code":request.form['code'],
        "comment":request.form['comment']
        })

app.run(debug=True)