
# app.py
try:
    import streamlit as st
except ModuleNotFoundError:
    raise ImportError("Streamlit is not installed. Please install it using 'pip install streamlit' in your environment.")

from signal_engine import generate_signals
from telegram_bot import send_telegram_alert
from utils.market_data import get_market_overview
from utils.oi_analysis import get_oi_volume_heatmap
from utils.news import get_latest_news
from utils.sentiment import get_market_sentiment
from utils.stats import get_performance_stats
import datetime

# Dark mode theme using Streamlit config
st.set_page_config(page_title="Ultimate Trading Dashboard", layout="wide")
st.markdown("""
    <style>
        body { background-color: #0e1117; color: white; }
        .reportview-container .markdown-text-container { color: white; }
        .sidebar .sidebar-content { background-color: #1e1e1e; }
        .stButton>button { background-color: #00acc1; color: white; border-radius: 10px; }
        .stProgress>div>div>div>div { background-color: #1de9b6; }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='color:#00e5ff;'>⚡ Ultimate Indian Market Trading Dashboard</h1>", unsafe_allow_html=True)

# Sidebar controls
st.sidebar.title("🔍 Filters")
symbol = st.sidebar.selectbox("Select Symbol", ["NIFTY", "BANKNIFTY", "RELIANCE", "HDFCBANK", "INFY"])
date = st.sidebar.date_input("Date", datetime.date.today())

# Signal Section
st.subheader("🚨 Trade Signals")
try:
    signals = generate_signals(symbol)
    if not signals:
        st.warning("No signals generated for the selected symbol.")
    for sig in signals:
        st.markdown(f"**{sig['type']}** | {sig['symbol']} | Reason: {sig['reason']} | Confidence: {sig['confidence']}%")
        st.progress(sig['confidence'] / 100)
except Exception as e:
    st.error(f"Error generating signals: {e}")

# Market Overview
st.subheader("📈 Market Overview")
try:
    overview = get_market_overview()
    if overview.empty:
        st.warning("No market overview data available.")
    else:
        st.dataframe(overview)
except Exception as e:
    st.error(f"Error fetching market overview: {e}")

# OI & Volume Heatmap
st.subheader("🔍 OI & Volume Analysis")
try:
    heatmap_fig = get_oi_volume_heatmap(symbol)
    if heatmap_fig:
        st.pyplot(heatmap_fig)
    else:
        st.warning("OI & Volume data not available.")
except Exception as e:
    st.error(f"Error generating OI/Volume heatmap: {e}")

# News Feed
st.subheader("📰 Latest Market News")
try:
    news_list = get_latest_news()
    if not news_list:
        st.warning("No news found.")
    for article in news_list:
        st.markdown(f"- [{article['title']}]({article['url']})")
except Exception as e:
    st.error(f"Error fetching news: {e}")

# Sentiment
st.subheader("📊 Market Sentiment & FII/DII Flows")
try:
    sentiment_data = get_market_sentiment()
    if sentiment_data:
        st.json(sentiment_data)
    else:
        st.warning("Sentiment data unavailable.")
except Exception as e:
    st.error(f"Error fetching sentiment data: {e}")

# Stats
st.subheader("📉 Performance Statistics")
try:
    stats = get_performance_stats(symbol)
    if stats.empty:
        st.warning("No performance statistics found.")
    else:
        st.table(stats)
except Exception as e:
    st.error(f"Error fetching performance statistics: {e}")

# Telegram Integration
if st.button("📤 Send Latest Signal to Telegram"):
    try:
        if signals:
            send_telegram_alert(signals[0])
            st.success("Signal sent to Telegram!")
        else:
            st.warning("No signal available to send.")
    except Exception as e:
        st.error(f"Error sending signal to Telegram: {e}")
