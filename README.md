# Trader Performance vs Market Sentiment

## Objective

This project analyzes how Bitcoin market sentiment (Fear vs Greed)
relates to trader behavior and performance on Hyperliquid.

The goal is to uncover behavioral patterns that can inform smarter trading strategies.

---

## Methodology

### 1. Data Preparation
- Loaded sentiment and trader datasets
- Cleaned column names and standardized formats
- Converted Unix timestamps to daily granularity
- Simplified sentiment into two regimes: Fear vs Greed
- Aggregated trade-level data to daily account-level metrics

### 2. Feature Engineering
Created daily metrics per account:
- Daily PnL
- Win rate
- Trade frequency
- Average trade size (USD)
- Long/Short ratio

### 3. Regime-Based Analysis
Compared performance and behavior across:
- Fear regimes
- Greed regimes

### 4. Trader Segmentation
Identified:
- High vs Low activity traders
- Consistent winners vs others
- Large vs small position traders

---

## Key Insights

1. Fear regimes produce significantly higher mean and median PnL.
2. Traders increase activity nearly 4x during Fear periods.
3. High-activity and consistent traders benefit disproportionately during Fear regimes.
4. Larger position sizing improves returns primarily in Fear regimes.

---

## Strategy Recommendations

**1. Volatility Participation Rule**
During Fear regimes:
- Increase trade frequency
- Allow larger position sizing
- Deploy high-activity strategies

**2. Controlled Risk in Greed Regimes**
During Greed regimes:
- Reduce trade frequency
- Avoid aggressive position sizing
- Focus on selective setups

---

## Bonus (Optional)
- Logistic regression model predicting profitability
- Streamlit dashboard for interactive exploration

---

## How to Run

1. Clone repository:
   git clone <repo_url>

2. Create virtual environment:
   python -m venv venv
   source venv/bin/activate

3. Install dependencies:
   pip install -r requirements.txt

4. Run notebook:
   notebook/analysis.ipynb

Run Streamlit dashboard:
    python -m streamlit run app.py