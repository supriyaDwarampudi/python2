import random
import pickle
import sys
#global variables
logged_in=False
user_id=0
password=''
class Train:
    def __init__(self,Name='',Train_number=0,arr_time='',dep_time='',source='',destination='',date_of_journey='',seat_avail_in_1AC=0,seat_avail_in_2AC=0,seat_avail_in_3AC=0,seat_avail_in_sleeper=0,fare_in_1AC=0,fare_in_sleeper=0):
        self.Name=Name
        self.Train_number=Train_number
        self.arr_time=arr_time
        self.dep_time=dep_time
        self.source=source
        self.destination=destination
        self.date_of_journey=date_of_journey
        self.seats={'1AC':seat_avail_in_1AC,'2AC':seat_avail_in_2AC,'3AC':seat_avail_in_3AC,'SL':seat_avail_in_sleeper}
        self.fare={'1AC':fare_in_1AC,'SL':fare_in_sleeper}
    def print_seat_availability(self):
        print('Number of seats availability in 1AC:- '+str(self.seats['1AC']))
        print('Number of seats availability in 2AC:- ' + str(self.seats['2AC']))
        print('Number of seats availability in 3AC:- ' + str(self.seats['3AC']))
        print('Number of seats availability in SL:- ' + str(self.seats['SL']))
    def check_availabilty(self,coach='',ticket_num=0):
        coach=coach.upper()
        if coach not in('SL','1AC','2AC','3AC'):
            print_seat_availability()
            coach=input("Enter the coach(1AC/2AC/3AC.SL) :-")
        else:
            if self.seats[coach]==0:
                return False
            elif self.seats[coach]>=ticket_num:
                return True
            else:
                return False
    def book_ticket(self,coach='',no_of_tickets=0):
        self.seats[coach]-=no_of_tickets
        return True
class ticket:
    def __int__(self,train,user,ticket_num,coach):
        self.pnr=str(train.num)+str(user.uid)+str(random.randint(99,999))
        