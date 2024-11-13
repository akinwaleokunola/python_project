import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

df = pd.read_csv("c:\\Users\\HP\\Downloads\\epa-sea-level.csv")

plt.figure(figsize=(10,6))
plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"],color="blue",label= "Observed Sea Level")
slope, intercept,r_value, p_value, std_err=linregress(df["Year"],df["CSIRO Adjusted Sea Level"])
years_extended=pd.Series(range(1880,2051))
sea_level_pred=intercept+slope*years_extended
plt.plot(years_extended,sea_level_pred, "r",label="Best Fit Line(1880-2050)")

recent_df= df[df["Year"]>=2000]
slope_recent, intercept_recent, r_value_recent,p_value_recent, std_err_recent=linregress(
recent_df["Year"],recent_df["CSIRO Adjusted Sea Level"])
sea_level_pred_recent= intercept_recent+slope_recent*years_extended
plt.plot(years_extended,sea_level_pred_recent,"green", label="Best Fit Line(2000-2050)")
plt.xlabel("Year")
plt.ylabel("Sea Level(inches)")
plt.title("Rise in Sea Level")
plt.legend()

plt.savefig("sea_level_plot_.png")
plt.show()