# Quantitative Finance Modelling

Selected models from **Advanced Financial Engineering** coursework, curated as a public portfolio project.

## Scope

This repository covers a progression from fixed-income fundamentals to derivatives and credit risk:

- mortgage amortisation under fixed and floating-rate scenarios
- bond pricing, discounting, pull-to-par and realised return
- spot-curve bootstrapping and implied forward rates
- forward and futures pricing under no-arbitrage
- FX hedging and currency swaps
- interest-rate swap valuation using discount and forward curves
- hazard rates, survival probabilities and CDS pricing

## Selected quantitative results

- bootstrapped a 1Y–6Y spot curve from bond market prices and derived implied forward rates
- valued and revalued a **EUR 10m payer interest-rate swap** using interpolated discount factors and 6M forward rates
- verified that the swap remained close to par when curves evolved consistently with the original term structure
- priced a 5-year CDS from premium and protection legs, obtaining a spread of approximately **224 bp** under the assignment assumptions
- analysed FX and currency-swap hedging structures across GBP, EUR and USD exposures

## Repository structure

`MODEL_INDEX.md` summarises the modelling sequence and `RESULTS.md` collects representative quantitative outputs. The original models were built in Excel; sanitized workbook copies are maintained separately so collaborator names and student identifiers are not exposed publicly.

## Tools

Excel, fixed-income mathematics, curve bootstrapping, interpolation, no-arbitrage pricing, cash-flow discounting, credit-risk modelling

## Authorship note

The underlying coursework was originally completed in a small group. This public portfolio version is curated by **Adrià Saz Guerra**; collaborator names are omitted for privacy. I was responsible for the large majority of the modelling, calculations and written analysis represented here.

## Disclaimer

Academic coursework only. Nothing in this repository constitutes investment advice.
