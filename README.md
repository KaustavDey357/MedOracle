# 🧬 MedOracle

> A decentralized platform for AI-powered medical report analysis and secure, tamper-proof health data verification using Web3 and IPFS.

---

## 🚀 Overview

**MedOracle** is a full-stack healthtech platform that helps users:
- Upload medical test reports (image or PDF)
- Automatically extract relevant values using OCR
- Analyze risk levels using a trained ML model
- Store and verify results on-chain via smart contracts and IPFS

---

## 💡 Problem It Solves

Modern healthcare systems often struggle with:

- ❓ Interpreting medical reports without expert help  
- 🐌 Delays in verifying health reports for insurance, jobs, etc.  
- 🔓 Security vulnerabilities in centralized record systems  

**MedOracle** provides:

- 📊 Instant health risk predictions with AI  
- 🔗 Blockchain-based verification  
- 🛡️ Secure, tamper-proof medical records via IPFS  

---

## 🖼️ Demo Preview

### 🏠 Home Page

![MedOracle Home](./assets/Screenshot%20(199).png)

---

### ✅ Result Page

![MedOracle Result](./assets/Screenshot%20(200).png)

---

## 🧪 Tech Stack

| Layer        | Technology |
|--------------|------------|
| Frontend     | HTML, TailwindCSS, Flask Templates |
| Backend      | Flask (Python), Tesseract OCR, Scikit-learn |
| ML Model     | Decision Tree Classifier (trained with health data) |
| Blockchain   | Solidity, Hardhat, Web3.py |
| Storage      | IPFS via `web3.storage` API |


## 📁 Project Structure
```
MedOracle/
├── backend/
│ ├── app.py
│ ├── ml_model/
│ │ ├── predict.py
│ │ ├── _pycache_
│ │ | └─ pridict.cpython-312.pyc
│ │ └── model.pkl
│ └── ocr/
│   └── extract_features.py
├── contract/
│ ├── medoracle.sol
│ └── deploy.js
├── frontend/
│ ├── templates/
│ │ ├── home.html
│ │ ├── base.html
│ │ └── results.html
├── assets/
│ ├── Screenshot (199).png
│ └── Screenshot (200).png
└── README.md

```

## ⚙️ Setup Instructions

### 1. 📦 Install Backend Requirements

```bash
cd backend
pip install -r requirements.txt
```
### 2. 🧠 Run Flask App
```
python app.py
```

Go to: http://localhost:5000

---

## 🌐 Web3 + IPFS Setup
### 1. Compile & Deploy Contract (using Hardhat)
```
cd contract
npm install
npx hardhat compile
npx hardhat run scripts/deploy.js --network <network>
```
### 2. Store Output in IPFS (using web3.storage)
Set your token in the environment and use the API from Python to upload results.

🧠 ML Model Training (Optional)
```
# backend/ml_model/retrain_model.py

from sklearn.tree import DecisionTreeClassifier
import joblib

# Example dummy training data
X = [[1, 2], [2, 3], [3, 4]]
y = ["Low", "Medium", "High"]

model = DecisionTreeClassifier()
model.fit(X, y)

joblib.dump(model, "model.pkl")
```

## 📝 License
MIT License. See LICENSE for more information.

## ✨ Credits
Kaustav – DevOps, Cloud & Blockchain Developer

### Powered by OpenAI, Chainlink, Flask, Hardhat, IPFS

## 🤝 Contributing
Pull requests welcome. Open issues for ideas, bugs, or feature suggestions.

## 📬 Contact
📨 ![LinkedIn](https://www.linkedin.com/in/kaustav-dey-107593244)
📨 ![Twitter](https://x.com/KaustavDey357)
📨 ![Portfolio](https://kaustavdey357.github.io/)
