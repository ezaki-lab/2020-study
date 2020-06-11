# Face-API-Tutorial

[qiita](https://qiita.com/YutoTakamatsu/private/017ad395076899abbc37)

# Azure portalでFace APIを使えるようにする。
AzureのFaceAPIを利用するためには、FaceAPIのリソースを作成します。
[Azure Portal](https://azure.microsoft.com/ja-jp/features/azure-portal/)


<img width="745" alt="スクリーンショット 2020-06-10 23.04.31.png" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/517357/3a1d97a2-c838-3e7b-7d90-15cdb2808dd1.png">

リソース作成をクリックします。

<img width="721" alt="スクリーンショット 2020-06-10 23.05.52.png" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/517357/7311636e-522f-6a59-7f27-0fbf329eb3d4.png">

クリックすると新規作成のページに行くので、検索ボックスにfaceと入力します。

<img width="1436" alt="スクリーンショット 2020-06-10 23.07.39.png" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/517357/fbd63072-cc3d-588a-e23b-c806a31f7db4.png">

作成ボタンを押します。

<img width="1438" alt="スクリーンショット 2020-06-10 23.09.02.png" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/517357/67bc7d11-1d82-1c67-5ad2-19418e36080b.png">

`名前`は適当に入力してください。
`サブスクリプション`はAzure for Studentsを選択してください。
`場所`は東日本を選択してください。
`価格レベル`は、Standard S0を選択してください。
`リソースグループ`は適当に選択してください。

<img width="1436" alt="スクリーンショット 2020-06-10 23.13.05.png" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/517357/79586ea5-9d03-b3de-7432-c196905ef542.png">

この画面が出力されていればFace APIのリソースを作成できています。

# Face APIの仕組み
FaceAPIで人物の顔を登録して、それを学習させる過程としては、まず、人物の集合であるグループを定義する必要があります。


# pythonでカメラを起動

今回は、pythonでカメラを起動して、カメラから顔を取得し、新規の顔はグループを定義して、学習して、次からはその人はリピーターですというふうに出力されるようにしてみたいと思います。

```python:camera.py
import cv2
import time
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
# カメラの映像を取得
cap = cv2.VideoCapture(0)
# カスケード型識別器の読み込み
cascade = cv2.CascadeClassifier(os.path.join(__location__,"haarcascade_frontalface_default.xml"))
i=0
while True:
    time.sleep(1)

    # 入力画像の読み込み
    ret, img = cap.read()
    # グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 顔領域の探索
    face = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=8, minSize=(30, 30))

    # 顔領域を赤色の矩形で囲む
    for (x, y, w, h) in face:
        cv2.rectangle(img, (x, y), (x + w, y+h), (0,0,300), 4)

    for rect in face:
        i+=1

        # 顔だけ切り出して保存
        x = rect[0]
        y = rect[1]
        width = rect[2]
        height = rect[3]
        dst = img[y:y+height, x:x+width]
        # new_image_path = dir_path + '/' + str(i) + path[1];
        cv2.imwrite(os.path.join(__location__, 'img/img.jpg'), dst)
        cv2.waitKey(1)

        # ビデオを表示
        cv2.imshow('video image', img)
        # 結果を出力
        cv2.imwrite("result.jpg",img)
```

このプログラムを動かすとパソコンのカメラを起動して、顔領域を切り出すことができます！
プログラムを動かすと、パソコンのカメラが起動され、自分の顔が赤い四角で囲まれていると思います。
その画像がimg/img.jpgとして保存されます！

#Large Face Listを作成！
次に、Large Face Listというグループを作成します！
その際に、APIに接続する時のサブスクリプションキーが必要となるのでそれを確認します。
<img width="1436" alt="スクリーンショット 2020-06-11 0.49.49.png" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/517357/70b37b2e-793b-db0f-1524-5233ff61e6ed.png">

先ほど作成したface apiのキーとエンドポイントを確認することができます！

確認して右側にあるコピーボタンをクリックしコピーします。

```python:create_large_face.py
import logging
import requests
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
# loggerのエラーが出ないおまじない
logger = logging.getLogger('face_api')

# サブスクリプションキー
subscription_key = '###################################'
# largeFaceListId
largeFaceListId = "b-face-list"
# base_url
face_api_url = '#######################################/face/v1.0'

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
```
サブスクリプションキーの部分を先ほどコピーしたものに書き換えてください。
base_urlの部分を先ほどコピーしたエンドポイントに書き換えてください。
最後に/face/v1.0を加えることに注意してください。

# Large Face Listをtrainする！

先ほど作成したLarge Face Listをtrainします！
そのためには、img/img.jpgが自分の顔になっている状態でtrain.pyを実行してください。

```python:train.py
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
subscription_key = '############################'
# largeFaceListId
largeFaceListId = "b-face-list"
# base_url
face_api_url = '#############################################/face/v1.0'

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
```

今回もサブスクリプションキーと、エンドポイントを変更してください。

# 顔を認識して年齢と性別を取り出してみよう！
顔認識をして年齢と性別を取り出してみましょう。
さらに、一度認識された顔かどうかを認識することもできます。

```python:detect.py
import os
import requests
import logging
import io
import cv2
import time
import datetime

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# loggerのエラーが出ないおまじない
logger = logging.getLogger('face_api')

# サブスクリプションキー
subscription_key = '##################################'
# largeFaceListId
largeFaceListId = "b-face-list"
# base_url
face_api_url = '#########################################/face/v1.0'

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
                
    logger.info({
        'action': 'create_large_face_list',
        'message': f'success to create large face list {largeFaceListId}'
        })
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

# LargeFace一覧を取得する
def get_LargeFaceList():
    url = f"{face_api_url}/largefacelists"

    params = {
        'returnRecognitionModel': 'false'
    }

    headers = {
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': subscription_key,
    }

    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
    except requests.exceptions.RequestException as e:
        logger.error(
            {'action': 'get_large_face_list', 'message': e})
        raise
    except requests.exceptions.ConnectTimeout:
        print("TimeoutError")

    result = response.json()
    print("get_LFL", result)

# 検出した顔から詳細を取得
def faceId_detect(image_data):
    print("detect_in")
    url = f"{face_api_url}/detect"

    params = {
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'age,gender',
    }
            
    headers = {
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': subscription_key,
    }
    try:
        response = requests.post(url, params=params, headers=headers, data=image_data, timeout=10)
        detect_result = response.json()
        
        faceId = detect_result[0]['faceId']
        gender = detect_result[0]['faceAttributes']['gender']
        age = int(detect_result[0]['faceAttributes']['age'])
        print("detect", faceId, gender, age)
        return faceId, gender, age

    except requests.exceptions.RequestException as e:
        logger.error({
            'action': 'faceId_detect', 'message': e
            })
        raise
    except:
        logger.error(
            {'action': 'faceId_detect', 'message': "unknown error"})
        raise

# 選択したLeargeFaceListの中身を全て表示させる
def get_LeargeFaceList_IdList():
    url = f"{face_api_url}/largefacelists/{largeFaceListId}/persistedfaces"

    headers = {
        'Content-Type': "application/json",
        'ocp-apim-subscription-key': subscription_key,
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
    except requests.exceptions.RequestException as e:
        logger.error(
            {'action': 'get_large_face_list', 'message': e})
        raise
    except:
        logger.error(
            {'action': 'get_large_face_list', 'message': "unknown error"})
        raise

    result = response.json()
    return result


# 過去の顔情報と照らし合わせる
def similar_Face(faceId, threshold=0.55, maxNumOfCandidatesReturned=1):
    url = f"{face_api_url}/findsimilars"

    headers = {
        'Content-Type': "application/json",
        'ocp-apim-subscription-key': subscription_key,
    }

    params = {
        "faceId": faceId,
        "largeFaceListId": largeFaceListId,
        "maxNumOfCandidatesReturned": maxNumOfCandidatesReturned,
        "mode": "matchPerson"
    }

    try:
        response = requests.post(url, json=params, headers=headers, timeout=10)
    except requests.exceptions.RequestException as e:
        logger.error({
            'action': 'find_similars', 'message': e})
        raise
    except:
        logger.error(
            {'action': 'find_similars', 'message': "unknown error"})
        raise

    faceList = response.json()
    print("similar_result", faceList)
    # 配列が空orNoneだったらLargeFaceListに追加する
    if not faceList or None:
        similar_id = newface_add_LargeFaceList()
        return similar_id
    else:
        similar_id = faceList[0]['persistedFaceId']
        confidence = faceList[0]['confidence']
        print("face_list", faceList)

        # リピータだったらuserDataを+1する
        if confidence > threshold:
            list_count = 0
            print("repeater", confidence)
            LFL_IdList = get_LeargeFaceList_IdList()

            for List in LFL_IdList:
                # similar_idで出たidを探す
                if similar_id == List['persistedFaceId']:
                    listcount = int(List['userData'])
                    listcount+=1
                    userdata = listcount
                    # 変更内容をupdateする
                    updata_LargeFaceList(similar_id, listcount)
                    return similar_id,userdata
            list_count += 1
            print("list_count", list_count)

        # confidence値が0.55以下だったらLargeFaceListに追加
        else:
            print("confidence", confidence)
            similar_id = newface_add_LargeFaceList()
            return similar_id,userdata

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

# 変更した顔情報を更新する
def updata_LargeFaceList(persistedFaceId, count_num):
    url = f'{face_api_url}/largefacelists/{largeFaceListId}/persistedfaces/{persistedFaceId}'

    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': subscription_key,
    }

    params = {
        'userData': count_num,
    }
    try:
        response = requests.patch(url, json=params, headers=headers, timeout=10)    
    except:
        print("updata_failed")

def main():
    i=0
    #Large_face_Listを作成
    create_large_face()
    # LargeFaceListを取得
    get_LargeFaceList()

    # カメラの映像を取得
    cap = cv2.VideoCapture(0)
    # カスケード型識別器の読み込み
    cascade = cv2.CascadeClassifier(os.path.join(__location__,"haarcascade_frontalface_default.xml"))

    while True:
        time.sleep(1)
        # 入力画像の読み込み
        ret, img = cap.read()
        # グレースケール変換
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # 顔領域の探索
        face = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=8, minSize=(30, 30))
        
        # 顔領域を赤色の矩形で囲む
        for (x, y, w, h) in face:
            cv2.rectangle(img, (x, y), (x + w, y+h), (0,0,300), 4)

        for rect in face:
            i+=1

            # 顔だけ切り出して保存
            x = rect[0]
            y = rect[1]
            width = rect[2]
            height = rect[3]
            dst = img[y:y+height, x:x+width]
            # new_image_path = dir_path + '/' + str(i) + path[1];
            cv2.imwrite(os.path.join(__location__, 'img/img.jpg'), dst)
            cv2.waitKey(1)

            try:
                image_data = io.open(os.path.join(__location__,'img/img.jpg'), 'rb')
                faceId, gender, age = faceId_detect(image_data)
                print("detect_result", faceId, gender, age)
            except:
                print("取得できませんでした")
                continue                                                                                                                                                               

            try:
                train_LargeFaceList()
                similar_id,userdata = similar_Face(faceId)
            except:
                continue

        key = cv2.waitKey(10)
        if key == 27:  # ESCキーで終了
            break


if __name__ == '__main__':
    main()
```

このプログラムを動かすことで、年齢と性別を取得できます。
さらに、一度認識したことがある場合にはどれくらいの可能性でその人と同一人物かを出力してくれます。




