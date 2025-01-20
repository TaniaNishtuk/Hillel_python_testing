import requests

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}

response = requests.get(url, params=params)
photos = response.json().get('photos', [])

# скачую перші два фото
for i, photo in enumerate(photos[:2], start=1):
    img_url = photo['img_src']
    img_data = requests.get(img_url).content
    with open(f'photo{i}.jpg', 'wb') as file:
        file.write(img_data)
    print(f'Фото {i} збережено')
