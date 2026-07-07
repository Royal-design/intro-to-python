import matplotlib.pyplot as plt
import numpy as np
from textwrap import fill

# --------------------------------------------------
# Labels
# --------------------------------------------------

rows = [
    "AI governance mechanisms\n(policies, frameworks or ethics board)",
    "Clear guidelines on the\nresponsible use of AI",
    "Guidance on acknowledging\nAI use in research outputs",
    "Training or awareness\nprogrammes on AI and ethics",
    "Institutional support for\nmonitoring or auditing AI use",
    "Effective communication of\nAI-related ethical policies",
    "Collaboration with external\npartners on responsible AI",
    "Access to major commercial\nAI platforms",
    "Mechanisms for reporting\nAI-related ethical concerns",
    "Investment in local AI tools\n(e.g., open-source models)",
    "I don't know"
]

cols = [
    "Doctoral",
    "Postdoc",
    "MSCA",
    "Host",
    "Research\nManager",
    "Evaluator",
    "Policy /\nFunder",
    "NCP",
    "Other"
]

# --------------------------------------------------
# Percentages
# --------------------------------------------------

data = np.array([
    [8.2,16.3,69.4,6.1,6.1,12.2,0.0,0.0,6.1],
    [13.4,12.2,59.8,2.4,9.8,8.5,0.0,0.0,11.0],
    [13.2,17.0,50.9,5.7,7.5,17.0,0.0,0.0,13.2],
    [10.0,15.0,57.0,4.0,13.0,13.0,1.0,0.0,8.0],
    [16.1,16.1,54.8,3.2,6.5,9.7,0.0,0.0,12.9],
    [14.0,14.0,54.0,2.0,8.0,16.0,0.0,0.0,14.0],
    [12.5,20.0,52.5,5.0,10.0,17.5,0.0,0.0,10.0],
    [6.5,9.7,67.7,3.2,12.9,11.3,1.6,0.0,4.8],
    [8.8,17.6,52.9,2.9,8.8,5.9,0.0,0.0,23.5],
    [10.9,10.9,70.9,1.8,9.1,7.3,1.8,0.0,7.3],
    [7.4,23.1,63.0,0.9,7.4,3.7,0.0,1.9,2.8]
])

# --------------------------------------------------
# Counts (for annotation)
# --------------------------------------------------

counts = np.array([
    [4,8,34,3,3,6,0,0,3],
    [11,10,49,2,8,7,0,0,9],
    [7,9,27,3,4,9,0,0,7],
    [10,15,57,4,13,13,1,0,8],
    [5,5,17,1,2,3,0,0,4],
    [7,7,27,1,4,8,0,0,7],
    [5,8,21,2,4,7,0,0,4],
    [4,6,42,2,8,7,1,0,3],
    [3,6,18,1,3,2,0,0,8],
    [6,6,39,1,5,4,1,0,4],
    [8,25,68,1,8,4,0,2,3]
])

# --------------------------------------------------
# Figure
# --------------------------------------------------

fig, ax = plt.subplots(figsize=(13,9))

im = ax.imshow(
    data,
    cmap="Blues",
    aspect="auto",
    vmin=0,
    vmax=75
)

# --------------------------------------------------
# Axis labels
# --------------------------------------------------

ax.set_xticks(np.arange(len(cols)))
ax.set_xticklabels(cols, fontsize=10, fontweight="bold")

ax.set_yticks(np.arange(len(rows)))
ax.set_yticklabels(rows, fontsize=9)

plt.setp(ax.get_xticklabels(), rotation=35, ha="right")

# --------------------------------------------------
# Cell annotations
# --------------------------------------------------

for i in range(data.shape[0]):
    for j in range(data.shape[1]):

        value = data[i, j]

        color = "white" if value >= 40 else "black"

        ax.text(
            j,
            i,
            f"{counts[i,j]}\n({value:.1f}%)",
            ha="center",
            va="center",
            fontsize=8,
            color=color
        )

# --------------------------------------------------
# Grid lines
# --------------------------------------------------

ax.set_xticks(np.arange(-.5, len(cols), 1), minor=True)
ax.set_yticks(np.arange(-.5, len(rows), 1), minor=True)

ax.grid(which="minor", color="white", linewidth=2)

ax.tick_params(which="minor", bottom=False, left=False)

# --------------------------------------------------
# Colorbar
# --------------------------------------------------

cbar = plt.colorbar(im, ax=ax, pad=0.02)
cbar.set_label(
    "Percentage (%)",
    fontsize=11,
    fontweight="bold"
)

# --------------------------------------------------
# Title
# --------------------------------------------------

ax.set_title(
    "Institutional Structures, Policies and Practices by Respondent Group",
    fontsize=16,
    fontweight="bold",
    pad=20
)

plt.tight_layout()

# --------------------------------------------------
# Save
# --------------------------------------------------

plt.savefig(
    "Institutional_Heatmap.png",
    dpi=600,
    bbox_inches="tight"
)

plt.savefig(
    "Institutional_Heatmap.pdf",
    bbox_inches="tight"
)

plt.show()