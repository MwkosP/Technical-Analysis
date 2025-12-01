# 📈 Technical Analysis Signal Generator & Search Framework

## Overview
This project is a full-featured **technical analysis signal engine** that:

- Loads OHLCV data from **Yahoo Finance (`yfinance`)** or any provider  
- Computes dozens of technical indicators  
- Defines **threshold-based triggers** (crossovers, ranges, time-based conditions, etc.)  
- Runs **search algorithms** (Grid, Random, Bayesian*) to explore multi-dimensional indicator spaces  
- Combines the resulting signal sets using a powerful **mixThresholds()** engine  
- Generates **PDF charts** for each configuration (for debugging, research, and optimization)

The system is built for **quantitative research**, **signal generation**, and **strategy prototyping**.

---

## ✨ Key Features

### 🔧 Technical Indicators
- **Momentum / Oscillators**  
  - RSI  
  - StochRSI  
  - ROC  
  - Williams %R  
  - ADX  
  - MACD  

- **Trend Indicators**  
  - MA (Simple Moving Average)  
  - EMA (Exponential Moving Average)  
  - EMA Ribbon  
  - EMA Crossover  
  - Ichimoku Cloud  

- **Volatility / Range Indicators**  
  - Bollinger Bands  
  - ATR  
  - Donchian Channels  

---

## ⚡ Threshold-Based Signal Engine
Each indicator generates signals using multiple threshold types:

- **crossUpThreshold** – indicator crosses a fixed numeric level  
- **crossUpLineThreshold** – fast-vs-slow line crossover  
- **inRangeThreshold** – indicator enters predefined numerical band  
- **timeThreshold** – indicator stays above/below a level for N candles  

All threshold functions output:

