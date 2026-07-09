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

labels = [fill(x, 40) for x in labels]

# Percentages
Opportunity = np.array([84.4, 71.1, 71.2, 70.4, 81.3])
Risk = np.array([6.3, 22.9, 14.4, 13.0, 6.3])
Other = np.array([9.4, 6.0, 14.4, 16.7, 12.5])

# Counts
Opportunity_n = [27, 59, 74, 38, 26]
Risk_n = [2, 19, 15, 7, 2]
Other_n = [3, 5, 15, 9, 4]

# Totals
totals = [32, 83, 104, 54, 32]
total_pct = [10.5, 27.2, 34.1, 17.7, 10.5]

# --------------------------------------------------
# Appearance
# --------------------------------------------------

colors = [
    "#2171B5",
    "#6BAED6",
    "#9ECAE1",
]

fig, ax = plt.subplots(figsize=(15, 6))

spacing=0.30
height=0.18

y = np.arange(len(labels)) * spacing

# --------------------------------------------------
# Bars
# --------------------------------------------------

left = np.zeros(len(labels))

series = [
    ("Mostly as an opportunity", Opportunity, Opportunity_n, colors[0], "white"),
    ("Mostly as a risk", Risk, Risk_n, colors[1], "white"),
    ("Other", Other, Other_n, colors[2], "black"),
]

for name, vals, counts, color, text_color in series:

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

        ax.text(
            left[i] + v / 2,
            y[i],
            f"{v:.1f}% ({counts[i]})",
            ha="center",
            va="center",
            fontsize=7.8,
            color=text_color,
            fontweight="bold"
        )

    left += vals


# --------------------------------------------------
# Axes
# --------------------------------------------------

ax.set_xlim(0, 110)

ax.set_yticks(y)
ax.set_yticklabels(labels, fontsize=10)

ax.invert_yaxis()

ax.set_xticks([0, 25, 50, 75, 100])
ax.set_xticklabels(["0%", "25%", "50%", "75%", "100%"])

ax.grid(axis="x", linestyle="--", alpha=0.3)
ax.set_axisbelow(True)

for spine in ax.spines.values():
    spine.set_visible(False)

ax.tick_params(axis="y", length=0)

# --------------------------------------------------
# Legend
# --------------------------------------------------

legend = [
    Patch(color=colors[0], label="Mostly as an opportunity"),
    Patch(color=colors[1], label="Mostly as a risk"),
    Patch(color=colors[2], label="Other"),
]

ax.legend(
    handles=legend,
    ncol=3,
    frameon=False,
    loc="upper left",
    bbox_to_anchor=(0, 1.10),
    fontsize=10,
    handlelength=1.5,
    columnspacing=2.0
)



plt.tight_layout()

# --------------------------------------------------
# Save
# --------------------------------------------------

plt.savefig(
    "AI_Perception_by_Career_Stage.png",
    dpi=600,
    bbox_inches="tight"
)


plt.show()
