from flask import Flask, render_template
from controllers.rooms_controller import rooms_blueprint
from controllers.guests_controller import guests_blueprint
from controllers.weapons_controller import weapons_blueprint

app = Flask(__name__)

app.register_blueprint(rooms_blueprint)
app.register_blueprint(guests_blueprint)
app.register_blueprint(weapons_blueprint)

if __name__ == '__main__':
    app.run() 

@app.route("/")
def main():
    return render_template('index.html')