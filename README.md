# 🧠 Object Detection with Hugging Face API (DETR Model)

This project performs object detection using the [facebook/detr-resnet-50](https://huggingface.co/facebook/detr-resnet-50) model via the Hugging Face Inference API. It processes an image, detects objects, and displays bounding boxes with labels and confidence scores.

---

## 📌 Features

- 🔍 Detects multiple objects in an image using DETR model.
- 🖼️ Visualizes bounding boxes and labels using `matplotlib`.
- 🔐 Uses environment variables to securely store API tokens.
- ⚙️ Clean and minimal Python code.

---

## 📁 Project Structure

```
object-detection-huggingface/
│
├── main.py               # Main script to perform object detection
├── requirements.txt      # Required Python packages
├── .env.example          # Sample environment variable file
├── man.jpg               # Sample image (you can replace it)
└── README.md             # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/dishapawarkhausi/object-detection-huggingface.git
cd object-detection-huggingface
```

### 2. Install Dependencies

Use pip to install the required packages:

```bash
pip install -r requirements.txt
```

### 3. Set Up API Key

- Create a `.env` file by copying the example:

```bash
cp .env.example .env
```

- Add your Hugging Face API token inside `.env`:

```
API_TOKEN=your_huggingface_api_token_here
```

You can get your token by signing up at [huggingface.co](https://huggingface.co/).

---

## 🧪 Usage

### Replace or add your image

Ensure you have an image file in the root directory. By default, the script uses:

```python
image_path = "man.jpg"
```

You can change it to any other file name.

### Run the script

```bash
python main.py
```

This will open a window showing the detected objects with bounding boxes and labels.

---

## 🖼️ Sample Output

> Detected objects will be visualized using `matplotlib`, like this:

```
[object name] (confidence)
[bounding box]
```

---

## 🔧 Customization

- Replace `facebook/detr-resnet-50` in the API URL to try other models from Hugging Face.
- Extend visualization using `cv2`, `streamlit`, or any GUI framework for custom apps.

---

## 📚 Technologies Used

- [Python](https://www.python.org/)
- [Hugging Face Inference API](https://huggingface.co/inference-api)
- [matplotlib](https://matplotlib.org/)
- [Pillow (PIL)](https://pillow.readthedocs.io/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

---

## 👩‍💻 Author

**Disha Pawar**  
🌐 [GitHub Profile](https://github.com/dishapawarkhausi)  
🧠 AI/ML Enthusiast | Python Developer  

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
