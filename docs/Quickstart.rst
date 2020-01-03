## Quick Start

### Installation

Install via `pip`:

```
pip install anacondo
```

## Getting Started

_anacondo_ is very straightforward and designed for novice to intermediate Python users. The main idea is that each investment property is created as `Block` object. A `Block` object contains all information related to a property as well as additional things like financial metrics (cash-on-cash return, return on investment). It also has additional capabilities such as calculating break even points of different financial metrics conditioned on input parameters.


### Creating your Block

Input parameters or assumptions are used to create your property `Block` objects. 

| parameter              | optional | description                                                                             | type  |
|------------------------|----------|-----------------------------------------------------------------------------------------|-------|
| rental_income          | no       | Monthly rental income from property                                                     | float |
| purchase_price         | no       | The purchase price of the real estate property.                                         | float |
| interest_rate          | no       | The interest rate of the mortgage. Values between 0 and 1                               | float |
| down_payment_pct       | no       | The percentage of down payment made on the real estate property. Values between 0 and 1 | float |
| loan_term              | no       | The number of years for the mortgage                                                    | int   |
| vacancy                | yes      | Vacancy rate or vacancy days? TBD                                                       |       |
| maintenance_reserve    | yes      | tbd                                                                                     |       |
| management_fee         | yes      | Property management fee                                                                 |       |
| monthly_property_tax   | yes      | Monthly property tax in dollar amount                                                   | float |
| monthly_insurance      | yes      | Monthly insurance in dollar amount                                                      | float |
| monthly_utility        | yes      | Monthly utility cost in dollar amount                                                   | float |
| rental_income_increase | yes      | Yearly rental income increase in percentage. Values between 0 and 1                     | float |
| property_tax_increase  | yes      | Yearly property tax increase in percentage. Values between 0 and 1                      | float |
| closing_cost_buy       | yes      | Dollar amount required upon closing property                                            | float |
| closing_cost_sell      | yes      | Dollar amount required upon selling property                                            | float |

A simple way to create your property `Block` object with the desired input parameters is to pass in a dictionary:

```
yorkville_assumptions = {
    'interest_rate': 0.031,
     'down_payment_pct': 0.25,
     'loan_term': 30,
     'purchase_price': 650000,
     'years': 10,
     'property_value': 650000,
     'rental_income': 2700,
     'vacancy': 0,
     'maintenance_reserve': 0,
     'management_fee': 0.15,
     'monthly_property_tax': 167.0,
     'monthly_insurance': 50.0,
     'monthly_utility': 90,
     'rental_income_increase': 2,
     'property_tax_increase': 2,
     'closing_cost_buy': 0.02,
     'closing_cost_sell': 0
}

yorkville = Blocks(**yorkville_assumptions)
```