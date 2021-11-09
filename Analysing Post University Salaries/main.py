import pandas as pd

major_salaries = pd.read_csv('csv_data/salaries_by_college_major.csv')

new_dataframe = major_salaries.dropna()
# print(new_dataframe.tail())

max_starting_median_salary = new_dataframe["Starting Median Salary"].max()
# print(max_starting_median_salary)

index_of_row_with_max_starting_median_salary = new_dataframe["Starting Median Salary"].idxmax(
)

undergraduate_major_with_max_starting_median_salary = new_dataframe[
    "Undergraduate Major"].loc[index_of_row_with_max_starting_median_salary]

min_mid_career_salary = new_dataframe["Mid-Career 90th Percentile Salary"].max()
undergraduate_major_with_min_mid_career_salary = new_dataframe[
    "Undergraduate Major"].loc[new_dataframe["Mid-Career 90th Percentile Salary"].idxmax()]
# print(undergraduate_major_with_max_starting_median_salary)
# print(min_mid_career_salary)

lowest_starting_salary = new_dataframe["Starting Median Salary"].min()
undergraduate_major_with_lowest_starting_salary = new_dataframe[
    "Undergraduate Major"].loc[new_dataframe["Starting Median Salary"].idxmin()]
# print(undergraduate_major_with_lowest_starting_salary)
# print(lowest_starting_salary)

lowest_mid_career_salary = new_dataframe["Mid-Career 90th Percentile Salary"].min()
undergraduate_major_with_lowest_mid_career_salary = new_dataframe[
    "Undergraduate Major"].loc[new_dataframe["Mid-Career 90th Percentile Salary"].idxmin()]
# print(undergraduate_major_with_lowest_mid_career_salary)
# print(lowest_mid_career_salary)

spread_column = new_dataframe["Mid-Career 90th Percentile Salary"] - new_dataframe[
    "Starting Median Salary"]

new_dataframe.insert(loc=len(new_dataframe.columns),
                     column="Spread",
                     value=spread_column)

lowest_risk = new_dataframe.sort_values(by="Spread", ascending=True)
# print(lowest_risk[["Undergraduate Major", "Spread"]].head())
degrees_with_highest_values = new_dataframe.sort_values(by="Mid-Career 90th Percentile Salary", ascending=False)
# print(degrees_with_highest_values)
top_five_degrees_90th_percentile = degrees_with_highest_values[
    ["Undergraduate Major", "Mid-Career 90th Percentile Salary"]].head()
# print(top_five_degrees_90th_percentile)

highest_risk = new_dataframe.sort_values(by="Spread", ascending=False)
# print(highest_risk[["Undergraduate Major", "Spread"]].head())
df_group = new_dataframe.groupby("Group")
# print(df_group.count()) 
#find the average salary by group
df_group_mean = df_group.mean()
#print every column in the dataframe
# print(df_group_mean)
#display panda float in 2sf
pd.options.display.float_format = '{:.2f}'.format
print(df_group_mean)