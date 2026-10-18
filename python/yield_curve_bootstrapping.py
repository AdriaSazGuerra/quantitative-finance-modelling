"""Bootstrap a 1Y-6Y spot curve and implied forward rates from coupon bonds."""
from __future__ import annotations
import numpy as np
import matplotlib.pyplot as plt

NOMINAL = 100.0
MATURITIES = np.arange(1, 7, dtype=int)
MARKET_PRICES = np.array([97.00, 95.74, 100.75, 92.00, 94.75, 98.00])
ANNUAL_COUPONS = np.array([0.000, 0.023, 0.057, 0.035, 0.043, 0.050])


def bootstrap_discount_factors() -> np.ndarray:
    dfs: list[float] = []
    for maturity, price, coupon_rate in zip(MATURITIES, MARKET_PRICES, ANNUAL_COUPONS):
        coupon = NOMINAL * coupon_rate
        pv_prior = sum(coupon * dfs[t - 1] for t in range(1, maturity))
        dfs.append((price - pv_prior) / (NOMINAL + coupon))
    return np.array(dfs)


def spot_rates(discount_factors: np.ndarray) -> np.ndarray:
    return discount_factors ** (-1.0 / MATURITIES) - 1.0


def one_year_forward_rates(discount_factors: np.ndarray) -> np.ndarray:
    fwds = np.full_like(discount_factors, np.nan, dtype=float)
    fwds[1:] = discount_factors[:-1] / discount_factors[1:] - 1.0
    return fwds


def forward_2y3y(discount_factors: np.ndarray) -> float:
    df_2_5 = discount_factors[4] / discount_factors[1]
    return df_2_5 ** (-1.0 / 3.0) - 1.0


def main() -> None:
    dfs = bootstrap_discount_factors()
    spots = spot_rates(dfs)
    fwds = one_year_forward_rates(dfs)
    print("Maturity | Discount factor | Spot rate | 1Y forward")
    for t, df, s, f in zip(MATURITIES, dfs, spots, fwds):
        f_txt = "-" if np.isnan(f) else f"{100*f:8.4f}%"
        print(f"{t:>8} | {df:>15.9f} | {100*s:>8.4f}% | {f_txt}")
    print(f"\n2Y3Y forward yield: {100*forward_2y3y(dfs):.4f}%")
    plt.plot(MATURITIES, 100*spots, "o-", label="Spot curve")
    plt.plot(MATURITIES[1:], 100*fwds[1:], "o-", label="1Y forwards")
    plt.xlabel("Maturity (years)"); plt.ylabel("Rate (%)")
    plt.title("Bootstrapped spot curve and implied 1Y forwards")
    plt.grid(alpha=.3); plt.legend(); plt.tight_layout(); plt.show()


if __name__ == "__main__":
    main()
