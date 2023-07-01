#!/usr/bin/env python
# coding: utf-8

# In[11]:


# If not already installed, do: pip install pandas fastparquet
import pandas as pd

URL_DATA = 'https://storage.googleapis.com/dosm-public-economy/salaries_state_sex_xs.parquet'

df = pd.read_parquet(URL_DATA)
if 'date' in df.columns: df['date'] = pd.to_datetime(df['date'])

print(df)


# In[12]:


df.head()


# In[13]:


df.tail()


# In[18]:


import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
data = pd.read_csv('salaries_state_sex.csv')

# Group the data by state and calculate the mean wage for each state and year
mean_wages = data.groupby(['variable_en', 'year'])['mean'].mean()

# Reset the index to convert the grouped data into a DataFrame
mean_wages = mean_wages.reset_index()

# Plot the mean wages over time for every state
plt.figure(figsize=(12, 6))
for state in mean_wages['variable_en'].unique():
    state_data = mean_wages[mean_wages['variable_en'] == state]
    plt.plot(state_data['year'], state_data['mean'], label=state)

plt.title('Mean Wages Over Time for Every State')
plt.xlabel('Year')
plt.ylabel('Mean Wage')
plt.legend()
plt.grid(True)
plt.show()


# In[37]:


import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
data = pd.read_csv('salaries_state_sex.csv')

# Filter the data for females and males
female_data = data[data['sex'] == 'female']
male_data = data[data['sex'] == 'male']

# Calculate the mean wages for females and males for each state
mean_wages_female = female_data.groupby('variable_en')['mean'].mean()
mean_wages_male = male_data.groupby('variable_en')['mean'].mean()

# Identify the states where female wages are equal to or higher than male wages
equal_or_higher_states = mean_wages_female[mean_wages_female >= mean_wages_male].index

# Plot the mean wages for females and males
plt.figure(figsize=(12, 6))

# Set the bar width
bar_width = 0.4

# Calculate the position of each bar on the x-axis
x = range(len(mean_wages_female))

# Plot the mean wages for females
plt.bar(x, mean_wages_female, width=bar_width, label='Female')

# Plot the mean wages for males
plt.bar([i + bar_width for i in x], mean_wages_male, width=bar_width, label='Male')

# Add a square box to highlight states where female wages are equal to or higher than male wages
for i, state in enumerate(mean_wages_female.index):
    if state in equal_or_higher_states:
        plt.text(i + bar_width/2, max(mean_wages_female[i], mean_wages_male[i]) + 50, '■', ha='center', va='bottom', color='green', fontsize=12)

# Set the x-axis ticks and labels
plt.xticks([i + bar_width/2 for i in x], mean_wages_female.index, rotation=45, ha='right')

plt.title('Mean Wages: Female vs Male by State')
plt.xlabel('State')
plt.ylabel('Mean Wage')
plt.legend()
plt.show()


# In[25]:


import pandas as pd

# Load the CSV file into a DataFrame
data = pd.read_csv('salaries_state_sex.csv')

# Filter the data for the years 2021 and 2022
filtered_data = data[(data['year'] >= 2021) & (data['year'] <= 2022)]

# Group the filtered data by the overall category and calculate the mean salary
overall_data = filtered_data[filtered_data['sex'] == 'overall']
mean_salaries = overall_data.groupby('variable_en')['mean'].mean()

# Sort the mean salaries in descending order
sorted_salaries = mean_salaries.sort_values(ascending=False)

# Select the top 5 salaries
top_5_salaries = sorted_salaries.head(5)

# Display the top 5 highest salaries
print(top_5_salaries)


# In[49]:


import pandas as pd
import matplotlib.pyplot as plt

# Define the data
data = {
    'variable_en': ['W.P. Putrajaya', 'W.P. Kuala Lumpur', 'Selangor', 'W.P. Labuan', 'Pulau Pinang'],
    'mean': [4503.7, 4013.1, 3543.5, 3268.2, 3079.6]
}

# Calculate the overall mean wage
overall_mean = sum(data['mean']) / len(data['mean'])

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Plot the data
plt.figure(figsize=(10, 6))
plt.bar(df['variable_en'], df['mean'], color='steelblue')


# Add labels and title
plt.xlabel('State')
plt.ylabel('Mean Salary')
plt.title('Top 5 Highest Salaries (2021-2022)')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Display the plot
plt.show()


# In[40]:


import pandas as pd

# Load the CSV file into a DataFrame
data = pd.read_csv('salaries_state_sex.csv')

# Filter the data for the 2021-2022 period
data_2021_2022 = data[data['year'] == 2021]

# Calculate the mean salaries for each state
mean_salaries = data_2021_2022.groupby('variable_en')['mean'].mean()

# Sort the mean salaries in ascending order
sorted_salaries = mean_salaries.sort_values()

# Select the 5 states with the lowest salaries
lowest_salaries = sorted_salaries.head(5)

# Display the 5 states with the lowest salaries
print(lowest_salaries)


# In[50]:


import pandas as pd
import matplotlib.pyplot as plt

# Define the data
data = {
    'State': ['Kedah', 'Terengganu', 'Perlis', 'Kelantan', 'Perak'],
    'Mean Salary': [2475.033333, 2489.100000, 2600.033333, 2600.200000, 2608.366667]
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Set the Y-axis limit
y_limit = 3000

# Plot the bar chart
plt.figure(figsize=(8, 6))
plt.bar(df['State'], df['Mean Salary'], color='blue')
plt.xlabel('State')
plt.ylabel('Mean Salary')
plt.title('5 States with the Lowest Mean Salaries (2021-2022)')
plt.ylim(0, y_limit)


plt.show()


# In[48]:


import pandas as pd

# Load the CSV file into a DataFrame
data = pd.read_csv('salaries_state_sex.csv')

# Calculate the mean wages for each state
mean_wages = data.groupby('variable_en')['mean'].mean()


# Sort the mean wages in descending order
sorted_mean_wages = mean_wages.sort_values(ascending=False)

# Print the sorted mean wages
print(sorted_mean_wages)


# In[ ]:




