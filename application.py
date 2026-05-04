from flask import Flask

application = Flask(__name__)

@application.route("/")
def home():
    return "CI/CD working on AWS Elastic Beanstalk"

if __name__ == "__main__":
    application.run()