import os
import sys
from io import BytesIO
import requests

subscription_key = os.getenv("MSV_SUBSCRIPTION_KEY")
endpoint = os.getenv("MSV_ENDPOINT")
analyze_url = endpoint + "vision/v3.1/analyze"


def recognize_image(image):
    '''
    Describe an Image
    This example describes the contents of an image with the confidence score.
    '''
    #image_data = image.read()

    # Call API
    headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/octet-stream'}
    params = {'visualFeatures': 'Categories,Description,Color'}
    response = requests.post(analyze_url, headers=headers, params=params, data=image)
    analysis = response.json()
    tags = analysis["description"]["tags"]
    captions = analysis["description"]["captions"][0]["text"]
    words = ' '.join(tags) + ' ' + captions
    words = words.split()

    print(words)

    # PACKAGING_CHECKER
    if any([x in words for x in ['plastic', 'can', 'aluminum']]):
        return 'PACKAGING'
    # GLASS_CHECKER
    elif any([x in words for x in ['glass']]):
        return 'GLASS'
    # PAPER_CHECKER
    elif any([x in words for x in ['paper']]):
        return 'PAPER'
    else:
        return 'NOT_FOUND'
    


