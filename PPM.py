# coding: utf-8
"""
PPM.py

ppmアルゴリズムを使って、じゃんけんのユーザの次の手を予測

Version:
    1.0

Note:
インスタンス生成後、事前にaddをしてデータベースを作っておく。
level数にたっするようにデータベースを作っておかないとエラー。
要素は"文字列","1文字"

Method:
    add:        要素追加
    predict:    次回手候補予測
    next_hand:  次回手返却
    dump:

Reference:
    http://www.pitecan.com/Puzzle/Predict/janken.html
"""
__author__ = u"Tomoyuki Nohara <fififactory.com>"
__date__ = "2015.05.10"


import math
import random


class Predict(object):

    def __init__(self, level=5):
        self.level = level
        # これまでの手順
        self.history = ''
        # ヒストグラム
        self.accum = {}
        # 手の種類？
        self.tokens = {}

    def add(self, c):
        """ 人間の手を格納して、データベースを作る
        """
        # 辞書型の必要はないかもしれない。['g','c','p']
        self.tokens[c] = True
        self.history += c
        for i in range(1, self.level+1):
            if len(self.history) < i:
                continue
            else:
                s = self.history[-i:]
                if self.accum.has_key(s):
                    # print 'exist'
                    self.accum[s] += 1
                else:
                    # print 'noexist'
                    self.accum[s] = 1

    def add_ary(self, ary):
        [self.add(c) for c in ary]

    def predict(self):
        """予測した手を返す

        これまでの手から、○前手分を読み込み、
        次に手を出した時の確率を調べる。

        Return:
            res: 次の手
        Example:
            # データベース
            history = "gcpgcpgcp"
            # 5手分取得
            s = "cpgcp"
            # 次の手のパターン
            c = "g", "c", "p"
            # 予想される次の手
            r = "cpgcpg", "cpgcpc", "cpgcpp"

        """
        res = []
        n = 0
        for i in range(1, self.level+1):
            # history辞書の末尾から(level-i) level>i
            s = self.history[-(self.level-i):]

            if s == '':
                # historyがなにも入っていなければbreak
                break

            # 次の手を予測.確率の一番良い手を探す
            # s: 現在から数手前の手
            # c: 仮の次に出す手
            # r: 仮の手を出した時の確率(既存出現度)

            for c in self.tokens:
                # r: historyとcを足す
                r = s + c
                # もし辞書にr(='gcpp')があるなら
                if self.accum.has_key(r):
                    # その要素数がn(defoult 0以上なら
                    if self.accum[r] > n:
                        # 累積ポイントが勝れば、新規に格納
                        n = self.accum[r]
                        res = [c]
                    elif self.accum[r] == n:
                        # 累積ポイントが同じであれば、返却リストに加える。
                        res.append(c)

            # 次の手の予想が出たら終了
            if len(res) > 0:
                break

        return res

    def dump(self):
        """格納されたヒストグラムを表示する。
        """
        for key, val in self.accum.items():
            print key, val

    def next_hand(self):

        next_hands = self.predict()
        # 手の中からランダムに選ぶ
        inx = int(math.floor(random.random() * len(next_hands)))

        # 手が足りな買ったときの対応
        try:
            return next_hands[inx]
        except:
            return ['error']


if __name__ == '__main__':

    import random
    import math
    token = {1: 'g', 2: 'c', 3: 'p'}

    p = Predict(30)
    for i in range(1, 100):
        no = random.randint(1, 3)
        p.add(token[no])

    s = 'gggcccppp'
    # p.add_ary(list(s))

    print p.history
    print "=========="
    print "next hand:", p.next_hand()
    print "=========="
    # print p.dump()
    print 'g', p.accum['g']
    print 'c', p.accum['c']
    print 'p', p.accum['p']
