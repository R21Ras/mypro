#!/usr/bin/env python

import os
import requests
import sys  

# Read the port from the environment or use a default (5000)
port = int(os.environ.get("PORT", 5000))
print(f"Running on port {port}")

def process_image(image_url):
    api_url = "https://detect.roboflow.com/foods-czdnp/3"
    api_key = "GgvL6bZqnfCkqC1yDmHL"

    params = {
        "api_key": api_key,
        "image": image_url
    }

    try:
        response = requests.post(api_url, params=params)
        response.raise_for_status()  
        result = response.json()

        class_counts = {}
        for prediction in result["predictions"]:
            class_name = prediction["class"]
            class_counts[class_name] = class_counts.get(class_name, 0) + 1

        result_array = [{"class": class_name, "count": count} for class_name, count in class_counts.items()]

        print(result_array)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <image_url>")
        sys.exit(1)

    image_url = sys.argv[1]
    process_image(image_url)
