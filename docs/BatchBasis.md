# Batch Basis

## Cooling  Window

The cooling window chosen for the crystallization of paracetamol runs from 50℃ → 15 ℃ . Across the whole window, Fujiwara et al.(2002) correlation was used, with a 5℃ extrapolation when crossing below 20 ℃ . This was verified against Granberg & Rasmuson (1999) at 15℃ , where Fujiwara’s value was  1.7%  below Granberg’s. The driving motive for cooling at 15℃ rather than the lower limit of Fujiwara’s fitted range 20 ℃  was at 15℃ , an estimate of 8.6% higher yield of product per batch. However, this bears the cost of requiring chilled-water to enable the cooling of the final 5℃. It is hard-capped at 15℃ as below this the gap between the two datasets (Fujiwara and Granberg)  widens on cooling from \-1.1% at 20 ℃ to \-1.7% at 15 ℃.

## Vessel Size 

Utilising a pilot scale, drawing on Fujiwara’s lab scale of a 500ml flask, 350g of charged water, a 70% fill. That ratio is scaled 1000x to a 500L pilot vessel, maintaining 70% fill, and an estimate of 350kg of water producing 8.26 kg paracetamol per batch.

| Item | Kg per batch |
| :---- | :---- |
| Dissolved at 50 ℃ : 34.39 g/kg \*350 kg | 12.04 |
| Recovery as crystals | 8.26  |
| Left in mother liquor at 15℃ : 10.78 g/kg \* 350 kg | 3.77  |

Recovery \= 69% meaning roughly 31% of paracetamol, 3.8 kg every batch goes out with the mother liquor 

For this design, water offers a small solubility swing of ~2 g/kg per 5°C  at the cold end, rising to ~5 g/kg per 5°C at 45-50°C (Fujiwara, 2002). Methanol, by comparison, swings 20-30 g/kg over the same step (Granberg 1999). 69% of the dissolved paracetamol is recovered and 3.8 kg per batch stays in the mother liquor. 

To put it into perspective, utilising  Granberg’s cooling window of 30 → 0℃, Water holds a recovery of 59% whereas Methanol has a  recovery capacity of \~48%. However, the low absolute solubility of water produces 10 g per kg of water against Methanol’s 180 g/kg per kg of methanol. Thus, whilst water on paper has the greatest fractional recovery, it lacks productivity and its low effectiveness is demonstrated by outputting 18x less product per kg of solvent than methanol over the same window.

To combat this a production plant may weigh implementing a cosolvent system or utilising an alcohol to improve efficiency. However, it is to be carefully considered the ICH Q3C guidelines regarding the limits of  how much a solvent is permitted in the final drug. Methanol, for instance as a Class 2 solvent demands routine residual solvent analysis to verify levels are below the mandated threshold before batch release.

Moreover, the design's recovery of 69%, emphasises 31% of solute stays dissolved in the residual liquid after crystallization. This is due to the cold-to-hot solubility ratio (ratio of 1:3.2), in which the mother-liquor lost at 31% as a single-pass level in an industrial plant would be too great to discard. To decrease this, lowering the cold end to 5℃ can improve the ratio, however will require Granberg’s data as Fujiwara’s isn’t validated at this temperature. As well, adding antisolvent forces more product of the solution and or mother-liquor recovery such as harvesting a second crop, by concentrating the primary mother liquor via evaporation and precipitating another batch. 

## Seeding

Seeding is used as a response to the lack of crystal surface for excess solute to deposit onto, which enables supersaturation to build until crossing the labile zone where it nucleates all at once. With seeding, we establish a surface from the initial starting point, and thus as cooling generates supersaturation it is taken up by growth on the existing seeds instead of building towards a nucleation burst. This bolsters larger, more uniform crystals which will filter and dry more easily. Fewer inclusions and better purity of product, and additionally as control over polymorphism, as seeding with stable form steers the batch to the desired form, offering reproducibility from batch to batch.

Seed loading is scaled from Fujiwara (0.5 g per 350 g water → 0.5 kg per batch), added within the metastable zone just below 50 ℃. Seeding is assumed to keep supersaturation consumed and to bring the batch to solubility equilibrium by 15℃. Thus, the theoretical yield of equilibrium, 8.26 kg is taken as achievable. Seed mass excluded from yield.

## Assumptions 

* Impurity Rejection: Impurities stay in the mother liquor and crystals are taken as pure.  
* Water is taken at a mass-volume of 1 kg per L.  At 50 ℃,  roughly 0.99 kg/L. 1% effect which is within the \~2% agreement between the two solubility datasets.  
* Single component, stable polymorph throughout  (seeded)  
* Batch ends at solubility equilibrium (seeding)  
* Fujiwara’s correlation is valid down to 15℃ (validated to \-1.7%)  
* Heat of crystalisation taken  as \-Δ H\* from Fujiwara. Temperature-dependent through Cp\*  
* Seed mass excluded from yield  
* Chilled-water utility below 20℃, not modelled  
* Volume of dissolved paracetamol neglected in working volume  
* No solvent loss to evaporation  
* Steady jacket-side heat transfer coefficient

## Non-Goals

- No population balance / crystal size distribution modelling \-\> the goal is the yield/purity, not predicting particle size, filtration behaviour or crystal morphology  
- No nucleation kinetics \-\> Model is equilibrium-based and assumed a practical cooling/seeding protocol  
- Single component, no polymorphs-\>No need to model competing crystal forms, form control or solvent-mediated transformations  
- No chiller sizing \-\> limited to a defined temperature profile  
- No mother-liquor recovery \-\> product left dissolved after filtration is written off rather than recovered  
- No solvent switch \-\> the process uses a consistent one-solvent system, so there is no solvent-exchange step to enable a different crystalisation or downstream process