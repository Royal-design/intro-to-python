import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch
from textwrap import fill


# --------------------------------------------------
# Data
# --------------------------------------------------

labels = [
    "Trust, transparency, and explainability",
    "Ethical, social, and accountability concerns",
    "Limited time to remain up-to-date with fast-evolving technologies",
    "Lack of knowledge about AI and how it can be applied in my area",
    "Skill gaps and uneven AI literacy in my team/organisation",
    "Data availability, quality, governance, and security",
    "Inadequate technical infrastructure and access",
    "Financial constraints",
    "Methodological and epistemic incompatibility",
    "Limited collaboration opportunities with AI experts",
    "Institutional or policy restrictions",
    "Regulatory and policy gaps",
    "I don't need AI for my research",
    "Other (please specify)"
]


labels = [fill(x, 42) for x in labels]


# --------------------------------------------------
# Percentages
# --------------------------------------------------

R1 = np.array([
    11.0,9.8,14.2,9.3,10.1,16.3,13.8,15.5,15.2,13.1,20.0,26.8,2.8,20.0
])

R2 = np.array([
    32.9,30.1,26.1,26.2,23.6,25.6,25.0,22.5,21.2,24.6,28.9,22.0,30.6,20.0
])

R3 = np.array([
    30.5,36.6,28.4,39.3,31.5,26.7,35.0,35.2,34.8,37.7,28.9,34.1,44.4,25.0
])

R4 = np.array([
    14.6,16.3,20.1,15.9,24.7,23.3,17.5,19.7,24.2,19.7,8.9,9.8,16.7,25.0
])

NR = np.array([
    11.0,7.2,11.2,9.3,10.1,8.1,8.8,7.0,4.5,4.9,13.3,7.3,5.6,10.0
])


# --------------------------------------------------
# Counts
# --------------------------------------------------

R1_n = [18,15,19,10,9,14,11,11,10,8,9,11,1,4]
R2_n = [54,46,35,28,21,22,20,16,14,15,13,9,11,4]
R3_n = [50,56,38,42,28,23,28,25,23,23,13,14,16,5]
R4_n = [24,25,27,17,22,20,14,14,16,12,4,4,6,5]
NR_n = [18,11,15,10,9,7,7,5,3,3,6,3,2,2]


# --------------------------------------------------
# Totals
# --------------------------------------------------

totals = [
    164,153,134,107,89,86,80,71,
    66,61,45,41,36,20
]


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


fig, ax = plt.subplots(figsize=(15,9))


spacing = 0.42
height = 0.25

y = np.arange(len(labels))*spacing


# --------------------------------------------------
# Bars
# --------------------------------------------------

left = np.zeros(len(labels))


series = [
    ("R1 – First Stage Researcher",R1,R1_n,colors[0],"white"),
    ("R2 – Recognised Researcher",R2,R2_n,colors[1],"white"),
    ("R3 – Established Researcher",R3,R3_n,colors[2],"black"),
    ("R4 – Leading Researcher",R4,R4_n,colors[3],"black"),
    ("Not a researcher",NR,NR_n,colors[4],"black")
]


for name,vals,counts,color,text_color in series:


    ax.barh(
        y,
        vals,
        left=left,
        height=height,
        color=color,
        edgecolor="white",
        linewidth=.8
    )


    for i,v in enumerate(vals):

        if v >= 0:

            ax.text(
                left[i] + v/2,
                y[i],
                f"{v:.1f}% ({counts[i]})",
                ha="center",
                va="center",
                fontsize=6.8,
                color=text_color,
                fontweight="bold"
            )


    left += vals




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
    fontsize=9
)


ax.invert_yaxis()


ax.grid(
    axis="x",
    linestyle="--",
    alpha=.3
)


ax.set_axisbelow(True)


for s in ax.spines.values():
    s.set_visible(False)


ax.tick_params(
    axis="y",
    length=0
)



# --------------------------------------------------
# Legend
# --------------------------------------------------

legend = [
    Patch(color=colors[0],label="R1 – First Stage Researcher"),
    Patch(color=colors[1],label="R2 – Recognised Researcher"),
    Patch(color=colors[2],label="R3 – Established Researcher"),
    Patch(color=colors[3],label="R4 – Leading Researcher"),
    Patch(color=colors[4],label="Not a researcher")
]


ax.legend(
    handles=legend,
    ncol=5,
    frameon=False,
    loc="upper left",
    bbox_to_anchor=(0,1.08),
    fontsize=9
)




plt.tight_layout()


plt.savefig(
    "Barriers_to_AI_Adoption_by_Career_Stage.png",
    dpi=600,
    bbox_inches="tight"
)


plt.show()