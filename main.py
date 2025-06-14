import openai

# Khởi tạo chatbot visible
if "show_chatbot" not in st.session_state:
    st.session_state.show_chatbot = False
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Nút bật/tắt chatbot
with st.sidebar:
    if st.button("🤖 Chat with Assistant"):
        st.session_state.show_chatbot = not st.session_state.show_chatbot

# Giao diện chatbot (nếu bật)
if st.session_state.show_chatbot:
    st.markdown("---")
    st.markdown("### 🤖 Chatbot Support")
    for chat in st.session_state.chat_history:
        st.write(f"**You:** {chat['user']}")
        st.write(f"**Bot:** {chat['bot']}")

    user_input = st.text_input("Ask something:", key="chat_input")
    if user_input:
        # BOT trả lời đơn giản (nếu không dùng AI)
        response = "I'm a virtual assistant. We'll get back to you soon!" if "price" not in user_input.lower() else "The prices are shown under each car."
        
        # Nếu bạn muốn dùng OpenAI thực sự, dùng dòng này:
        # openai.api_key = "YOUR_API_KEY"
        # response = openai.ChatCompletion.create(...)

        st.session_state.chat_history.append({"user": user_input, "bot": response})
        st.experimental_rerun()
