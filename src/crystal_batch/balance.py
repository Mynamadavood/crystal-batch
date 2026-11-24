"""Balance calculations for paracetamol crystallization. 
Verified against hand calculations in validation/03_mass_balance_hand.pdf (p.1-2). 
Note: seed mass is excluded from product (added, not produced) - 03 p.2."""

from .solubility import mole_fraction, g_per_kg

def dissolved(m_water, T_sat):
    """Calculates the charge amount of paracetamol dissolved at saturated temperature by multiplying 
    the solubility in g PA / kg H2O by the mass of water in kg and converting to kg PA.
    
    Parameters
    ----------
    m_water : float, Mass of water in kg [kg]
    T_sat : float, Saturated temperature in Kelvin [K]

    Returns
    -------
    float, Mass of paracetamol dissolved in water at saturated temperature in kg [kg]
    """
    X_PA = mole_fraction(T_sat)
    gPA_per_kgH2O = g_per_kg(X_PA)
    CHARGE_kg_PA = gPA_per_kgH2O * m_water / 1000.0

    return CHARGE_kg_PA

def mother_liquor(m_water, T_final):
    """Calculates the remaining amount of paracetamol dissolved in the mother liquor at the final temperature 
    by multiplying the solubility in g PA / kg H2O by the mass of water in kg and converting to kg PA.

    Parameters
    ----------
    m_water : float, Mass of water in kg [kg]
    T_final : float, Final temperature in Kelvin [K]

    Returns
    -------
    float, Mass of paracetamol dissolved in mother liquor at final temperature in kg [kg]
    """
    X_PA = mole_fraction(T_final)
    gPA_per_kgH2O = g_per_kg(X_PA)
    ML_kg_pa = gPA_per_kgH2O * m_water / 1000.0

    return ML_kg_pa

def product(m_water,T_sat,T_final):
    """Calculates the Paracetamol product (yield) per batch by subtracting the mass of charge (dissolved at saturated temperature) 
    by the mass of mother liquor (dissolved at final temperature).
       
    Parameters
    ----------
    m_water : float, Mass of water in kg [kg]
    T_sat : float, Saturated temperature in Kelvin [K]
    T_final : float, Final temperature in Kelvin [K]

    Returns
    -------
    float, Mass of paracetamol product (yield) in kg [kg]
    """
    if T_final > T_sat:
        raise ValueError("Final temperature must be less than or equal to saturated temperature.")
    Charge = dissolved(m_water, T_sat)
    ML = mother_liquor(m_water, T_final)
    P = Charge - ML

    return P

def recovery(m_water,T_sat,T_final):
    """Calculates the recovery of paracetamol product (yield) per batch as a fraction, by dividing the mass of product (yield) 
    by the mass of charge (dissolved at saturated temperature).

    Parameters
    ----------
    m_water : float, Mass of water in kg [kg]
    T_sat : float, Saturated temperature in Kelvin [K]
    T_final : float, Final temperature in Kelvin [K]

    Returns
    -------
    float, Recovery of paracetamol product (yield) as a fraction [fraction]
    """
    Charge = dissolved(m_water, T_sat)
    P = product(m_water,T_sat,T_final)
    R = P / Charge 
    
    return R
