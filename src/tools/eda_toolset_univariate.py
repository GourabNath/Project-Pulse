# Tools
import pandas as pd
import numpy as np

# Tail profiling (right)
def right_tail_percentiles(series: pd.Series):
    '''
    Activation:
    Used when the interpretation suggests a right skew, long upper tail, or unusually large maximum values compared to Q3.
    
    What it analyzes:
    Computes high percentiles (e.g., P90, P95, P99) to understand how rapidly the distribution expands in the upper tail.
    
    Example:
    Q3 = 20, max = 150  
    P90 = 22  
    P95 = 30  
    P99 = 120  
    Interpretation: Most values remain below ~30 but a very small fraction extends dramatically higher.
    '''
    s = series.dropna()
    return {
        "p80": float(s.quantile(0.90)),
        "p85": float(s.quantile(0.90)),
        "p90": float(s.quantile(0.90)),
        "p95": float(s.quantile(0.95)),
        "p99": float(s.quantile(0.99)),
        "p99.5": float(s.quantile(0.995)),
        "max": float(s.max())
    }




# Tail profiling (left)
def left_tail_percentiles(series: pd.Series):
    '''
    Activation:
    Used when the interpretation suggests a left skew, long lower tail, or unusually small minimum values compared to Q1.
    
    What it analyzes:
    Computes low percentiles (e.g., P1, P5, P10) to determine how far the distribution stretches toward smaller values.
    
    Example:
    Q1 = 40, min = 2  
    P10 = 35  
    P5 = 25  
    P1 = 4  
    Interpretation: Most observations stay above ~35 but a few extend much lower.
    '''
    s = series.dropna()
    return {
        "p80": float(s.quantile(0.20)),
        "p85": float(s.quantile(0.15)),
        "p90": float(s.quantile(0.10)),
        "p95": float(s.quantile(0.05)),
        "p99": float(s.quantile(0.01)),
        "max": float(s.max())
    }




# Outlier analysis
def outlier_analysis(series: pd.Series):
    '''
    Activation:
    Triggered when boxplot whiskers appear long or when max/min seem far from the central range.
    
    What it analyzes:
    Uses the IQR rule to identify observations outside the normal spread.
    
    Method:
    Lower Bound = Q1 − 1.5 × IQR  
    Upper Bound = Q3 + 1.5 × IQR
    
    Example:
    Q1 = 10  
    Q3 = 20  
    IQR = 10  
    
    Upper bound = 35  
    
    Values above 35 are classified as outliers.

    '''
    s = series.dropna()

    q1 = s.quantile(0.25)
    q3 = s.quantile(0.75)
    iqr = q3 - q1

    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    outliers = s[(s < lower) | (s > upper)]
    outliers_upper = s[s > upper]
    outliers_lower = s[s < lower]

    return {
        "iqr": float(iqr),
        "lower_bound": float(lower),
        "upper_bound": float(upper),
        "outlier_count": int(len(outliers)),
        "outlier_count_upper": int(len(outliers_upper)),
        "outlier_count_lower": int(len(outliers_lower)),
        "max_outlier": float(outliers.max()) if len(outliers) else None,
        "min_outlier": float(outliers.min()) if len(outliers) else None
    }




# clustering or concentration of values - This supports investigations like “values cluster between 1–5” seen in histograms.
def bin_distribution(series: pd.Series):
    '''
    Activation:
    Used when the histogram suggests clustering or uneven concentration of observations across ranges.
    
    What it analyzes:
    Divides the variable range into bins and counts observations in each bin to measure where values are concentrated.
    
    Example:
    Range: 0–50  
    
    Bins:
    0–10 → 60 observations  
    10–20 → 25 observations  
    20–30 → 10 observations  
    30–40 → 3 observations  
    40–50 → 2 observations  
    
    Interpretation: Majority of observations cluster in the lower range.
    '''
    s = series.dropna()

    k = int(np.ceil(np.log2(len(s)) + 1))
    bins = np.linspace(s.min(), s.max(), k)
    counts = pd.cut(s, bins=bins).value_counts().sort_index()

    return {
        "bin_ranges": [str(i) for i in counts.index],
        "counts": counts.tolist()
    }


#Analyse data with large variance
def variability_analysis(series: pd.Series):
    '''
    Activation:
    Triggered when the spread of the variable appears unusually wide relative to its average.
    
    What it analyzes:
    Measures variability using standard deviation, variance, and coefficient of variation.
    
    Method:
    Coefficient of Variation = std / mean
    
    Example:
    mean = 20  
    std = 25  
    CV = 1.25  
    
    Interpretation: The variable varies more than its average magnitude, indicating high dispersion.
    '''
    s = series.dropna()

    mean = s.mean()
    std = s.std()

    cv = std / mean if mean != 0 else None

    return {
        "mean": float(mean),
        "std": float(std),
        "variance": float(s.var()),
        "coefficient_of_variation": float(cv) if cv else None
    }





def missing_analysis(series: pd.Series):
    '''
    Activation:
    Used when missing values are present or when the summary indicates a non-zero missing percentage.
    
    What it analyzes:
    Counts missing values and computes the percentage of missing observations.
    
    Example:
    Total records = 1000  
    Missing = 120  
    
    Missing percent = 12%
    
    Interpretation: A meaningful portion of the data is absent and may influence analysis.
    '''
    total = len(series)
    missing = series.isna().sum()

    return {
        "total_values": int(total),
        "missing_values": int(missing),
        "missing_percent": float((missing / total) * 100)
    }





def tight_distribution(series: pd.Series):
    '''
    Activation:
    Triggered when the histogram appears very narrow or when standard deviation is small relative to the mean.
    
    What it analyzes:
    Measures how tightly observations cluster around the center using standard deviation, IQR, and coefficient of variation.
    
    Example:
    mean = 50  
    std = 2  
    IQR = 3  
    CV = 0.04  
    
    Interpretation: Values are highly concentrated around the central range with very little variation.
    '''
    s = series.dropna()

    q1 = s.quantile(0.25)
    q3 = s.quantile(0.75)
    iqr = q3 - q1

    mean = s.mean()
    std = s.std()

    cv = std / mean if mean != 0 else None

    return {
        "std": float(std),
        "iqr": float(iqr),
        "coefficient_of_variation": float(cv) if cv else None
    }
