import azure.functions as func
import logging
import requests

app = func.FunctionApp()

# Azure Custom Vision config
PREDICTION_URL = "https://sortinghattraining-prediction.cognitiveservices.azure.com/customvision/v3.0/Prediction/fa6916f4-1d77-4a4c-bb20-2177d6637199/classify/iterations/WasteClassificationIteration1/image"
PREDICTION_KEY = "7rL9C5goaOwqnWGSCFzUqdEmIxgAd4kvIPf2kPAnBaXlU9XkfNCYJQQJ99BGACYeBjFXJ3w3AAAIACOG6fJJ"

@app.route(route="classifyWaste", auth_level=func.AuthLevel.FUNCTION)
def classifyWaste(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("♻️ Sorting Hat Waste Classifier triggered.")

    try:
        # Expecting file upload as form-data with key "file"
        file = req.files.get('file')
        if not file:
            return func.HttpResponse("❌ No file uploaded. Use 'file' as form-data key.", status_code=400)

        image_data = file.stream.read()

        headers = {
            'Prediction-Key': PREDICTION_KEY,
            'Content-Type': 'application/octet-stream'
        }

        response = requests.post(PREDICTION_URL, headers=headers, data=image_data)

        if response.status_code != 200:
            return func.HttpResponse(f"❌ Prediction failed: {response.text}", status_code=500)

        return func.HttpResponse(response.text, status_code=200, mimetype="application/json")

    except Exception as e:
        logging.exception("❌ Error processing request.")
        return func.HttpResponse(f"❌ Server error: {str(e)}", status_code=500)
