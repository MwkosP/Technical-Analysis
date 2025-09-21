# Technical Analysis Signal Generator  

## Overview  
This project is a **technical analysis toolkit** designed to fetch financial market data and generate robust trading signals. It retrieves OHLCV data (Open, High, Low, Close, Volume) from **Yahoo Finance (`yfinance`)** and other providers, then applies a wide range of **technical indicators**.  

The system allows you to:  
- Compute multiple indicators.  
- Define **thresholds** for signals.  
- Label signals as "good" or not based on performance.  
- Combine thresholds using a flexible `mixThreshold()` method.  
- (In progress) Run **Grid Search optimization** across hyperparameters to discover the most effective indicator combinations.  

---

## Features  

### Indicators Implemented  
- **Momentum / Oscillators**:  
  - RSI (Relative Strength Index)  
  - Stochastic RSI  
  - ROC (Rate of Change)  
  - Williams %R  
  - ADX (Average Directional Index)  
  - MACD (Moving Average Convergence Divergence)  

- **Trend Indicators**:  
  - MA (Simple Moving Average)  
  - EMA (Exponential Moving Average)  
  - EMA Ribbon  
  - EMA Crossover  
  - Ichimoku Cloud  

- **Volatility / Range Indicators**:  
  - Bollinger Bands  
  - ATR (Average True Range)  
  - Donchian Channels  

---

### Signal Processing  
- Each indicator generates signals when predefined **thresholds** are crossed.  
- Signals are labeled as **good** if they satisfy set criteria (e.g., profitable outcomes, favorable momentum).  
- The function `mixThreshold()` enables combining multiple thresholds into **robust signal sets**.  

---

### Optimization (Work in Progress 🚧)  
- A **Grid Search (ML optimizer)** is being developed.  
- It will test all possible hyperparameter combinations across the indicator space.  
- Goal: Automatically find the **most effective combination of thresholds** for generating reliable signals.  

---

## Installation  

```bash
git clone https://github.com/yourusername/technical-analysis-signal-generator.git
cd technical-analysis-signal-generator
pip install -r requirements.txt
