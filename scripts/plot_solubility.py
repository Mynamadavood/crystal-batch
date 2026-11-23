"""Plot C*(T), 15-50 °C, from crystal_batch.solubility with Granberg & Rasmuson (1999) points overlaid.

Run from repo root:  .venv/Scripts/python scripts/plot_solubility.py
Writes docs/solubility.png.
"""
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))  # no package install; same as pytest.ini pythonpath

from crystal_batch.solubility import g_per_kg, mole_fraction  # noqa: E402

T_C = np.linspace(15, 50, 141)
C_star = g_per_kg(mole_fraction(T_C + 273.15))  # warns once: 15-20 °C is extrapolated
fitted = T_C >= 20

gr = np.genfromtxt(ROOT / "data/granberg_1999_water.csv", delimiter=",", names=True, skip_header=4)
gr = gr[gr["T_C"] >= 15]  # plot window only; 0-10 °C points stay in the CSV

fig, ax = plt.subplots(figsize=(7, 4.5))
ax.plot(T_C[fitted], C_star[fitted], color="#1f4e79", lw=1.8,
        label="Fujiwara et al. (2002), fitted 20–50 °C")
ax.plot(T_C[T_C <= 20], C_star[T_C <= 20], color="#1f4e79", lw=1.8, ls="--",
        label="Fujiwara, extrapolated 15–20 °C")
ax.plot(gr["T_C"], gr["g_per_kg"], ls="none", marker="o", ms=6, mfc="white", mec="#c55a11", mew=1.5, clip_on=False,
        label="Granberg & Rasmuson (1999)")

ax.set_xlabel("Temperature (°C)")
ax.set_ylabel("Solubility C* (g paracetamol / kg water)")
ax.set_title("Paracetamol solubility in water")
ax.set_xlim(15, 50)
ax.grid(color="0.9", lw=0.8)
ax.spines[["top", "right"]].set_visible(False)
ax.legend(frameon=False, loc="upper left")
fig.tight_layout()

out = ROOT / "docs/solubility.png"
fig.savefig(out, dpi=150)
print(f"wrote {out}")
