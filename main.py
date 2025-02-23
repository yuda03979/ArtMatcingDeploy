from fastapi import FastAPI
from src.art_matching import ArtMatching

app = FastAPI()
art_matching = ArtMatching()


@app.post('/insert_image')
def insert_image(image) -> bool:
    # should return bool
    return art_matching.insert_image(image)


@app.post('/del_image')
def del_image(image_id) -> bool:
    return art_matching.del_image(image_id)


@app.post('/get_matching_images')
def get_matching_images(data):
    # should return list of ids
    return art_matching.get_matching_images(data)


@app.get('/get_existing_images')
def get_existing_images():
    # should return list of ids
    return art_matching.get_existing_images()


@app.post('/get_image_data')
def get_image_data(image_id):
    return art_matching.get_image_data(image_id)
