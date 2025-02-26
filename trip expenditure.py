def hotelCost(nights):
    return 140 * nights

def planeRideCost(country):
    if country == "South Korea":
        return 800
    elif country == "Japan":
        return 920
    elif country == "China":
        return 625
    elif country == "Uganda":
        return 700
    
def rentalCarCost(days):
    if days >= 7:
        return(100 * days) - 30
    elif days >= 3:
        return(60 * days) - 10
    else:
        return(40 * days)
    
def tripCost(city, days):
    hC = hotelCost(days)
    rC = rentalCarCost(days)
    pC = planeRideCost(city)
    
    sum = hC + rC + pC
    
    return sum


d = int(input("Enter the amount of days you will stay(in digit) : "))
c = input("Enter the city you are going to: ")

print()

print(f"Hotel cost : ${hotelCost(d)}")
print(f"Car cost : ${rentalCarCost(d)}")
print(f"Plane cost : ${planeRideCost(c)}")
print(f"Total cost : ${tripCost(c, d)}")
    
    
     
     
    