[元リポジトリ](https://github.com/satoyuichi/BlenderRokuro)

# BlenderRokuro rotary_encoder compatible version
　メッシュオブジェクトをロータリーエンコーダで回転させ続けます。ろくろで作る器のような形状を作る時に便利です。

## 使用条件
* Blender 2.78 以上

## 機能
* 回転軸の選択
* 回転方向の選択
* 一周の分割数の選択
* 時間のステップ数の選択

## 使い方
1. アドオンをインストールして有効にします
2. メッシュを選択してスカルプトモードにします
3. ツールシェルフに "Rokuro" パネルが開きます
4. お好みの設定をして "Enable Rokuro" ボタンを押してから、ロータリーエンコーダを操作すると回る
5. x,y,z軸のチェックボックスをonにしているものが
6. "Disable Rokuro" ボタンを押して終了します←(今の所ロータリーエンコーダ回しながらでないと操作できない)

 　~~Start, End 値で一周を何分割するか、Step 値で１フレーム当たりいくつ進めるかが決まります。~~

(オマケとしてテクスチャペイントモードでも動作します)

## 上手く作るコツ
* Stroke Method で Airbrush を有効にする
* Symmetry / Lock で Mirror を切る
* Brush で Front Faces Only を有効にする
* 厚みは後で Solidify などでつける
* あまり早く回さない

## ライセンス
[MIT ライセンス](http://takuro.mit-license.org/)

## 既知のバグ
* 回転前の Rotation 値が戻らないことがあります
* "Enable Rokuro"クリック後,シリアル通信(?)の関係でロータリーエンコーダ操作しながらでないと、停止やチェックボックスなどの操作ができない

## 参考サイト
 - http://nn-hokuson.hatenablog.com/entry/2017/03/26/102145
 - 文字コード削除→ https://qiita.com/moritama1515/items/bc37c3d7d5280c877950


###製作者
 - 元データ:[Yuichi sato様](https://github.com/satoyuichi)
 - ロータリーエンコーダ操作対応作成:[youk720(自分)](https://github.com/youk720)
