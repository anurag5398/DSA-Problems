import logging
logging.getLogger().setLevel(logging.INFO)

class User:
    """Users of the application"""
    def __init__(self, name):
        self.__name = name
        self.rides = list()
        self.no_of_rides = 0
    def __str__(self):
        return self.__name    
    def user_type(self):
        raise NotImplementedError

class Driver(User):
    """User of type driver"""
    def __init__(self, name):
        User.__init__(self, name)

    def user_type(self):
        return "Driver"

    def create_ride(self, start, end, seats):
        ar = Active_Rides()
        id = ar.generate_id()
        self.rides.append((id, start, end, seats))
        ar.add_ride(id, start, end, seats)
        logging.info("Ride created by {}".format(self))
        return id

    def update_ride(self, id, new_start, new_end, new_seats):
        ar = Active_Rides()
        for rideid, _, _, _, _, _ in ar.view_booked_rides():
            if rideid == id:
                logging.error("Cant update ride which has active riders")
                return
        active_rides = ar.view_active_ride()
        found = False
        for i in range(len(active_rides)):
            if active_rides[i][0] == id:
                found = True
                break
        if found is False:
            logging.error("No matching ride found to update")
            return
        active_rides.pop(i)
        active_rides.append((id, new_start, new_end, new_seats))
        
        
    def withdraw_ride(self, id):
        ar = Active_Rides()
        booked_rides = ar.view_booked_rides()
        i = 0
        while i < len(booked_rides):
            if booked_rides[i][0] == id:
                booked_rides[i][1].remove_ride(id)
                booked_rides.pop(i)
            else: i+=1

        active_rides = ar.view_active_ride()
        i = 0
        while i < len(active_rides):
            if active_rides[i][0] == id:
                active_rides.pop(i)
            else: i+=1
        for i in range(len(self.rides)):
            if self.rides[i][0] == id:
                self.rides.pop(i)
                self.no_of_rides-=1
                break
        logging.info("Ride {} is withdrawn successfully".format(id))

    def close_ride(self, id):
        found = False
        for tempid, _, _, _ in self.rides:
            if id == tempid:
                found = True
                break
        if found is False:
            logging.warning("Ride {} not found for driver {}".format(id, self))
            return
        self.no_of_rides+=1
        ar = Active_Rides()
        print()
        print("Closing Ride {}".format(id))
        booked_rides = ar.view_booked_rides()
        i = 0
        while i < len(booked_rides):
            if booked_rides[i][0] == id:
                print("Ride Amount for {}: {}".format(booked_rides[i][1], booked_rides[i][5]))
                ar.add_completed_ride(booked_rides[i])
                booked_rides.pop(i)
            else: i+=1
        print()




class Rider(User):
    """User od type Rider"""
    def __init__(self, name):
        User.__init__(self, name)
    def user_type(self):
        return "Rider"
    def calculate_cost(self, start, end, seats):
        PerKM = 20
        if self.no_of_rides > 10:
            cost = (end - start) * PerKM * seats * ((seats > 1) * 0.5) * ((seats == 1) * 0.75)
        else:
            cost = (end - start) * PerKM * seats * ((seats > 1) * 0.75)
        return cost

        
    def book_ride(self, start, end, seats):
        ar = Active_Rides()
        found = False
        for tempid, tempstart, tempend, tempseats in ar.view_active_ride():
            if tempstart <= start and tempend >= end and tempseats >= seats:
                found = True
                break
        if found is False: 
            logging.warning("No Ride match for {}".format(self))
            return
        self.no_of_rides+=1
        self.rides.append((tempid, start, end, seats))
        ar.remove_ride(tempid, tempstart, tempend, tempseats)
        if tempstart < start: ar.add_ride(tempid, tempstart, start - 1, tempseats)
        if tempend > end: ar.add_ride(tempid, end + 1, tempend, tempseats)
        if tempseats > seats: ar.add_ride(tempid, start, end, tempseats - seats)
        cost = self.calculate_cost(start, end, seats)
        ar.add_booked_ride(tempid, self, start, end, seats, cost)
        logging.info("Ride booked for {}".format(self))
        return id
    
    def remove_ride(self, id):
        found = False
        for i in range(len(self.rides)):
            if id == self.rides[i][0]: 
                found = True
                break
        if found:
            self.rides.pop(i)
            self.no_of_rides-=1






class Active_Rides:
    __shared = dict()
    __id = 0
    active_rides = list()
    booked_rides = list()
    completed_rides = list()
    def __init__(self):
        self.__dict__ = self.__shared
        self.active_rides = self.active_rides
        self.booked_rides = self.booked_rides
        self.completed_rides = self.completed_rides
    def generate_id(self):
        self.__id+=1
        return self.__id
    def add_ride(self, id, start, end, seats):
        self.active_rides.append((id, start, end, seats))
    def view_active_ride(self):
        return self.active_rides
    def view_booked_rides(self):
        return self.booked_rides
    def remove_ride(self, id, start, end, seats):
        self.active_rides.remove((id, start, end, seats))
    def add_booked_ride(self, rideid, rider, start, end, seats, cost):
        self.booked_rides.append((rideid, rider, start, end, seats, cost))
    def add_completed_ride(self, ride):
        self.completed_rides.append(ride)



d1 = Driver("Neelesh")
d2 = Driver("Harish")
r1 = Rider("Ram")
r2 = Rider("Josh")

ride1 = d1.create_ride(10, 100, 3)
ride2 = d2.create_ride(25, 75, 10)

book1 = r1.book_ride(15, 35, 5)
book2 = r1.book_ride(15, 35, 3)
book3 = r2.book_ride(25, 50, 3)

d2.update_ride(ride2, 25, 100, 8)
d2.withdraw_ride(ride2)
d1.close_ride(ride1)
d2.close_ride(ride2)
