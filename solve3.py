import marimo

# This Marimo notebook demonstrates interactive data analysis
# Author email: 24ds3000072@ds.study.iitm.ac.in

app = marimo.App()

# -----------------------------
# Cell 1: Import libraries
# -----------------------------
# This cell provides the base libraries used by later computations.
@app.cell
def _(pd=__import__("pandas"), np=__import__("numpy")):
    import pandas as pd
    import numpy as np
    return pd, np


# -----------------------------
# Cell 2: Create synthetic dataset
# -----------------------------
# Data created here is used by the analysis cell and visualization cells.
@app.cell
def _(np):
    np.random.seed(42)
    x = np.linspace(0, 10, 100)
    y = 3 * x + np.random.normal(0, 3, 100)  # linear relationship with noise
    return x, y


# -----------------------------
# Cell 3: Slider widget
# -----------------------------
# The slider controls the smoothing factor used in later analysis.
@app.cell
def _(mo):
    smoothing_slider = mo.ui.slider(
        start=1,
        stop=20,
        step=1,
        label="Smoothing Window Size"
    )
    smoothing_slider
    return smoothing_slider


# -----------------------------
# Cell 4: Compute smoothed data (depends on slider + source data)
# -----------------------------
# Demonstrates variable dependency: uses x, y, and smoothing_slider.
@app.cell
def _(pd, x, y, smoothing_slider):
    window = smoothing_slider.value
    df = pd.DataFrame({"x": x, "y": y})
    df["y_smoothed"] = df["y"].rolling(window=window, min_periods=1).mean()
    df
    return df, window


# -----------------------------
# Cell 5: Visualization (depends on df)
# -----------------------------
# Shows how the smoothing parameter affects the plotted curve.
@app.cell
def _(df, window):
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.scatter(df["x"], df["y"], alpha=0.4, label="Raw Data")
    ax.plot(df["x"], df["y_smoothed"], color="red", label=f"Smoothed (window={window})")
    ax.legend()
    ax.set_title("Relationship Between x and y")
    fig
    return


# -----------------------------
# Cell 6: Dynamic Markdown output
# -----------------------------
# The text changes based on the slider value.
@app.cell
def _(mo, window):
    if window < 5:
        msg = "### 🔍 Fine smoothing applied — capturing local fluctuations."
    elif window < 12:
        msg = "### 📊 Moderate smoothing — balancing noise and trend."
    else:
        msg = "### 🧹 Heavy smoothing — trend is emphasized, noise suppressed."

    mo.md(msg)
    return msg


# -----------------------------
# Cell 7: Summary text
# -----------------------------
# Documents data flow across cells for reproducibility.
@app.cell
def _():
    summary = """
### Data Flow Summary

1. **Cell 1** loads `pandas` and `numpy`.
2. **Cell 2** creates synthetic linear data (`x`, `y`).
3. **Cell 3** defines a slider widget controlling the smoothing window.
4. **Cell 4** computes smoothed data using slider value.
5. **Cell 5** visualizes both raw and smoothed data.
6. **Cell 6** outputs *dynamic markdown* based on smoothing level.

This ensures a transparent, self-documenting computational workflow.
"""
    summary
    return summary


if __name__ == "__main__":
    app.run()
