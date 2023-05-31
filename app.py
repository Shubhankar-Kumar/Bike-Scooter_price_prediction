from flask import Flask, render_template, request, url_for
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def show():
    return render_template('index.html')

@app.route('/prediction', methods=['POST'])
def pred():
    engine_size = float(request.form.get('CC'))
    mileage = np.log(float(request.form.get('mileage')))
    bike_type = request.form.get('bike_type')
    weight = np.log(float(request.form.get('weight')))
    acceleration = np.log(float(request.form.get('acceleration')))
    top_speed = np.log(float(request.form.get('top_speed')))
    # print(bike_type)
    
    if bike_type == "Electric bike":
        bike_type = 0
    else:
        bike_type = 1

    features = [engine_size, mileage, bike_type, weight, acceleration, top_speed]
    features = np.array(features).reshape(1, -1)
    predicted_value = model.predict(features)
    # print(features)

    return render_template('index.html', prediction_text="Congratulations! Your dream bike comes with a price tag of {}".format(round(predicted_value[0],2)))

if __name__ == "__main__":
    app.run(debug=True)

