class Whatsapp1():
    def __init__(self,name,chat,Dp):
        self.name = name
        self.chat = chat
        self.Dp   = Dp

    def Details(self):
        print(f'Name = {self.name}')
        print(f'chat = {self.chat}')
        print(f'Display picture = {self.Dp}')

class Whatsapp2(Whatsapp1):
    def __init__(self,name,chat,Dp,Audio_msg,Audio_call,status):
        super().__init__(name,chat,Dp)
        self.Audio_msg  = Audio_msg
        self.Audio_call = Audio_call
        self.status     = status

    def Details(self):
        super().Details()
        print(f'Audio_msg  = {self.Audio_msg}')
        print(f'Audio_call = {self.Audio_call}')
        print(f'status = {self.status}')

class Whatsapp3(Whatsapp2):
    def __init__(self,name,chat,Dp,Audio_msg,Audio_call,status,Vedio_call,Business,channels):
        Whatsapp2.__init__(self,name,chat,Dp,Audio_msg,Audio_call,status)
        self.Vedio_call = Vedio_call
        self.Business = Business
        self.channels = channels

    def Details(self):
        Whatsapp2.Details(self)
        print(f'Vedio_call = {self.Vedio_call}')
        print(f'Business = {self.Business}')
        print(f'channels = {self.channels}')

user1 = Whatsapp1('Nikhil','given','given')
user2 = Whatsapp2('Manohar','given','given','yes','yes','yes')
user3 = Whatsapp3('Rajya Lakshmi','given','given','yes','yes','yes','Gave','Gave','Gave')
user3.Details()
