```python
from anacondo.blocks import Blocks
from test.test_blocks import generate_sample_block as g
```


```python
yorkville = g()
```


```python
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
```


```python
# Create Yorkville property based on assumptions
yorkville = Blocks(**yorkville_assumptions)
```


```python
# Print financial metrics
yorkville.print_financial_performance()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Year</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>8</th>
      <th>9</th>
      <th>10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Cash on Cash COC</th>
      <td>-0.006500</td>
      <td>-0.003600</td>
      <td>-0.000500</td>
      <td>0.002500</td>
      <td>0.005700</td>
      <td>0.008900</td>
      <td>0.012200</td>
      <td>0.015500</td>
      <td>0.018900</td>
      <td>0.022400</td>
    </tr>
    <tr>
      <th>Return on Equity ROE</th>
      <td>0.051500</td>
      <td>0.053100</td>
      <td>0.054600</td>
      <td>0.055900</td>
      <td>0.057000</td>
      <td>0.058100</td>
      <td>0.059100</td>
      <td>0.059900</td>
      <td>0.060700</td>
      <td>0.061400</td>
    </tr>
    <tr>
      <th>Annualized Return APY</th>
      <td>-0.018078</td>
      <td>0.021873</td>
      <td>0.035883</td>
      <td>0.043137</td>
      <td>0.047605</td>
      <td>0.050633</td>
      <td>0.052807</td>
      <td>0.054425</td>
      <td>0.055657</td>
      <td>0.056605</td>
    </tr>
    <tr>
      <th>Return On Investment</th>
      <td>-0.005000</td>
      <td>0.051400</td>
      <td>0.112600</td>
      <td>0.178900</td>
      <td>0.250400</td>
      <td>0.327100</td>
      <td>0.409300</td>
      <td>0.497000</td>
      <td>0.590300</td>
      <td>0.689500</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Print mortgage payment summary
yorkville.mortgage_balance_summary()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>Total Paid</th>
      <th>Mortgage Balance</th>
      <th>Principal Paydown</th>
      <th>Interest Paydown</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>24980.459336</td>
      <td>477490.62</td>
      <td>10009.380979</td>
      <td>14971.078357</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>24980.459336</td>
      <td>467166.50</td>
      <td>10324.118690</td>
      <td>14656.340646</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>24980.459336</td>
      <td>456517.75</td>
      <td>10648.753099</td>
      <td>14331.706237</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>24980.459336</td>
      <td>445534.15</td>
      <td>10983.595402</td>
      <td>13996.863934</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>24980.459336</td>
      <td>434205.19</td>
      <td>11328.966578</td>
      <td>13651.492758</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>24980.459336</td>
      <td>422519.99</td>
      <td>11685.197699</td>
      <td>13295.261637</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>24980.459336</td>
      <td>410467.36</td>
      <td>12052.630249</td>
      <td>12927.829087</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>24980.459336</td>
      <td>398035.74</td>
      <td>12431.616449</td>
      <td>12548.842887</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>24980.459336</td>
      <td>385213.22</td>
      <td>12822.519594</td>
      <td>12157.939742</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>24980.459336</td>
      <td>371987.51</td>
      <td>13225.714405</td>
      <td>11754.744931</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Rerun with 30 years worth of data
yorkville.update(years=30)
yorkville.mortgage_balance_summary()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>Total Paid</th>
      <th>Mortgage Balance</th>
      <th>Principal Paydown</th>
      <th>Interest Paydown</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>24980.459336</td>
      <td>477490.62</td>
      <td>10009.380979</td>
      <td>14971.078357</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>24980.459336</td>
      <td>467166.50</td>
      <td>10324.118690</td>
      <td>14656.340646</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>24980.459336</td>
      <td>456517.75</td>
      <td>10648.753099</td>
      <td>14331.706237</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>24980.459336</td>
      <td>445534.15</td>
      <td>10983.595402</td>
      <td>13996.863934</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>24980.459336</td>
      <td>434205.19</td>
      <td>11328.966578</td>
      <td>13651.492758</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>24980.459336</td>
      <td>422519.99</td>
      <td>11685.197699</td>
      <td>13295.261637</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>24980.459336</td>
      <td>410467.36</td>
      <td>12052.630249</td>
      <td>12927.829087</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>24980.459336</td>
      <td>398035.74</td>
      <td>12431.616449</td>
      <td>12548.842887</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>24980.459336</td>
      <td>385213.22</td>
      <td>12822.519594</td>
      <td>12157.939742</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>24980.459336</td>
      <td>371987.51</td>
      <td>13225.714405</td>
      <td>11754.744931</td>
    </tr>
    <tr>
      <th>10</th>
      <td>11</td>
      <td>24980.459336</td>
      <td>358345.92</td>
      <td>13641.587383</td>
      <td>11338.871953</td>
    </tr>
    <tr>
      <th>11</th>
      <td>12</td>
      <td>24980.459336</td>
      <td>344275.38</td>
      <td>14070.537185</td>
      <td>10909.922151</td>
    </tr>
    <tr>
      <th>12</th>
      <td>13</td>
      <td>24980.459336</td>
      <td>329762.41</td>
      <td>14512.975002</td>
      <td>10467.484334</td>
    </tr>
    <tr>
      <th>13</th>
      <td>14</td>
      <td>24980.459336</td>
      <td>314793.08</td>
      <td>14969.324954</td>
      <td>10011.134381</td>
    </tr>
    <tr>
      <th>14</th>
      <td>15</td>
      <td>24980.459336</td>
      <td>299353.06</td>
      <td>15440.024500</td>
      <td>9540.434836</td>
    </tr>
    <tr>
      <th>15</th>
      <td>16</td>
      <td>24980.459336</td>
      <td>283427.53</td>
      <td>15925.524850</td>
      <td>9054.934486</td>
    </tr>
    <tr>
      <th>16</th>
      <td>17</td>
      <td>24980.459336</td>
      <td>267001.24</td>
      <td>16426.291406</td>
      <td>8554.167930</td>
    </tr>
    <tr>
      <th>17</th>
      <td>18</td>
      <td>24980.459336</td>
      <td>250058.44</td>
      <td>16942.804202</td>
      <td>8037.655134</td>
    </tr>
    <tr>
      <th>18</th>
      <td>19</td>
      <td>24980.459336</td>
      <td>232582.88</td>
      <td>17475.558368</td>
      <td>7504.900968</td>
    </tr>
    <tr>
      <th>19</th>
      <td>20</td>
      <td>24980.459336</td>
      <td>214557.81</td>
      <td>18025.064601</td>
      <td>6955.394734</td>
    </tr>
    <tr>
      <th>20</th>
      <td>21</td>
      <td>24980.459336</td>
      <td>195965.96</td>
      <td>18591.849659</td>
      <td>6388.609677</td>
    </tr>
    <tr>
      <th>21</th>
      <td>22</td>
      <td>24980.459336</td>
      <td>176789.51</td>
      <td>19176.456861</td>
      <td>5804.002475</td>
    </tr>
    <tr>
      <th>22</th>
      <td>23</td>
      <td>24980.459336</td>
      <td>157010.06</td>
      <td>19779.446612</td>
      <td>5201.012724</td>
    </tr>
    <tr>
      <th>23</th>
      <td>24</td>
      <td>24980.459336</td>
      <td>136608.66</td>
      <td>20401.396937</td>
      <td>4579.062399</td>
    </tr>
    <tr>
      <th>24</th>
      <td>25</td>
      <td>24980.459336</td>
      <td>115565.76</td>
      <td>21042.904038</td>
      <td>3937.555298</td>
    </tr>
    <tr>
      <th>25</th>
      <td>26</td>
      <td>24980.459336</td>
      <td>93861.18</td>
      <td>21704.582864</td>
      <td>3275.876472</td>
    </tr>
    <tr>
      <th>26</th>
      <td>27</td>
      <td>24980.459336</td>
      <td>71474.11</td>
      <td>22387.067699</td>
      <td>2593.391637</td>
    </tr>
    <tr>
      <th>27</th>
      <td>28</td>
      <td>24980.459336</td>
      <td>48383.10</td>
      <td>23091.012774</td>
      <td>1889.446561</td>
    </tr>
    <tr>
      <th>28</th>
      <td>29</td>
      <td>24980.459336</td>
      <td>24566.00</td>
      <td>23817.092891</td>
      <td>1163.366445</td>
    </tr>
    <tr>
      <th>29</th>
      <td>30</td>
      <td>24980.459336</td>
      <td>-0.00</td>
      <td>24566.004069</td>
      <td>414.455267</td>
    </tr>
  </tbody>
</table>
</div>




```python
# look at cash on cash return specifically. index of array is the year.
yorkville.cash_on_cash_return()


