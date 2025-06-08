import streamlit as st
import time

st.set_page_config(page_title="🎂 민주 생일 축하 페이지 🎉", layout="centered")

st.title("🎉 민주야 생일 축하해!!! 🎉")

st.markdown("""
<div style='font-size: 26px; text-align: center; padding: 30px; background-color: #ffe6f0; border-radius: 20px; line-height: 2'>
    🎂 민주야 생축생축!! 💖<br>
    🥰 사랑해!!!!! 💗 싸랑해!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1!!!!!!!!!!!!!!!!!!!!!!<br>
    ❤️‍🔥 <span style='color: red; font-weight: bold;'>i love you!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!</span><br>
    💞 사랑해애애ㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐ<br>
    💘 tkfkdgksekrh!!!!!!!!!!!!!!!!!!!!!!!민주!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
</div>
""", unsafe_allow_html=True)

st.balloons()  # 🎈 풍선 팡팡!

# 감성 타이밍 추가
time.sleep(1.2)
st.success("🎂 민주야 진짜진짜 생일 축하해 💕")

# 마지막 감동 메시지
st.markdown("""
<div style='text-align: right; font-size: 20px; margin-top: 40px;'>
    by 너를 사랑하는 다은이가...... 🥹💌
</div>
""", unsafe_allow_html=True)
