import streamlit as st
import psutil

# Streamlitアプリケーションのタイトルを設定
st.title("ネットワーク情報アプリ")

# ネットワーク情報を取得
net_info = psutil.net_if_addrs()

# ネットワーク情報を表示
st.write("ネットワーク情報:")
for interface, addrs in net_info.items():
    st.write(f"インターフェース名: {interface}")
    for addr in addrs:
        st.write(f"  アドレスタイプ: {addr.family}, アドレス: {addr.address}")
    st.write("---")

