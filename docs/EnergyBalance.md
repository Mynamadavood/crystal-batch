# **System Boundary**

Defined System (Batch Contents \- taken from [BatchBasis.md](http://BatchBasis.md)):  
Boundary starts at saturated solution, 50 ℃, after seeding; heat-up and dissolution excluded

* Pilot vessel, 500L,70% Fill, 350 kg Water  
* Dissolved Paracetamol ; 34.39 PA g/kg water \* 350 kg, 12.04 kg per batch \+ 0.5 kg seeded paracetamol  
* Wetted 316L Vessel Shell (89.8 kg)

Assumptions 

* Heat of crystallisation taken as \-𝜟H(T) \= R(-A \+BT) from Fujiwara’s correlation (van ‘t Hoff). Evaluated at 50 ℃ (29.69 kJ/mol) to pair consistently with solid-phase Cp (Hess’s law) ; Kirchhoff : d𝜟H/dT \= Cp\* \= R\*B  
* Transient batch overall (integral balance): Overall balance from initial state (50 ℃) to final state (15 ℃)  
* Closed System: No mass crosses boundary during cooling, boundary ranging from seed addition to end of hold.  
* Constant pressure (using atmospheric): heat is a pure enthalpy change, Q=𝜟H  
* No work done apart from stirrer; kinetic and potential energy changes are negligible.  
* Stirrer work: Neglected here; revisited in stage 2 once batch time is known.  
* Ignore Heat loss to room; For insulated vessels it is small, above room temperatures batch loses heat helping jacket, below room temperature it gains heat, by neglecting it is making the model conservative.   
* Vessel wall heat capacity : Using a steel wall, Jacket has to remove heat stored in the vessel’s wall. Sensible-heat term magnitude, (m\_steel\*Cp\_steel\*𝜟T) \= 1.571 MJ, water  \= 51.22  MJ. A considerable amount of heat and thus is included in the model (3.07% of water term)  
* Equilibrium at end-state: batch reaches saturation at 15 ℃, thus full 8.26 kg crystallises (seeded with sufficient hold at 15 ℃)  
* No evaporation: closed vessel and cooling  
* Ideal solution: Using apparent van ‘t Hoff 𝜟H value from mole-fraction fit, assuming ideal behaviour.  
* Heat capacities:  
- Water : Taken from NIST enthalpy difference (NIST SRD 69\)   
- Paracetamol: Xu’s CP, linear T, integrated using midpoint (Xu et al. 2006\)   
- Steel: Constant CP, using mean over 0-100 ℃ from Atlas Datasheet (Atlas 316 datasheet)   
* Single polymorph, no solvent inclusion.

## **Sign of the Heat of Crystallisation**

The van’t Hoff 𝜟H values \> 0, with solubility rising with temperature. Dissolution is thus an endothermic process, absorbing heat from surroundings. Crystallisation, being the reverse process of dissolution is thus an exothermic process, releasing heat to the batch:

$PA\ (aq)\ →\ PA(s),\ 𝜟{H}_{crystal}\ <0{\ }$

   ∴  Therefore, crystallisation adds heat, which the jacket must remove. 

**Cooling Duty:**

**${Q}_{Jacket}={Q}_{sensible}\ +\ {Q}_{crystallisation\ }-\ {Q}_{losses}$**

With:

-  $\ {Q}_{losses}$ \= 0 (neglected, conservative)

-    All Q terms reported as heat ***removed***  by the jacket (positive)  
  

    
    
  


## **Sensible Heat**

Sensible heat is the thermal energy from a change in temperature. It applies to all material that cools, regardless of phase; the phase change is counted separately in Qcryst This results in the equation:

${Q}_{sensible}\ =\ {Q}_{{H}_{2}O}+\ {Q}_{PA}\ +{Q}_{steel}$  

Each term is the heat removed from 50 to 15°C  (ΔT \= 35 K)

**Water (350 kg)**

Utilised the NIST enthalpy difference, so no constant-Cp assumption needed.

\-\>    $\Delta {H}_{m}\ =\ H(323.15\ K)\ -\ H(288.15\ K)\ =\ 3.7727\ -\ 1.1363\ =\ 2.6364\ kJ/mol$  
     $n=\ 350/0.018015\ =\ 19,428\ mol\ ->\ {Q}_{{H}_{2}O\ }=\ 51.22\ MJ$

**Check:** mean Cp \= (4.189+4.181)/2 \= 4.185 kJ/kg\*K giving 51.27 MJ. 

   ∴  Both agree within 0.1%

Enthalpy difference is used because water’s Cp isn’t linear in T, so averaging the endpoint values only approximates the true integral.

**Source: NIST SRD 69**

**Paracetamol (12.54 kg \=12.04 dissolved \+ 0.5 seed)**

**Method,**  Xu’s Form I Cp;  
$C{p}_{m}=\ 17.645\ +\ 0.5226T$   
(fitted over 150-330 K, covering the 288-323 K \- no extrapolation needed)

As Cp is linear ;   
$∫Cp\ dT\ =\ Cp({T}_{mid}\ )\ *\ \Delta T$

${T}_{2\ }=323.15\ K$  
${T}_{1\ }=288.15\ K$${}$

${}$$∫(a+bT)\ dT\ =\ {(T}_{2}-{T}_{1})[a+b({T}_{1}+{T}_{2})/2]=\Delta T*Cp({T}_{mid})$

${T}_{mid\ }=305.65\ K$  
${}$  
**Integrating Xu’s Form I Cp:**

**$[17.645T+0.2613{T}^{2}{{]}^{323.15}}_{288.15}$**

$\Delta {H}_{mPA}=\ 6208.22\ J/mol$  
$\Delta T=35\ K$

6208.22/35 \= 177.378 J / mol K

${n}_{PA}=\ \frac{12540}{151.16}=\ 82.96\ mol$

${Q}_{pa\ =\ 82.96\ *\ 6208.22\ =\ 0.515\ MJ}$  
**Check:** Mass route  
$12540\ *\ \ 1.174\ *\ 35\ =\ 0.515\ MJ$

**Note:** Solid Form I Cp is used here; the 3.77 kg remaining dissolved is corrected in Path Consistency (+0.197 MJ)

**Source:** Xu et al.2006

**Steel (wetted, 316L Shell)**

Geometry : Cylinder, H/D \= 1.2 (assumed), V=0.5${m}^{3}$, giving D=0.810m and H=0.971m

* Wetted area at 70% fill;

                                        $A=\pi D(0.7H)\ +\ \pi {D}^{2}/4\ =\ 2.244\ {m}^{2}$  
(Ignoring upper shell headspace; Poor gas-phase heat transfer, vapours and gases in the headspace have much lower thermal conductivity than liquids. Headspace steel lags behind significantly during cooling cycle)

* Thickness (t) \= 5mm, $\rho \ =\ 8,000kg/{m}^{3\ }$ \-\> m= 89.76 kg  
* ${Q}_{steel}=mc\Delta T\ =\ 89.76*0.500*35\ =\ 1.571\ MJ{\ }$(3.07% of the water term)

**Source:** Atlas Steel 316 Datasheet (ρ and Cp, 0–100 °C mean)

**Total Q sensible:**

**${Q}_{sensible\ =\ 51.22+0.515+1.571\ =\ 53.31\ MJ}$**

## 

## **Heat of Crystallisation** 

Heat of Crystallisation is derived from the following equation;

${Q}_{cryst\ }={n}_{crystal}*\ |Δ\ {H}_{cryst}|$

**Moles Crystallised**

n=yield / molar weight of PA \= 8.262 kg / 0.15116kg/mol \= 54.64 mol

- (seed excluded. Added as solid, so it releases no heat of crystallisation)

**Δ H from Fujiwara (using van’t Hoff)**

Δ H(T) \= R(-A+BT), with R=8.314, A=5193.109, B=27.121124

Δ H at 15°C (extrapolated value: fit covers 20-50°C):

→  Δ H(15°C)=21.80 kJ/mol

Δ H at  50 °C :

→  Δ H(50°C)=29.69 kJ/mol

* Spread \= 7.89 kJ/mol \= R\*B\* Δ T \= Cp\* Δ T (Matches Fujiwara’s fitted Cp\* of 225.5 J/mol\*K

**Which** Δ **H Value?**  
*The choice of*  *Δ H is fixed by path consistency (section below), not by bounding.*

**Result:**  
**${Q}_{cryst\ }=\ 54.64\ *\ 29.69\ =\ 1.622\ MJ$**

## Path Consistency (Hess’ Law/ Kirchhoff Law)

*The principle of enthalpy is it is a state function and thus the ${Q}_{jacket}$ depends only on start and end states, not on the route between them according to Hess’s Law.*

This offers two equivalent routes;

A:    Crystallise at 50°C (ΔH=29.69 kJ/mol), then cool the solid using solid Cp

B:   Cool everything while dissolved (solid Cp+Cp\*), then crystallise at 15°C(ΔH \= 21.80 kJ/mol)

Kirchhoff’s law bridges both routes as :   
$\frac{dΔH\ }{dT}=\Delta Cp=Cp*=R*B{\ }$

The 7.89 kJ/mol spread in ΔH is exactly the extra heat capacity of dissolved paracetamol over 35 K.

Route A is the consistent choice and thus used because the sensible heat uses solid Cp so it pairs with the ΔH at 50 °C.  

**Mother Liquor correction:**  the 3.774 kg left at 15°C stays dissolved throughout and thus needs a dissolved Cp:

${n}_{ML}=\frac{3.774}{0.15116}=24.97\ mol$

Extra heat $→$ $24.97*225.5*35\ =\ 0.197\ MJ$

**Total Jacket duty**

**${Q}_{jacket}=51.2{2}_{}+\ 0.515\ +\ 1.571\ +\ 0.197+1.622\ =\ 55.12\ MJ$**

**Check: Route B (Cool first, crystallise last)**

*Cool everything from 50 °C to 15°C* 

* Water : 51.22 MJ (unchanged)  
* Steel : 1.571 MJ (unchanged)  
* Seed, solid Cp: 3.308 mol \* 177.4 \* 35 \=0.021 MJ  
* Dissolved Paracetamol;  dissolved Cp \= solid Cp+Cp\* \= 177.4  \+225.5 \= 402.9 J/mol\*k   
  → 79.62 mol \* 402.9 \* 35 \= 1.123 MJ


(Dissolved Cp is apparent; ideal-solution, from Fujiwara’s Cp\*)

Crystallise at 15°C 

* 54.64 mol \* ΔH  (15°C) \= 54.64 \* 21.80 \= 1.191 MJ  
  


**Total :**   
$51.22+1.571+0.021+1.123+1.191\ =\ 55.13\ MJ$  
 

**Note:** *Path consistency resolved the earlier bounded ΔH between 15°C and 50 °C (54.5-54.9 MJ) to a single value.*

## **Summary: Jacket Duty per Batch (50 →15°C)** 

| Term | Method/Source | Q(MJ) | Share |
| :---- | :---- | :---- | :---- |
| Water (350kg) | NIST enthalpy difference | 51.22 | 92.9% |
| Steel Shell (89.8kg, wetted 316L) | **$m*Cp*\Delta T{\ }$,** Atlas | 1.571 | 2.9% |
| Crystallisation (54.64 mol) | **$n*\Delta H(50°C\ ),\ Fujiwara$** | 1.622 | 2.9% |
| Paracetamol (12.54 kg, solid Cp) | Xu, Midpoint integral | 0.515 | 0.9% |
| Mother Liquor correction (dissolved Cp) | **${n}_{ML}*Cp*\Delta T$** | 0.197 | 0.4% |
| ${Q}_{Jacket}$ |  | 55.12 | 100% |

*Sensible heat ≈ 97%, crystallisation ≈ 3%. The jacket is sized by the cooling load.*

### ***Verification***

1. ***Mass closure:** 8.262 \+ 3.774 \= 12.036 kg ✓*  
2. ***Yield direction:** a 20 °C endpoint gives 7.610 kg, versus 8.262 kg at 15 °C. That’s \+8.6%, matching the 12 Nov decision ✓*  
3. ***Energy direction:** a 20 °C endpoint gives about **47.4 MJ**, versus 55.1 MJ (−14%) ✓. Sensible heat scales with ΔT (0.858 vs 30/35 \= 0.857).*  
4. ***Order of magnitude:** 55.12 ÷ (350 × 4.18 × 35 / 1000\) \= **1.076**. The extra 7.6% is exactly the non-water terms in the table ✓*  
5. ***Path independence:** Routes A and B agree to within 0.01 MJ ✓*  
6. ***Review note:**  Reviewed and corrected 19 Nov: × sign, NIST Cp at 323 K, transcription fixes; ΔH band replaced by the path-consistent value. Hand calcs in validation/03–05.*

## **Discussion**

 The sensible heat term dominates at about 97%, and crystallisation at about 3%, and thus the jacket is sized by the cooling load. Therefore large uncertainty in ΔH makes a negligible impact on the total duty.

Moreover, crystallisation here is front loaded, resulting in twice as much product per degree at 50°C as at 15 °C.  Under linear cooling, that front loading causes supersaturation spikes early, hence the use for Stage 2’s cubic profile. As well, the jacket whilst has a calculated 55 MJ energy, it is sized primarily by **peak rate** (kW), Timing therefore is a critical piece and can have more sway than total energy (explored in stage 2 deeper)

Additionally, the operating cost of a cooler endpoint has to be considered. At 15 °C, the synthesis gives \+8.6% product for 16% duty (55.1 vs 47.4 MJ).  In real conditions, the coolant must be colder than 15°C, so cooling-tower water  (25-30°C in a Melbourne summer) cannot finish the batch. Chilled water or glycol is therefore needed for the final stage.

### 

### ***Sources***

* ***Fujiwara et al. (2002)**, Cryst. Growth Des. 2(5), 363–370: solubility correlation, ΔH(T), Cp\**  
* ***Granberg & Rasmuson (1999)**, J. Chem. Eng. Data 44(6), 1391–1395: solubility validation*  
* ***NIST Chemistry WebBook, SRD 69** (Lemmon, McLinden & Friend): water enthalpy and Cp*  
* ***Xu et al. (2006)**, J. Therm. Anal. Calorim. 83(1), 187–191: Cp of paracetamol Form I*  
* ***Atlas Steels**, Grade 316/316L datasheet (rev. Jan 2011): density and Cp of steel*

