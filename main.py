import streamlit as st

# Cấu hình trang
st.set_page_config(page_title="Premium Car Showroom", layout="wide")

# Khởi tạo giỏ hàng nếu chưa có
if "cart" not in st.session_state:
    st.session_state.cart = []

# Dữ liệu xe
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

# Header hiện đại
st.markdown("""
    <div style='text-align:center;'>
        <h1 style='font-size:48px;'>🚘 <span style="color:#2c3e50">Premium Car Showroom</span></h1>
        <p style='font-size:20px; color:gray;'>Choose your next ride in style!</p>
    </div>
    <hr style='border:1px solid #ccc;'/>
""", unsafe_allow_html=True)

# Layout chính: trái - phải
left, right = st.columns([2, 1])

# Cột trái: Danh sách xe
with left:
    st.markdown("<h2 style='color:#e74c3c;'>🏎️ Cars for Sale</h2>", unsafe_allow_html=True)
    for car in cars:
        with st.container(border=True):
            st.image(car["image"], use_container_width=True)
            st.markdown(f"<h4>{car['name']}</h4>", unsafe_allow_html=True)
            st.markdown(f"<b>💰 Price:</b> ${car['price']:,}")
            st.caption(car["desc"])
            if st.button("➕ Add to Cart", key=f"add_{car['id']}"):
                st.session_state.cart.append(car)
                st.success(f"{car['name']} added to cart!")

# Cột phải: Giỏ hàng
with right:
    st.markdown("<h3>🛒 Your Cart</h3>", unsafe_allow_html=True)
    total = 0
    if st.session_state.cart:
        for item in st.session_state.cart:
            st.write(f"• {item['name']} - ${item['price']:,}")
            total += item['price']
        st.markdown(f"<b>🧾 Total: ${total:,}</b>", unsafe_allow_html=True)
        if st.button("✅ Checkout"):
            st.success("🎉 Purchase successful! Thank you.")
            st.balloons()
            st.session_state.cart = []
        if st.button("❌ Clear Cart"):
            st.session_state.cart = []
            st.info("Cart cleared!")
    else:
        st.info("Your cart is empty.")

# FOOTER
st.markdown("---")
st.markdown("""
    <div style="background-color:#2c3e50;padding:40px;color:white;border-radius:10px;margin-top:30px;">
        <div style="display:flex;justify-content:space-between;flex-wrap:wrap;">
            <div>
                <h3 style="color:white;">Motorist</h3>
                <p>Câu Chuyện Thương Hiệu<br/>Công Việc<br/>Liên Hệ Chúng Tôi<br/>Cảm Nhận</p>
            </div>
            <div>
                <h3 style="color:white;">Dịch Vụ</h3>
                <p>Bán Xe<br/>Thẩm Định Xe</p>
            </div>
            <div>
                <h3 style="color:white;">Liên Hệ</h3>
                <p>📍 Căn D-00.03, Tầng 3, Số 02 Đường Số 13, TP. Thủ Đức<br/>
                🕒 10:00 - 18:00 (cả ngày lễ)<br/>
                📞 02873080018<br/>
                📧 enquiry@motorist.vn</p>
            </div>
            <div>
                <h3 style="color:white;">Đăng Ký Nhận Tin</h3>
                <input type="text" placeholder="Email của bạn" style="padding:8px;border:none;border-radius:5px;width:200px;">
                <button style="padding:8px;background-color:#27ae60;color:white;border:none;border-radius:5px;margin-left:5px;">Đăng ký</button>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)
