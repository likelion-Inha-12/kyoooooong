class bank:
    def __init__(self, name="", money=0):
        self.name = name
        self.money = money

    def setting(self):
        self.name = input("이름을 입력해주세요: ")
        self.money = int(input("잔액을 입력해주세요: "))
        print("%s님의 계좌 잔액은 %d 원입니다."%(self.name, self.money))

    def deposit(self):
        depo = int(input("얼마를 입금하시겠습니까? "))
        if depo < 0:
            print("금액은 양수여야 합니다.")
        else:
            self.money += depo
            print("%d원이 입금되었습니다."%depo)

    def withdraw(self):
        withd = int(input("얼마를 출금하시겠습니까? "))
        if withd < 0:
            print("금액은 양수여야 합니다.")
        elif withd > self.money:
            print("출금 금액이 잔액을 초과하거나 잘못 입력되었습니다.")
        else:
            self.money -= withd
            print("%d원이 출금되었습니다." % withd)

    def checking(self):
        print("%s 님의 계좌 잔액은 %d원입니다" % (self.name, self.money))

class savings(bank):
    def interest(self):
        inter = float(input("이자율을 입력해주세요: "))
        print("이자율: %s"%inter)
        print("%s님의 계좌에 %s원의 이자가 추가되었습니다."%(self.name, self.money * inter/100))
        self.money += self.money * inter/100

if __name__ == "__main__":
    m = savings()
    m.setting()
    m.deposit()
    m.interest()
    m.withdraw()
    m.checking()
