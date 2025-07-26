# ReparoEarth


# ♻️ Reparo Earth – Waste-to-Wonder Platform (Azure Implementation)

This project implements an AI-powered, modular system on Microsoft Azure for environmental sustainability. Inspired by the magical world of Harry Potter, it features intelligent agents that manage waste classification, conversion suggestions, and routing visualizations.

---

## 🔧 Architecture Overview

```
Users (Web/Mobile)
       │
Azure API Management (APIM)
 ┌─────┼──────────────┬──────────────────────────────┐
 ▼     ▼              ▼
Sorting Hat      Muggle-Magic             Marauder’s Map
(Waste Classifier)  Converter               (Heatmap & Routing)
```

---

## 🧠 Agents & Azure Components

### 1. **Sorting Hat (Auto Waste Classifier)**
- **Purpose**: Classifies waste images into categories like plastic, organic, e-waste, etc.
- **Azure Services Used**:
  - Azure **Function App**: Handles image input and API trigger
  - Azure **Custom Vision**: Pretrained image classification model
  - Azure **Blob Storage**: Stores input/output images
- **Flow**:
  - Users upload an image via APIM
  - Function App calls Custom Vision Prediction API
  - Result is returned with waste category

---

### 2. **Muggle-Magic Converter**
- **Purpose**: Provides eco-friendly upcycling or reuse ideas for the classified waste
- **Azure Services Used**:
  - Azure **Function App**: Handles logic and request flow
  - Azure **OpenAI (GPT-4)**: Suggests conversion ideas or reuse tips
- **Flow**:
  - Waste category is passed to Function App
  - OpenAI generates a sustainability suggestion
  - Response is sent back to the user via APIM

---

### 3. **Marauder’s Map (Heatmap & Routing Intelligence)**
- **Purpose**: Shows waste collection hotspots and optimal collection routes
- **Azure Services Used**:
  - Azure **Function App**: Aggregates and formats geospatial data
  - Azure **Maps APIs**: Provides heatmap visualization and routing info
- **Flow**:
  - Function App processes location data
  - Azure Maps API visualizes it on a map
  - Output returned to the user for field-level insights

---

## 🔌 API Management

All interactions between users and backend services are secured and managed via **Azure API Management (APIM)**. This helps expose and monitor APIs safely.

---

## 🛠️ Prerequisites

- Azure Subscription
- Azure CLI or Azure Portal access
- Pretrained Custom Vision model (with Prediction URL and Key)
- OpenAI access via Azure (with deployment and endpoint info)
- Azure Maps account (with keys)

---

## 🚀 Deployment Steps

### 1. Set up Resources

Provision the following in Azure:
- Function Apps (3)
- Custom Vision (Training + Prediction resource)
- Blob Storage (Container for images)
- Azure OpenAI resource (GPT-4 deployment)
- Azure Maps (with API keys)
- API Management instance

### 2. Deploy Functions

Each agent has its own Function App (in Python or C#):
- Sorting Hat: `waste-classifier-function`
- Muggle-Magic: `upcycling-suggester-function`
- Marauder’s Map: `heatmap-router-function`

Use VS Code + Azure Functions extension or deploy via CLI.

```bash
func azure functionapp publish <FunctionAppName>
```

### 3. Integrate with APIM

- Import each function's HTTP trigger into APIM
- Define proper routes and policies
- Secure with API keys or OAuth as needed

---

## 📦 Sample Input/Output

### Sorting Hat
- **Input**: JPEG image of a waste item
- **Output**: `{"label": "Plastic", "confidence": 92.5}`

### Muggle-Magic Converter
- **Input**: `"Plastic"`
- **Output**: `"You can reuse this plastic bottle to make a bird feeder or planter!"`

### Marauder’s Map
- **Input**: Coordinates or area ID
- **Output**: GeoJSON or rendered heatmap route

---

## 📊 Monitoring

- **Azure Application Insights**: Enable for each Function App
- **APIM Analytics**: For traffic, latency, and error tracking

---

## 🧙 Magic Tech Stack

| Layer            | Azure Services                                      |
|------------------|------------------------------------------------------|
| APIs             | Azure API Management                                |
| AI/ML Layer      | Azure Custom Vision, Azure OpenAI, Azure Functions  |
| Storage          | Azure Blob Storage                                  |
| Mapping & Geo    | Azure Maps APIs                                     |
| Monitoring       | Azure Monitor, App Insights                         |

---

## 📁 Folder Structure (Optional Codebase)

```bash
reparo-earth/
├── sorting-hat/
│   └── waste_classifier_function.py
├── muggle-magic/
│   └── converter_function.py
├── marauders-map/
│   └── routing_function.py
├── shared/
│   └── config.json
├── README.md
```

---

## 📫 Contact

For help, suggestions, or magic debugging, reach out to the project wizard team or open an issue.
