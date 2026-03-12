
#Generate summmary:
def generate_summary(df, variable):

    desc = df[variable].describe()

    summary = {
        "variable": variable,
        "count": float(desc["count"]),
        "mean": float(desc["mean"]),
        "std": float(desc["std"]),
        "min": float(desc["min"]),
        "25%": float(desc["25%"]),
        "50%": float(desc["50%"]),
        "75%": float(desc["75%"]),
        "max": float(desc["max"]),
        "missing_pct": float(df[variable].isna().mean() * 100)
    }

    return summary


# Save summary statistics to JSON
import json
import os

def save_summary(summary, run_path, variable):

    variable_path = os.path.join(run_path, variable)
    os.makedirs(variable_path, exist_ok=True)

    summary_path = os.path.join(variable_path, "summary.json")

    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=4)

    return summary_path
