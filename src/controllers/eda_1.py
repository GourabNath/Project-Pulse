
def univariate_eda_num(df_path, meta_data_path):
      import json
      import time
      import pandas as pd
      import matplotlib.pyplot as plt
      from src.engines.utils.typewriter import stream_markdown
      from src.engines.utils.print_multiple_lines import print_multiple_lines

      # Read df
      df = pd.read_csv(df_path)
      # Open the JSON file and load its content into a dictionary
      with open(meta_data_path, 'r') as f:
          meta_data_dict = json.load(f)


      #PLAYGROUND 1 - SUMMARY STATISTICS
      stream_markdown("## Summary Statistics")
      stream_markdown("\n" + "-"*80 + "\n")

      eda = meta_data_dict['eda1_univariate']['numeric']['summary']
      stream_markdown("**Variable:** " + eda['variable'])
      stream_markdown("**Variable Type:** " + eda['variable_type'])
      stream_markdown(eda['methodology'])
      stream_markdown("\n" + "-"*80 + "\n")

      stream_markdown("**Use code:** ")
      stream_markdown(eda['code'])
      print("\n")

      print(df[eda['variable']].describe())
      stream_markdown("\n" + "-"*80 + "\n")

      #time.sleep(0.5)
      print("\n")
      stream_markdown("*Now let's discuss how we can interpret and report these results.*")
      print("\n")
      
      for key in eda["statistics"].keys():
        #time.sleep(0.5)
        stream_markdown(eda["statistics"][key].replace("  ", "").replace("\t", ""))
        stream_markdown("\n" + "-"*80 + "\n")
      print("\n")
      stream_markdown(eda['remark'])
      print("\n\n")
      input("Press ENTER to continue")

      #-----------------
      # GRAPHICAL ANALYSIS - HISTOGRAM
      stream_markdown("## Graphical analysis using Histogram")
      stream_markdown("\n" + "-"*80 + "\n")

      hist = meta_data_dict['eda1_univariate']['numeric']['histogram']
      stream_markdown(hist["intro"])
      stream_markdown("\n" + "-"*80 + "\n")
      stream_markdown("Use the code below to plot the histogram.")
      stream_markdown(hist["code"])
      stream_markdown("\n" + "-"*80 + "\n")
      print("\n")

      #plt.figure(figsize=(6, 4))
      df[eda['variable']].hist(bins=10)                   # Plot histogram with 10 bins
      plt.title('Distribution of ' + eda['variable']) # Add a title
      plt.xlabel(eda['variable'])                         # Add x-axis label
      plt.ylabel('Frequency')                   # Add y-axis label
      plt.grid(axis='y', alpha=0.2)             # Add transparency to grid lines
      plt.grid(axis='x', alpha=0.2)
      plt.show()

      print("\n")
      stream_markdown("\n" + "-"*80 + "\n")
      stream_markdown(hist["observation"])
      stream_markdown("\n" + "-"*80 + "\n")
      print("\n\n")
      input("Press ENTER to continue")

      #----------------
      # GRAPHICAL ANALYSIS - BOXPLOT
      stream_markdown("## Graphical analysis using Boxplot")
      stream_markdown("\n" + "-"*80 + "\n")

      box = meta_data_dict['eda1_univariate']['numeric']['boxplot']
      stream_markdown(box["intro"])
      stream_markdown("Use the code below to plot the boxplot.")
      stream_markdown(box["code"])
      stream_markdown("\n" + "-"*80 + "\n")
      print("\n")

      import matplotlib.pyplot as plt

      #plt.figure(figsize=(6, 4))                      # Create a new figure with a specified size
      plt.boxplot(df[eda['variable']])                # Create a boxplot of the 'Age' column from the DataFrame 'df'
      plt.title('Boxplot of ' + eda['variable'])      # Add a title to the boxplot
      plt.ylabel(eda['variable'])                     # Add a label to the y-axis
      plt.grid(axis='y', alpha=0.20)                  # Add a grid to the y-axis with some transparency
      plt.show()                                      # Display the plot

      print("\n")
      stream_markdown("\n" + "-"*80 + "\n")
      stream_markdown(box["observation"])
      stream_markdown("\n" + "-"*80 + "\n")
      print("\n\n")

      input("Press ENTER to continue")
      stream_markdown(meta_data_dict['eda1_univariate']['numeric']['Next steps'])
