#在class 裡面的function 叫做method
#關於最基本的屬性建議加在init 裡面

class Player:
    def __init__(self, name , ap):
        print('我誕生了')
        self.name = name
        self.hp = 100
        self.ap = ap

    def attck(self, target):
        print(self.name, 'attacking', target.name)
        target.hp = target.hp - self.ap


p1 = Player('Player1', 5)
p2 = Player('Player2', 10)
p1.attck(p2)
print(p2.hp)