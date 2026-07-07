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
    "Research manager/\nadministrator",
    "Evaluator/reviewer",
    "Policymaker/funder",
    "National Contact Point\n(NCP)/similar",
    "Other (please specify)"
]

labels = [fill(x, 35) for x in labels]


# Percentages
Yes = np.array([
    84.0,
    75.0,
    71.1,
    66.7,
    81.5,
    66.7,
    0.0,
    0.0,
    75.0
])

No = np.array([
    16.0,
    25.0,
    28.9,
    33.3,
    18.5,
    33.3,
    100.0,
    100.0,
    25.0
])


# Counts
Yes_n = np.array([
    21,
    39,
    138,
    6,
    22,
    18,
    0,
    0,
    15
])

No_n = np.array([
    4,
    13,
    56,
    3,
    5,
    9,
    1,
    2,
    5
])


# Totals
totals = [
    25,
    52,
    194,
    9,
    27,
    27,
    1,
    2,
    20
]


# --------------------------------------------------
# Appearance
# --------------------------------------------------

colors = [
    "#2171B5",
    "#6BAED6",
]


fig, ax = plt.subplots(figsize=(14,7))


spacing = 0.38
height = 0.22

y = np.arange(len(labels))*spacing


# --------------------------------------------------
# Bars
# --------------------------------------------------

left = np.zeros(len(labels))


series = [
    ("Yes", Yes, Yes_n, colors[0], "white"),
    ("No", No, No_n, colors[1], "black")
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

        if v >= 8:

            ax.text(
                left[i] + v/2,
                y[i],
                f"{v:.1f}% ({counts[i]})",
                ha="center",
                va="center",
                fontsize=8.5,
                fontweight="bold",
                color=text_color
            )


    left += vals



# --------------------------------------------------
# Total labels
# --------------------------------------------------

for i in range(len(labels)):

    ax.text(
        102,
        y[i],
        f"N={totals[i]}",
        va="center",
        fontsize=9,
        fontweight="bold"
    )


# --------------------------------------------------
# Axes
# --------------------------------------------------

ax.set_xlim(0,115)

ax.set_xticks(
    [0,25,50,75,100]
)

ax.set_xticklabels(
    ["0%","25%","50%","75%","100%"]
)


ax.set_yticks(y)

ax.set_yticklabels(
    labels,
    fontsize=10
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
        color=colors[0],
        label="Yes"
    ),
    Patch(
        color=colors[1],
        label="No"
    )
]


ax.legend(
    handles=legend,
    ncol=2,
    frameon=False,
    loc="upper left",
    bbox_to_anchor=(0,1.08),
    fontsize=10
)



# --------------------------------------------------
# Title
# --------------------------------------------------

ax.set_title(
    "Current Role in Relation to the MSCA Programme",
    fontsize=15,
    fontweight="bold",
    loc="left",
    pad=45
)


# Header
ax.text(
    102,
    -0.45,
    "Total",
    fontsize=10,
    fontweight="bold"
)



plt.tight_layout()


# --------------------------------------------------
# Save
# --------------------------------------------------

plt.savefig(
    "MSCA_Current_Role.png",
    dpi=600,
    bbox_inches="tight"
)

plt.savefig(
    "MSCA_Current_Role.pdf",
    bbox_inches="tight"
)


plt.show()