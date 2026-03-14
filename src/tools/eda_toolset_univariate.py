# Tools
import pandas as pd
import numpy as np

# Tail profiling (right)
def right_tail_percentiles(series: pd.Series):
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
    total = len(series)
    missing = series.isna().sum()

    return {
        "total_values": int(total),
        "missing_values": int(missing),
        "missing_percent": float((missing / total) * 100)
    }


def tight_distribution(series: pd.Series):
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
