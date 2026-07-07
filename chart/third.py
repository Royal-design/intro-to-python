import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch
from textwrap import fill

# --------------------------------------------------
# Data
# --------------------------------------------------

labels = [
    "AI as both an opportunity and a risk (context-dependent)",
    "AI as a tool to support research",
    "Cautious optimism",
    "Limited or no use / neutral perception",
    "Negative or sceptical perception"
]

labels = [fill(x, 38) for x in labels]


# Percentage and frequency
percent = np.array([33.3, 27.8, 13.9, 13.9, 11.1])
counts = np.array([12, 10, 5, 5, 4])


# --------------------------------------------------
# Appearance
# --------------------------------------------------

colors = [
    "#08306B",
    "#2171B5",
    "#6BAED6",
    "#9ECAE1",
    "#D9F0F7"
]


fig, ax = plt.subplots(figsize=(16,8))


spacing = 0.55
height = 0.30

y = np.arange(len(labels))*spacing


# --------------------------------------------------
# Bars
# --------------------------------------------------

for i in range(len(labels)):

    ax.barh(
        y[i],
        percent[i],
        color=colors[i],
        edgecolor="white",
        linewidth=0.8,
        height=height
    )


    ax.text(
        percent[i]/2,
        y[i],
        f"{counts[i]} ({percent[i]:.1f}%)",
        ha="center",
        va="center",
        fontsize=11,
        fontweight="bold",
        color="white" if i < 2 else "black"
    )


# --------------------------------------------------
# Frequency labels at end
# --------------------------------------------------

for i in range(len(labels)):

    ax.text(
        35,
        y[i],
        f"n = {counts[i]}",
        va="center",
        fontsize=11,
        fontweight="bold"
    )


# --------------------------------------------------
# Axes
# --------------------------------------------------

ax.set_xlim(0,42)


ax.set_xticks(
    [0,10,20,30,40]
)

ax.set_xticklabels(
    ["0%","10%","20%","30%","40%"],
    fontsize=11
)


ax.set_yticks(y)

ax.set_yticklabels(
    labels,
    fontsize=12
)


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
    Patch(
        color=colors[i],
        label=labels[i].replace("\n"," ")
    )
    for i in range(len(labels))
]


ax.legend(
    handles=legend,
    ncol=2,
    frameon=False,
    loc="upper left",
    bbox_to_anchor=(0,1.20),
    fontsize=10,
    handlelength=1.5,
    columnspacing=2
)



# --------------------------------------------------
# Title
# --------------------------------------------------

ax.set_title(
    "Themes Identified from 'Other' Responses on AI Perception",
    fontsize=18,
    fontweight="bold",
    loc="left",
    pad=80
)


plt.tight_layout()


# --------------------------------------------------
# Save high quality
# --------------------------------------------------

plt.savefig(
    "AI_Themes.png",
    dpi=600,
    bbox_inches="tight",
    pad_inches=0.3
)





plt.show()