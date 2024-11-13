import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv("c:\\Users\\HP\\Downloads\\fcc-forum-pageviews.csv", parse_dates=["date"], index_col="date")

lower_bound=df["value"].quantile(0.025)
upper_bound=df["value"].quantile(0.975)
df_cleaned= df[(df["value"]>= lower_bound)&(df["value"]<=upper_bound)]


def draw_line_plot():
    fig, ax=plt.subplots(figsize=(10,5))
    
    ax.plot(df_cleaned.index, df_cleaned["value"],color= "tab:blue")
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016/-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page views")
    
    plt.show()
    
# Generate the plot
draw_line_plot()

def draw_bar_plot():
    df_bar= df_cleaned.copy()
    df_bar["Year"]=df_bar.index.year
    df_bar["Month"]= df_bar.index.month_name()
    
    df_bar= df_bar.groupby(["Year","Month"])["value"].mean().unstack()
    fig, ax=plt.subplots(figsize=(12,6))
    df_bar.plot(kind="bar",ax=ax, legend=True,cmap="tab10")
    
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    ax.legend(title= "Months")
    
    plt.show()
    
draw_bar_plot()
    
def draw_box_plot():
    df_box =df_cleaned.copy()
    df_box["Year"]= df_box.index.year
    df_box["Month"]= df_box.index.month_name()
    df_box["Month"]=pd.Categorical(df_box["Month"], 
    categories=["January","February","March", "April","May","June","July","August","September","October","November","December"], ordered=True)
        
    fig,(ax1, ax2)=plt.subplots(1, 2, figsize=(15,6))
        
    sns.boxplot(x="Year",y="value",data=df_box,ax=ax1)
    ax1.set_title("Year-wise Box Plot(Trend)")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("page views")
        
    sns.boxplot(x="Month",y="value", data=df_box, ax=ax2)
    ax2.set_title("Month-wise Box Plot(seasonality)")
    ax2.set_xlabel("Month")
    ax2.set_ylabel("page views")
        
    plt.show()
        
draw_box_plot()
            

        
