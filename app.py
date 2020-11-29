from flask import Flask, render_template
from controllers.rooms_controller import rooms_blueprint

app = Flask(__name__)

app.register_blueprint(rooms_blueprint)

if __name__ == '__main__':
    app.run() 

@app.route("/")
def main():
    return render_template('index.html')