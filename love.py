import streamlit as st
import time

st.set_page_config(page_title="🎂 민주 생일 축하 페이지 🎉", layout="centered")

st.title("🎉 민주야 생일 축하해!!! 🎉")

st.markdown("""
<div style='font-size: 26px; text-align: center; padding: 30px; background-color: #ffe6f0; border-radius: 20px; line-height: 2'>
    🎂 민주야 생축생축!! 💖<br>
    🥰 사랑해!!!!! 💗 싸랑해!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1ㅂ!!!!!!!!!!!!!!!!!!!!!!<br>
    ❤️‍🔥 <span style='color: red; font-weight: bold;'>i love you!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!</span><br>
    💞 사랑해애애ㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐ<br>
    💘 tkfkdgksekrh!!!!!!!!!!!!!!!!!!!!!!!민주!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
</div>
""", unsafe_allow_html=True)

st.balloons()  # 🎈 풍선 팡팡!

time.sleep(1.2)
st.success("🎂 민주야 진짜진짜 생일 축하해 💕")

st.markdown("""
<div style='text-align: right; font-size: 20px; margin-top: 40px;'>
    by 너를 사랑하는 다은이가...... 🥹💌
</div>
""", unsafe_allow_html=True)

# ----------- 친구 메시지 입력 폼 -------------
st.write("---")
st.header("💌 친구들의 축하 메시지 남기기")

# 메시지 입력창
message = st.text_area("여기에 축하 메시지를 적어주세요:", height=100)

# 제출 버튼
if st.button("메시지 보내기"):
    if message.strip() == "":
        st.warning("메시지를 입력해 주세요!")
    else:
        # 메시지를 세션 상태에 저장 (앱 실행 중에만 유지됨)
        if "messages" not in st.session_state:
            st.session_state.messages = []
        st.session_state.messages.append(message)
        st.success("메시지를 성공적으로 보냈어요! 🎉")

# 저장된 메시지 출력
if "messages" in st.session_state and st.session_state.messages:
    st.write("### 💬 지금까지 남겨진 메시지들:")
    for i, msg in enumerate(st.session_state.messages, 1):
        st.markdown(f"**{i}.** {msg}")
