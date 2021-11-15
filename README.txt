Jacob Richard

To run a trial of the farm model, please type
python3 main.py
You will be asked to pick a color for the cattle, R for red, P for Purple, Y for yellow.


To run a unit test over the three classes (Pen, Cow, CreateGraphs) please type
python3 unitTest.py
The unit tests run over each possible color type.

Library versions
  Numpy version: 1.16.4
  csv version: 1.0
  matplotlib version: 3.1.0
  Python version: 3.6.8
  unittest version: it is the same for all python 3, no version




Welcome to the model I have created for a farm.

There are three objects, Cow, Pen, and createGraphs.

The user can pick to have a pen with Red Cows, Purple Cows, or Yellow Cows. Each pen has one color of cow in it.
The color of the cow determines parameters such as max population of the pen, and mean greenhouse gas.

The cows population is determined by a logistic model.

A cow produces milk according to a Bernoulli distribution multiplied by the probablility of the given cow being female.
The model for milk is determined by Bayes rule.

A cow produces greenhouse gases according to a Gaussian distribution.
There is a zero cut off for the distribution making sure no cow produces negative greenhouse gases.

The amount of milk for a population is equal to the sum of the milk for each cow.
The same is True for Greenhouse gas.

The cost of a pen is proportional to the population times the amount of feed given.


When the user runs the main program, a trial is set up which creates a pen with the specified cow type.
10 Years on the farm pass, metrics are collected including milk daily, milk total, greenhouse daily, greenhouse total, population, and cost.
The information is saved to a csv file. Graphs are created of various metrics and printed to the screen.
Metrics for the graphs include, Milk daily for the Pen, GreenHouse gases daily for the pen, Population for the Pen, and Cost of The Pen.
