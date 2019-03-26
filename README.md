# discord-region-chenge-bot

勉強目的で作成中のDiscord Bot

Discordのサーバーリージョンをコマンドで変更するBOT

今のコードでは、短時間でリージョン変更を行うと、10分間変更不能になり、<br>
10分後に突然変更されるため要timeout機能の実装。

 コマンド | 説明 |
|:---|:---|
|!region  |現在のサーバーリージョンを表示します。 |
|!region ja |サーバーリージョンを「japan」に切り替えます。 |
|!region sg |サーバーリージョンを「singapore」に切り替えます。 |
|!region hg |サーバーリージョンを「hongkong」に切り替えます。 |
