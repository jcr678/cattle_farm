import numpy as np
import csv
from matplotlib import pyplot as plt
#each cow breed has its own parameters for the below calculations
#the user chooses the cow


#milk yield: (binomial model)*p(female)
#greenhouse: gaussian distributed, with no negative values
#population per pen: logistic function with cap proportional to amount of feed.


class CreateGraphs:
    def __init__(self, arrayOfOuput, nameOfFile, timer):
        self.arrayOfOuput = arrayOfOuput
        self.nameOfFile = nameOfFile
        self.timer = timer
    def createGraphsAndPrintToScreen(self):
        #create graphs for population, co2 daily , milk daily, cost
        #print said graphs to the screen. Please click exit on a given graph to print the next one
        x = np.arange(0,self.timer)
        milk = [self.arrayOfOuput[i][0] for i in range(len(self.arrayOfOuput))]
        plt.title("Milk Daily")
        plt.xlabel("Time")
        plt.ylabel("Milk")
        plt.plot(x,milk,"ob")
        plt.show()
        greenhouse = [self.arrayOfOuput[i][2] for i in range(len(self.arrayOfOuput))]
        plt.title("GreenHouse Gas Daily")
        plt.xlabel("Time")
        plt.ylabel("GreenHouse Gas")
        plt.plot(x,greenhouse,"ob")
        plt.show()
        population = [self.arrayOfOuput[i][4] for i in range(len(self.arrayOfOuput))]
        plt.title("Population vs Time")
        plt.xlabel("Time")
        plt.ylabel("Population")
        plt.plot(x,population,"ob")
        plt.show()
        cost = [self.arrayOfOuput[i][5] for i in range(len(self.arrayOfOuput))]
        plt.title("Cost vs Time")
        plt.xlabel("Time")
        plt.ylabel("Cost")
        plt.plot(x,cost,"ob")
        plt.show()

    def writeExcelSheet(self):

        #write Excel sheet in current file location according to naming convention given by nameOfFile
        with open(self.nameOfFile, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(["milk_day", "milk_total", "greenhouse_day", "greenhouse_total","population", "cost"])
            csvwriter.writerows(self.arrayOfOuput)

class Cow:
    def __init__(self, color):
        self.color = color
        self.meanCo2 = self.initializeMeanCo2(self.color)
    def milk_yield_cow(self): #discrete amount of milk, P(female)*P(amount of milk | female) by bayes rule
        #p(amount of milk | female) is modeled by a binomial distribution

        isFemale = np.random.randint(low=0, high=2) #assume probability of female is .5 for all cow types
        #print(isFemale)
        if(isFemale):
            maxGallonsOfACow = 30 #all female cows have same max gallons for a day
            probabilityOfAGallonGivenFemale = .25
            #probability of milk given female is same for each color of cow
            amountOfMilk = np.random.binomial(n=maxGallonsOfACow, p=probabilityOfAGallonGivenFemale, size=None)
            #print(amountOfMilk)
            return amountOfMilk
        else: #males do not give milk
            return 0

    def greenhouse_cow(self): #The amount of greenhouse is given by a gaussian model
        amountOfCo2 = np.random.normal(loc=self.meanCo2, scale=20.0) #mean is different for every type of cow
        if amountOfCo2 <= 0: #cut off for gaussian, no negative greenhouse gas.
            return 0
        else:
            return amountOfCo2
    def initializeMeanCo2(self, color):
        #co2 is dependent on color of cow
        if color == 'purple': #purple cows produce least co2
            return 50.0
        elif color == 'yellow': #yellow
            return 60.0
        else:
            return 80.0 #red cows produce least co2


class Pen:
    def __init__(self, color):
        self.color = color
        #just initialize 1 cow and call the necessary functions (size population) times.
        self.cow = Cow(self.color) #no need to initialize an array of (size population) cows.
        self.amountOfFeed = self.initializeAmountOfFeed(self.color)
        self.timer = 0 #the timer determines the population
        self.milkYieldDay = 0 #total milk for the day
        self.milkYieldCumulative = 0 #total milk for all days
        self.greenHouseDay = 0 #total greenhouse for the day
        self.greenHouseCumulative = 0 #total greenhouse for all days
    def get_cost(self):
        #population * feed)
        return (self.get_population()) * self.amountOfFeed/100.0
    def get_population(self): #logistic model https://en.wikipedia.org/wiki/Logistic_function
        #dy/dt = y*(1-y)
        #the rate of growth for the given model
        rate = .003
        #the function is shifted right three days
        shiftGraph = 5.0
        #max amount of population is proportional to feed given. Amount of feed is dependent on color of cow.
        y = int(self.amountOfFeed/(1 + np.exp(-rate*(self.timer-shiftGraph))))
        return y

    def increase_timer(self): #another day on the farm
        self.timer += 1.0

    def milk_yield(self): #sum over population of cows
        tempMilk = 0
        for i in range(self.get_population()):
            tempMilk += self.cow.milk_yield_cow()
        self.milkYieldDay = tempMilk
        self.milkYieldCumulative += self.milkYieldDay
        return self.milkYieldDay, self.milkYieldCumulative
    def greenhouse(self): #sum over population of cows
        tempGreenHouse = 0
        for i in range(self.get_population()):
            tempGreenHouse += self.cow.greenhouse_cow()
        self.greenHouseDay= tempGreenHouse
        self.greenHouseCumulative += self.greenHouseDay
        return self.greenHouseDay, self.greenHouseCumulative

    def initializeAmountOfFeed(self, color):
        #amount of feed is dependent on color of cow
        if color == 'purple': #purple
            return 100.0
        elif color == 'yellow': #yellow
            return 200.0
        else: #red
            return 400.0
