import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")


    # Create scatter plot
    plt.scatter(df["Year"],df['CSIRO Adjusted Sea Level'])


    # Create first line of best fit
    year_predict = [range(1881,2051)]
    line1 = linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    y1 = [line1.slope*x +line1.intercept for x in year_predict]
    plt.plot(year_predict, y1)


    # Create second line of best fit
    df_filt = df[df['Year']>=2000]
    line2 = linregress(df_filt['Year'],df_filt['CSIRO Adjusted Sea Level'])
    y2 = [line2.slope*x +line2.intercept for x in year_predict]
    plt.plot(year_predict,y2)


    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()