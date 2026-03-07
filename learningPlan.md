# Python for Finance Learning Plan

Book: Python for Finance – Yves Hilpisch  
Duration: 8 Weeks  
Daily Study Time: ~1 hour  
Environment:
- OS: Windows
- Editor: VS Code
- Terminal: CMD / PowerShell
- Python: 3.12
- Virtual Environment: myvenv
- GitHub Repo: volatility-surface-tool

---

# Project Structure

volatility-surface-tool/

myvenv/
notes/
learning_plan.md
src/
data/
notebooks/
tests/

---

# WEEK 1 — Environment & Scientific Stack

## Day 1 — Environment Setup

Goal  
Setup development environment

Tasks

Install Python 3.12  
Install VS Code  
Install Git  

Create project folder

mkdir volatility-surface-tool
cd volatility-surface-tool

Initialize Git

git init

Create virtual environment

python -m venv myvenv

Activate environment (CMD)

myvenv\Scripts\activate

Expected

(myvenv)

Commit

git add .
git commit -m "initial setup"

---

## Day 2 — Scientific Python Stack

Goal  
Install and test Python scientific libraries

Install packages

pip install numpy pandas matplotlib yfinance

Create file

stack_test.py

Code

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = np.random.randn(1000)

print("mean:", np.mean(data))
print("std:", np.std(data))

Run

python stack_test.py

Commit

git add .
git commit -m "scientific stack test"

---

## Day 3 — Financial Data

Goal  
Download market data

Create file

financial_data.py

Code

import pandas as pd
import yfinance as yf

data = yf.download("AAPL", start="2020-01-01")

print(data.head())

Run

python financial_data.py

Commit

git add .
git commit -m "download financial data"

---

## Day 4 — Returns Calculation

Goal  
Compute asset returns

Code

import pandas as pd
import yfinance as yf

data = yf.download("AAPL", start="2020-01-01")

data["returns"] = data["Close"].pct_change()

print(data[["Close","returns"]].head())

Commit

git commit -am "calculate daily returns"

---

## Day 5 — Volatility Calculation

Goal  
Compute annualized volatility

Create file

volatility.py

Code

import pandas as pd
import yfinance as yf

data = yf.download("AAPL", start="2020-01-01")

returns = data["Close"].pct_change()

volatility = returns.std() * (252 ** 0.5)

print("Annualized volatility:", volatility)

Commit

git commit -am "volatility calculation"

---

## Day 6 — Rolling Volatility

Goal  
Compute rolling volatility

Code

rolling_vol = returns.rolling(30).std() * (252 ** 0.5)

print(rolling_vol.tail())

Commit

git commit -am "rolling volatility"

---

## Day 7 — Volatility Visualization

Goal  
Plot volatility

Create file

vol_plot.py

Code

import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

data = yf.download("AAPL", start="2020-01-01")

returns = data["Close"].pct_change()

rolling_vol = returns.rolling(30).std() * (252 ** 0.5)

rolling_vol.plot()

plt.title("Rolling Volatility")

plt.show()

Commit

git commit -am "volatility plot"

---

# WEEK 2 — NumPy & pandas

Day 8  
Learn NumPy arrays

Day 9  
Matrix operations

Day 10  
DataFrame manipulation

Day 11  
Time series analysis

Day 12  
Missing data handling

Day 13  
Multi-asset dataset

Day 14  
Portfolio return calculation

---

# WEEK 3 — Time Series Analysis

Day 15  
Moving averages

Day 16  
Correlation analysis

Day 17  
Volatility clustering

Day 18  
Value at Risk

Day 19  
Drawdown analysis

Day 20  
Portfolio volatility

Day 21  
Visualization dashboard

---

# WEEK 4 — Object-Oriented Programming

Day 22  
Python classes

Day 23  
Asset class

Day 24  
Portfolio class

Day 25  
Risk methods

Day 26  
Code refactoring

Day 27  
Docstrings

Day 28  
Unit tests

---

# WEEK 5 — Monte Carlo Simulation

Day 29  
Random processes

Day 30  
Geometric Brownian motion

Day 31  
Price simulation

Day 32  
Monte Carlo engine

Day 33  
Option payoff simulation

Day 34  
Risk-neutral pricing

Day 35  
Performance optimization

---

# WEEK 6 — Option Pricing

Day 36  
Black-Scholes model

Day 37  
Greeks

Day 38  
Vectorized pricing

Day 39  
Calibration

Day 40  
Implied volatility

Day 41  
Market data integration

Day 42  
Volatility smile

---

# WEEK 7 — Volatility Surface

Day 43  
Option chain data

Day 44  
Implied volatility grid

Day 45  
Interpolation

Day 46  
Surface construction

Day 47  
3D visualization

Day 48  
Surface smoothing

Day 49  
Validation

---

# WEEK 8 — Final Project

Day 50  
Refactor code

Day 51  
Modular architecture

Day 52  
Documentation

Day 53  
Notebook demo

Day 54  
Git tagging

Day 55  
Project README

Day 56  
Final commit

---

# Final Project

Volatility Surface Engine

Features

- download options data
- compute implied volatility
- construct volatility surface
- visualize surface
- modular Python architecture
- version controlled with Git