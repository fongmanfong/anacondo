# anacondo

_anacondo_ simplifies real estate investment analysis. Implemented in pure Python, it provides a simple API to access a comprehensive set of analytical tools including, but not limited to, cash-on-cash return, return-on-equity, mortgage principal paydown and balance etc. In addition to tradition financial analysis, _anacondo_ includes advanced capabilities including:

- probabilistic risk and uncertainty modelling
- marginal return on investment
- breakeven scenarios
- easy way to compare across multiple investment properties
- integration with other Python real estate API [COMING SOON]
- internal plotting capabilities

## Installation

```
pip install anacondo
```

## Dependencies
- pandas
- NumPy, NumPy Financials

## Getting Started

_anacondo_ is very straightforward and designed for novice to intermediate Python users. The `Block` class represents one property unit and contains all information related to it as well as financial metrics. This provides a simple and intuitive way to assess and compare across multiple properties.

```
from anacondo.blocks import Blocks

property_1 = Block(property_value=500000, .....)
property_2 = Block(property_value=400000, .....)

property_1.mortgage_balance_summary()

property_2.cash_on_cash_return()

```

See more detail in [documentations](/docs/Quickstart.md)


