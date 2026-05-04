from flask import Flask

application = Flask(__name__)

@application.route("/")
def home():
   return "CI/CD is working successfully!"

if __name__ == "__main__":
    application.run()
