
def extract_metadata(df, column):

    col = df[column]

    metadata = {
        "dtype": str(col.dtype),
        "unique_values": int(col.nunique()),
        "sample_values": col.dropna().sample(min(10, len(col))).tolist()
    }

    if col.dtype in ["int64", "float64"]:
        metadata.update({
            "min": float(col.min()),
            "max": float(col.max()),
            "mean": float(col.mean())
        })

    else:
        metadata["top_values"] = col.value_counts().head(5).to_dict()

    return metadata


def generate_variable_description(variable_name, problem, metadata):
  import json
  system_prompt = """
      You are a data science assistant helping document dataset variables.

      You will receive:
      1. The business problem context
      2. A variable name
      3. Metadata about the variable (data type, example values, statistics)

      Your tasks:
      1. Write a short and precise description of the variable.
      2. Determine the variable type.
      3. Explain the reasoning.

      The possible variable types are:
      - Continuous
      - Discrete
      - Nominal
      - Ordinal

      Follow the procedure below strictly.

      --------------------------------
      STEP 1 — Determine if the variable is numerical or categorical

      If the values are numbers → Numerical variable.
      If the values are labels or text categories → Categorical variable.

      --------------------------------
      CASE 1 — Numerical Variable

      Ask the question:

      "Can the variable take ANY possible value within a range (an interval)?"

      Examples:
      2.13, 2.131, 2.1315 etc.

      If YES → Continuous variable

      Examples:
      temperature, salary, weight, time duration.

      If the variable can take only specific separated values (even if decimals are present) → Discrete variable.

      Examples:
      Number of purchases: 0,1,2,3
      Rating: 1,2,3,4,5
      Score: 0, 0.5, 1

      Important rule:
      If the allowed values form a finite or countable set → Discrete.

      --------------------------------
      CASE 2 — Categorical Variable

      Ask the question:

      "Do the categories represent ordered levels of an underlying quantity, intensity, or frequency?"

      If the categories can logically be arranged from lower to higher → Ordinal.

      Examples:
      Satisfaction: Low, Medium, High
      Education: High School, Bachelor, Master, PhD
      BusinessTravel: Non-Travel, Travel_Rarely, Travel_Frequently

      Important:
      Even if numeric thresholds are not visible, if the categories represent levels of intensity or frequency, the variable is Ordinal.

      Example:
      Non-Travel < Travel_Rarely < Travel_Frequently

      This represents increasing travel frequency, so it is Ordinal.

      If the categories do NOT have any meaningful order → Nominal.

      Examples:
      Gender: Male, Female
      Department: Sales, HR, Finance
      Country: USA, India, Germany

      --------------------------------

      Return the answer strictly in JSON format:

      {
      "description": "...",
      "variable_type": "Continuous | Discrete | Nominal | Ordinal",
      "reason": "short explanation"
      }
    """


  user_prompt = f'''
  Problem: 
  {problem}

  Variable Name: 
  {variable_name}

  Variable Metadata:
  {json.dumps(metadata, indent=2)}
  Generate the variable description'''

  messages = [
      {"role":"system", "content":system_prompt}, 
      {"role":"user", "content":user_prompt}
      ]

  client = OpenAI()
  response = client.chat.completions.create(model="gpt-4.1-nano", messages=messages)
  return response.choices[0].message.content
