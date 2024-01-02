import json
import os
import requests

batches = [1, 2, 3, 4]

def get_transactions(access_key, token, batch):
    base_url = "https://www.ura.gov.sg/uraDataService/invokeUraDS?service=PMI_Resi_Transaction&batch={batch}"
    url = base_url.format(batch=batch)
    headers = {
        "AccessKey": f"{access_key}",
        "Token": f"{token}",
        "User-Agent": "PostmanRuntime/7.28.4"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        transactions = json.loads(response.content.decode('ISO-8859-1'))
        return transactions
    else:
        return None

def get_token(access_key):
    url = "https://www.ura.gov.sg/uraDataService/insertNewToken.action"
    headers = {
        "AccessKey": f"{access_key}",
        "User-Agent": "PostmanRuntime/7.28.4"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        token = json.loads(response.content.decode('utf-8'))['Result']
        return token
    else:
        return None

def print_external_ip():
    response = requests.get('https://curlmyip.org/')
    external_ip = response.text
    print(f"EXTERNAL_IP: {external_ip}")
    return external_ip

def get_access_key():
    access_key = os.getenv('ACCESS_KEY')
    return access_key