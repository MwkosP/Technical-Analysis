# === External libraries ===
import os, threading, time
from src.ta.utils.helper import setup_env, kill_uvicorn_on_port, open_swagger, start_cloudflared
setup_env() # 🛠 Ensure environment + dependencies before importing anything else
# --- Imports  AFTER setup_env ---
import uvicorn
from src.ta.functions import *
from src.ta.tests.general import *
#########
from src.ta.functions.indicators.universal_threshold_dispatcher  import *
from src.ta.functions.indicators.universal_indicator_dispatcher import *
from src.ta.functions.indicators.threshold_functions import *
from src.ta.functions.plots import *
from src.ta.ml.optimizers.search import *

from src.ta.data.fetch_yfinance import download_underlying_stock
from src.ta.ml.optimizers.search import gridSearch,plot_results_pdf
import matplotlib.pyplot as plt






underlying_stock = "BTC-USD"
start="2024-02-06"
end="2025-09-15"
tmfrm='1d' #1d 1wk

#Download Set
df = download_underlying_stock(title=underlying_stock,start=start,end=end,tmfrm="1d",plot=False)
#print(df)


'''
pdf_name ="all_plots.pdf"
period1=14
period2=30

search_space = [
    {
        "type": "inRange",
        "indicator": "rsi",
        "periods": list(range(period1, period2)),  # RSI periods 
        "ranges": [
            (low, high)
            for low in range(0, 51, 5)        # 0..50
            for high in range(low + 5, 51, 5) # up to 50
        ]
    },
    {
        "type": "inRange",
        "indicator": "williams",
        "periods": list(range(period1, period2)),  # Williams periods 14–40
        "ranges": [
            (low, high)
            for low in range(-100, -59, 5)     # -100..-60
            for high in range(low + 5, -59, 5) # up to -60
        ]
    },
    {
        "type": "inRange",
        "indicator": "roc",
        "periods": list(range(period1, period2)),  # ROC periods 14–40
        "ranges": [
            (low, high)
            for low in range(-50, 11, 5)       # -50..10
            for high in range(low + 5, 11, 5)  # up to 10
        ]
    }
]
'''










def main():
    print("✅ All dependencies ready. Program running...")



    
    ''' 
    print("🔍Running Grid Search...")
    # Run grid search
    results = gridSearch(df, search_space)

    # Save top n results to PDF
    plot_results_pdf(df, results, pdf_name=pdf_name, top_n=10)
    print(f"\n📄 Report ready: {pdf_name}")
    '''


    #plot_signals(df, signals['Date'].tolist(), title="rsi RANGE ind.")

    if os.environ.get("INSIDE_VENV") != "1":
        print("⏩ Skipping server startup (outside venv process)")
        return

    # Show links
    print("\n🚀 FastAPI server starting...")
    print("📑 Swagger docs:   http://127.0.0.1:8000/docs")

    
    # Kill any leftover uvicorn
    kill_uvicorn_on_port(8000)

    # ✅ Launch Swagger in browser BEFORE  uvicorn
    open_swagger("http://127.0.0.1:8000/docs")

    # Start cloudflared in background with delay
    #threading.Thread(target=start_cloudflared, daemon=True).start()

    # Run the GLOBAL app
    uvicorn.run("app:app", host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()
