import base64

with open('image/000000.jpg', 'rb') as image_file:
    image_data = image_file.read()
    image_base64 = base64.b64encode(image_data).decode('utf-8')
    image_url = f'data:image/jpeg;base64,{image_base64}'
    print(image_url)