import streamlit as st

# Cấu hình trang
st.set_page_config(page_title="Car Showroom", layout="wide")

# Tạo session lưu giỏ hàng
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

# Tiêu đề hiện đại
st.markdown("""
    <div style='text-align:center;'>
        <h1 style='font-size:3.2em;'>🚘 <span style='color:#2c3e50;'>Premium Car Showroom</span></h1>
        <p style='font-size:1.2em; color:gray;'>Choose your next ride!</p>
    </div>
    <hr style='margin-top:20px;'>
""", unsafe_allow_html=True)

# Layout 2 cột
left, right = st.columns([2, 1])

# Cột trái: Danh sách sản phẩm
with left:
    st.markdown("<h2 style='margin-bottom:20px;'>🏎️ Cars for Sale</h2>", unsafe_allow_html=True)
    for car in cars:
        with st.container(border=True):
            st.image(car["image"], use_container_width=True)
            st.markdown(f"<h4 style='margin-top:10px;'>{car['name']}</h4>", unsafe_allow_html=True)
            st.write(f"💰 **Price**: ${car['price']:,}")
            st.caption(car["desc"])
            if st.button("➕ Add to Cart", key=f"add_{car['id']}"):
                st.session_state.cart.append(car)
                st.success(f"{car['name']} added to cart!")

# Cột phải: Giỏ hàng
with right:
    st.subheader("🛒 Your Cart")
    total = 0
    if st.session_state.cart:
        for item in st.session_state.cart:
            st.write(f"• {item['name']} - ${item['price']:,}")
            total += item['price']
        st.markdown(f"**🧾 Total: ${total:,}**")

        if st.button("❌ Clear Cart"):
            st.session_state.cart = []
            st.info("Cart cleared!")

        if st.button("✅ Checkout"):
            st.success("🎉 Purchase successful! Thank you.")
            st.balloons()
            st.session_state.cart = []
    else:
        st.info("Your cart is empty.")

# ==== FOOTER ====
st.markdown("""
<style>
.footer {
    background-color: #2c2c2c;
    color: white;
    padding: 40px 60px;
    border-top-left-radius: 60px;
    margin-top: 50px;
}
.footer h4 {
    margin-bottom: 15px;
    color: white;
}
.footer a, .footer p {
    color: #ccc;
    text-decoration: none;
    font-size: 14px;
}
.footer a:hover {
    color: white;
}
.footer-section {
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 40px;
}
.footer .subscribe {
    display: flex;
    margin-top: 10px;
}
.footer .subscribe input {
    padding: 8px 12px;
    border: none;
    border-radius: 5px 0 0 5px;
    outline: none;
}
.footer .subscribe button {
    background-color: #27ae60;
    border: none;
    color: white;
    padding: 8px 15px;
    border-radius: 0 5px 5px 0;
    cursor: pointer;
}
.footer .subscribe button:hover {
    background-color: #1e8449;
}
</style>

<div class="footer">
    <div class="footer-section">
        <div>
            <img src="https://upload.wikimedia.org/wikipedia/commons/4/4d/Motorist_logo_red_white_text.png" style="height:40px;">
            <p style="margin-top:10px;">CHO TÀI XẾ THÔNG MINH</p>
            <p>Việt Nam</p>
        </div>
        <div>
            <h4>Motorist</h4>
            <p><a href="#">Câu Chuyện Thương Hiệu</a></p>
            <p><a href="#">Công Việc</a></p>
            <p><a href="#">Liên Hệ Chúng Tôi</a></p>
            <p><a href="#">Cảm Nhận</a></p>
        </div>
        <div>
            <h4>Dịch Vụ</h4>
            <p><a href="#">Bán Xe</a></p>
            <p><a href="#">Thẩm Định Xe</a></p>
        </div>
        <div>
            <h4>Liên Hệ</h4>
            <p>📍 Căn D-00.03, Tầng 3, Số 02 Đường Số 13, Thủ Thiêm, TP. Thủ Đức, TP.HCM</p>
            <p>🕐 10:00am – 6:00pm (Đóng cửa ngày lễ)</p>
            <p>📞 02873080018</p>
            <p>📧 enquiry@motorist.vn</p>
        </div>
        <div>
            <h4>Đăng Ký Bản Tin</h4>
            <p>Hãy là người đầu tiên nhận ưu đãi & tin tức.</p>
            <div class="subscribe">
                <input type="email" placeholder="Email của bạn">
                <button>✈️</button>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
