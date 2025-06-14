import streamlit as st

# Cấu hình trang
st.set_page_config(page_title="Car Shop", page_icon="🚗", layout="wide")

# CSS tuỳ chỉnh cho giao diện đẹp
st.markdown("""
    <style>
    .title {
        text-align: center;
        font-size: 48px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .subtitle {
        text-align: center;
        font-size: 20px;
        color: gray;
        margin-bottom: 40px;
    }
    .car-card {
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 0px 15px rgba(0,0,0,0.1);
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Tiêu đề trang
st.markdown('<div class="title">🚗 Premium Car Dealership</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Find your dream car with ease and style</div>', unsafe_allow_html=True)

# Dữ liệu xe (không có ảnh)
cars = [
    {
        "name": "Lamborghini Huracan",
        "price": "$250,000",
        "desc": "V10 engine, 0-100km/h in 2.9s, aggressive and iconic design."
    },
    {
        "name": "Tesla Model S Plaid",
        "price": "$135,000",
        "desc": "Electric, 0-100km/h in 1.99s, autopilot, luxury interior."
    },
    {
        "name": "Mercedes-Benz S-Class",
        "price": "$120,000",
        "desc": "Luxury sedan, advanced tech, unmatched comfort."
    }
]

# Hiển thị danh sách xe theo cột
cols = st.columns(3)
for i, car in enumerate(cars):
    with cols[i]:
        st.markdown('<div class="car-card">', unsafe_allow_html=True)
        st.subheader(car["name"])
        st.write(f"💰 **Price**: {car['price']}")
        if st.button("🔍 View Details", key=f"btn{i}"):
            st.info(f"📌 {car['desc']}")
        st.markdown('</div>', unsafe_allow_html=True)
