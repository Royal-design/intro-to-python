import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch
from textwrap import fill

# --------------------------------------------------
# Data
# --------------------------------------------------

labels = [
    "R1 – First Stage Researcher\n(e.g., PhD candidate or equivalent)",
    "R2 – Recognised Researcher\n(PhD holder or equivalent; not yet fully independent)",
    "R3 – Established Researcher\n(independent researcher)",
    "R4 – Leading Researcher\n(e.g., professor or principal investigator)",
    "Not a researcher",
    "Total"
]

labels = [fill(x, 42) for x in labels]


# Percentages
Yes = np.array([
    84.4,
    78.3,
    65.4,
    70.4,
    81.3,
    73.4
])

No = np.array([
    15.6,
    21.7,
    34.6,
    29.6,
    18.8,
    26.6
])


# Counts
Yes_n = np.array([
    27,
    65,
    68,
    38,
    26,
    224
])

No_n = np.array([
    5,
    18,
    36,
    16,
    6,
    81
])


# Total N
totals = [
    32,
    83,
    104,
    54,
    32,
    305
]


# --------------------------------------------------
# Appearance
# --------------------------------------------------

colors = [
    "#2171B5",
    "#6BAED6",
]


fig, ax = plt.subplots(figsize=(14,7))


spacing = 0.22
height = 0.15

y = np.arange(len(labels))*spacing


# --------------------------------------------------
# Bars
# --------------------------------------------------

left = np.zeros(len(labels))


series = [
    ("Yes, integrated AI", Yes, Yes_n, colors[0], "white"),
    ("No, not integrated AI", No, No_n, colors[1], "black")
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
# Total labels at right
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
        label="Yes, integrated AI"
    ),
    Patch(
        color=colors[1],
        label="No, not integrated AI"
    )
]


ax.legend(
    handles=legend,
    ncol=2,
    frameon=False,
    loc="upper left",
    bbox_to_anchor=(0,1.10),
    fontsize=10
)



# --------------------------------------------------
# Title
# --------------------------------------------------

ax.set_title(
    "Integration of AI into Research Activities by Career Stage",
    fontsize=15,
    fontweight="bold",
    loc="left",
    pad=45
)


# Total header

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
    "AI_Integration_by_Career_Stage.png",
    dpi=600,
    bbox_inches="tight"
)

plt.savefig(
    "AI_Integration_by_Career_Stage.pdf",
    bbox_inches="tight"
)


plt.show()