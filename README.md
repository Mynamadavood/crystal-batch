# crystal-batch

Crystallisation is a defining step in the production of paracetamol and small molecule APIs. How a solute is crystalised determines
yield, particle size, purity and therefore dissolution rate. This system is a Batch API Crystallization Model, which calculates the mass-balance and yield of paracetamol 
at final temperature, accounting for mother-liquor losses; computes the energy balance and jacket duty; sizes the slurry transfer line to produce GMP-style 
batch records modelled on pharmaceutical procedure

Paracetamol is chosen for this model due to paracetamol's aqueous solubility being well documented, and thus the model can be validated against independent published data.


## Batch basis

| | |
|---|---|
| System | Paracetamol in water, seeded cooling crystallisation |
| Cooling window | 50 → 15 °C |
| Vessel | 500 L, 70% fill, ~350 kg water |
| Product per batch | 8.26 kg (theoretical equilibrium yield) |
| Recovery | ~69%, with ~3.8 kg per batch remaining in mother liquor |

Full design basis, assumptions and non-goals: [docs/BatchBasis.md](docs/BatchBasis.md)

## Data sources

- **Fujiwara et al. (2002)**, *Crystal Growth & Design*: primary solubility correlation
- **Granberg & Rasmuson (1999)**, *J. Chem. Eng. Data*: independent validation

Full citations: [sources/README.md](sources/README.md)

## Validation

Fujiwara's and Granberg's data were used as a cross-check of solubility, with results agreeing within ~2%
over 15-30°C, with a systematic slope difference Fujiwara's values falling increasingly  below Granberg's on cooling from +0.8% at 30°C
to -1.7% at 15°C, and the curves cross near 27°C.


The apparent enthalpy of solution, derived from the correlation via van 't Hoff (ΔH=R(-A+BT)), gives 24.05 kJ/mol at 298.15K, matching Fujiwara's published value.




Workings: [validation/](validation/)

## Status

Foundation complete (9–13 Nov 2026). Build starts 23 Nov 2026.

## How to run

*Not yet. Code arrives in the build phase.*
