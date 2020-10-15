import enum

"""Stores all static values"""
class StaticValues(enum.Enum):
    ChargePerKm = 20

"""Stores information about a ride"""
class RideObject:
    def __init__(self, user, origin, destination, no_of_seats, status = True):
        self.user = user
        self.origin = origin
        self.destination = destination
        self.seats = no_of_seats
        self.status = True

"""Stores information about a booked ride"""
class BookedRideObject(RideObject):
    def __init__(self, user, origin, destination, no_of_seats, cost):
        super().__init__(user, origin, destination, no_of_seats)
        self.cost = cost

"""Abstract Class for AppUser"""
class AppUser:
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return self.__name

    def user_type(self):
        raise NotImplementedError

    def validate_ride(self, origin, destination):
        if destination <= origin: return False
        return True

"""Driver user"""
class OnboardDriver(AppUser):
    def __init__(self, name):
        super().__init__(name)
        self.ride = None
        self.datastore = Datastore()

    def user_type(self):
        return "Driver"

    def create_ride(self, origin, destination, no_of_seats):
        if self.validate_ride(origin, destination) is False:
            print(Exception("Cant create ride, invalid input"))
            return
        if self.ride is not None:
            print(Exception("Driver {} already has a ride".format(self)))
            return
        new_ride = RideObject(self, origin, destination, no_of_seats)
        self.ride = new_ride
        self.datastore.add_driver_ride(new_ride)
        print("Ride created for {}".format(self))
    
    def update_ride(self, origin, destination, no_of_seats):
        if self.validate_ride(origin, destination) is False:
            print(Exception("Cant update ride for {}, invalid input".format(self)))
            return
        if self.ride is None:
            print(Exception("Driver {} has no ride to update".format(self)))
            return
        self.datastore.remove_driver_ride(self.ride)
        updated_ride = RideObject(self, origin, destination, no_of_seats)
        self.datastore.add_driver_ride(updated_ride)
        self.ride = updated_ride
        print("Ride updated for {}".format(self))

    def withdraw_ride(self):
        if self.ride is None:
            print(Exception("Driver {} has no ride to withdraw".format(self)))
            return
        self.datastore.remove_driver_ride(self.ride)
        self.ride = None
        print("Ride withdrawn for Driver {}".format(self))
    

        

        
"""Rider user"""
class OnboardRider(AppUser):
    def __init__(self, name):
        super().__init__(name)
        self.no_of_rides = 0
        self.preferred = False
        self.datastore = Datastore()
        self.ride_sharing_service = RideSharingService()
        self.utils = Utils()
    
    def user_type(self):
        return "Rider"
    
    def book_ride(self, origin, destination, no_of_seats):
        print()
        print("{} requesting for ride".format(self))
        if self.validate_ride(origin, destination) is False:
            print(Exception("Cant book ride for {}, invalid input".format(self)))
            return
        print("INPUT: {} requests {}, {}, {}".format(self, origin, destination, no_of_seats))
        tempride = RideObject(self, origin, destination, no_of_seats)
        found_driver = self.ride_sharing_service.find_ride(tempride, self.datastore.get_offered_rides())
        if found_driver is False:
            print(Exception("No ride found for {}".format(self)))
            return
        cost = self.utils.basic_cost_calculate(destination - origin, no_of_seats, self.preferred)
        book_ride = BookedRideObject(self, origin, destination, no_of_seats, cost)
        self.datastore.add_booked_ride(book_ride)
        print("OUTPUT: Ride Amount = {} ".format(cost))
        print()
        
        
        
"""Storage for all booked and offered rides"""
"""Singelton class"""
class Datastore:
    __shared = dict()
    __driver_rides = set()
    __booked_rides = set()
    def __init__(self):
        self.__dict__ = self.__shared
        self.__driver_rides = self.__driver_rides
        self.__booked_rides = self.__booked_rides
    def add_driver_ride(self, ride):
        self.__driver_rides.add(ride)
    def get_offered_rides(self):
        return self.__driver_rides
    def remove_driver_ride(self, ride):
        self.__driver_rides.remove(ride)
    def add_booked_ride(self, ride):
        self.__booked_rides.add(ride)
    def get_booked_rides(self):
        return self.__booked_rides

    
"""Ride sharing Service"""
"""stateless class"""
class RideSharingService:
    def find_ride(self, temp_ride, available_rides):
        for rides in available_rides:
            if rides.origin <= temp_ride.origin and rides.destination >= temp_ride.destination and \
            rides.seats >= temp_ride.seats:
                return True
            return False

"""Common utilitity functions"""
"""stateless"""
class Utils:
    def cost_calculating_algorithms(self, type = "basic"):
        algos = {
            "basic" : self.basic_cost_calculate,
        }
        

    def basic_cost_calculate(self, distance, seats, preffered = False):
        if preffered and seats >= 2:
            cost = distance * seats * StaticValues['ChargePerKm'].value * 0.5
        elif preffered:
            cost = distance * StaticValues['ChargePerKm'].value * 0.75
        elif seats >= 2:
            cost = distance * seats * 0.75 * StaticValues['ChargePerKm'].value
        else:
            cost = distance * StaticValues['ChargePerKm'].value
        return cost


#def create_user()

def app_activities():
    d1 = OnboardDriver("Ram")
    d1.create_ride(0, 10, 3)
    d1.update_ride(5, 12, 2)
    d1.update_ride(95, 12, 2)

    r1 = OnboardRider("John")
    r1.book_ride(7, 10, 2)


if __name__ == "__main__":
    app_activities()

