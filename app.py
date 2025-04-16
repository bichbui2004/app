import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Trực quan hóa dân số thế giới")
st.markdown("Nguồn dữ liệu từ World Bank")

# Đọc dữ liệu
url = "https://raw.githubusercontent.com/datasets/population/master/data/population.csv"
data = pd.read_csv(url)

# Lọc dữ liệu mới nhất (ví dụ: 2018)
year_selected = st.slider("Chọn năm", 1960, 2018, 2018)
data_year = data[data['Year'] == year_selected]

# Lọc top N quốc gia có dân số cao nhất
top_n = st.slider("Số quốc gia có dân số cao nhất", 5, 20, 10)
top_countries = data_year.sort_values(by='Value', ascending=False).head(top_n)

# Biểu đồ
fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(top_countries['Country Name'], top_countries['Value'], color='skyblue')
plt.xticks(rotation=45)
plt.title(f"Dân số {top_n} quốc gia đông dân nhất năm {year_selected}")
plt.ylabel("Dân số")
st.pyplot(fig)

# Hiển thị dữ liệu thô nếu muốn
if st.checkbox("Hiển thị dữ liệu chi tiết"):
    st.dataframe(top_countries)