from flask import Flask,render_template
import os
app=Flask(__name__)


@app.route('/')
def index():
    return "Hello Word"
    
    
  
@app.route('/profile/<user>')
def profile(user=None):
    return render_template("profile.html",name=user)
    
    
    
if __name__ == "__main__":
    #app.debug = True
    #port = int(os.environ.get("PORT",5000))
    #app.run(host='0.0.0.0',port = port)
    app.run()