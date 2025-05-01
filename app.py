from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return """
    <html>
        <body style="background-color: blue;">
            <h1 style="text-align: center; color: white;">Welcome to my web page!</h1>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8085, debug=True)
