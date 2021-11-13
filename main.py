from objects_farm import *
#each cow breed has its own parameters for the below calculations
#choose cow


#milk yield: (binomial model)*p(female)
#greenhouse: gaussian distributed
#population per pen: logistic function with max population equal to amount of feed.
if __name__ == "__main__":
    #3 colors
    #yellow, purple, red.
    #please run with purple and with yellow to test how this works.
    while True:
        cow_color = input('-'*50 + "\nWelcome to the model for a farm. Please choose a color for your cows. \nType P for purple\nType Y for yellow\nType R for red\n")
        if cow_color.lower() == 'p':
            cow_color = 'purple'
            print("You chose Purple")
            break
        elif cow_color.lower() == 'y':
            cow_color = 'yellow'
            print("You chose Yellow")
            break
        elif cow_color.lower() == 'r':
            cow_color = 'red'
            print("You chose Red")
            break
        else:
            print("Please choose P, R, or Y")

    p = Pen(color=cow_color)
    years = 10
    arrayOfOuput = [] #array to save the information
    nameOfCSVFile = "outPutFarm-" + cow_color + ".csv"
    for i in range(365 * years): #run the trial for n years
        milk_day, milk_total = p.milk_yield()
        greenhouse_day, greenhouse_total = p.greenhouse()
        population = p.get_population()
        cost = p.get_cost()
        print("pop: " + str(population) + ", milk day " +  str(milk_day) + ", milk total " +
        str(milk_total) + ", green day " + str(greenhouse_day) + ", green total " + str(greenhouse_total))
        print("Cost = " + str(cost))
        arrayOfOuput.append([milk_day, milk_total, greenhouse_day, greenhouse_total,population, cost])
        p.increase_timer()

    #to do:
    #    unit test https://realpython.com/python-testing/
    #    write documentation (use pictures)

    graphCreator = CreateGraphs(arrayOfOuput, nameOfCSVFile, 365 * years)
    graphCreator.writeExcelSheet()
    graphCreator.createGraphsAndPrintToScreen()
