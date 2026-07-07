import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch
from textwrap import fill

# --------------------------------------------------
# Data
# --------------------------------------------------

labels = [
    "Institution provides training or awareness programmes on AI and ethics",
    "I don't know",
    "Institution has clear guidelines on the responsible use of AI",
    "Institution provides access to major commercial AI platforms",
    "Institution is investing in local AI tools (e.g., locally hosted open-source models)",
    "Institution has clear guidance on acknowledging AI use in research outputs",
    "Institution effectively communicates AI-related ethical policies",
    "Institution has AI governance mechanisms (policies, frameworks, ethics board)",
    "Institution collaborates with external partners on responsible AI",
    "Institution has mechanisms for reporting or addressing AI ethics concerns",
    "Institution provides support for monitoring or auditing AI use"
]

labels = [fill(x, 42) for x in labels]

# Percentages
R1 = np.array([15.0,8.3,17.1,6.5,9.1,15.1,20.0,12.2,12.5,11.8,19.4])
R2 = np.array([30.0,26.9,23.2,19.4,21.8,26.4,32.0,26.5,27.5,26.5,32.3])
R3 = np.array([26.0,41.7,23.2,30.6,34.5,26.4,16.0,26.5,20.0,20.6,19.4])
R4 = np.array([20.0,12.0,26.8,27.4,18.2,26.4,24.0,22.4,30.0,32.4,16.1])
NR = np.array([9.0,11.1,9.8,16.1,16.4,5.7,8.0,12.2,10.0,8.8,12.9])

# Counts
R1_n=[15,9,14,4,5,8,10,6,5,4,6]
R2_n=[30,29,19,12,12,14,16,13,11,9,10]
R3_n=[26,45,19,19,19,14,8,13,8,7,6]
R4_n=[20,13,22,17,10,14,12,11,12,11,5]
NR_n=[9,12,8,10,9,3,4,6,4,3,4]

# Totals
totals=[100,108,82,62,55,53,50,49,40,34,31]
total_pct=[32.8,35.4,26.9,20.3,18.0,17.4,16.4,16.1,13.1,11.1,10.2]

# --------------------------------------------------
# Appearance
# --------------------------------------------------

colors=[
    "#08306B",
    "#2171B5",
    "#6BAED6",
    "#9ECAE1",
    "#D9F0F7"
]

fig, ax = plt.subplots(figsize=(15,8))

spacing=0.42
height=0.24

y=np.arange(len(labels))*spacing

# --------------------------------------------------
# Bars
# --------------------------------------------------

left=np.zeros(len(labels))

series=[
    ("First Stage Researcher",R1,R1_n,colors[0],"white"),
    ("Recognised Researcher",R2,R2_n,colors[1],"white"),
    ("Established Researcher",R3,R3_n,colors[2],"black"),
    ("Leading Researcher",R4,R4_n,colors[3],"black"),
    ("Not a researcher",NR,NR_n,colors[4],"black"),
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

        # only label segments >=10%
        if v>=10:
            ax.text(
                left[i]+v/2,
                y[i],
                f"{v:.1f}% ({counts[i]})",
                ha="center",
                va="center",
                fontsize=7.8,
                color=text_color
            )

    left+=vals

# --------------------------------------------------
# Totals at end
# --------------------------------------------------

for i in range(len(labels)):
    ax.text(
        101,
        y[i],
        f"{totals[i]} ({total_pct[i]}%)",
        va="center",
        fontsize=9,
        fontweight="bold"
    )

# --------------------------------------------------
# Axes
# --------------------------------------------------

ax.set_xlim(0,110)

ax.set_yticks(y)
ax.set_yticklabels(labels,fontsize=9)

ax.invert_yaxis()

ax.set_xticks([0,25,50,75,100])
ax.set_xticklabels(["0%","25%","50%","75%","100%"])

ax.grid(axis="x",linestyle="--",alpha=.30)

ax.set_axisbelow(True)

for s in ax.spines.values():
    s.set_visible(False)

ax.tick_params(axis='y',length=0)

# --------------------------------------------------
# Legend
# --------------------------------------------------

legend=[
    Patch(color=colors[0],label="First Stage Researcher"),
    Patch(color=colors[1],label="Recognised Researcher"),
    Patch(color=colors[2],label="Established Researcher"),
    Patch(color=colors[3],label="Leading Researcher"),
    Patch(color=colors[4],label="Not a researcher"),
]

ax.legend(
    handles=legend,
    ncol=5,
    frameon=False,
    loc="upper left",
    bbox_to_anchor=(0,1.08),
    fontsize=9,
    handlelength=1.4,
    columnspacing=1.8
)

# --------------------------------------------------
# Title
# --------------------------------------------------

ax.set_title(
    "Institutional Structures, Policies and Practices by Career Stage",
    fontsize=15,
    fontweight="bold",
    loc="left",
    pad=70
)

plt.tight_layout()

plt.savefig(
    "Institutional_Structures_by_Career_Stage.png",
    dpi=600,
    bbox_inches="tight"
)

plt.savefig(
    "Institutional_Structures_by_Career_Stage.pdf",
    bbox_inches="tight"
)

plt.show()
