import os
import numpy as np
import cv2
import torch
import torchvision.transforms as transforms
import torchvision.models as models
import time
import onnxruntime as ort
from ultralytics import YOLO

# Define models for benchmarking
MODELS = {
    "mobilenet_v3": models.mobilenet_v3_small(pretrained=True),
    "efficientnet_v2": models.efficientnet_v2_s(pretrained=True),
    "resnet18_int8": models.resnet18(pretrained=True),
    "vision_transformer": models.vit_b_16(pretrained=True)
}

# Ensure test image directory exists
IMAGE_DIR = "test_images"
os.makedirs(IMAGE_DIR, exist_ok=True)

def preprocess_image(image_path):
    """ Preprocess image for models. """
    image = cv2.imread(image_path)
    image = cv2.resize(image, (224, 224))
    image = transforms.ToTensor()(image).unsqueeze(0)
    return image

def generate_test_images(num_images=5):
    """ Generate random test images. """
    image_paths = []
    for i in range(num_images):
        image = np.random.randint(0, 256, (224, 224, 3), dtype=np.uint8)
        path = os.path.join(IMAGE_DIR, f"image_{i}.jpg")
        cv2.imwrite(path, image)
        image_paths.append(path)
    return image_paths

def benchmark_model(model_name, model, image_paths):
    """ Benchmark a model. """
    total_time = 0
    num_images = len(image_paths)

    for image_path in image_paths:
        image = preprocess_image(image_path)
        start_time = time.time()
        model.eval()
        with torch.no_grad():
            _ = model(image)
        total_time += time.time() - start_time

    avg_time = total_time / num_images
    return avg_time

# Generate images
test_images = generate_test_images()

# Benchmark each model and print results
results = {}
for model_name, model in MODELS.items():
    print(f"Running inference for {model_name}")
    avg_time = benchmark_model(model_name, model, test_images)
    results[model_name] = avg_time
    print(f"{model_name}: {avg_time:.4f} seconds per image\n")

# Print final results summary
print("\nFINAL BENCHMARK RESULTS:")
for model_name, avg_time in results.items():
    print(f"{model_name}: {avg_time:.4f} seconds per image")