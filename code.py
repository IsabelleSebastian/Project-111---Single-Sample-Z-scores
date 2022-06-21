import plotly.graph_objects as pg
import plotly.figure_factory as pf
import statistics
import random
import pandas as pd

df = pd.read_csv("medium_article.csv")
data = df["reading_time"].tolist()

pop_mean = statistics.mean(data)
print("Population Mean: ", pop_mean)

#------------------------------------> taking data sample

def random_means(counter):
    meanList = []
    for i in range(0,counter):
        index = random.randint(0,len(data)-1)
        rand_data = data[index]
        meanList.append(rand_data)
    mean1 = statistics.mean(meanList)
    return(mean1)

finalMeanList = []
for i in range(0,10):
    setOfMeans = random_means(30)
    finalMeanList.append(setOfMeans)
sampleMean = statistics.mean(finalMeanList)
stdev = statistics.stdev(finalMeanList)
print("Sample Mean: ", sampleMean, "& Sample Standard Dev: ", stdev)

#-------------------------------> finding z-score
z = (sampleMean - pop_mean) / stdev
print("Z-score: ", z)



