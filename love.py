import streamlit as st
import os
import json
import time

st.set_page_config(page_title="🎂 민주 생일 축하 페이지 🎉", layout="centered")

st.title("🎉 민주야 생일 축하해!!! 🎉")

st.markdown("""
<div style='font-size: 26px; text-align: center; padding: 30px; background-color: #ffe6f0; border-radius: 20px; line-height: 2'>
    🎂 민주야 생축생축!! 💖<br>
    🥰 사랑해!!!!! 💗 싸랑해!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1!!!!!!!!!!!!!!!!!!!!!!<br>
    ❤️‍🔥 <span style='color: red; font-weight: bold;'>i love you!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!</span><br>
    💞 사랑해애애ㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐ<br>
    💘 tkfkdgksekrh!!!!!!!!!!!!!!!!!!!!!!!민주!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1<br>
    민주야 너를 처음 만났을 때 부터 내 심장은 뛰고 있었어 암튼 사랑해 내마음을 바아ㅏㅏㅏㅏㅏㅏ줄래ㅐㅐ????????????????
</div>
""", unsafe_allow_html=True)

st.balloons()
time.sleep(1.2)
st.success("🎂 민주야 진짜진짜 생일 축하해 💕")

st.markdown("""
<div style='text-align: right; font-size: 20px; margin-top: 40px;'>
    by 너를 사랑하는 다은이가...... 🥹💌
</div>
""", unsafe_allow_html=True)

st.write("---")
st.header("💌 친구들의 사랑의 축하 메시지 남기기")

# 메시지 저장 파일 경로
MESSAGE_FILE = "messages.json"

# 메시지 불러오기
if os.path.exists(MESSAGE_FILE):
    with open(MESSAGE_FILE, "r", encoding="utf-8") as f:
        messages = json.load(f)
else:
    messages = []

# 입력창
new_message = st.text_area("여기에 사랑의 축하 메시지를 적어주세요:", height=100)

# 제출 처리
if st.button("메시지 보내기"):
    if new_message.strip() == "":
        st.warning("메시지를 입력해 주세요!")
    else:
        messages.append(new_message.strip())
        with open(MESSAGE_FILE, "w", encoding="utf-8") as f:
            json.dump(messages, f, ensure_ascii=False, indent=2)
        st.success("메시지를 성공적으로 보냈어요! 🎉")

# 모든 메시지 표시
if messages:
    st.write("### 💬 지금까지 남겨진 사랑의 💘 메시지들:")
    for i, msg in enumerate(messages, 1):
        st.markdown(f"**{i}.** {msg}")
