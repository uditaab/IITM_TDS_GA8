import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# -----------------------------------------------------------------------------
# Synthetic Data Generation for Customer Support Response Times
# -----------------------------------------------------------------------------

np.random.seed(42)

# Realistic response times (minutes) across support channels
data = {
    "Channel": np.repeat(
        ["Email", "Chat", "Phone", "Social Media"], repeats=150
    ),
    "Response_Time": np.concatenate([
        np.random.normal(loc=45, scale=12, size=150),  # Email slower
        np.random.normal(loc=8, scale=3, size=150),    # Chat fastest
        np.random.normal(loc=15, scale=5, size=150),   # Phone moderate
        np.random.normal(loc=25, scale=6, size=150)    # Social Media varied
    ])
}

df = pd.DataFrame(data)

# Clean invalid values (e.g., negative response times)
df["Response_Time"] = df["Response_Time"].clip(lower=1)

# -----------------------------------------------------------------------------
# Seaborn Styling (Professional Presentation-Ready)
# -----------------------------------------------------------------------------

sns.set_style("whitegrid")
sns.set_context("talk")  # Larger fonts suitable for executive presentations
palette = sns.color_palette("Set2")

# -----------------------------------------------------------------------------
# Create Violin Plot
# -----------------------------------------------------------------------------

plt.figure(figsize=(8, 8))   # Ensures output = 512 x 512 at dpi=64

sns.violinplot(
    data=df,
    x="Channel",
    y="Response_Time",
    palette=palette,
    inner="quartile",
    linewidth=1.2
)

plt.title("Customer Support Response Time Distribution by Channel", fontsize=18)
plt.xlabel("Support Channel", fontsize=14)
plt.ylabel("Response Time (minutes)", fontsize=14)

plt.tight_layout()

# -----------------------------------------------------------------------------
# Export Chart (exact 512x512 px)
# -----------------------------------------------------------------------------

plt.savefig("chart.png", dpi=64, bbox_inches="tight")  # 8in * 64dpi = 512px
plt.close()
