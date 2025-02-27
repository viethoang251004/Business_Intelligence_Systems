import matplotlib.pyplot as plt
from scipy import stats

x = [i for i in range(1, 13)]
y = [2925.5, 2705, 3116, 3310, 3396, 2964, 3478, 3147, 3145, 3027.5, 3367.5, 3048.5]

revenue_years = []
revenue_year = 0

#---Linear regression - continuous prediction - considering...---
slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

x = [i for i in range(1, 121)]
for i in range(13, 121):
    y.append(myfunc(i))

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.title("Current and future prediction for revenue for the Classic Deluxe Pizza for each year")
plt.xlabel("Months")
plt.ylabel("Revenue")
plt.show()

#Test r
print(r)

#Testing prediction
revenue_pred = myfunc(24)
print(revenue_pred)