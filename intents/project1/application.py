import os

from flask import Flask, session, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from training import *
app = Flask(__name__, template_folder=r"C:\Users\Himaja\Desktop\intents\project1\templates")

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/output", methods=['GET','POST'])
def output():
    if request.method == 'POST':
        try:
            project_id = "test-chatbot2-rhylal"         
            display_name = "Java"
            training_phrases_parts = ["What is java", "Java", "Importance of java", "why do I need java"]
            message_texts = ["Java is a programming language and computing platform first released by Sun Microsystems in 1995. There are lots of applications and websites that will not work unless you have Java installed, and more are created every day. Java is fast, secure, and reliable. From laptops to datacenters, game consoles to scientific supercomputers, cell phones to the Internet, Java is everywhere!"]
            
            create_intent(project_id, display_name, training_phrases_parts,
                        message_texts)           
                
            data = "executed"
        except Exception:
            data = "Error!! "+ display_name + " already exists.."

        return render_template('index.html', data = data)
    
    return render_template('index.html')

if __name__ == '__main__': 
    app.run()
