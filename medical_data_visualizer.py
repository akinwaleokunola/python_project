import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Importing the dataset
df = pd.read_csv("c:\\Users\\HP\\Downloads\\medical_examination.csv")

# add an overweight column to the data, to determine if a person is overweight, first calculate their BMI by dividing their weight 
# in kilograms by the square of their height in meters. if that value is>25 then the person is overweight. use the value 0 for NOT 
# overweight and the value 1 for overweight.
df["overweight"]= ((df["weight"] / ((df["height"] / 100) ** 2)) >25).astype(int)

# Normalize data by making 0 always good and1 always bad. if the value of cholesterol or gluc is 1, set the value to 0. IF THE VALUE
# is more 1, set the value to 1.
df["cholesterol"]= df["cholesterol"].apply(lambda x: 0 if x== 1 else 1)
df["gluc"] =df["gluc"].apply(lambda x:0 if x==1 else 1)

# Draw the categorical plot in the draw_cat_plot function.
def draw_cat_plot():
    # create a dataframe for the cat plot using pd.melt with values from cholesterol, gluc, allco, active, overweight in the df_cat variable.
    df_cat = pd.melt(df,id_vars=["cardio"],value_vars=["cholesterol","gluc","smoke","alco", "active","overweight"])

    # Group and reformat the datain df_cat to split it by cardio. show the countsof each feature,.
    # You will have to rename one of the columns for catplot to work correctlY
    df_cat=df_cat.groupby(["cardio", "variable", "value"]).size().reset_index(name="total") 

    fig=sns.catplot(data=df_cat, kind="bar",x="variable",y="total",hue="value",col="cardio")
    fig. set_axis_labels("variable", "total")
    fig.set_titles("cardio={col_name}")
    fig.despine(left=True)
    return fig
cat_plot_fig =draw_cat_plot()

def draw_heat_map():
    df_heat = df[
    (df["ap_lo"]<= df["ap_hi"])&
    (df["height"]>= df["height"].quantile(0.025)) &
    (df["height"] <= df["height"].quantile(0.975))&
    (df["weight"] >= df["weight"].quantile(0.025))&
    (df["weight"] <= df["weight"].quantile(0.975)) 
    ]

    corr=df_heat.corr()

    mask=np.triu(np.ones_like(corr,dtype=bool))

    fig, ax=plt.subplots(figsize=(12, 12))
    sns.heatmap(corr, annot=True, mask=mask, square=True, fmt=".1f", center=0, vmin=0.1,vmax=0.25,cmap="coolwarm")

    return fig

heat_map_fig=draw_heat_map()

cat_plot_fig.savefig("c:\\Users\\HP\\OneDrive\\Desktop\\Visualizations\\categorical_plot.png")
heat_map_fig.savefig("c:\\Users\\HP\\OneDrive\\Desktop\\Visualizations\\heat_map.png")