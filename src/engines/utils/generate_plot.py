#Generate plots (Only for numerical variables)
import os
import matplotlib.pyplot as plt
import seaborn as sns

def generate_plots_num(df, variable, run_path):

    # create variable folder
    variable_path = os.path.join(run_path, variable)
    os.makedirs(variable_path, exist_ok=True)

    # Histogram
    plt.figure()
    sns.histplot(df[variable], kde=False)
    plt.title(f"{variable} Distribution")
    hist_path = os.path.join(variable_path, "histogram.png")
    plt.savefig(hist_path)
    plt.close()

    # Boxplot
    plt.figure()
    sns.boxplot(x=df[variable])
    plt.title(f"{variable} Boxplot")
    box_path = os.path.join(variable_path, "boxplot.png")
    plt.savefig(box_path)
    plt.close()

    return hist_path, box_path
