__author__ = "Emirhan Enisoglu"
__copyright__ = "MIT"

__version__ = "1.0"
__maintainer__ = "Rob Knight"
__email__ = "emirhan.enisoglu@gmail"
__status__ = "Production"

from flask import Flask

app = Flask(__name__)


@app.route("/flask")
def hello():
    return "Hello from Flask!"


@app.route("/staj")
def hello():
    return "Hello from Staj!"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
