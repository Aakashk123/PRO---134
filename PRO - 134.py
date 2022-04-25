from turtle import distance
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("starsGravity.csv")

print(df.head())

star_dist=[]

for i in df.Distance:
    if i <= 100:
        star_dist.append(True)
    else:
        star_dist.append(False)
    

is_dist = pd.Series(star_dist)

print(is_dist.head())


starDistanceList = df[is_dist]

starDistanceList.reset_index(inplace=True , drop = True)
print(starDistanceList.head())

# ----------------- gravity in range of 150 - 350 ------------------

gravity=[]

for i in df.Gravity:
    if i <= 350 & i >= 150:
        gravity.append(True)
    else:
        gravity.append(False)
    

is_gravity = pd.Series(gravity)

finalStars = starDistanceList[is_gravity]
print(finalStars.head())


finalStars.reset_index(inplace=True , drop = True)
print(finalStars.head())

finalStars.to_csv("FilteredStars.csv")

