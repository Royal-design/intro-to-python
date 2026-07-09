import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch
from textwrap import fill

# --------------------------------------------------
# Data
# --------------------------------------------------

labels = [
    "R1 – First Stage Researcher\n(PhD candidate or equivalent)",
    "R2 – Recognised Researcher\n(PhD holder; not yet fully independent)",
    "R3 – Established Researcher\n(Independent researcher)",
    "R4 – Leading Researcher\n(Professor, PI, or equivalent)",
    "Not a researcher"
]

labels = [fill(x, 38) for x in labels]

yes = np.array([18.8, 14.5, 7.7, 7.4, 9.4])
no = np.array([68.8, 80.7, 86.5, 81.5, 68.8])
dontknow = np.array([0.0, 2.4, 3.8, 1.9, 6.3])
not_participated = np.array([12.5, 2.4, 1.9, 9.3, 15.6])

yes_n = [6,12,8,4,3]
no_n = [22,67,90,44,22]
dontknow_n = [0,2,4,1,2]
not_participated_n = [4,2,2,5,5]

totals = [32,83,104,54,32]
total_pct = [10.5,27.2,34.1,17.7,10.5]

# --------------------------------------------------
# Colours
# --------------------------------------------------

colors = [
    "#08306B",
    "#2171B5",
    "#6BAED6",
    "#9ECAE1"
]

# --------------------------------------------------
# Figure
# --------------------------------------------------

fig, ax = plt.subplots(figsize=(16,9))

y = np.arange(len(labels))

bar_height = 0.16

offsets = [-0.24, -0.08, 0.08, 0.24]

# --------------------------------------------------
# Bars
# --------------------------------------------------

bars = [
    ("Yes", yes, yes_n, colors[0], offsets[0], "white"),
    ("No", no, no_n, colors[1], offsets[1], "white"),
    ("I don't know", dontknow, dontknow_n, colors[2], offsets[2], "black"),
    ("Have not participated", not_participated, not_participated_n, colors[3], offsets[3], "black")
]

for name, values, counts, color, offset, txt_color in bars:

    ax.barh(
        y + offset,
        values,
        height=bar_height,
        color=color,
        edgecolor="white"
    )

    for i, v in enumerate(values):

        if v == 0:
            ax.text(
                0.5,
                y[i]+offset,
                "0",
                va="center",
                fontsize=8
            )
        else:
            ax.text(
                v + 1,
                y[i]+offset,
                f"{v:.1f}% ({counts[i]})",
                va="center",
                fontsize=8,
                fontweight="bold"
            )


# --------------------------------------------------
# Axes
# --------------------------------------------------

ax.set_xlim(0,120)

ax.set_xticks([0,20,40,60,80,100])

ax.set_xticklabels([
    "0%",
    "20%",
    "40%",
    "60%",
    "80%",
    "100%"
])

ax.set_yticks(y)
ax.set_yticklabels(labels, fontsize=10)

ax.invert_yaxis()

ax.grid(axis="x", linestyle="--", alpha=0.3)

ax.set_axisbelow(True)

for spine in ax.spines.values():
    spine.set_visible(False)

ax.tick_params(axis='y', length=0)

# --------------------------------------------------
# Legend
# --------------------------------------------------

legend = [
    Patch(color=colors[0], label="Yes"),
    Patch(color=colors[1], label="No"),
    Patch(color=colors[2], label="I don't know"),
    Patch(color=colors[3], label="I have not participated in an MSCA project")
]

ax.legend(
    handles=legend,
    ncol=2,
    frameon=False,
    loc="upper left",
    bbox_to_anchor=(0,1.16),
    fontsize=10
)

# --------------------------------------------------
# Title
# --------------------------------------------------

# ax.set_title(
#     "Awareness of MSCA Guidelines on the Use of Artificial Intelligence by Career Stage",
#     fontsize=16,
#     fontweight="bold",
#     loc="left",
#     pad=80
# )

plt.tight_layout()

plt.savefig(
    "MSCA_Guidelines_Grouped.png",
    dpi=600,
    bbox_inches="tight"
)


plt.show()