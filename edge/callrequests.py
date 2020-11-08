import os
import requests
from datetime import datetime

BASE_URL = 'http://35.198.189.129:443/smartbin/api/v1/bins'


def send_bin_open_info(card_id, bin_id, bin_type, weight):
    url = BASE_URL + "/bin_opened"
    data = {
        "card_id": card_id,
        "bin_id": bin_id,
        "bin_type": bin_type,
        "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        "weight": weight
    }
    data = requests.post(url, json=data)
    return data.json()


def send_update_bin_status(bin_id, waste_status):
    url = BASE_URL + "/update_bin_status"
    data = {
        "bin_id": bin_id,
        "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        "waste_status": waste_status
    }
    requests.post(url, json=data)

def analyze_image(transaction_id, image_path):
    url = BASE_URL + "/upload_image/" + transaction_id
    with open(image_path, 'rb') as img:
        name_img= os.path.basename(image_path)
        files= {'file': (name_img,img,'multipart/form-data', {'Expires': '0'})}
        with requests.Session() as s:
            r = s.post(url, files=files)
            print(r.status_code)


if __name__ == "__main__":
    data = send_bin_open_info('12,45,78,85', 2, 'PAPER', 1458)
    trans_id = data['transaction_id']
    file_path = 'paper.jpg'
    analyze_image(trans_id, file_path)

    print('running')



    #send_update_bin_status(1, 0)