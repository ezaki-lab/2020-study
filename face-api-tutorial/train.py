import os
import requests
import logging
import io
import cv2
import time
import datetime

# loggerのエラーが出ないおまじない
logger = logging.getLogger('face_api')

# サブスクリプションキー
subscription_key = '####################################'
# largeFaceListId
largeFaceListId = "b-face-list"
# base_url
face_api_url = '##############################################/face/v1.0'

# LargeFaceListを学習させる
def train_LargeFaceList():
    url = f"{face_api_url}/largefacelists/{largeFaceListId}/train"

    headers = {
        'ocp-apim-subscription-key': subscription_key,
    }

    try:
        requests.post(url, headers=headers, timeout=10)
    except requests.exceptions.RequestException as e:
        logger.error({
            'action': 'train_large_face_list',
            'message': e
        })
        raise
    except:
        logger.error(
            {'action': 'train_large_face_list', 'message': "unknown error"})
        raise

    logger.info({
        'action': 'train_large_face_list',
        'message': f'training face list {largeFaceListId}'
    })

# 新規の人の顔情報を登録する
def add_LargeFace_with_FaceId(imageData):
    url = f"{face_api_url}/largefacelists/{largeFaceListId}/persistedfaces"

    headers = {
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': subscription_key,
    }

    params = {
        'userData' : 1
    }

    response = requests.post(url, params=params,data=imageData, headers=headers, timeout=10)
    add_LargeFace = response.json()
    add_LargeFace['userData'] = 1
    print("add_LF", add_LargeFace)
    return add_LargeFace

# 新規に追加したい顔をadd_add_LargeFace_with_FaceIdに送る   
def newface_add_LargeFaceList():
    image_data = io.open(os.path.join(__location__,'img/img.jpg'), 'rb')
    add_LargeFace = add_LargeFace_with_FaceId(image_data)
    
    print("add_LF_result", add_LargeFace)
    similar_id = add_LargeFace['persistedFaceId']
    return similar_id

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

image_data = io.open(os.path.join(__location__,'img/img.jpg'), 'rb')
add_LargeFace_with_FaceId(image_data)
train_LargeFaceList()

