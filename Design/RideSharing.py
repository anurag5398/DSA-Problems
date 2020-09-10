
#@class contains rider deatils
class Rider:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.rides = list()
        self.numberOfRides = 0
    
    def bookRide(self, start, end, seats, allRides):
        found = False
        for l, r, s, d in allRides.listOfRides:
            if start >= l and end <= r and seats <= s:
                found = True
                break
        if found is False:
            print("No matching ride found for {}.".format(self.name))
            return FaultyRide()
        self.rides.append((start, end, seats, d))
        allRides.listOfRides.remove((l, r, s, d))
        if s - seats > 0: allRides.listOfRides.append((l, r, s - seats, d))
        if l < start: allRides.listOfRides.append((s, start - 1, s - seats, d))
        if r > end: allRides.listOfRides.append((end + 1, r, s - seats, d))

        costPerKm = 20
        if self.numberOfRides > 10 and seats >= 2:
            cost = (end - start) * seats * costPerKm * 0.5
        elif self.numberOfRides > 10 and seats == 1:
            cost = (end - start) * costPerKm * 0.75
        elif seats >= 2:
            cost = (end - start) * seats * costPerKm * 0.75
        else:
            cost = (end - start) * costPerKm
        print("Ride booked for {}".format(self.name))
        return BookedRides(d, self, int(cost))


#@temp class for no rides available
class FaultyRide:
    def completeRide(self):
        print("No ride was created to complete.")

#@class contains driver deatils
class Driver:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.rides = list()
    
    def createRide(self, start, end, seats, allRides):
        self.rides.append((start, end, seats))
        allRides.listOfRides.append((start, end, seats, self.name))

#@temp class to store all rides
class Rides:
    def __init__(self):
        self.listOfRides = list()

#class creats object for each trip
class BookedRides:
    def __init__(self, driver, rider, cost, status = True):
        self.driver = driver
        self.rider = rider
        self.cost = cost
        self.status = status
    
    def completeRide(self):
        if self.status is False:
            print("Ride already completed")
            return
        self.rider.numberOfRides+=1
        print("{} has to pay {} to the driver {}".format(self.rider.name, self.cost, self.driver))
        self.status = False


def main():
    allRides = Rides()
    d1 = Driver(1, "Yusuf")
    d2 = Driver(2, "Ram")
    d3 = Driver(3, "Smith")

    r1 = Rider(4, "Kamal")
    r2 = Rider(5, "Shanti")
    r3 = Rider(6, "Mangal")

    d1.createRide(10, 50, 5, allRides)
    d1.createRide(60, 70, 3, allRides)
    d2.createRide(25, 55, 1, allRides)
    d3.createRide(0 , 60, 3, allRides)

    t1 = r1.bookRide(15, 25, 1, allRides)
    t3 = r2.bookRide(0, 100, 1, allRides)
    t2 = r3.bookRide(10 , 20, 3, allRides)

    t1.completeRide()
    t3.completeRide()
    t2.completeRide()



if __name__ == "__main__":
    main()