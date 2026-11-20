import streamlit as st

# Cấu hình trang
st.set_page_config(
    page_title="Biểu mẫu Khảo sát", page_icon="📝", layout="centered"
)

st.title("📝 Khảo sát người nhà.")
st.write("Vui lòng điền thông tin dưới đây để hoàn thành khảo sát.")

# Biểu mẫu nhập liệu
with st.form("survey_form", clear_on_submit=True):
  ho_ten = st.text_input("1. Họ và tên của bạn (*):")

  do_tuoi = st.selectbox(
      "2. Nhóm tuổi của bạn:",
      ["Dưới 18", "18 - 24", "25 - 34", "35 - 44", "Trên 45"],
  )

  muc_do_hai_long = st.radio(
      "3. Bạn đánh giá chất lượng dịch vụ thế nào?",
      ["Rất hài lòng", "Hài lòng", "Bình thường", "Không hài lòng"],
      horizontal=True,
  )

  tinh_nang = st.multiselect(
      "4. Bạn quan tâm đến tính năng nào nhất? (Chọn nhiều)",
      ["Tốc độ xử lý", "Giao diện đẹp"],
  )

  gop_y = st.text_area("5. Góp ý thêm của bạn:")

  submitted = st.form_submit_button("Gửi khảo sát")

# Xử lý và hiển thị kết quả ngay lập tức (không lưu trữ)
if submitted:
  if not ho_ten.strip():
    st.error("⚠️ Vui lòng nhập Họ và tên trước khi gửi!")
  else:
    st.success("✅ Cảm ơn bạn đã hoàn thành khảo sát!")

    with st.container(border=True):
      st.subheader("📋 Tóm tắt câu trả lời của bạn")
      st.write(f"- **Họ và tên:** {ho_ten}")
      st.write(f"- **Nhóm tuổi:** {do_tuoi}")
      st.write(f"- **Đánh giá:** {muc_do_hai_long}")
      st.write(
          "- **Tính năng quan tâm:**"
          f" {', '.join(tinh_nang) if tinh_nang else 'Không chọn'}"
      )
      st.write(f"- **Góp ý:** {gop_y if gop_y.strip() else 'Không có'}")
