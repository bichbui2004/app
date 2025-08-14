import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title và mô tả
st.title("Movie Data Visualization")
st.markdown("Trực quan hóa dữ liệu phim")

# Đọc dữ liệu từ URL
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/nv-thang/Data-Visualization-Course/main/Dataset%20for%20Practice/movies.csv"
    df = pd.read_csv(url)
    df.dropna(inplace=True)
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("Tuỳ chọn hiển thị")
genre_options = df['genre'].unique()
selected_genres = st.sidebar.multiselect("Chọn thể loại phim:", genre_options, default=genre_options)

year_min = int(df['year'].min())
year_max = int(df['year'].max())
selected_year_range = st.sidebar.slider("Chọn khoảng năm sản xuất:", year_min, year_max, (year_min, year_max))

chart_type = st.sidebar.selectbox("Chọn loại biểu đồ:", ["Bar Chart", "Pie Chart", "Histogram"])

# Filter dữ liệu
filtered_df = df[(df['genre'].isin(selected_genres)) & (df['year'].between(*selected_year_range))]

# Hiển thị dữ liệu lọc
st.subheader("Dữ liệu đã lọc")
st.write(filtered_df.head())

# Vẽ biểu đồ
if chart_type == "Bar Chart":
    avg_budget = filtered_df.groupby('genre')['budget'].mean().round().reset_index()
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(avg_budget['genre'], avg_budget['budget'], color='skyblue')
    ax.set_xlabel("Thể loại")
    ax.set_ylabel("Ngân sách trung bình")
    ax.set_title("Ngân sách trung bình theo thể loại")
    st.pyplot(fig)

elif chart_type == "Pie Chart":
    genre_counts = filtered_df['genre'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(genre_counts, labels=genre_counts.index, autopct='%1.1f%%', startangle=90)
    ax.set_title("Tỷ lệ thể loại phim")
    st.pyplot(fig)

elif chart_type == "Histogram":
    fig, ax = plt.subplots()
    ax.hist(filtered_df['budget'], bins=20, color='coral', edgecolor='black')
    ax.set_xlabel("Ngân sách")
    ax.set_ylabel("Số lượng phim")
    ax.set_title("Phân bố ngân sách phim")
    st.pyplot(fig)
