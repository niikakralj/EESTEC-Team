import time
import random as rd
from MFRC522_python import Read_api as ra
import callrequests as rq
import getDistance as gd
while True:
    uid=ra.read_card()
    dist=gd.getDistance()
    uid = ''.join([str(x) for x in uid])
    print uid
    bin_id = rd.randint(1,10)
    data = rq.send_bin_open_info(uid, bin_id, 'GLASS', rd.randint(1000,10000))
    trans_id = data['transaction_id']
    file_path = 'glass.jpg'
    rq.analyze_image(trans_id, file_path)
    rq.send_update_bin_status(bin_id, dist)
    time.sleep(2)