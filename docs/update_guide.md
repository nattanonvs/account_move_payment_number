## Update Guide — autoinfo_account_move_link_payment_number (Odoo 15)

### แนวทางอัปเดตเวอร์ชัน (แนะนำ)
1. สำรองข้อมูลฐานข้อมูล (DB backup) ก่อนทุกครั้ง
2. วางโฟลเดอร์โมดูลเวอร์ชันใหม่ทับของเดิมใน `C:\odoo\APPreadytouse`
3. Restart Odoo server
4. เปิด Odoo → Apps → Update Apps List
5. ค้นหา `Vendor Bill Payment Number` แล้วกด Upgrade

### อัปเดตผ่านคำสั่ง (ทางเลือก)
- `-u autoinfo_account_move_link_payment_number`

### Timeline & Change Log

#### 15.0.1.0.0
- เริ่มต้นโมดูล: เพิ่มฟิลด์คำนวณ `payment_number` บน `account.move`
- เพิ่ม view เพื่อแสดงฟิลด์ในหน้าฟอร์มและรายการ

#### 15.0.1.0.1
- เพิ่มเอกสารพื้นฐาน (README/INSTALL)
- เพิ่ม Credits
- ปรับชื่อ repo และชื่อ technical name ของโมดูลเป็น `autoinfo_account_move_link_payment_number`

#### 15.0.1.1.0
- ปรับโครงสร้างโมดูลให้พร้อมใช้งานแบบแยกติดตั้ง/ถอนการติดตั้งได้โดยไม่กระทบโมดูลหลัก
- เพิ่มเอกสารแบบแยกไฟล์ในโฟลเดอร์ `docs/` ครบหัวข้อ
- เพิ่ม tests ขั้นพื้นฐานสำหรับตรวจสอบว่าโมดูลโหลดได้และ view/field พร้อมใช้งาน
- จำกัดการแสดงผลฟิลด์ `Payment Number` ให้โฟกัสเฉพาะ Vendor Bills (ลดผลกระทบกับ flow อื่น)

### Credits

Development Team: The Auto-Info Co., Ltd. : Dev Team / Mr. Nattanon Vinyangkoon – Project conception, implementation, and thorough review of all deliverables.
AI Coding Assistant: TRAE SOLO / MICROSOFT 365 COPILOT - Utilized to support code generation and productivity improvements under human oversight (e.g., suggesting code snippets and optimizations).

