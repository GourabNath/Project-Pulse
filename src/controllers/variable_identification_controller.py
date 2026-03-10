
def variable_identification(variable_df):
  import time
  for i in range(1,13):
    if i not in (4,6,10,12):
      stream_markdown("**"+ variable_df.loc[variable_df.useExample == i, "variable"] +"**")
      variable_description = variable_df.loc[variable_df.useExample == i, "variable_description"]
      print_multiple_lines(variable_description)
      stream_markdown("\n" + "-"*80 + "\n")

      texts = variable_df.loc[variable_df.useExample == i, "Question"]
      print_multiple_lines(texts)
      print("\n")
      response = input()
      #time.sleep(0.5)
      print("\n")
      if response.lower() == "yes":
        yes_route = variable_df.loc[variable_df.useExample == i, "Yes"]
        print_multiple_lines(yes_route)
        stream_markdown("\n" + "-"*80 + "\n")

      if response.lower() == "no":
        no_route = variable_df.loc[variable_df.useExample == i, "No"]
        print_multiple_lines(no_route)
        stream_markdown("\n" + "-"*80 + "\n")

      print("\n\n")
      #time.sleep(1)
    
    #Examples of continuous data types
    if i == 4:
      stream_markdown("*Similarly, you won't find it difficult to identify that the following variables are continious:*")
      print("\n")
      df_subset = variable_df.loc[variable_df.useExample == i, ["variable", "variable_description", "useExample"]]
      df_subset = df_subset[~df_subset["useExample"].isin([1,2,3])].reset_index(drop=True)
      for index in range(0, len(df_subset)):
          stream_markdown("**"+ df_subset.loc[index, "variable"] +"**")
          variable_description = df_subset.loc[index, "variable_description"]
          stream_markdown(variable_description)
          stream_markdown("\n" + "-"*80 + "\n")
      print("\n\n")


    #Examples of discrete data types
    if i == 6:
      stream_markdown("*Similarly, you won't find it difficult to identify that the following variables are discrete:*")
      print("\n")
      df_subset = variable_df.loc[variable_df.useExample == i, ["variable", "variable_description", "useExample"]]
      df_subset = df_subset[~df_subset["useExample"].isin([1,2,3,4,5])].reset_index(drop=True)
      for index in range(0, len(df_subset)):
          stream_markdown("**"+ df_subset.loc[index, "variable"] +"**")
          variable_description = df_subset.loc[index, "variable_description"]
          stream_markdown(variable_description)
          stream_markdown("\n" + "-"*80 + "\n")
      print("\n\n")

    
    #Examples of Nominal data types
    if i == 10:
      stream_markdown("*Similarly, you won't find it difficult to identify that the following variables are nominal:*")
      print("\n")
      df_subset = variable_df.loc[variable_df.useExample == i, ["variable", "variable_description", "useExample"]]
      df_subset = df_subset[~df_subset["useExample"].isin([1,2,3,4,5,7,8,9])].reset_index(drop=True)
      for index in range(0, len(df_subset)):
          stream_markdown("**"+ df_subset.loc[index, "variable"] +"**")
          variable_description = df_subset.loc[index, "variable_description"]
          stream_markdown(variable_description)
          stream_markdown("\n" + "-"*80 + "\n")
      print("\n\n")


    #Examples of ordinal data types
    if i == 12:
      stream_markdown("*Similarly, you won't find it difficult to identify that the following variables are ordinal:*")
      print("\n")
      df_subset = variable_df.loc[variable_df.useExample == i, ["variable", "variable_description", "useExample"]]
      df_subset = df_subset[~df_subset["useExample"].isin([1,2,3,4,5,7,8,9,11])].reset_index(drop=True)
      for index in range(0, len(df_subset)):
          stream_markdown("**"+ df_subset.loc[index, "variable"] +"**")
          variable_description = df_subset.loc[index, "variable_description"]
          stream_markdown(variable_description)
          stream_markdown("\n" + "-"*80 + "\n")
      print("\n\n")

    
    
