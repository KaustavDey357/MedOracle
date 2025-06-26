from flask import Flask, request, render_template, redirect, url_for
from ml_model.predict import predict_risk
from ocr.extract import extract_health_metrics
import os
from werkzeug.utils import secure_filename


app = Flask(__name__, template_folder='../frontend/templates')


@app.route('/')
def func():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_and_predict():
    file = request.files['report']
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    features = extract_health_metrics(filepath)
    features.update({...})
    risk = predict_risk(features)

    return render_template("result.html", risk=risk, features=features)


if __name__ == "__main__":
    app.run(debug=True)
