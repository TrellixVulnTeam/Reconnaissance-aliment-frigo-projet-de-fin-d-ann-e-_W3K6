#!/usr/bin/env python

from __future__ import print_function
import requests
import json
import cv2

addr = 'http://e65a7b58d83f.ngrok.io'
test_url = addr + '/recognition'

# prepare headers for http request
content_type = 'image/jpeg'
headers = {'content-type': content_type}

img = cv2.imread('panier.jpg')
# encode image as jpeg
_, img_encoded = cv2.imencode('.jpg', img)
# send http request with image and receive response
response = requests.post(test_url, data=img_encoded.tostring(), headers=headers)
# decode response
print(json.loads(response.text))

