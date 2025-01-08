class BOI():
    HQ = 'Mumbai'
    IFSC = 'BKID0008400'
    ROI = 7.5
    
    def __init__(self,name,age,adhar,gender,Pin,bal):
        self.name = name
        self.age = age
        self.adhar = adhar
        self.gender = gender
        self.Pin = Pin
        self.bal = bal


    def Display_Details(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Adhar Number: {self.adhar}')
        print(f'Gender: {self.gender}')
        print(f'Balance: {self.bal}')
    

    def Check_Balance(self):
        try:
            assert self.Pin == self.Check_Pin(),'Invalid Pin Entered'
            print(f'Current bal is : {self.bal}')

        except AssertionError as e:
            print(e)

    def Deposite(self):
        try:
            assert self.Pin == self.Check_Pin(),'Invalid Pin Entered'
            Amount =  int(input('Enter the amount: '))
            self.bal += Amount
            print(f'Current Bal is : {self.bal}')
            
        except AssertionError as e:
            print(e)

    def Withdraw(self):
        try:
            assert self.Pin == self.Check_Pin(),'Invalid Pin Entered'
            Amount =  int(input('Enter the amount: '))

            assert Amount <= self.bal,'Insufficent Funds'
            self.bal -= Amount
            print(f'Current Bal is : {self.bal}')
            
        except AssertionError as e:
            print(e)

    @classmethod
    def Update_ROI(cls):
        New_ROI = float(input('Enter the new rate of intrest: '))
        BOI.ROI = New_ROI
        
    @staticmethod
    def Check_Pin():
        Pin = int(input('Enter Pin: '))
        return Pin
    
customer1 = BOI('Nikhil',23,548523987598,'Male',1111,2000)
customer2 = BOI('Raji',49,725796886258,'Female',2222,3000)
customer3 = BOI('Manohar',14,235476354698,'Male',3333,5000)
customer4 = BOI('Ravi',54,275847917953,'Male',4444,10000)
                
