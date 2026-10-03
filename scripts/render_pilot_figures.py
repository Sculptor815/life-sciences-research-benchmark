"""Reproduce the four original synthetic teaching figures; no answer keys needed."""
import argparse
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def render(output):
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({"font.size":11,"axes.spines.top":False,"axes.spines.right":False,"savefig.dpi":150})
    blue, orange = "#216b96", "#b56428"
    fig, ax = plt.subplots(figsize=(7,4.2), layout="constrained")
    x = np.arange(2)
    ax.bar(x-.18,[100,95],.36,label="Control",color=blue)
    ax.bar(x+.18,[5,93],.36,label="Validated KO",color=orange)
    ax.set(xticks=x,xticklabels=["50 kDa","75 kDa"],ylabel="Normalized intensity (arbitrary units)",title="Synthetic band quantification; equal loading")
    ax.legend()
    fig.savefig(output/"mol-k02.png"); plt.close(fig)
    fig, ax = plt.subplots(figsize=(7,4.2),layout="constrained")
    substrate = np.linspace(0,300,500)
    ax.plot(substrate,100*substrate/(20+substrate),label="Vehicle",color=blue)
    ax.plot(substrate,100*substrate/(60+substrate),label="Inhibitor",color=orange)
    ax.axhline(100,color="#888888",ls=":",label="Shared asymptote")
    ax.set(xlabel="Substrate (micromolar)",ylabel="Initial rate (nmol/min)",title="Synthetic initial-rate curves",ylim=(0,110))
    ax.legend()
    fig.savefig(output/"bio-k02.png"); plt.close(fig)
    fig, axes = plt.subplots(1,2,figsize=(8,4),layout="constrained")
    jitter = np.array([-.1,-.06,-.02,.02,.06,.1])
    values = [([38,40,43,36,46,41],[13,18,16,20,14,17]),([12,11,14,10,13,12],[4,6,5,7,4,6])]
    for ax, pair, label in zip(axes,values,["Open-arm time (%)","Speed (cm/s)"]):
        for i,(points,color) in enumerate(zip(pair,[blue,orange])):
            ax.scatter(i+jitter,points,color=color)
            ax.plot([i-.18,i+.18],[np.mean(points)]*2,color=color)
        ax.set(xticks=[0,1],xticklabels=["Control","Perturbed"],ylabel=label,ylim=(0,None))
    fig.suptitle("Synthetic behavioral observations; six animals per group")
    fig.savefig(output/"neu-k02.png"); plt.close(fig)
    fig, axes = plt.subplots(2,1,figsize=(7,6),layout="constrained")
    positions = [101,102,103,104,105]
    axes[0].scatter(positions,[4,8,11,9,3],c=[blue,blue,orange,blue,blue],s=60)
    axes[0].axhline(7.3,ls="--",color="#777777")
    axes[0].set(xticks=positions,xticklabels=["v1","v2","v3","v4","v5"],ylabel="-log10(p)",title="Synthetic association results at one locus")
    ld=np.array([[1,.2,.1,.1,.1],[.2,1,.9,.8,.1],[.1,.9,1,.9,.1],[.1,.8,.9,1,.2],[.1,.1,.1,.2,1]])
    im=axes[1].imshow(ld,vmin=0,vmax=1,cmap="Blues")
    axes[1].set(xticks=range(5),xticklabels=["v1","v2","v3","v4","v5"],yticks=range(5),yticklabels=["v1","v2","v3","v4","v5"],title="Pairwise linkage disequilibrium (r squared)")
    fig.colorbar(im,ax=axes[1],shrink=.8)
    fig.savefig(output/"inf-k02.png"); plt.close(fig)
    (output/"provenance.json").write_text(json.dumps({"origin":"Original synthetic teaching figures", "license":"CC-BY-4.0", "creator":"Life Sciences Research Workbench contributors", "script":"scripts/render_pilot_figures.py", "processing":"Deterministic plotting; no real specimens, journal panels or external images", "raw_values":"All source arrays and kinetic equations are preserved in the plotting script", "created":"2026-10-03"},indent=2)+"\n",encoding="utf-8")


if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",default="data/public/assets")
    render(parser.parse_args().output)
