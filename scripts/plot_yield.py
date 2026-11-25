"""Plots recovery vs final temperature, 15-50 °C, from crystal_batch.balance with hand calcs.
Run from repo root:  .venv/Scripts/python scripts/plot_yield.py
Writes docs/yield.png.
"""
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np



ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))  # no package install; same as pytest.ini pythonpath

from crystal_batch.balance import recovery #noqa: E402

M_WATER = 350.0        # kg
T_SAT = 323.15         # K, saturated at 50 °C
HAND_T_C = [15, 20]    # °C, hand calc 03 p.2
HAND_R = [68.6, 63.2]  # %

T_C = np.linspace(15, 50, 141)
R = []
for T in T_C:
    R.append(100*recovery(M_WATER, T_SAT, T + 273.15))

R = np.array(R)

fitted = T_C >= 20

fig, ax = plt.subplots(figsize=(7, 4.5))
ax.axvspan(15, 50, color="#1f4e79", alpha=0.08, lw=0, label="Cooling window 50 → 15 °C")
ax.plot(T_C[fitted], R[fitted], color="#1f4e79", lw=1.8,
        label="Recovery, fitted 20–50 °C")
ax.plot(T_C[T_C <= 20], R[T_C <= 20], color="#1f4e79", lw=1.8, ls="--",
        label="Recovery extrapolated 15–20 °C")
ax.plot(HAND_T_C, HAND_R, ls="none", marker="o", ms=6, mfc="white", mec="#c55a11", mew=1.5, clip_on=False,
        label="Hand Calc points, 15–20 °C (03 p.2)")

ax.set_xlabel("Final Temperature, T_final (°C)")
ax.set_ylabel("Recovery (%)")
ax.set_title("Recovery vs Final Temperature, 15–50 °C")
ax.set_xlim(10, 55)  # margin so the shaded cooling window reads as a band
ax.grid(color="0.9", lw=0.8)
ax.spines[["top", "right"]].set_visible(False)
ax.legend(frameon=False, loc="upper right")
fig.tight_layout()

out = ROOT / "docs/yield.png"
fig.savefig(out, dpi=150)
print(f"wrote {out}")