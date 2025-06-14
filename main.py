import streamlit as st

# Cấu hình trang
st.set_page_config(page_title="Login Page", page_icon="🔐", layout="centered")

# HÌNH ẢNH TRANG ĐĂNG NHẬP (Ảnh từ URL hoặc file local)
st.image("https://cdn-icons-png.flaticon.com/512/747/747376.png", width=120, caption="Welcome to My App")

# Tiêu đề và mô tả
st.markdown("<h2 style='text-align: center;'>🔐 Secure Login</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Please enter your credentials to continue</p>", unsafe_allow_html=True)

# STYLE tuỳ chỉnh bằng HTML
st.markdown("""
    <style>
    .login-container {
        background-color: #f9f9f9;
        padding: 2rem;
        border-radius: 15px;
        max-width: 400px;
        margin: auto;
        box-shadow: 0px 0px 12px rgba(0, 0, 0, 0.1);
    }
    </style>
""", unsafe_allow_html=True)

# FORM
with st.form("login_form"):
    st.markdown('<div class="login-container">', unsafe_allow_html=True)

    username = st.text_input("👤 Username")
    password = st.text_input("🔒 Password", type="password")
    remember = st.checkbox("Remember me")

    login_button = st.form_submit_button("Log In")

    st.markdown('</div>', unsafe_allow_html=True)

# Kiểm tra đăng nhập
if login_button:
    if username == "admin" and password == "123456":
        st.success(f"✅ Welcome back, **{username}**!")
        st.balloons()
    else:
        st.error("❌ Wrong username or password. Try again.")
