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