import requests
import sys  

image_url = sys.argv[1]

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