import random

class numBaseballGame:
    def __init__(self):
        #self.numAnswer;

        self.qn = int(input("몇자리 숫자를 맞추시겠습니까? "));

        #정답 만들기
        set1 = set();
        
        while(self.qn != len(set1)):
            set1.add(random.randint(0,9));
        
        self.list1 = list(set1);



        
    '''def numAnswer(self, cm):
        set1 = set();
        
        while(cm != len(set1)):
            set1.add(random.randint(0,9));

        listc = list(set1);

        
        
        return listc2;'''

    def playerNum(self, n):
        list2 = [];
        print("");
        print(n,"번 문제 : ","숫자", self.qn, "자리를 입력하시오.");
        num = input();

        for e in range(0, self.qn):
            list2.append(num[e]);

        list3 = [];
        for c in range(0, self.qn):
            list3.append(int(list2[c]));

        r = self.result(self.list1,list3);
        return r;

    def result(self, cn, pn):
        strike = 0;
        ball = 0;
        o = 0;
        out = 0;
        
        for i in range(0, len(pn)):
            for j in range(0, len(cn)):
                if cn[j] == pn[i]:
                    if i == j:
                        strike += 1;
                        break;
                    else:
                        ball += 1;
                        break;
                else:
                    o += 1;
                    
            if o == self.qn:
                out += 1;
            o = 0;

        if strike == 3:
            print("[END]");
            return 1;

        else:
            print("[ strike : ",strike, "\t", end='');
            print("ball : ",ball, "\t", end='');
            print("out : ",out, "]\n");
            return 0;
    

result = [];

g1 = numBaseballGame();
g2 = numBaseballGame();
g3 = numBaseballGame();

result = [0,0,0];
radd = 0;

while radd != 3:
    if result[0] != 1:
        result[0] = g1.playerNum(1);
    if result[1] != 1:
        result[1] = g2.playerNum(2);
    if result[2] != 1:
        result[2] = g3.playerNum(3);
    radd = result[0] + result[1] + result[2];
    
print("\nCongratulations you got the problem right\n");

#qn = int(input("몇자리 숫자를 맞추시겠습니까? "));
#c = g.numAnswer(qn);
#print(c);
#g.playerNum(); #플레이어가 숫자를 입력하는

    


