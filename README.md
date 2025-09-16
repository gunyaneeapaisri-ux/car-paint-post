# 🚗 Car Paint Caption Generator

เว็บแอปฟรีสำหรับอู่ซ่อมสีรถ ใช้งานง่าย:  
- อัพโหลดรูป BEFORE และ AFTER  
- อัพโหลดไฟล์ลายน้ำ (PNG)  
- กรอกยี่ห้อรถ, สี, รายละเอียดก่อน-หลัง  
- ระบบจะรวมรูป + ใส่วอเตอร์มาร์ก + สร้างแคปชันอัตโนมัติ  
- ดาวน์โหลดรูปที่เสร็จแล้ว พร้อม copy แคปชันไปโพสต์ Facebook ได้ทันที  

## วิธี Deploy บน Streamlit Cloud
1. สมัครหรือเข้าสู่ระบบที่ [Streamlit Cloud](https://share.streamlit.io)  
2. สร้างโปรเจกต์ใหม่ → เลือก repo GitHub ที่มีไฟล์ `app.py`, `requirements.txt`  
3. กด Deploy → จะได้ URL เช่น `https://carpaint.streamlit.app`  
4. แชร์ลิงก์ให้ทีมงานเข้าใช้งานได้เลย 🚀  

## วิธี Deploy บน Hugging Face Spaces
1. สมัครที่ [Hugging Face](https://huggingface.co)  
2. ไปที่ **Spaces** → Create New Space  
3. เลือก SDK = Streamlit  
4. อัพโหลดไฟล์ `app.py`, `requirements.txt` และ `README.md`  
5. ระบบจะ build อัตโนมัติ → พร้อมใช้งานทันที  
