import streamlit as st
from engine.signal import get_signal
from engine.backtest import run_backtest
from engine.risk import check_risk
from data.fetch_data import get_latest_price

st.set_page_config(page_title="Smart Options Bot", layout="centered")
st.title("🤖 Smart Options Trading Bot")

ticker = st.text_input("Enter Stock Symbol:", value="AAPL")
run_signal = st.button("🔍 Run Signal")

if run_signal:
    price = get_latest_price(ticker)
    signal = get_signal(ticker)
    risk_ok = check_risk(signal)

    st.write(f"**Current Price:** ${price}")
    st.write(f"**Signal:** {signal}")

    if risk_ok:
        st.success("✅ Signal passed risk checks. Ready to trade!")
    else:
        st.warning("⚠️ Risk filter blocked this trade.")

    with st.expander("📊 Backtest Results"):
        st.pyplot(run_backtest(ticker, signal))