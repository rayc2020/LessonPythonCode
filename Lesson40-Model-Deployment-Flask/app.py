# 第二步在localhost上建立flask-app
# 安装pip install flask

import numpy as np
from flask import Flask, request, render_template
import pickle

# 第2.1步 Loading the saved model
# We load the model.pkl file and initialize the flask app.
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

# 第2.2步 Redirecting the API to the home page index.html
@app.route('/')
def home():
    return render_template('index.html')

# 第2.3步 Redirecting the API to predict the result (salary)
@app.route('/predict',methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output))

# 第2.4步 Starting the flask server
# Navigate to URL http://127.0.0.1:5000/ (or) http://localhost:5000
if __name__ == "__main__":
#    app.run(debug=True)
    app.run(host='127.0.0.1', port=8080, debug=True)