```




    array([-0.0065, -0.0036, -0.0005,  0.0025,  0.0057,  0.0089,  0.0122,
            0.0155,  0.0189,  0.0224,  0.0259,  0.0296,  0.0332,  0.037 ,
            0.0408,  0.0447,  0.0487,  0.0528,  0.057 ,  0.0612,  0.0655,
            0.0699,  0.0744,  0.079 ,  0.0837,  0.0884,  0.0933,  0.0983,
            0.1033,  0.1085])




```python
# How much can I buy Yorkville for so that my cash on cash return is > 0
# Returns the break even purchase price after X number of years. For example, based on input assumptions
# if I purchase Yorkville for 648000, It will take me 3 years before I get positive cash on cash return
yorkville.simulate_break_even('coc', 'purchase_price')
```




    {621000: 1,
     634000: 2,
     648000: 3,
     662000: 4,
     676000: 5,
     690000: 6,
     705000: 7,
     720000: 8,
     735000: 9,
     751000: 10,
     766000: 11,
     783000: 12,
     799000: 13,
     816000: 14,
     833000: 15,
     851000: 16,
     869000: 17,
     887000: 18,
     905000: 19,
     924000: 20,
     944000: 21,
     964000: 22,
     984000: 23,
     1004000: 24,
     1025000: 25,
     1047000: 26,
     1068000: 27,
     1091000: 28,
     1113000: 29,
     1136000: 30}




```python
# Similarly, returns the break even interest rate after X number of years. 
# A borrowing rate of 4.8% based on current input assumnptions will take 4 years before achieving positive ROI
yorkville.simulate_break_even('roi', 'interest_rate')
```




    {0.03: 1,
     0.042: 2,
     0.046: 3,
     0.048: 4,
     0.05: 5,
     0.052: 6,
     0.054: 7,
     0.056: 8,
     0.058: 9,
     0.06: 10,
     0.062: 11,
     0.064: 12,
     0.066: 13,
     0.068: 14,
     0.07: 15,
     0.072: 16,
     0.074: 17,
     0.076: 18,
     0.078: 19,
     0.08: 20,
     0.082: 21,
     0.084: 22,
     0.086: 23,
     0.088: 24,
     0.09: 25,
     0.092: 26,
     0.094: 27,
     0.096: 28,
     0.098: 29,
     0.1: 30}




```python

```
