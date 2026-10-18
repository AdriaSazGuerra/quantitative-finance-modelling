"""Five-year CDS pricing with constant hazard and continuous discounting."""
from __future__ import annotations
import numpy as np
import matplotlib.pyplot as plt

MATURITY = 5
RISK_FREE_RATE = 0.07
HAZARD_RATE = 0.03
RECOVERY_RATE = 0.30
LOSS_GIVEN_DEFAULT = 1.0 - RECOVERY_RATE


def fair_spread() -> float:
    years = np.arange(1, MATURITY + 1, dtype=float)
    survival = (1.0 - HAZARD_RATE) ** years
    survival_prev = np.r_[1.0, survival[:-1]]
    default_prob = HAZARD_RATE * survival_prev
    df_premium = np.exp(-RISK_FREE_RATE * years)
    df_default = np.exp(-RISK_FREE_RATE * (years - 0.5))
    protection_pv = np.sum(LOSS_GIVEN_DEFAULT * default_prob * df_default)
    premium_annuity = np.sum(survival * df_premium)
    return protection_pv / premium_annuity


def cds_legs(spread: float):
    years = np.arange(1, MATURITY + 1, dtype=float)
    survival = (1.0 - HAZARD_RATE) ** years
    survival_prev = np.r_[1.0, survival[:-1]]
    default_prob = HAZARD_RATE * survival_prev
    df_premium = np.exp(-RISK_FREE_RATE * years)
    df_default = np.exp(-RISK_FREE_RATE * (years - 0.5))
    return years, spread * survival * df_premium, LOSS_GIVEN_DEFAULT * default_prob * df_default


def main():
    spread = fair_spread()
    years, premium, protection = cds_legs(spread)
    print(f"Fair CDS spread: {10000*spread:.3f} bp")
    print(f"Premium-leg PV: {premium.sum():.9f}")
    print(f"Protection-leg PV: {protection.sum():.9f}")
    width=.34
    plt.bar(years-width/2,premium,width,label="Premium leg PV")
    plt.bar(years+width/2,protection,width,label="Protection leg PV")
    plt.xlabel("Year"); plt.ylabel("PV per unit notional"); plt.title("CDS legs at the fair spread")
    plt.grid(axis="y",alpha=.3); plt.legend(); plt.tight_layout(); plt.show()

if __name__ == "__main__": main()
