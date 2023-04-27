class PrintHelloWld:
    #16進ASCIIコードに変換する
    def trans_ascii(self,ex_typ):
        a = "Hello World!"
        str_ary = []    
        if ex_typ == 1:
            for i in range(len(a)):
                str_ary.append(format(ord(a[i]),'x'))
        elif ex_typ == 2:
            for i in range(len(a)):
                str_ary.append(ord(a[i]))
        return str_ary
    #16進コードを表示する
    def prt_code(self,tof=1):
        tmp = self.trans_ascii(tof)
        print(tmp)
        return 1
    #これらは2と3から四則演算で求めることができるとわかる。
    #2と3のみでこれを構成してみる
    def code_only23(self):        
        rtnary = []
        a = 2
        b = 3
        tmp = 0
        #H
        tmp += a * a * a * b * b
        rtnary.append(tmp)
        tmp = 0
        #e
        for i in range(17):
            tmp += b
        for i in range(25):
            tmp += a
        rtnary.append(tmp)
        tmp = 0
        #l(2つ)
        tmp += a * a * b * b * b
        rtnary.append(tmp)
        rtnary.append(tmp)
        tmp = 0
        #o
        for i in range(9):
            tmp += b
        for i in range(5):
            tmp += a
        tmp *= b
        rtnary.append(tmp)
        tmp = 0
        # スペース
        tmp = a * a * a * a * a    
        rtnary.append(tmp)
        tmp = 0
        #W
        for i in range(7):
            tmp += a
        for i in range(5):
            tmp += b
        tmp *= 3
        rtnary.append(tmp)
        tmp = 0
        #o
        for i in range(9):
            tmp += b
        for i in range(5):
            tmp += a
        tmp *= b
        rtnary.append(tmp)
        tmp = 0
        #r
        for i in range(5):
            tmp += a
        for i in range(3):
            tmp += b
        tmp *= a * b
        rtnary.append(tmp)
        tmp = 0
        #l
        tmp += a * a * b * b * b
        rtnary.append(tmp)
        tmp = 0
        #d
        tmp += a*a * (a + b) * (a + b)
        rtnary.append(tmp)
        tmp = 0
        #感嘆符    
        for i in range(3):
            tmp += b
        tmp += a
        tmp *= b
        rtnary.append(tmp)

        return rtnary
    #手作りのやつを表示する
    def prt_mkself(self):
        a = self.code_only23()
        print(a)
    #あっていることを確認したので、いざ出力！
    def print_hw(self):
        a = self.code_only23()
        ans = ""
        for i in range(len(a)):
            ans += chr(a[i])
        print(ans) #Hello World!

prt_hw = PrintHelloWld()
prt_hw.print_hw()

"""
説明用

#prt_hw = PrintHelloWld()
まず"Hello World!"をASCIIコード変換
#prt_hw.prt_code()

で10進数バージョンも
#prt_hw.prt_code(2)

10進数にすると以下のような素因数となっていることがわかる
H(72) = 2^3 * 3^2
e(101) = 101
l(108) = 2^2 * 3^3
o(111) = 3 * 37
 (32) = 2^5
W(87) = 3 * 29
r(114) = 2 * 3 * 19
d(100) = 2^2 * 5^2
!(33) = 3 * 11 

これをもとに作成するとさっきの10進バージョンと一致する
#prt_hw.prt_mkself()

これを復元して、Hello World!
#prt_hw.print_hw()


"""
