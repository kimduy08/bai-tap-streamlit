import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Cau hinh trang web
st.set_page_config(
    page_title="Quan ly diem sinh vien",
    page_icon="📚",
    layout="wide"
)

# 2. Tieu de
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

st.write(
    "Ứng dụng quản lý điểm của 10 sinh viên "
    "bằng Python, Pandas và Streamlit."
)

# 3. Tao du lieu
data = {
    "Ho_ten": [
        "An", "Binh", "Chi", "Dung", "Ha",
        "Lan", "Minh", "Nam", "Phuc", "Trang"
    ],
    "Chuyen_can": [
        8.0, 9.0, 7.0, 9.5, 8.0,
        7.5, 9.0, 8.0, 8.5, 9.5
    ],
    "Giua_ky": [
        7.0, 8.5, 6.5, 9.0, 7.5,
        6.0, 8.0, 7.5, 8.0, 9.0
    ],
    "Cuoi_ky": [
        7.5, 8.0, 6.0, 9.5, 7.0,
        6.5, 8.5, 7.0, 7.5, 9.0
    ]
}

df = pd.DataFrame(data)

# 4. Tinh diem tong ket
df["Tong_ket"] = (
    0.2 * df["Chuyen_can"]
    + 0.3 * df["Giua_ky"]
    + 0.5 * df["Cuoi_ky"]
).round(2)

# 5. Xep loai
def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7.0:
        return "Khá"
    elif diem >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"

df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

# 6. Hien thi bang diem
st.header("1. Bảng điểm sinh viên")

bang_diem = df.rename(columns={
    "Ho_ten": "Họ tên",
    "Chuyen_can": "Chuyên cần",
    "Giua_ky": "Giữa kỳ",
    "Cuoi_ky": "Cuối kỳ",
    "Tong_ket": "Tổng kết",
    "Xep_loai": "Xếp loại"
})

st.dataframe(bang_diem, use_container_width=True)

# 7. Thong ke
st.header("2. Thống kê kết quả")

diem_tb = df["Tong_ket"].mean()
sv_max = df.loc[df["Tong_ket"].idxmax()]
sv_min = df.loc[df["Tong_ket"].idxmin()]
so_sv_dat = (df["Tong_ket"] >= 5).sum()

col1, col2 = st.columns(2)

with col1:
    st.metric("Điểm trung bình lớp", f"{diem_tb:.2f}")
    st.metric("Số sinh viên đạt", int(so_sv_dat))

with col2:
    st.write(
        f"**Điểm cao nhất:** {sv_max['Ho_ten']} "
        f"({sv_max['Tong_ket']:.2f})"
    )
    st.write(
        f"**Điểm thấp nhất:** {sv_min['Ho_ten']} "
        f"({sv_min['Tong_ket']:.2f})"
    )

# 8. Chon sinh vien
st.header("3. Tra cứu sinh viên")

ten_sv = st.selectbox(
    "Chọn một sinh viên:",
    df["Ho_ten"].tolist()
)

sv = df[df["Ho_ten"] == ten_sv].iloc[0]

st.subheader(f"Kết quả của sinh viên {ten_sv}")

col1, col2, col3 = st.columns(3)

col1.metric("Chuyên cần", f"{sv['Chuyen_can']:.1f}")
col2.metric("Giữa kỳ", f"{sv['Giua_ky']:.1f}")
col3.metric("Cuối kỳ", f"{sv['Cuoi_ky']:.1f}")

st.write(f"**Điểm tổng kết:** {sv['Tong_ket']:.2f}")
st.write(f"**Xếp loại:** {sv['Xep_loai']}")

# 9. Ve bieu do
st.header("4. Biểu đồ điểm tổng kết")

fig, ax = plt.subplots(figsize=(10, 5))

ax.bar(df["Ho_ten"], df["Tong_ket"])
ax.set_title("Điểm tổng kết của 10 sinh viên")
ax.set_xlabel("Họ tên sinh viên")
ax.set_ylabel("Điểm tổng kết")
ax.set_ylim(0, 10)

plt.tight_layout()
st.pyplot(fig)
plt.close(fig)

# 10. Thong tin nguoi tao
st.divider()
st.caption("Châu Kim Duy")
st.caption("Họ và tên: [Châu Kim Duy]")
st.caption("MSSV: [052208012882]")
