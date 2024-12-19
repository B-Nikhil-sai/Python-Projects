def Booking(arg):
    l=[]
    def inner():
        if len(l)==0:
            l.append(arg())
            return l[0]
    return inner
@Booking
class Devara():
    def __init__(self) -> None:
        self.max_number_of_tickets = 200
    def Ticket_booking(self,request_no_of_ticktes):
        if request_no_of_ticktes<=self.max_number_of_tickets:
            self.max_number_of_tickets -= request_no_of_ticktes
            print(f'{request_no_of_ticktes} tickets are booked successfully....!😎😎😎😎😎😎😎')
        else:
            print('Tickets are not available ...!😒😒😒😒😒😒')
@Booking
class Swag():
    def __init__(self) -> None:
        self.max_number_of_tickets = 200
    def Ticket_booking(self,request_no_of_ticktes):
        if request_no_of_ticktes<=self.max_number_of_tickets:
            self.max_number_of_tickets -= request_no_of_ticktes
            print(f'{request_no_of_ticktes} tickets are booked successfully....!😎😎😎😎😎😎😎')
        else:
            print('Tickets are not available ...!😒😒😒😒😒😒')
@Booking
class Pushpa_2():
    def __init__(self) -> None:
        self.max_number_of_tickets = 200
    def Ticket_booking(self,request_no_of_ticktes):
        if request_no_of_ticktes<=self.max_number_of_tickets:
            self.max_number_of_tickets -= request_no_of_ticktes
            print(f'{request_no_of_ticktes} tickets are booked successfully....!😎😎😎😎😎😎😎')
        else:
            print('Tickets are not available ...!😒😒😒😒😒😒')
@Booking
class Salar_part_2():
    def __init__(self) -> None:
        self.max_number_of_tickets = 200
    def Ticket_booking(self,request_no_of_ticktes):
        if request_no_of_ticktes<=self.max_number_of_tickets:
            self.max_number_of_tickets -= request_no_of_ticktes
            print(f'{request_no_of_ticktes} tickets are booked successfully....!😎😎😎😎😎😎😎')
        else:
            print('Tickets are not available ...!😒😒😒😒😒😒')
def Google_pay():
    print('Available movies are shown in below \n1)Devara Part 1 \n2)Swag  \n3)Pushpa Part 2 \n4) Salar Part 2')
    user_choice = int(input('Enter the movie number which are available in the above numbers .. : '))
    if user_choice ==1:
        User = Devara()
        Number_of_tickets = int(input('Enter the number of tickets : '))
        User.Ticket_booking(Number_of_tickets)
    elif user_choice ==2:
        User = Swag()
        Number_of_tickets = int(input('Enter the number of tickets: '))
        User.Ticket_booking(Number_of_tickets)
    elif user_choice ==3:
        User = Pushpa_2()
        Number_of_tickets = int(input('Enter the number of tickets: '))
        User.Ticket_booking(Number_of_tickets)
    elif user_choice==4:
        User = Salar_part_2()
        Number_of_tickets = int(input('Enter the number of tickets: '))
        User.Ticket_booking(Number_of_tickets)
    else:
        print('Options are unavailable ...😊😊😊😊')
def Paytm_pay():
    print('Available movies are shown in below \n1)Devara Part 1 \n2)Swag  \n3)Pushpa Part 2 \n4) Salar Part 2')
    user_choice = int(input('Enter the movie number which are available in the above numbers .. : '))
    if user_choice ==1:
        User = Devara()
        Number_of_tickets = int(input('Enter the number of tickets : '))
        User.Ticket_booking(Number_of_tickets)
    elif user_choice ==2:
        User = Swag()
        Number_of_tickets = int(input('Enter the number of tickets: '))
        User.Ticket_booking(Number_of_tickets)
    elif user_choice ==3:
        User = Pushpa_2()
        Number_of_tickets = int(input('Enter the number of tickets: '))
        User.Ticket_booking(Number_of_tickets)
    elif user_choice==4:
        User = Salar_part_2()
        Number_of_tickets = int(input('Enter the number of tickets: '))
        User.Ticket_booking(Number_of_tickets)
    else:
        print('Options are unavailable ...😊😊😊😊')
def Phone_pay():
    print('Available movies are shown in below \n1)Devara Part 1 \n2)Swag  \n3)Pushpa Part 2 \n4) Salar Part 2')
    user_choice = int(input('Enter the movie number which are available in the above numbers .. : '))
    if user_choice ==1:
        User = Devara()
        Number_of_tickets = int(input('Enter the number of tickets : '))
        User.Ticket_booking(Number_of_tickets)
    elif user_choice ==2:
        User = Swag()
        Number_of_tickets = int(input('Enter the number of tickets: '))
        User.Ticket_booking(Number_of_tickets)
    elif user_choice ==3:
        User = Pushpa_2()
        Number_of_tickets = int(input('Enter the number of tickets: '))
        User.Ticket_booking(Number_of_tickets)
    elif user_choice==4:
        User = Salar_part_2()
        Number_of_tickets = int(input('Enter the number of tickets: '))
        User.Ticket_booking(Number_of_tickets)
    else:
        print('Options are unavailable ...😊😊😊😊')
def Book_my_show():
    print('Available movies are shown in below \n1)Devara Part 1 \n2)Swag  \n3)Pushpa Part 2 \n4) Salar Part 2')
    user_choice = int(input('Enter the movie number which are available in the above numbers .. : '))
    if user_choice ==1:
        User = Devara()
        Number_of_tickets = int(input('Enter the number of tickets : '))
        User.Ticket_booking(Number_of_tickets)
    elif user_choice ==2:
        User = Swag()
        Number_of_tickets = int(input('Enter the number of tickets: '))
        User.Ticket_booking(Number_of_tickets)
    elif user_choice ==3:
        User = Pushpa_2()
        Number_of_tickets = int(input('Enter the number of tickets: '))
        User.Ticket_booking(Number_of_tickets)
    elif user_choice==4:
        User = Salar_part_2()
        Number_of_tickets = int(input('Enter the number of tickets: '))
        User.Ticket_booking(Number_of_tickets)
    else:
        print('Options are unavailable ...😊😊😊😊')
def Amazon_pay():
    print('Available movies are shown in below \n1)Devara Part 1 \n2)Swag  \n3)Pushpa Part 2 \n4) Salar Part 2')
    user_choice = int(input('Enter the movie number which are available in the above numbers .. : '))
    if user_choice ==1:
        User = Devara()
        Number_of_tickets = int(input('Enter the number of tickets : '))
        User.Ticket_booking(Number_of_tickets)
    elif user_choice ==2:
        User = Swag()
        Number_of_tickets = int(input('Enter the number of tickets: '))
        User.Ticket_booking(Number_of_tickets)
    elif user_choice ==3:
        User = Pushpa_2()
        Number_of_tickets = int(input('Enter the number of tickets: '))
        User.Ticket_booking(Number_of_tickets)
    elif user_choice==4:
        User = Salar_part_2()
        Number_of_tickets = int(input('Enter the number of tickets: '))
        User.Ticket_booking(Number_of_tickets)
    else:
        print('Options are unavailable ...😊😊😊😊')
Google_pay()
Paytm_pay()
Phone_pay()
Book_my_show()




