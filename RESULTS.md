# Selected results

This note highlights some of the quantitative outputs produced across the Advanced Financial Engineering models.

## Fixed income and term structure

- Bootstrapped annual discount factors and a **1Y–6Y spot-rate curve** from coupon-bond market prices
- Derived implied forward rates from the bootstrapped term structure
- Analysed bond pull-to-par behaviour and realised return when coupons are reinvested at a new market yield

## Forwards, futures and FX

- Applied no-arbitrage carry relationships to forward pricing
- Computed futures profit/loss from entry and close-out prices
- Built an FX-forward hedge for a sterling receivable and analysed cross-currency cash flows

## Interest-rate swaps

- Valued a **EUR 10 million payer interest-rate swap** using a discount curve and a 6M forward curve with interpolation between market nodes
- Under a curve evolution consistent with the original term structure, obtained an NPV close to zero (about **EUR 1.9k**, small relative to the EUR 10m notional), providing a numerical consistency check
- Revalued the same structure under a shifted observed term structure to analyse mark-to-market exposure

## Credit risk and CDS

- Mapped credit spreads and recovery assumptions into hazard rates and survival probabilities
- Priced a five-year CDS by equating the discounted premium and protection legs
- Under the assignment assumptions, obtained an annual CDS spread of approximately **224.21 bp**

## Mortgage modelling

- Compared fixed and floating-rate mortgage cash flows over a 30-year horizon
- In one floating-rate scenario, total interest reached approximately **EUR 154.6k**, about **EUR 55.9k** above the comparison fixed-rate case

All figures here are outputs of the academic models and depend on the assumptions and market inputs specified in the corresponding assignments.
