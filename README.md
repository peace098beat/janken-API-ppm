## 概要

じゃんけんのプレーヤ(人間)が出してきた手から次に出す手を予測するプログラムです。

## API

http://fififactory.sakura.ne.jp/API/index.cgi

## 使い方

プレーヤが出してきた過去の手をgetの引数として渡す

http://fififactory.sakura.ne.jp/API/index.cgi?player=ggccppcgpcpg

## 返り値

Json形式で値がかえります。


	[
		{"next_hand": "g"}, 
		{"hand_set": "gcpgcpgcpgcp"},
		{"histgram":
			{
			"gcpgcpg": 2, 
			"pgc": 3, 
			"gc": 4,
			"cp": 4,
			"pgcpgcpg": 1,
			"cpgc": 3,
			"cpgcpgcpgc": 1,
			"gcpgcp": 3,
			"cpgcpgcp": 2,
			"gcpgcpgcpg": 1,
			"gcp": 4,
			"pg": 3,
			"gcpgcpgc": 2,
			"gcpg": 3,
			"cpgcp": 3,
			"pgcpg": 2,
			"pgcpgcpgcp": 1,
			"cpgcpgcpg": 1,
			"pgcpgcp": 2,
			"gcpgcpgcp": 2,
			"cpgcpgc": 2,
			"pgcpgcpgc": 1,
			"c": 4,
			"pgcp": 3,
			"g": 4,
			"pgcpgc": 2,
			"cpgcpg": 2,
			"cpg": 3,
			"p": 4,
			"gcpgc": 3
			}
		}
	]
