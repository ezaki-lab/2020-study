# PWA（Progressive Web Apps）

モバイル向けWebサイトをスマートフォン向けアプリのようなユーザー体験を提供する技術

マチシルクエストの基盤で用いられた技術を元に作成したサンプル
- Web App Manifest
- ServiceWorker
- (比率固定画面 js,css)


## 実施日

2020/04/x

## Installation

### 環境構築

#### webが使える環境
AzurePotalで動きます
言語：html,js,css

## サンプルを動かす

- [デモサイト](https://my-16421.azurewebsites.net/zemi-pwa)

#### JSONをAzurePotalで読み込む際
web.config が必要です
```web.config
<?xml version="1.0" encoding="UTF-8" ?>
<configuration>
    <system.webServer>
        <staticContent>
            <remove fileExtension=".json" />
            <mimeMap fileExtension=".json" mimeType="application/json" />
        </staticContent>
    </system.webServer>
</configuration>
```

## 基礎学習

### PWA(Progressive Web Apps)

- [PWA（Progressive Web Apps）とは？メリットと実装事例について](https://digital-marketing.jp/seo/what-is-progressive-web-apps/)
スマートフォンアプリと同じような機能や、安定して高速に動作する快適なUXを、ウェブで実現する手法や、そうした技術でつくられたサイト

#### 導入事例

[PWA導入による成功事例9選](https://yapp.li/magazine/3175/#PWA9)

### Web App Manifest

- [Web App Manifestについて](https://developer.mozilla.org/ja/docs/Web/Manifest)
PWAの一部であり、これはアプリストアを通さずに端末のホーム画面にインストールすることができ、オフライン作業やプッシュ通知の受け取りなどのその他の可能性を持ったウェブサイト

#### 作ってくれるツールが

[iconを各pxに複製とmanifestjson自動生成するサイト](https://app-manifest.firebaseapp.com/)

### ServiceWorker

- [Service Worker の紹介](https://developers.google.com/web/fundamentals/primers/service-workers?hl=ja)
PWAで「アプリのように高速かつ信頼性のある動作」をするための仕組みや、その仕組みで動作しているプログラムを指す

#### ServiceWorkerは身近に

chromeのデペロッパーツールから以下の赤線を押していくと、聞き覚えのあるURLが
![f12](https://user-images.githubusercontent.com/39362040/78881227-74fff700-7a91-11ea-8665-95637b87622d.PNG)


## 参考

- [SEO担当者向け PWA・SPA・Service Worker 超入門。もう「JavaScript苦手」なんて言ってられない](https://webtan.impress.co.jp/e/2019/08/19/33635)
- [Add a web app manifest](https://web.dev/add-manifest/)
- [ServiceWorkerとCache APIを使ってオフラインでも動くWebアプリを作る](https://qiita.com/horo/items/175c8fd7513138308930)
