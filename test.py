
from transformers import ViTImageProcessor, ViTForImageClassification
from PIL import Image
import requests
import torch

# Load an image from URL
url = "http://images.cocodataset.org/val2017/000000039769.jpg"
image = Image.open(requests.get(url, stream=True).raw).convert("RGB")

# Load processor and model locally (public model)
processor = ViTImageProcessor.from_pretrained("google/vit-base-patch16-224")
model = ViTForImageClassification.from_pretrained("google/vit-base-patch16-224")

# Preprocess image
inputs = processor(images=image, return_tensors="pt")

# Run model
with torch.no_grad():
    outputs = model(**inputs)

# Get prediction
logits = outputs.logits
predicted_class_idx = logits.argmax(-1).item()
print("Predicted class:", model.config.id2label[predicted_class_idx])
