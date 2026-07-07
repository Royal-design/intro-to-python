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
total_percent = 100.0


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

ax.set_xlim(0,110)

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
# Legend
# --------------------------------------------------

legend = [
    Patch(color=colors[0], label="Mostly as an opportunity"),
    Patch(color=colors[1], label="Mostly as a risk"),
    Patch(color=colors[2], label="Others"),
]

ax.legend(
    handles=legend,
    ncol=3,
    frameon=False,
    loc="upper left",
    bbox_to_anchor=(0, 1.12),
    fontsize=10,
    handlelength=1.5,
    columnspacing=2.0
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
# Totals at end
# --------------------------------------------------

for i in range(len(labels)):
    ax.text(
        101,
        y[i],
        f"{counts[i]} ({percent[i]:.1f}%)",
        va="center",
        fontsize=10,
        fontweight="bold"
    )

# Header
ax.text(
    101,
    -0.28,
    "Total (N)",
    fontsize=10,
    fontweight="bold"
)

# Grand total at bottom
ax.text(
    101,
    y[-1] + 0.32,
    f"{total} ({total_percent:.1f}%)",
    fontsize=11,
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



plt.show()