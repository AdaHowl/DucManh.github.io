import streamlit as st

# Giao diện tiêu đề và mô tả
st.set_page_config(page_title="Login Form", page_icon="🔐", layout="centered")
st.title("🔐 Welcome to My App")
st.subheader("Please log in to continue")

# Tùy chỉnh style một chút cho dễ nhìn
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
        padding: 2rem;
        border-radius: 10px;
        max-width: 400px;
        margin: auto;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Tạo form đăng nhập
with st.form("login_form"):
    st.markdown('<div class="main">', unsafe_allow_html=True)

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    remember = st.checkbox("Remember me")

    login_button = st.form_submit_button("Log In")

    st.markdown('</div>', unsafe_allow_html=True)

# Xử lý đăng nhập giả lập
if login_button:
    if username == "admin" and password == "123456":
        st.success("✅ Login successful! Welcome, admin.")
    else:
        st.error("❌ Invalid username or password.")
