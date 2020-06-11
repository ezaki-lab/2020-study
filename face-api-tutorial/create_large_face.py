import logging
import requests
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
# loggerのエラーが出ないおまじない
logger = logging.getLogger('face_api')

# サブスクリプションキー
subscription_key = '############################'
# largeFaceListId
largeFaceListId = "b-face-list"
# base_url
face_api_url = '##############################/face/v1.0'

# LeargeFaceListを作る
def create_large_face():
    url = f"{face_api_url}/largefacelists/{largeFaceListId}"

    headers = {
        'Content-Type': "application/json",
        'Ocp-Apim-Subscription-Key': subscription_key,
    }

    params = {
        'name': largeFaceListId
    }

    try:
        response = requests.put(url, json=params, headers=headers, timeout=10)
    except requests.exceptions.RequestException as e:
        logger.error({
            'action': 'create_large_face_list', 'message': e
            })
        print("TimeoutError")
        raise
    except requests.exceptions.ConnectTimeout as e:
        logger.error({
            'action': 'create_large_face_list', 'message': e
            })
        raise
    except:
        logger.error(
            {'action': 'create_large_face_list', 'message': "unknown error"})
        raise

create_large_face()
