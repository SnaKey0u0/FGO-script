# FGO-script

script for lazy people (ex: me)

## Requirements

```
pip install mss
pip install opencv-python
```

## Exe Usage

```
1.擷取螢幕可至positions_config.json調整screen_num參數，並進行測試(在根目錄生成myScreen.png)
2.各別腳本可至scripts資料夾建立
3.將模擬器放至最大(非全螢幕)，畫面停留在入關前，點選執行(該螢幕縮放需調整成100%)
4.loop留白視為999次

# 指令說明
# EX: [1, 2]            => 從者1施放2技(不用選擇目標)
# EX: [1, 2, 3]         => 從者1施放2技給從者3
# EX: ["CLOTH", 1]      => 使用衣服技能1(不用選擇目標)
# EX: ["CLOTH", 1, 2]   => 衣服技能1施放給從者2
# EX: ["CLOTH", 3, 2, 6]=> 換人禮裝專用，從者2換從者6
# EX: ["ATTACK", 1]     => 開始戰鬥，從者1施放寶具(僅能1人施放)

最後，背景可透過wife.png修改，大小為320x180
```

## Todo

```
解放螢幕
可選擇職階
可指定色卡
吃銅蘋果
自動開箱
自動友抽
選取從者下拉
優化時間間隔
優化螢幕擷取
增強例外處理(log)
```

## 終極目標

```
GUI=>EXE(努力中)
APP(放棄)
```

## 測試版 EXE

[MEGA 下載](https://mega.nz/file/xnIHiY4b#g2weTU8gnfe3XBprvtaYYrnvYtWrEWN3mnuKR0vPfpQ)
[ico&bgImg](https://twitter.com/erichpcsc/status/1201033067135033344)
