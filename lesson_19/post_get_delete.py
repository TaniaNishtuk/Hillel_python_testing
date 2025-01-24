import requests

base_url = "http://127.0.0.1:8080"

# picture to upload
file_path = "pyrozhochok.jpeg"
post_url = 'upload'

# POST request to upload picture
def upload_picture(file):
    upload_url = f"{base_url}/{post_url}"
    with open(file, 'rb') as file:
        picture = {'image': file}
        post_response = requests.post(upload_url, files=picture)

    if post_response.status_code == 201:
        upload_data = post_response.json()
        print(f"Picture uploaded successfully: {upload_data}")
        return upload_data
    else:
        print(f"Failed to upload picture: {post_response.status_code}")

# uploading picture to the server
upload_picture(file_path)


# GET request to retrieve the image
def get_image(file):
    get_url = f"{base_url}/image/{file}"
    get_headers = {'Content-Type': 'text'}  # Request JSON format response
    get_response = requests.get(get_url, headers=get_headers)

    if get_response.status_code == 200:
        get_data = get_response.json()
        print(f"Picture details retrieved: {get_data}")
    else:
        print(f"Failed to get picture: {get_response.status_code}")

# getting picture from the server
get_image(file_path)


# Delete request to delete the image
def delete_image(file):
    delete_url = f"{base_url}/delete/{file}"
    delete_response = requests.delete(delete_url)

    if delete_response.status_code == 200:
        delete_data = delete_response.json()

        print(f"Picture '{file_path}' deleted successfully. Server response {delete_data}")
    else:
        print(f"Failed to delete picture: {delete_response.status_code}")

# deleting picture from the server
delete_image(file_path)

