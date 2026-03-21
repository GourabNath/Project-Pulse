
def univariate_eda_num(df_path, meta_data_path):
      '''
      Note: This introduction is static (and not generative). 
      This function initiates a playground that walks an user to start learning EDA for numerical variable.

      PARAMETERS
            df_path: path to the dataframe
            meta_data_path: path to the meta_data. The meta_data stores various calculated parameters of the variable and their interpretation.
      '''
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
      stream_markdown("## Summary Statistics")                               # Heading
      stream_markdown("\n" + "-"*80 + "\n")                                  # Seperating line

      eda = meta_data_dict['eda1_univariate']['numeric']['summary']          # Reads the full suummary - a pre-written analysis
      stream_markdown("**Variable:** " + eda['variable'])                    # Print the name of the variable
      stream_markdown("**Variable Type:** " + eda['variable_type'])          # Print the variable type
      stream_markdown(eda['methodology'])                                    # Print the methodology 
      stream_markdown("\n" + "-"*80 + "\n")                                  # Separating line

      stream_markdown("**Use code:** ")                                      # Sub-heading
      stream_markdown(eda['code'])                                           # Print the code to reproduce the result
      print("\n")

      print(df[eda['variable']].describe())                                  # Print the descriptive summary of the variable under study
      stream_markdown("\n" + "-"*80 + "\n")                                  # Separating line
      print("Press ENTER to continue")                                       # Just to pause for a while
      input()                                                                # The next section continues after user presses any key

      #time.sleep(0.5)
      print("\n")
      stream_markdown("*Now let's discuss how we can interpret and report these results...*")
      print("\n")
      
      for key in eda["statistics"].keys():                                    # keys: count, min, 25%, 50%, 75% max, mean, std
        #time.sleep(0.5)
        stream_markdown(eda["statistics"][key].replace("  ", "").replace("\t", ""))   # Print statistica interpretation (one statistic at a time)
        stream_markdown("\n" + "-"*80 + "\n")                                         # separating line
      print("\n") 
      stream_markdown(eda['remark'])                                                  # A final expert advice
      print("\n\n")
      print("Press ENTER to continue")
      input()

      #-----------------
      # GRAPHICAL ANALYSIS - HISTOGRAM
      stream_markdown("## Graphical analysis using Histogram")
      stream_markdown("\n" + "-"*80 + "\n")

      hist = meta_data_dict['eda1_univariate']['numeric']['histogram']                # Reads the entire histogram analysis from metadata
      stream_markdown(hist["intro"])                                                  # Prints an intro about hostogram
      stream_markdown("\n" + "-"*80 + "\n")                                           # separating line
      stream_markdown("Use the **code** below to plot the **histogram**.")            # subheading
      stream_markdown(hist["code"])                                                   # print code to reproduce result
      stream_markdown("\n" + "-"*80 + "\n")                                           # separating line
      print("\n")                                                                     

      time.sleep(1)
      #plt.figure(figsize=(6, 4))
      df[eda['variable']].hist(bins=10)                   # Plot histogram with 10 bins
      plt.title('Distribution of ' + eda['variable'])     # Add a title
      plt.xlabel(eda['variable'])                         # Add x-axis label
      plt.ylabel('Frequency')                             # Add y-axis label
      plt.grid(axis='y', alpha=0.2)                       # Add transparency to grid lines
      plt.grid(axis='x', alpha=0.2)
      plt.show()

      print("\n")
      stream_markdown("\n" + "-"*80 + "\n")
      stream_markdown("**Observation:** " + hist["observation"])     # interpretation of histogram
      stream_markdown("\n" + "-"*80 + "\n")
      print("\n\n")
      print("Press ENTER to continue")
      input()

      #----------------
      # GRAPHICAL ANALYSIS - BOXPLOT
      stream_markdown("## Graphical analysis using Boxplot")
      stream_markdown("\n" + "-"*80 + "\n")

      box = meta_data_dict['eda1_univariate']['numeric']['boxplot']
      stream_markdown(box["intro"])
      stream_markdown("Use the **code** below to plot the **boxplot**.")
      stream_markdown("\n" + "-"*80 + "\n")
      stream_markdown(box["code"])
      stream_markdown("\n" + "-"*80 + "\n")
      print("\n")

      import matplotlib.pyplot as plt

      time.sleep(1)
      #plt.figure(figsize=(6, 4))                     # Create a new figure with a specified size
      plt.boxplot(df[eda['variable']])                # Create a boxplot of the 'Age' column from the DataFrame 'df'
      plt.title('Boxplot of ' + eda['variable'])      # Add a title to the boxplot
      plt.ylabel(eda['variable'])                     # Add a label to the y-axis
      plt.grid(axis='y', alpha=0.20)                  # Add a grid to the y-axis with some transparency
      plt.show()                                      # Display the plot

      print("\n")
      stream_markdown("\n" + "-"*80 + "\n")
      stream_markdown("**Observation:** " + box["observation"])
      stream_markdown("\n" + "-"*80 + "\n")
      print("\n\n")

      print("Press ENTER to continue")
      input()
      stream_markdown(meta_data_dict['eda1_univariate']['numeric']['Next steps'].replace("  ", "").replace("\t", ""))
