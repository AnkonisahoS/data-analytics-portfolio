# Recreate energy analysis charts and summaries
import pandas as pd, matplotlib.pyplot as plt
df=pd.read_csv("data/hourly_energy_demand.csv",parse_dates=["Timestamp"])
df["Month"]=df.Timestamp.dt.to_period("M").astype(str)
df.groupby("Month").DemandMW.mean().plot(marker="o",title="Average Energy Demand by Month")
plt.ylabel("Demand (MW)"); plt.xticks(rotation=45); plt.tight_layout(); plt.savefig("outputs/monthly_demand.png",dpi=160)
df.groupby("Hour").DemandMW.mean().plot(marker="o",title="Average Demand by Hour")
plt.xlabel("Hour of day"); plt.ylabel("Demand (MW)"); plt.tight_layout(); plt.savefig("outputs/hourly_profile.png",dpi=160)
df.plot.scatter(x="TemperatureC",y="DemandMW",alpha=.3,title="Temperature vs Energy Demand")
plt.tight_layout(); plt.savefig("outputs/temp_demand.png",dpi=160)
print(df[["TemperatureC","DemandMW"]].corr())
