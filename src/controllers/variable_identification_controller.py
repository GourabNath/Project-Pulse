def variable_identification(variable_df, row_description):
  import time

  intro_message = '''
  ## MODULE 2: IDENTIFICATION OF VARIABLE TYPES
  
  In this module you will spend some time to understand the variables you have in your dataset. You will also determine the variable type of each variable. 
  This is a very important step before you do your data analysis. Identifying the variable type will guide you towards the right choice of analysis you should perform for each variable.
  Hence, this is your must do step before you start your EDA and data analysis.

  '''

  intro_rows = '''
  **Rows**: One small step before you jump into the columns.
  Ask yourself, what does each row in the dataset represent? Each row represents an entity.
  In this problem, %s

  This is often the most ignored step. why do you need it? Because all your data interpretation and reporting depends on this identification. 

  ''' %row_description

  intro_variable = '''
  **Columns**: Each column in the dataset represent a variable. From a Statistical perspective, a variable is a characterestics of an entity.

  '''


  stream_markdown(intro_message)
  print("\n")
  stream_markdown(intro_rows)
  print("\n")
  stream_markdown(intro_variable)
  print("\n")


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
    
    #Examples:
    else:
      variable_type = variable_df.loc[variable_df.useExample == i, "variable_type"].reset_index(drop=True)
      variable_type = variable_type[0].lower()
      string = "Similarly, you won't find it difficult to identify that the following variable is also %s in nature" %variable_type
      stream_markdown("*"+ string+"*")
      print("\n")
      df_subset = variable_df.loc[variable_df.useExample == i, ["variable", "variable_description", "useExample"]]
      df_subset = df_subset[~df_subset["useExample"].isin([1,2,3])].reset_index(drop=True)
      for index in range(0, len(df_subset)):
          stream_markdown("**"+ df_subset.loc[index, "variable"] +"**")
          variable_description = df_subset.loc[index, "variable_description"]
          stream_markdown(variable_description)
          stream_markdown("\n" + "-"*80 + "\n")
      print("\n\n")

    
