"""Sources: Fujiwara et al. (2002), Cryst. Growth Des. 2(5), 363–370, doi:10.1021/cg0200098
Validations: validation/03_mass_balance_hand.pdf and validation/05_checks_hand.pdf"""

import warnings 
import numpy as np

#Constants used for the solubility equation from Fujiwara et al. (2002): ln x = A/T + B ln T + C

A = 5193.109   # Kelvin constant used in the solubility equation from Fujiwara et al. (2002)
B = 27.121124  # Dimensionless B constant used in the solubility equation from Fujiwara et al. (2002)
C = -178.28055 # Dimensionless C constant used in the solubility equation from Fujiwara et al. (2002)

M_PA = 151.16 #Molar mass of paracetamol in g/mol
M_H2O = 18.015 #Molar mass of water in g/mol
R = 8.314 #Universal gas constant in J/(mol*K)

def mole_fraction(T_K):
    """Calculates the mole fraction of Paracetamol in water in mol PA / mol solution, within a given temperature, T_K (in Kelvin), 
    using the solubility equation from Fujiwara et al. (2002).

    Parameters
    ----------
    T_K : float or array, Temperature in Kelvin [K]

    Returns 
    -------
    float or array, Mole fraction of Paracetamol in water [mol PA / mol solution]
    
    Source: Fujiwara et al. (2002), Cryst. Growth Des. 2(5), 363–370, doi:10.1021/cg0200098 Valid Range: 293.15 K to 323.15 K (20 °C to 50 °C)
    """
    if np.any((T_K < 293.15) | (T_K > 323.15)):
        warnings.warn("Temperature chosen falls outside of the valid range of the solubility equation (293.15 K to 323.15 K).", stacklevel=2)
        
    X_PA = np.exp(A/T_K +  B*np.log(T_K) + C)
        
    return X_PA   

def g_per_kg(X_PA):
    """Calculates the solubility of Paracetamol in water in g PA / kg H2O, using the calculated mole fraction at given temperature,
    using the equation : g PA /kg H2O = 1000*X_PA*M_PA/[(1-X_PA)*M_H2O]

    Parameters
    ----------
    X_PA : float or array, Mole fraction of Paracetamol in water [mol PA / mol solution]

    Returns
    -------
    float or array, Solubility of Paracetamol in water [g PA / kg H2O]
    """
    gPA_per_kgH2O = 1000*M_PA*X_PA/((1-X_PA)*M_H2O)

    return gPA_per_kgH2O

def delta_H(T_K):
    """Calculates the apparent enthalpy of solution (dissolution) by applying van 't Hoff to Fujiwara's correlation using the equation:
    ΔH = R*(-A+BT), with ΔH being positive, indicating that the dissolution of paracetamol in water is an endothermic process and 
    crystalisation is -ΔH, which is exothermic.

    Derivation of van 't Hoff and Fujiwara:

    ln x = A/T + B ln T + C -> d(ln x)/dT = -A/T^2 +B/T # Fujiwara's correlation derived
    d(ln x)/dT = ΔH/(R*T^2) # van 't Hoff equation
    ΔH = R*T^2*(-A/T^2 +B/T) = R*(-A+BT) 

    Parameters
    ----------
    T_K : float or array, Temperature in Kelvin [K]

    Returns
    -------
    float or array, Apparent enthalpy of solution (dissolution) [J/mol]

    Sources
    -------
    Fujiwara et al. (2002), Cryst. Growth Des. 2(5), 363–370, doi:10.1021/cg0200098
    """
    if np.any((T_K < 293.15) | (T_K > 323.15)):
        warnings.warn("Temperature chosen falls outside of the valid range of the solubility equation (293.15 K to 323.15 K).", stacklevel=2)   

    dH= R*(-A+B*T_K)
    return dH

