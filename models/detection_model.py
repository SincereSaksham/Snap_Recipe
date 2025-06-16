from transformers import DetrImageProcessor, DetrForObjectDetection
from PIL import Image
import torch

# Load model and processor
processor = DetrImageProcessor.from_pretrained("facebook/detr-resnet-50")
model = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-50")

device = torch.device("cpu")
model.to(device)

def detect_objects(image: Image.Image, threshold: float = 0.9):
    if image.mode != "RGB":
        image = image.convert(mode="RGB")

    inputs = processor(images=image, return_tensors="pt").to(device)
    outputs = model(**inputs)

    target_sizes = torch.tensor([image.size[::-1]])
    results = processor.post_process_object_detection(outputs, target_sizes=target_sizes, threshold=threshold)[0]

    labels = [model.config.id2label[label.item()] for label in results["labels"]]
    return labels
