from datetime import datetime
class Bus:
    def __init__(self,bno,Ac,cap):
        self.bno=bno
        self.Ac=Ac
        self.cap=cap  
        
    def get_bno(self):
        return self.bno
    def get_Ac(self):
        return self.Ac
    def get_cap(self):
        return self.cap
    def display(self):
        print("BusNo {} : Ac {} : Capacity is {}".format(self.bno,self.Ac,self.cap))
class Bookings:
    def __init__ (self):
        self.name=" "
        self.date=None
        self.bno=None
    def make_booking(self,BUSES,BOOKINGS):
        self.name=input("Enter passenger name:")
        self.bno=int(input("Enter the bus no:"))
        d=input("Enter the date in dd-mm-yyyy:")
        self.date=datetime.strptime(d,"%d-%m-%Y").date()
        if(self.isavailable(BUSES,BOOKINGS,self.bno,self.date)):
            BOOKINGS.append(self)
            print("Your seat is confirmed  ")
        else: 
            print("Bus is full,try another bur or date")
    def isavailable(self,BUSES,BOOKINGS,bno,date):
        capacity=0
        booked=0
        for i in BUSES:
            if(bno==i.bno):
                capacity=i.cap
            for j in BOOKINGS:
                if(date==j.date and bno==j.bno):
                    booked=booked+1
        return booked<capacity
def main():
    BUSES=[Bus(100,True,2),Bus(200,False,50),Bus(300,False,45)]
    BOOKINGS=[]
    for i in BUSES:
        i.display()
    while True:
        opt=int(input("Enter 1 to book, 2 to exit:"))    
        if(opt==1):
            book=Bookings()
            book.make_booking(BUSES,BOOKINGS)
        else:
            break
        
    
    
if __name__ == "__main__":
    main()
