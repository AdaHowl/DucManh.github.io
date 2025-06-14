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
        "image": "https://cafefcdn.com/203337114487263232/2023/7/20/lambor-1689840945762-16898409458521341482549.jpg",
        "desc": "V12 engine, aggressive design, supercar class."
    },
    {
        "id": 2,
        "name": "Tesla Model 3",
        "price": 48000,
        "image": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fdantri.com.vn%2Fo-to-xe-may%2Ftop-10-xe-moi-dat-nhat-the-gioi-hien-nay-20221005154110406.htm&psig=AOvVaw1oNjTyRx2Ae_zTW8cWfp38&ust=1749966595599000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCJiBo-Cb8I0DFQAAAAAdAAAAABAL",
        "desc": "Electric, autopilot, budget-friendly luxury."
    },
    {
        "id": 3,
        "name": "BMW M4",
        "price": 90000,
        "image": "https://www.google.com/imgres?q=xe&imgurl=https%3A%2F%2Ftapchi.toyota.com.vn%2Fuploads%2Fimages%2Fcac-dong-xe-toyota-16.png&imgrefurl=https%3A%2F%2Ftapchi.toyota.com.vn%2Fvi%2Ftin-tuc%2F228%2Fcac-dong-xe-toyota&docid=sFWpKsuoDzjc7M&tbnid=zyqjYxiBRIExSM&vet=12ahUKEwjgqYPbm_CNAxUPnK8BHXhwAMEQM3oECEAQAA..i&w=1218&h=1015&hcb=2&ved=2ahUKEwjgqYPbm_CNAxUPnK8BHXhwAMEQM3oECEAQAA",
        "desc": "Sporty coupe, high performance, German engineering."
    }
]

# Tiêu đề
st.markdown("<h1 style='text-align:center;'>🚘 Premium Car Showroom</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center; color:gray;'>Choose your next ride!</h4>", unsafe_allow_html=True)
st.markdown("---")
 "image": "https://www.google.com/imgres?q=xe&imgurl=https%3A%2F%2Fimg.docnhanh.vn%2Fimages%2Fuploads%2F2023%2F01%2F02%2Fanh-1-1270.jpg&imgrefurl=https%3A%2F%2Fdocnhanh.vn%2Fo-to-xe-may%2Fnhung-mau-sieu-xe-xe-the-thao-lan-dau-ve-viet-nam-trong-nam-2022-tintuc857860&docid=KqyiMw8fV2jR6M&tbnid=HxDVYmjoOjCZqM&vet=12ahUKEwjgqYPbm_CNAxUPnK8BHXhwAMEQM3oECGkQAA..i&w=2048&h=1365&hcb=2&ved=2ahUKEwjgqYPbm_CNAxUPnK8BHXhwAMEQM3oECGkQAA",
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
