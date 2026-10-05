from flask import Flask
import socket

app = Flask(__name__)


@app.route("/")
def home():
    hostname = socket.gethostname()

    return f"""
    <html>
        <head>
            <title>AWS DevOps Project</title>
        </head>
        <body>
            <h1>Hello from AWS Cloud-Native DevOps!</h1>
            <p><strong>Version:</strong> 1.2</p>
            <p><strong>Environment:</strong> Production</p>
            <p><strong>Hostname:</strong> {hostname}</p>
        </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
