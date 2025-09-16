import streamlit as st
from PIL import Image

st.set_page_config(page_title="Car Paint Caption Generator", page_icon="🚗")

st.title("🚗 ระบบสร้างภาพก่อน/หลังทำสี + แคปชันอัตโนมัติ")
st.write("อัพโหลดรูปก่อนทำสี + หลังทำสี พร้อมเลือกโลโก้ลายน้ำ ระบบจะรวมภาพ + ใส่วอเตอร์มาร์ก + สร้างแคปชันให้อัตโนมัติ")

before_file = st.file_uploader("📷 อัพโหลดรูป BEFORE", type=["jpg", "jpeg", "png"])
after_file = st.file_uploader("📷 อัพโหลดรูป AFTER", type=["jpg", "jpeg", "png"])
watermark_file = st.file_uploader("🖼️ อัพโหลดไฟล์ลายน้ำ (PNG พื้นหลังโปร่งใส)", type=["png"])
position = st.radio("ตำแหน่งลายน้ำ", ["ขวาล่าง", "ซ้ายล่าง"])

brand = st.text_input("🚘 ยี่ห้อรถ")
color = st.text_input("🎨 สีรถ")
before_text = st.text_area("✏️ รายละเอียด ก่อนทำสี")
after_text = st.text_area("✏️ รายละเอียด หลังทำสี")

if st.button("✨ สร้างรูป + แคปชัน"):
    if before_file and after_file and watermark_file:
        # เปิดรูป
        before_img = Image.open(before_file).convert("RGB")
        after_img = Image.open(after_file).convert("RGB")
        watermark = Image.open(watermark_file).convert("RGBA")

        # รวม before+after เป็นภาพคู่
        max_h = max(before_img.height, after_img.height)
        total_w = before_img.width + after_img.width
        combined = Image.new("RGB", (total_w, max_h), (255,255,255))
        combined.paste(before_img, (0,0))
        combined.paste(after_img, (before_img.width,0))

        # ใส่ watermark
        wm_scale = int(combined.width * 0.15)
        wm_ratio = watermark.width / watermark.height
        wm_resized = watermark.resize((wm_scale, int(wm_scale / wm_ratio)))

        pad = 20
        if position == "ขวาล่าง":
            pos = (combined.width - wm_resized.width - pad, combined.height - wm_resized.height - pad)
        else:
            pos = (pad, combined.height - wm_resized.height - pad)

        combined.paste(wm_resized, pos, wm_resized)

        st.image(combined, caption="✅ รูป AFTER ประมวลผลแล้ว", use_column_width=True)

        # ให้ดาวน์โหลด
        combined.save("final.jpg", format="JPEG")
        with open("final.jpg", "rb") as f:
            st.download_button("⬇️ ดาวน์โหลดรูป", f, file_name="car_result.jpg", mime="image/jpeg")

        # สร้างแคปชัน
        caption = f"""
🚗 {brand} — สี {color}
ก่อน: {before_text}
หลัง: {after_text}

สนใจสอบถามเพิ่มเติมได้ที่ 📲 0X-XXXX-XXXX
        """
        st.subheader("📋 แคปชันที่ได้:")
        st.code(caption, language="markdown")
    else:
        st.warning("กรุณาอัพโหลดรูปทั้ง BEFORE / AFTER และลายน้ำให้ครบก่อนค่ะ")
