from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)
upload_directory = './uploads'
if not os.path.exists(upload_directory):
    os.makedirs(upload_directory)


@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    image = request.files['image']
    if image.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    filename = os.path.join(upload_directory, image.filename)
    image.save(filename)

    return jsonify({'image_url': request.host_url + 'uploads/' + image.filename}), 201


@app.route('/image/<filename>', methods=['GET'])
def get_image(filename):
    content_type = request.headers.get('Content-Type')
    filepath = os.path.join(upload_directory, filename)
    if os.path.exists(filepath):
        if content_type == 'text':
            return jsonify({'image_url': request.host_url + 'uploads/' + filename}), 200
        elif content_type == 'image':
            return send_from_directory(upload_directory, filename)
        else:
            return jsonify({'error': 'Unsupported Content-Type'}), 400
    else:
        return jsonify({'error': 'Image not found'}), 404


@app.route('/delete/<filename>', methods=['DELETE'])
def delete_image(filename):
    filepath = os.path.join(upload_directory, filename)
    if not os.path.exists(filepath):
        return jsonify({'error': 'Image not found'}), 404

    os.remove(filepath)
    return jsonify({'message': f'Image {filename} deleted'}), 200


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 8080
    app.run(host=host, port=port, debug=True)




import requests

# URL для серверних операцій (приклад URL)
base_url = "https://example.com/files"
def upload_picture():
    # 1. Завантаження зображення через POST
    upload_url = f"{base_url}/upload"
    file_path = "pyrozhochok.jpeg"
    with open(file_path, 'rb') as file:
        files = {'file': file}
        post_response = requests.post(upload_url, files=files)

        if post_response.status_code == 200:
            upload_data = post_response.json()
            file_id = upload_data.get('id')
            print(f"Файл завантажено. ID: {file_id}")
        else:
            print(f"Помилка завантаження: {post_response.status_code}")
upload_picture()
"""
# 2. Отримання посилання на файл через GET
get_url = f"{base_url}/{file_id}"
get_response = requests.get(get_url)
"""
"""
if get_response.status_code == 200:
    file_data = get_response.json()
    file_link = file_data.get('url')  # Припустимо, сервер повертає URL файлу
    print(f"Посилання на файл: {file_link}")
else:
    print(f"Помилка отримання файлу: {get_response.status_code}")
    exit()

# 3. Видалення файлу через DELETE
delete_url = f"{base_url}/{file_id}"
delete_response = requests.delete(delete_url)

if delete_response.status_code == 200:
    print("Файл успішно видалено.")
else:
    print(f"Помилка видалення файлу: {delete_response.status_code}")"""

