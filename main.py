import streamlit as st

# Cấu hình trang
st.set_page_config(page_title="Car Showroom", page_icon="🚘", layout="wide")

# Tạo session lưu giỏ hàng
if "cart" not in st.session_state:
    st.session_state.cart = []

# Dữ liệu xe (ảnh từ Unsplash - chắc chắn chạy được)
cars = [
    {
        "id": 1,
        "name": "Lamborghini Aventador",
        "price": 300000,
        "image": "https://images.unsplash.com/photo-1616352119484-0c3a3bd1269d",
        "desc": "V12 engine, aggressive design, supercar class."
    },
    {
        "id": 2,
        "name": "Tesla Model 3",
        "price": 48000,
        "image": "https://images.unsplash.com/photo-1603791440384-56cd371ee9a7",
        "desc": "Electric, autopilot, budget-friendly luxury."
    },
    {
        "id": 3,
        "name": "BMW M4",
        "price": 90000,
        "image": "https://images.unsplash.com/photo-1619025082454-2b9a7fe55bd2",
        "desc": "Sporty coupe, high performance, German engineering."
    }
]

# Tiêu đề
st.markdown("<h1 style='text-align:center;'>🚘 Premium Car Showroom</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center; color:gray;'>Choose your next ride!</h4>", unsafe_allow_html=True)
st.markdown("---")

# Layout: trái (sản phẩm) - phải (giỏ hàng)
left, right = st.columns([2, 1])

# CỘT TRÁI: Danh sách sản phẩm
with left:
    st.subheader("🏎️ Cars for Sale")
    for car in cars:
        with st.container(border=True):
            st.image(car["image"], use_column_width=True)
            st.markdown(f"### {car['name']}")
            st.write(f"💰 **Price**: ${car['price']:,}")
            st.caption(car["desc"])
            if st.button("➕ Add to Cart", key=f"add_{car['id']}"):
                st.session_state.cart.append(car)
                st.success(f"{car['name']} added to cart!")

# CỘT PHẢI: Giỏ hàng
with right:
    st.subheader("🛒 Your Cart")
    total = 0
    if st.session_state.cart:
        for item in st.session_state.cart:
            st.write(f"• {item['name']} - ${item['price']:,}")
            total += item['price']
        st.markdown(f"**🧾 Total: ${total:,}**")
        
        # Xoá giỏ hàng
        if st.button("❌ Clear Cart"):
            st.session_state.cart = []
            st.info("Cart cleared!")

        # Mua hàng
        if st.button("✅ Checkout"):
            st.success("🎉 Purchase successful! Thank you.")
            st.balloons()
            st.session_state.cart = []
    else:
        st.info("Your cart is empty.")
