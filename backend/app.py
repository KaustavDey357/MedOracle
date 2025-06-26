from flask import Flask, request, render_template, redirect, url_for
from ml_model.predict import predict_risk
from ocr.extract import extract_health_metrics
from contract_connector import store_on_chain
import os
from werkzeug.utils import secure_filename
from ipfs_uploader import upload_file_to_ipfs


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
    ipfs_cid = upload_file_to_ipfs(filepath)

    tx_hash = store_on_chain(risk, ipfs_cid)

    return render_template("result.html", risk=risk, features=features, cid=ipfs_cid, tx=tx_hash)


if __name__ == "__main__":
    app.run(debug=True)
