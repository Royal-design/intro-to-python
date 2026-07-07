import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch
from textwrap import fill

# --------------------------------------------------
# Data
# --------------------------------------------------

labels = [
    "Mostly as an opportunity",
    "Mostly as a risk",
    "Others"
]

labels = [fill(x, 35) for x in labels]

# Percentages
percent = np.array([73.4, 14.8, 11.8])

# Counts
counts = np.array([224, 45, 36])

# Total
total = 305


# --------------------------------------------------
# Appearance
# --------------------------------------------------

colors = [
    "#2171B5",
    "#6BAED6",
    "#9ECAE1",
]


fig, ax = plt.subplots(figsize=(12,4))

spacing = 0.28
height = 0.18

y = np.arange(len(labels))*spacing


# --------------------------------------------------
# Bars
# --------------------------------------------------

for i, value in enumerate(percent):

    ax.barh(
        y[i],
        value,
        height=height,
        color=colors[i],
        edgecolor="white",
        linewidth=0.8
    )

    ax.text(
        value/2,
        y[i],
        f"{value:.1f}% ({counts[i]})",
        ha="center",
        va="center",
        fontsize=10,
        fontweight="bold",
        color="white" if i < 2 else "black"
    )


# --------------------------------------------------
# Axes
# --------------------------------------------------

ax.set_xlim(0,100)

ax.set_xticks([0,25,50,75,100])
ax.set_xticklabels(
    ["0%","25%","50%","75%","100%"]
)

ax.set_yticks(y)
ax.set_yticklabels(labels, fontsize=11)

ax.invert_yaxis()


ax.grid(
    axis="x",
    linestyle="--",
    alpha=0.3
)

ax.set_axisbelow(True)


for spine in ax.spines.values():
    spine.set_visible(False)

ax.tick_params(
    axis="y",
    length=0
)


# --------------------------------------------------
# Title
# --------------------------------------------------

ax.set_title(
    "Overall Perception of Artificial Intelligence",
    fontsize=15,
    fontweight="bold",
    loc="left",
    pad=20
)


# --------------------------------------------------
# Total annotation
# --------------------------------------------------

ax.text(
    101,
    -0.5,
    f"Total N = {total}",
    fontsize=10,
    fontweight="bold"
)


plt.tight_layout()


# --------------------------------------------------
# Save
# --------------------------------------------------

plt.savefig(
    "Overall_AI_Perception.png",
    dpi=600,
    bbox_inches="tight"
)

plt.savefig(
    "Overall_AI_Perception.pdf",
    bbox_inches="tight"
)


plt.show()