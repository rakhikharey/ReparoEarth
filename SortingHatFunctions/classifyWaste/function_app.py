import azure.functions as func
import logging
import requests
import os

from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

app = func.FunctionApp()

# Azure Custom Vision config (move sensitive data to Key Vault)
PREDICTION_URL = os.environ["PREDICTION_URL"]
KEY_VAULT_URL = os.environ["KEY_VAULT_URL"]
SECRET_NAME = os.environ["PREDICTION_KEY_NAME"]  # Name of secret in Key Vault

# Fetch secret from Azure Key Vault
def get_prediction_key():
    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=KEY_VAULT_URL, credential=credential)
    return client.get_secret(SECRET_NAME).value

@app.route(route="classifyWaste", auth_level=func.AuthLevel.FUNCTION)
def classifyWaste(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("♻️ Sorting Hat Waste Classifier triggered.")

    try:
        # Get uploaded file
        file = req.files.get('file')
        if not file:
            return func.HttpResponse("❌ No file uploaded. Use 'file' as form-data key.", status_code=400)

        image_data = file.stream.read()

        # Get secret key from Key Vault
        prediction_key = get_prediction_key()

        headers = {
            'Prediction-Key': prediction_key,
            'Content-Type': 'application/octet-stream'
        }

        response = requests.post(PREDICTION_URL, headers=headers, data=image_data)

        if response.status_code != 200:
            return func.HttpResponse(f"❌ Prediction failed: {response.text}", status_code=500)

        return func.HttpResponse(response.text, status_code=200, mimetype="application/json")

    except Exception as e:
        logging.exception("❌ Error processing request.")
        return func.HttpResponse(f"❌ Server error: {str(e)}", status_code=500)
