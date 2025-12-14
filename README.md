<img src="https://raw.githubusercontent.com/MwkosP/Technical-Analysis/main/AutoTAIcon.png"
     alt="AutoTA Logo"
     width="200"
     align="right"
     style="margin-left:16px;" />

## AutoTA: Technical Analysis Signal Generator & Hyperparameter Optimization Framework

<br />





## Overview
This project is a full-featured **technical analysis signal engine** that:

- Loads price and more data from **Yahoo Finance (`yfinance`)** and other providers  
- Computes technical indicators  
- Defines **threshold-based triggers** (crossovers, ranges, time-based conditions, etc.)  
- Runs **search algorithms** (Grid, Random, Bayesian*) to explore multi-dimensional indicator spaces and relationships  
- Combines the resulting signal sets using a powerful **mixThresholds()** func
- Filters Data based on  Historiy & Statistics.    
- Optionally Generates **PDF charts** for each configuration (for debugging, research, and optimization)
- Implements Models on the Statistically best Datasets from earlier and trains models.(in the Future)

The system is built for **quantitative research**, **signal generation**, and **strategy prototyping**.

---
![Preview](https://raw.githubusercontent.com/MwkosP/Technical-Analysis/main/signals.png)


## Tech Stack:
(Backend)
- Python(Numpy,Pandas,Matplotlib,Plotly,fastapi,finta,etc...)
- SQLite
<br>
(Frontend)<br>
-ReactRouter,Tailwind,Typescript,3D JS 



### Technical Indicators
- **Momentum / Oscillators**  
  - RSI,StochRSI,ROC,Williams %R,ADX ,MACD  

- **Trend Indicators**  
  - MA ,EMA,EMA Ribbon,EMA Crossover,Ichimoku Cloud  

- **Volatility / Range Indicators**  
  - Bollinger Bands,ATR,Donchian Channels  

---
![Preview](https://raw.githubusercontent.com/MwkosP/Technical-Analysis/main/image.png)
## Threshold-Based Signal Engine
Each indicator generates signals using multiple threshold types:

- **crossUpThreshold** – indicator crosses a fixed numeric level  
- **crossUpLineThreshold** – fast-vs-slow line crossover  
- **inRangeThreshold** – indicator enters predefined numerical band  
- **timeThreshold** – indicator stays above/below a level for N candles  

## 🔍 Search Algorithms (Grid / Random / Bayesian)
The system supports **multi-dimensional search spaces**, e.g.:

{
    "type": "crossUpThreshold",
    "indicator": "rsi",
    "period": [7, 14, 21],
    "threshold": [30],
    "indicator_params": {
        "indicator_period": [7, 14, 21]
    }
}
![Preview](https://raw.githubusercontent.com/MwkosP/Technical-Analysis/main/search.webp)
<br>mixThresholds()
will:
Expand all combinations of parameters, Run threshold detection for each sub-config, Collect all signals inside , UNION them ,AND/OR combine them across blocks, This creates extremely powerful multi-indicator composite signals.


## Fututre: 
Find Best Historical Data-Signals and train models on them

































