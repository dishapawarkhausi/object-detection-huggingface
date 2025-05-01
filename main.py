import requests
import os
import dotenv
import json
from PIL import Image
import matplotlib.pyplot as plt

# Load environment variables from .env file
dotenv.load_dotenv()

# Get API Token from environment variable
API_TOKEN = os.getenv("API_TOKEN")
if not API_TOKEN:
    raise ValueError("❌ API_TOKEN is missing! Please check your .env file.")

# Hugging Face API URL (DETR model for object detection)
API_URL = "https://api-inference.huggingface.co/models/facebook/detr-resnet-50"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def detect_objects(image_path):
    """Send an image to the Hugging Face API and display detected objects."""

    # Load image
    with open(image_path, "rb") as f:
        image_data = f.read()

    # Send request to Hugging Face API
    response = requests.post(API_URL, headers=headers, data=image_data)

    try:
        predictions = response.json()  # Convert response to JSON
    except json.JSONDecodeError:
        print("❌ Error: Unable to decode JSON response from API.")
        print("API Response:", response.text)  # Print response for debugging
        return

    # Check if API response contains an error
    if isinstance(predictions, dict) and "error" in predictions:
        print(f"❌ API Error: {predictions['error']}")
        return

    # Open image for visualization
    img = Image.open(image_path)
    plt.imshow(img)

    # Draw bounding boxes on detected objects
    for obj in predictions:
        if "box" in obj and "label" in obj and "score" in obj:
            box = obj["box"]
            label = obj["label"]
            score = obj["score"]

            x, y, w, h = box["xmin"], box["ymin"], box["xmax"] - box["xmin"], box["ymax"] - box["ymin"]

            # Draw rectangle around detected objects
            plt.gca().add_patch(plt.Rectangle((x, y), w, h, fill=False, edgecolor="green", linewidth=1))
            plt.text(x, y, f"{label} ({score:.2f})", color="blue", fontsize=10)
        else:
            print("⚠️ Unexpected response format:", obj)  # Debugging info

    plt.axis("off")
    plt.show()

# Run object detection
image_path = "man.jpg"  # Replace with your image file
detect_objects(image_path)
