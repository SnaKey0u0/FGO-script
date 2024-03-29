# FGO-script

    本來是想做給自己用的，但越做越起勁了0u0

## EXE 載點

[MEGA 下載](https://mega.nz/file/crxmCSJT#kY5XOXpM-wlHYNAJ1JIax-PF6WEjX-OnHyDxlCe35kk)

## 腳本製作靜態網頁

[製作腳本](https://snakey0u0.github.io/FGO-script/)

## 特色

-   [x] 可背景執行
-   [x] 可自動開箱
-   [x] 可自動友抽
-   [x] 可調整模擬器視窗大小(但不可全螢幕)
-   [x] 可透過 wife.png 修改背景，大小為 320x180(錯了也沒差，就是你老婆會怪一些)

## 注意事項

-   [x] windows 螢幕縮放請設定成 100%
-   [x] 不可縮小畫面至工具列
-   [x] 模擬器的名字必須是"夜神模擬器"
-   [x] 開始執行後勿再縮放模擬器
-   [x] 執行時請勿讓電腦進入休眠或睡眠
-   [x] 夜神右方的小工具列需打開(若測試截圖無法出現請試著更新夜神版本)
        如下正常
        ![image](https://github.com/SnaKey0u0/FGO-script/blob/dev/imgs/example.png)

## 腳本說明

    開始前可進行截圖測試(會在根目錄生成 myScreen.png)
    各別腳本可至 scripts 資料夾根據模板建立(選擇職階目前沒用)
    loop 留白視為 999 次

    team               => 隊伍，1~10
    class              => 直接分類，目前沒用
    server             => imgs資料夾內從者檔名，不用+.png
    prefer_card        => 戰鬥時偏好的指令卡，可選B, A, Q
    prefer_weak        => 戰鬥時是否弱點優先，true或false

    [1, 2]             => 從者1施放2技(不用選擇目標)
    [1, 2, 3]          => 從者1施放2技給從者3
    ["CLOTH", 1]       => 使用衣服技能1(不用選擇目標)
    ["CLOTH", 1, 2]    => 衣服技能1施放給從者2
    ["CLOTH", 3, 2, 6] => 換人禮裝專用，從者2換從者6
    ["ATTACK", 1]      => 開始戰鬥，從者1施放寶具
    ["ATTACK", 1, 2]   => 開始戰鬥，從者1、從者2施放寶具

    positions_config裡可以調整各情況等待的時間
    skills_time        => 施放技能等待時間，包含從者技能、從者寶具、衣服技能(不包含換人)
    transitions_time   => 過場時間，包含選隊、選角
    switch_servant     => 換人等待時間


## 有一個麻煩的地方

    若想自行增加好友從者，請將夜神放至最大(非全螢幕)，利用測試截圖功能取得畫面，再利用小畫家或其他工具局部截圖，另存新檔至imgs資料夾內。
    之後在script中即可將server設定成該從者的檔名(不用+.png)

## Todo

    ERROR 活動時不使用道具
    ERROR 活動獎勵結算畫面
    簡化新增好友助戰的流程(沒好方法就準備ㄘ我的工人智慧)
    選擇職階
    選擇禮裝(FGO活動中已有內建)
    選取從者下拉
    優化時間間隔
    增強例外處理

## 終極目標

```
GUI=>EXE(優化中)
APP(放棄)
```

## 備註

    pyinstaller -F main.py -w --icon=fgo.ico

## 圖片來源

[ico&bgImg](https://twitter.com/erichpcsc/status/1201033067135033344)
