#Saurav Hossain
#09/21/18
#Borough Stats

import matplotlib.pyplot as plt
import pandas as pd

x = input()

pop = pd.read_csv('nycHistPop.csv',skiprows=5)

print("Average Population", pop[x].mean())
print("Max Population", pop[x].max())
