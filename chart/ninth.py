import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch
from textwrap import fill

# --------------------------------------------------
# Data
# --------------------------------------------------

labels = [
    "Current MSCA doctoral fellow",
    "Current MSCA postdoctoral fellow",
    "MSCA alumni",
    "Host supervisor",
    "Research manager/administrator",
    "Evaluator/reviewer",
    "Other"
]

labels = [fill(x, 32) for x in labels]

# --------------------------------------------------
# Percentages
# --------------------------------------------------

Selected = np.array([0.0, 0.0, 7.1, 0.0, 0.0, 0.0, 0.0])

AllMembers = np.array([37.5, 11.1, 21.4, 66.7, 50.0, 33.3, 0.0])

OutsideMSCA = np.array([37.5, 55.6, 50.0, 0.0, 0.0, 33.3, 100.0])

DontKnow = np.array([25.0, 33.3, 21.4, 33.3, 50.0, 33.3, 0.0])

# --------------------------------------------------
# Counts
# --------------------------------------------------

Selected_n = [0,0,1,0,0,0,0]

AllMembers_n = [3,1,3,2,2,1,0]

OutsideMSCA_n = [3,5,7,0,0,1,1]

DontKnow_n = [2,3,3,1,2,1,0]

# --------------------------------------------------
# Totals
# --------------------------------------------------

totals = [8,9,14,3,4,3,1]
total_pct = [24.2,27.3,42.4,9.1,12.1,9.1,3.0]

# --------------------------------------------------
# Appearance
# --------------------------------------------------

colors = [
    "#08306B",
    "#2171B5",
    "#6BAED6",
    "#9ECAE1"
]

fig, ax = plt.subplots(figsize=(15,7))

spacing = 0.38
height = 0.22

y = np.arange(len(labels))*spacing

left = np.zeros(len(labels))

series = [
    ("Only selected MSCA project members", Selected, Selected_n, colors[0], "white"),
    ("Training available to all MSCA project members", AllMembers, AllMembers_n, colors[1], "white"),
    ("Training also available outside the MSCA project", OutsideMSCA, OutsideMSCA_n, colors[2], "black"),
    ("I don't know", DontKnow, DontKnow_n, colors[3], "black"),
]

# --------------------------------------------------
# Bars
# --------------------------------------------------

for name, vals, counts, color, txt in series:

    ax.barh(
        y,
        vals,
        left=left,
        height=height,
        color=color,
        edgecolor="white",
        linewidth=0.8
    )

    for i, v in enumerate(vals):

        if v > 0:

            ax.text(
                left[i] + v/2,
                y[i],
                f"{counts[i]}\n({v:.1f}%)",
                ha="center",
                va="center",
                fontsize=8,
                color=txt,
                fontweight="bold"
            )

    left += vals

# --------------------------------------------------
# Totals
# --------------------------------------------------

for i in range(len(labels)):

    ax.text(
        101,
        y[i],
        f"{totals[i]} ({total_pct[i]:.1f}%)",
        va="center",
        fontsize=9,
        fontweight="bold"
    )

ax.text(
    101,
    -0.42,
    "Total (N)",
    fontsize=10,
    fontweight="bold"
)

# --------------------------------------------------
# Axes
# --------------------------------------------------

ax.set_xlim(0,110)

ax.set_xticks([0,25,50,75,100])

ax.set_xticklabels([
    "0%",
    "25%",
    "50%",
    "75%",
    "100%"
])

ax.set_yticks(y)
ax.set_yticklabels(labels, fontsize=10)

ax.invert_yaxis()

ax.grid(axis="x", linestyle="--", alpha=.3)

ax.set_axisbelow(True)

for s in ax.spines.values():
    s.set_visible(False)

ax.tick_params(axis="y", length=0)

# --------------------------------------------------
# Legend
# --------------------------------------------------

legend = [
    Patch(color=colors[0], label="Only selected MSCA project members"),
    Patch(color=colors[1], label="Training available to all MSCA project members"),
    Patch(color=colors[2], label="Training also available outside the MSCA project"),
    Patch(color=colors[3], label="I don't know"),
]

ax.legend(
    handles=legend,
    ncol=2,
    frameon=False,
    loc="upper left",
    bbox_to_anchor=(0,1.18),
    fontsize=9,
    handlelength=1.5,
    columnspacing=2
)

# --------------------------------------------------
# Title
# --------------------------------------------------

ax.set_title(
    "Perceived Eligibility for AI Training within MSCA Projects by Current Role",
    fontsize=16,
    fontweight="bold",
    loc="left",
    pad=60
)

plt.tight_layout(rect=[0,0,1,0.92])

plt.savefig(
    "MSCA_AI_Training_Eligibility.png",
    dpi=600,
    bbox_inches="tight"
)


plt.show()