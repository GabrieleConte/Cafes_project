from flask import Flask, render_template, json
from flask_wtf import FlaskForm
from wtforms import StringField
import pandas as pd

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'


class CafeForm(FlaskForm):
    cafename = StringField()
    location = StringField()
    open = StringField()
    close = StringField()
    coffee = StringField()
    wifi = StringField()
    power = StringField()


# Exercise:
# add: Location URL, open time, closing time, coffee rating, power outlet rating fields
# make coffee/ Wi-Fi /power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/addcafes/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    try:
        cafename = form.cafename.data
        location = form.location.data
        opened = form.open.data
        close = form.close.data
        coffee = form.coffee.data
        wifi = form.wifi.data
        power = form.power.data
        new_coffe = ""
        new_wifi = ""
        new_power = ""
        for i in range(0, int(coffee)):
            new_coffe = new_coffe + "☕️"
        for i in range(0, int(wifi)):
            new_wifi = new_wifi + "💪️"
        for i in range(0, int(power)):
            new_power = new_power + "️🔌"
        row = [cafename, location, opened, close, new_coffe, new_wifi,new_power]
        new_row=pd.DataFrame([row],columns=[0,1,2,3,4,5,6])
        df = pd.read_csv("./static/assets/cafe_data.csv", header=None)
        df = df.append(new_row, ignore_index=True)
        df.to_csv("./static/assets/cafe_data.csv", index=False, header=False)
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'},
    except:
        print(form.errors)
        errors = form.errors
        return json.dumps({'success': False, 'errors': errors}), 404, {'ContentType': 'application/json'}  #


if __name__ == '__main__':
    app.run(debug=True)
