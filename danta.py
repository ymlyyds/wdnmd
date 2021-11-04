'''
    三个蛋挞师傅，制作蛋挞数目达到500个时，等待3秒再制作，工资 = 蛋挞数量 * 12
6个客人，没人有3000元，都买蛋挞，当蛋挞数量不够时，等待3秒，再次购买直到没钱
师傅类：
    属性：师傅姓名、制作蛋挞数量、工资
    操作：制作蛋挞
客人类：
    属性：客人姓名、购买蛋挞数量、余额
    操作：买蛋挞
店家类：
    属性：
        蛋挞制作数量：
        售卖蛋挞数量：
        销售金额：
        蛋挞成本：
        盈利：
    操作：
        打印总盈利，总生产，总消费
'''
from threading import Thread
import time
#生产者
class Producer(Thread):
    __name=""
    __count=0
    __money=0
    __kfc=None
    def __init__(self,name,kfc):
        Thread.__init__(self)
        self.name=name
        self.__kfc=kfc

    def getCount(self):
        return self.__count

    def setMoney(self,money):
        if money<0:
            print("输入非法！")
        else:
            self.__money=money
    def getMoney(self):
        return self.__money

    def run(self) -> None:
        while True:
            if self.__kfc.getBasket()==500:
                time.sleep(3)
                print(self.name,"总共做了",self.__count,"个蛋挞,工资是",self.__money)

            elif self.__kfc.getBasket()<500 and self.__kfc.getBasket()>=0:
                self.__count +=1
                self.__kfc.setBasket(self.__kfc.getBasket()+1)
                self.__money = self.__count*12
                self.__kfc.setMoney(self.__kfc.getMoney()-12)
                print(self.name, "做了", self.__count, "个蛋挞")
#消费者
class Consumer(Thread):
    __name=""
    __count=0
    __money=3000
    __kfc=None

    def __init__(self,name,kfc):
        Thread.__init__(self)
        self.name=name
        self.__kfc=kfc


    def getCount(self):
        return self.__count

    def getMoney(self):
        return self.__money

    def run(self) -> None:
        while True:
            if self.__kfc.getBasket()==0:
                time.sleep(3)
            elif self.__kfc.getBasket()>0 and self.__kfc.getBasket()<=500 and self.__money>0:
                self.__count += 1
                self.__kfc.setBasket(self.__kfc.getBasket()-1)
                self.__money -= 3
                self.__kfc.setMoney(self.__kfc.getMoney()+3)
                print(self.name, "买了", self.__count, "个蛋挞")
            elif self.__money<=0:
                print(self.name, "总共买了", self.__count, "个蛋挞,还剩钱", self.__money,"元")
                break
#蛋挞售卖店
class KFC:
    __money=0
    __basket=500

    def setMoney(self,money):
        self.__money=money
    def getMoney(self):
        return self.__money

    def setBasket(self,basket):
        self.__basket=basket
    def getBasket(self):
        return self.__basket
#多线程运行
kfc = KFC()
p1=Producer("生产者1",kfc)
p2=Producer("生产者2",kfc)
p3=Producer("生产者3",kfc)

c1 = Consumer("消费者1",kfc)
c2 = Consumer("消费者2",kfc)
c3 = Consumer("消费者3",kfc)
c4 = Consumer("消费者4",kfc)
c5 = Consumer("消费者5",kfc)
c6 = Consumer("消费者6",kfc)
c7 = Consumer("消费者7",kfc)
c8 = Consumer("消费者8",kfc)

p1.start()
p2.start()
p3.start()

c1.start()
c2.start()
c3.start()
c4.start()
c5.start()
c6.start()
c7.start()
c8.start()