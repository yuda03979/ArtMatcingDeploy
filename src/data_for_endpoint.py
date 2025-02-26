import os
import requests


image_dir = ''
FASTAPI_URL = 'http://localhost:8000/insert_arts'

data = []
for filename in os.listdir(image_dir):
    if filename.endswith(".jpg"):  # Ensure it's an image file
        img_id = os.path.splitext(filename)[0]  # Extract ID from filename (without extension)
        image_path = os.path.join(image_dir, filename)

        data.append({
            "id": int(img_id),  # Convert ID to integer
            "url": filename,  # FastAPI expects 'url' to be the filename
            "name": "string",  # Placeholder name, update as needed
            "size": [0, 0]
        })


def send_data_to_fastapi(data):
    try:
        response = requests.post(FASTAPI_URL, json=data)
        if response.status_code == 200:
            print("Data successfully sent to FastAPI")
        else:
            print(f"Error: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"Failed to send data: {e}")


# Send the extracted data
send_data_to_fastapi(data)