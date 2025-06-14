import streamlit as st

# ==== Cấu hình Streamlit ====
st.set_page_config(page_title="Car Showroom", layout="wide")

# ==== Tạo session lưu giỏ hàng ====
if "cart" not in st.session_state:
    st.session_state.cart = []

# ==== Thanh điều hướng giống BMW ====
st.markdown("""
    <style>
        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 40px;
            background-color: white;
            box-shadow: 0 2px 6px rgba(0,0,0,0.05);
            position: sticky;
            top: 0;
            z-index: 999;
        }
        .navbar-left {
            display: flex;
            align-items: center;
            gap: 25px;
        }
        .navbar-left img {
            height: 40px;
        }
        .navbar-left a {
            text-decoration: none;
            color: black;
            font-weight: 500;
            font-size: 16px;
        }
        .navbar-left a:hover {
            color: #007BFF;
        }
        .navbar-right {
            display: flex;
            align-items: center;
            gap: 20px;
            font-size: 16px;
            color: #555;
        }
        .navbar-right span {
            cursor: pointer;
        }
        .navbar-right span:hover {
            color: #000;
        }
    </style>

    <div class="navbar">
        <div class="navbar-left">
            <img src="https://upload.wikimedia.org/wikipedia/commons/4/44/BMW.svg" alt="logo">
            <a href="#">Trang chủ</a>
            <a href="#">Mẫu Xe</a>
            <a href="#">Đặt Hẹn Lái Thử</a>
            <a href="#">Hệ Thống Phân Phối</a>
            <a href="#">Tìm Hiểu Thêm BMW</a>
        </div>
        <div class="navbar-right">
            <span>ENG</span>
            <span>🛒</span>
            <span>📍</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# ==== Tiêu đề chính ====
st.markdown("""
    <div style="text-align:center; padding:30px 0 10px;">
        <h1 style="font-size:3.5em; color:#FF4B4B;">🚘 Premium Car Showroom</h1>
        <p style="font-size:1.3em; color:gray;">Choose your next ride with style!</p>
    </div>
    <hr style="border:1px solid #eee;">
""", unsafe_allow_html=True)

# ==== Dữ liệu các dòng xe ====
cars = [
    {
        "id": 1,
        "name": "Lamborghini Aventador",
        "price": 300000,
        "image": "https://cafefcdn.com/203337114487263232/2023/7/20/lambor-1689840945762-16898409458521341482549.jpg",
        "desc": "V12 engine, aggressive design, supercar class."
    },
    {
        "id": 2,
        "name": "Tesla Model 3",
        "price": 48000,
        "image": "https://www.electrive.com/media/2025/01/tesla-model-y-facelift-supercharger-ladestation-charging-station-2025-04.jpg.webp",
        "desc": "Electric, autopilot, budget-friendly luxury."
    },
    {
        "id": 3,
        "name": "BMW M4",
        "price": 90000,
        "image": "https://images.netdirector.co.uk/gforces-auto/image/upload/q_auto,c_fill,f_auto,fl_lossy,w_1600,h_727/auto-titan/1e152d896f300c6721210deaa02ed215/di23_000189521.jpg",
        "desc": "Sporty coupe, high performance, German engineering."
    }
]

# ==== Layout: trái (sản phẩm) - phải (giỏ hàng) ====
left, right = st.columns([2.5, 1])

# ==== CỘT TRÁI: Sản phẩm ====
with left:
    st.markdown("""
        <h2 style="color:#2E86C1; font-weight:700;">🏎️ Cars for Sale</h2>
    """, unsafe_allow_html=True)

    for car in cars:
        with st.container(border=False):
            st.markdown(f"""
                <div style="background-color:#f9f9f9; padding:20px; margin-bottom:25px; border-radius:15px; box-shadow: 0px 4px 10px rgba(0,0,0,0.05);">
                    <img src="{car['image']}" style="width:100%; border-radius:10px;"/>
                    <h3 style="margin-top:15px;">{car['name']}</h3>
                    <p style="color:#888;">{car['desc']}</p>
                    <p style="font-weight:bold; color:#27AE60;">💰 Price: ${car['price']:,}</p>
                </div>
            """, unsafe_allow_html=True)

            if st.button(f"➕ Add to Cart: {car['name']}", key=f"add_{car['id']}"):
                st.session_state.cart.append(car)
                st.success(f"{car['name']} added to cart!")

# ==== CỘT PHẢI: Giỏ hàng ====
with right:
    st.subheader("🛒 Your Cart")
    total = 0
    if st.session_state.cart:
        for item in st.session_state.cart:
            st.write(f"• {item['name']} - ${item['price']:,}")
            total += item['price']
        st.markdown(f"**🧾 Total: ${total:,}**")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("❌ Clear Cart"):
                st.session_state.cart = []
                st.info("Cart cleared!")
        with col2:
            if st.button("✅ Checkout"):
                st.success("🎉 Purchase successful! Thank you.")
                st.balloons()
                st.session_state.cart = []
    else:
        st.info("Your cart is empty.")
