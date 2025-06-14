import streamlit as st

# Cấu hình trang
st.set_page_config(page_title="Car Showroom", layout="wide")

# Tạo session lưu giỏ hàng
if "cart" not in st.session_state:
    st.session_state.cart = []

# Dữ liệu xe (ảnh từ Unsplash - chắc chắn chạy được)
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
