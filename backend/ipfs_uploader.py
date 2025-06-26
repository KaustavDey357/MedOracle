import os
import requests

# set this in .env or directly in code
WEB3_STORAGE_TOKEN = os.getenv("WEB3_STORAGE_TOKEN")


def upload_file_to_ipfs(filepath):
    if not WEB3_STORAGE_TOKEN:
        raise Exception("Missing Web3.Storage API token")

    headers = {
        "Authorization": f"Bearer {WEB3_STORAGE_TOKEN}",
    }

    with open(filepath, "rb") as f:
        files = {
            'file': (os.path.basename(filepath), f)
        }
        response = requests.post(
            "https://api.web3.storage/upload",
            headers=headers,
            files=files
        )

    if response.status_code != 200:
        raise Exception(f"Upload failed: {response.text}")

    cid = response.json()["cid"]
    print(f"✅ File uploaded to IPFS: https://{cid}.ipfs.w3s.link")
    return cid
