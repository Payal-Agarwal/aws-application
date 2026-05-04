from flask import Flask

application = Flask(__name__)

@application.route("/")
def home():
    return "CI/CD working successfully on AWS Elastic Beanstalk"
