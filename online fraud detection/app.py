from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model=pickle.load(open('fraud_detection_model.pkl','rb'))


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[float(x) for x in request.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=model.predict(final)
    output=prediction[0]

    if output== "Fraud":
        return render_template('result.html',pred='this is fraud transaction.')
    else:
        return render_template('result.html', pred='this is not fraud transaction.')


if __name__ == '__main__':
    app.run(debug=True)
