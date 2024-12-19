class SBI():
    HOD        = 'Mumbai'
    Branch_LOC = 'Bangalore' 
    IFSC       = 'SBIN0000813'
    ROI        = 10

    def __init__(self,Name,Age,Mobile,Bal,Pin):
        self.Name    =  Name
        self.Age     =  Age
        self.Mobile  =  Mobile
        self.Bal     =  Bal
        self.Pin     =  Pin

    def Check_Balance(self):
        if self.Pin == self.Check_Pin():
            print(f'Current Balance is {self.Bal}')
        else:
            print('Invalid Pin')

    def Deposit(self):
        if self.Pin == self.Check_Pin():
            amount = int(input('Enter the amount: '))
            self.Bal += amount
            print('Amount credited Successfully')
            print(f'Current Balance is {self.Bal}')
        else:
            print('Invalid Pin')

    def Withdraw(self):
        if self.Pin == self.Check_Pin():
            amount = int(input('Enter the amount: '))
            if amount <= self.Bal:
                self.Bal -= amount
                print('Amount debited Successfully')
                print(f'Current Balance is {self.Bal}')
            else:
                print('Insufficent Funds')
        else:
            print('Invalid Pin')

    @classmethod
    def Update_ROI(cls):
        new_ROI = float(input('Enter the new ROI: '))
        cls.ROI = new_ROI
        
    @staticmethod
    def Check_Pin():
        pin = int(input('Enter the Pin: '))
        return pin
    
Account_Holder1 = SBI('Nikhil',22,123456789,10000,1111)
Account_Holder2 = SBI('Manohar',18,987654321,5000,2222)
Account_Holder3 = SBI('Rajya Lakshmi',45,135792468,15000,3333)
Account_Holder4 = SBI('Ravi Sankar',55,975318642,25000,4444)
Account_Holder1.Withdraw()


