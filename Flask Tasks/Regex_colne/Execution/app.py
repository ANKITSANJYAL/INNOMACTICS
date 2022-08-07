from flask import Flask,render_template,url_for,request
import re

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        text=request.form.get('in_1')
        regex=request.form.get('in_2')
        
        pattern=re.compile(regex)
        valid_pattern=re.findall(pattern,text)
        numofpatterns=len(valid_pattern)
        return render_template('index.html',valid_pattern=valid_pattern,text=text,regex=regex,number=numofpatterns)
        print(text)
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
