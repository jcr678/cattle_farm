import unittest
from objects_farm import *


param_list = ['purple', 'yellow', 'red'] #colors of cows
#test cow objects for all colors
class test_cow(unittest.TestCase):
    def test_cow_init(self):
        for color in param_list:
            with self.subTest():
                c = Cow(color)
                self.assertIsInstance(c, Cow)
    def test_cow_milk(self): #randomly generated numbers
        for color in param_list:
            with self.subTest():
                c = Cow(color)
                milk = c.milk_yield_cow()
                self.assertIsInstance(milk, int)
    def test_greenhouse_cow(self): #randomly generated numbers
        for color in param_list:
            with self.subTest():
                c = Cow(color)
                milk = c.greenhouse_cow()
                self.assertIsInstance(milk, float)
    def test_initializeMeanCo2(self): #constant numbers
        for color in param_list:
            with self.subTest():
                c = Cow(color)
                meanCo2 = c.initializeMeanCo2(color)
                if color == 'purple': #purple cows produce least co2
                    self.assertEqual(meanCo2, 50.0)
                elif color == 'yellow': #yellow
                    self.assertEqual(meanCo2, 60.0)
                else:
                    self.assertEqual(meanCo2, 80.0) #red cows produce least co2

#test pen for all colors
class test_pen(unittest.TestCase):
    def test_pen_init(self):
        for color in param_list:
            with self.subTest():
                p = Pen(color)
                self.assertIsInstance(p, Pen)
    def test_cost(self):
        for color in param_list:
            with self.subTest():
                p = Pen(color)
                cost = p.get_cost()
                self.assertIsInstance(cost, float)
    def test_population(self):
        for color in param_list:
            with self.subTest():
                p = Pen(color)
                cost = p.get_population()
                self.assertIsInstance(cost, int)
    def test_increase_timer(self): #timer returns none
        for color in param_list:
            with self.subTest():
                p = Pen(color)
                cost_boolean = p.increase_timer() is None
                self.assertTrue(cost_boolean)
    def test_milk_yield(self):
        for color in param_list:
            with self.subTest():
                p = Pen(color)
                milk_day, milk_total = p.milk_yield()
                self.assertIsInstance(milk_day, int)
                self.assertIsInstance(milk_total, int)

    def test_greenhouse_yield(self):
        for color in param_list:
            with self.subTest():
                p = Pen(color)
                greenhouse_day, greenhouse_total = p.greenhouse()
                self.assertIsInstance(greenhouse_day, float)
                self.assertIsInstance(greenhouse_total, float)

    def test_initializeMeanCo2(self): #constant numbers
        for color in param_list:
            with self.subTest():
                p = Pen(color)
                feed = p.initializeAmountOfFeed(color)
                if color == 'purple':
                    self.assertEqual(feed , 100.0)
                elif color == 'yellow':
                    self.assertEqual(feed , 200.0)
                else:
                    self.assertEqual(feed , 400.0)

class testGraphs(unittest.TestCase):
    def test_excel(self):
        graphCreator = CreateGraphs([[0,0,0,0,0,0]], "testcsv.csv", 1)
        csv = graphCreator.writeExcelSheet() is None
        self.assertTrue(csv)
    def test_graph_creation(self):
        graphCreator = CreateGraphs([[0,0,0,0,0,0]], "testcsv.csv", 1)
        graph = graphCreator.createGraphsAndPrintToScreen() is None
        self.assertTrue(graph)
if __name__ == '__main__':
    unittest.main()
