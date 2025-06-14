import streamlit as st

# Cấu hình trang
st.set_page_config(page_title="Car Shop", page_icon="🚗", layout="wide")

# Tạo giỏ hàng bằng session state
if "cart" not in st.session_state:
    st.session_state.cart = []

# Danh sách xe với ảnh từ internet (link an toàn, minh họa)
cars = [
    {
        "id": 1,
        "name": "Lamborghini Huracan",
        "price": 250000,
        "image": "https://cdn.motor1.com/images/mgl/BE22b/s1/lamborghini-huracan-tecnica.jpg",
        "desc": "V10 engine, 0-100km/h in 2.9s. Iconic and aggressive."
    },
    {
        "id": 2,
        "name": "Tesla Model S Plaid",
        "price": 135000,
        "image": "https://tesla-cdn.thron.com/delivery/public/image/tesla/342c3173-f6fd-4c7e-b99f-d4a31fdf2a3f/bvlatuR/std/2880x1800/MS-Interior-Grid-A-Desktop",
        "desc": "Electric, 0-100km/h in 1.99s. Autopilot. Futuristic."
    },
    {
        "id": 3,
        "name": "Mercedes-Benz S-Class",
        "price": 120000,
        "image": "https://www.mercedes-benz.com/en/vehicles/passenger-cars/s-class/_jcr_content/image/MQ6-12-image-20230705115110/01-mercedes-benz-vehicles-s-class-v223-2023-3400x1440.jpeg",
        "desc": "Luxury sedan, world-class tech & comfort."
    }
]

# Tiêu đề
st.markdown("<h1 style='text-align:center;'>🚗 Luxury Car Showroom</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center; color:gray;'>Buy your dream car – fast, safe, modern</h4>", unsafe_allow_html=True)
st.markdown("---")

# Giao diện chia cột: Trái (sản phẩm), Phải (giỏ hàng)
left_col, right_col = st.columns([2, 1])

# 👉 CỘT TRÁI: DANH SÁCH XE
with left_col:
    st.subheader("🏎️ Available Cars")
    for car in cars:
        with st.container(border=True):
            st.image(car["image"], use_column_width=True)
            st.markdown(f"### {car['name']}")
            st.write(f"💰 Price: **${car['price']:,}**")
            st.caption(car["desc"])
            if st.button("➕ Add to Cart", key=f"add_{car['id']}"):
                st.session_state.cart.append(car)
                st.success(f"{car['name']} added to cart!")

# 🛒 CỘT PHẢI: GIỎ HÀNG & THANH TOÁN
with right_col:
    st.subheader("🛒 Your Cart")
    total = 0
    if st.session_state.cart:
        for idx, item in enumerate(st.session_state.cart):
            st.write(f"• {item['name']} - ${item['price']:,}")
            total += item['price']
        st.markdown(f"**🧾 Total: ${total:,}**")
        
        # Nút xoá giỏ hàng
        if st.button("❌ Clear Cart"):
            st.session_state.cart = []
            st.info("Cart cleared.")

        # Nút mua hàng
        if st.button("✅ Checkout"):
            st.success("🎉 Purchase successful! Thank you.")
            st.balloons()
            st.session_state.cart = []
    else:
        st.info("Your cart is empty.")
