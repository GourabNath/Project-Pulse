
import json

# Define the path to your JSON file
json_file_path = "/content/drive/MyDrive/0_AI_Projects/00_Project_Pulse/Attrition/attrition_data.json"

# Open the JSON file and load its content into a dictionary
with open(json_file_path, 'r') as f:
    attrition_data_dict = json.load(f)


import time
import matplotlib.pyplot as plt
from src.engines.utils.typewriter import stream_markdown
from src.engines.utils.print_multiple_lines import print_multiple_lines

eda = attrition_data_dict['eda1_univariate']['numeric']['summary']
stream_markdown("**Variable:** " + eda['variable'])
stream_markdown("**Variable Type:** " + eda['variable_type'])
stream_markdown(eda['methodology'])
print("\n")
stream_markdown("**Use code:** ")
stream_markdown(eda['code'])
print("\n")
print(df[eda['variable']].describe())
time.sleep(0.5)
print("\n")
stream_markdown("Now let's discuss how we can interpret and report these results.")
print("\n")
for key in eda["statistics"].keys():
  time.sleep(0.5)
  stream_markdown(eda["statistics"][key].replace("  ", "").replace("\t", ""))
  stream_markdown("\n" + "-"*80 + "\n")
print("\n")
stream_markdown(eda['remark'])
print("\n\n")


#-----------------

hist = attrition_data_dict['eda1_univariate']['numeric']['histogram']
stream_markdown(hist["intro"])
stream_markdown("Use the code below to plot the histogram.")
stream_markdown(hist["code"])
print("\n")

plt.figure(figsize=(6, 4))
df['Age'].hist(bins=10)                   # Plot histogram with 10 bins
plt.title('Distribution of Employee Age') # Add a title
plt.xlabel('Age')                         # Add x-axis label
plt.ylabel('Frequency')                   # Add y-axis label
plt.grid(axis='y', alpha=0.2)             # Add transparency to grid lines
plt.grid(axis='x', alpha=0.2)
plt.show()

print("\n")
stream_markdown(hist["observation"])
print("\n\n")

#----------------

box = attrition_data_dict['eda1_univariate']['numeric']['boxplot']
stream_markdown(box["intro"])
stream_markdown("Use the code below to plot the boxplot.")
stream_markdown(box["code"])
print("\n")

import matplotlib.pyplot as plt

plt.figure(figsize=(6, 4))            # Create a new figure with a specified size
plt.boxplot(df['Age'])                # Create a boxplot of the 'Age' column from the DataFrame 'df'
plt.title('Boxplot of Employee Age')  # Add a title to the boxplot
plt.ylabel('Age')                     # Add a label to the y-axis
plt.grid(axis='y', alpha=0.20)        # Add a grid to the y-axis with some transparency
plt.show()                            # Display the plot

print("\n")
stream_markdown(box["observation"])
print("\n\n")


stream_markdown(attrition_data_dict['eda1_univariate']['numeric']['Next steps'])
