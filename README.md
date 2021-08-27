# FGO-script

script for lazy people (ex: me)

## 特色 Feature

-   [x] 可以背景執行
-   [x] 執行時可以使用滑鼠
-   [x] 背景可透過 wife.png 修改，大小為 320x180(錯了也沒差，就是你老婆會怪一些)
-   [ ] 不可縮小畫面至工具列
-   [ ] 螢幕設定需符合特定條件(下面將說明)

## 使用須知 Usage

    1.模擬器的名字必須是"夜神模擬器"
    2.開始前可進行截圖測試(會在根目錄生成myScreen.png)
    3.各別腳本可至scripts資料夾根據模板建立(選擇職階目前沒用)
    4.loop留白視為999次

## 使用須知 Cont.

    螢幕擺放樣式需如圖一，工具列必須鎖定至底部，螢幕必須為1920*1080、縮放100%
    測試截圖結果如圖二即為正確

![螢幕擺放樣式1](https://i.imgur.com/sRnU03B.png)

![螢幕擺放樣式2](https://i.imgur.com/QEbOJlT.png)

## 指令說明

    [1, 2]             => 從者1施放2技(不用選擇目標)
    [1, 2, 3]          => 從者1施放2技給從者3
    ["CLOTH", 1]       => 使用衣服技能1(不用選擇目標)
    ["CLOTH", 1, 2]    => 衣服技能1施放給從者2
    ["CLOTH", 3, 2, 6] => 換人禮裝專用，從者2換從者6
    ["ATTACK", 1, 2]   => 開始戰鬥，從者1、從者2施放寶具

## Todo

    選擇職階
    自動開箱
    選取從者下拉
    優化時間間隔
    增強例外處理

## 終極目標

```
GUI=>EXE(努力中)
APP(放棄)
```

## 測試版 EXE

[MEGA 下載](https://mega.nz/file/oy5AQZYA#1xfskIrAFqQDQb7cgsNftCSBVTCTdP1c4yy6Pvs2xww)

## 圖片來源

[ico&bgImg](https://twitter.com/erichpcsc/status/1201033067135033344)