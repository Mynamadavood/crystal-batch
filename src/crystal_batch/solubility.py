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
  