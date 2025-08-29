import pandas as pd

clean_data = pd.read_csv("Clean Data.csv")
demand_df = pd.read_excel("AA.Sakakah 2021 Demand dataset.xlsx")

# Ensure both timestamp columns are in datetime format
clean_data["DATE & TIME"] = pd.to_datetime(clean_data["DATE & TIME"])
demand_df["DATE-TIME"] = pd.to_datetime(demand_df["DATE-TIME"])

# Merge the datasets
clean_data = pd.merge(clean_data, demand_df, left_on = "DATE & TIME", right_on = "DATE-TIME", how = "inner")
clean_data.drop(["DATE-TIME"], axis = 1, inplace = True)

clean_data.rename(columns = {
    "MW" : "MW Demand",
    "Mega Watts" : "MW Supply"
}, inplace = True)

# Linear Interpolation to fix NaN values
clean_data["MW Demand"] = clean_data["MW Demand"].interpolate(method = 'linear')

clean_data.to_csv("AA.Complete Data.csv", index = False)