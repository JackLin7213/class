#class 類別種類
#在class的參數值投self是為了讓他能執行自己內部的function
#就不需要像之前寫function那樣一直需要參數向外面拿功能，自己用自己裡面的function就好

#不是原生的class 要是大寫開頭
class Student:
    def __init__(self, name, score): #initialize 初始化
        self.name = name
        self.score = score
        print('我誕生惹')
        self.do_hw('英文')     #因為第一個参數已經被self 投掉了，所以英文會對應到第二個參數
        self.study()
        self.sleep()

    def do_hw(self, hw):
        print('我在做', hw, '作業')

    def study(self):
        print('我在讀書')
        self.score += 5

    def sleep(self):
        print('I am sleeping~!')


s1 = Student('Jack', 80)
s2 = Student('John', 90)
print(dir(s1)) #把他身上的屬性印出來
print(s1.name, s2.name)
print(s1.score, s2.score)

s2.study()
print(s2.score)