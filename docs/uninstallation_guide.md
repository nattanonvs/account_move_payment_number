## Uninstallation Guide — autoinfo_account_move_link_payment_number (Odoo 15)

### Uninstall (ผ่านหน้า Odoo)
1. เปิด Odoo → Apps
2. ค้นหา `Vendor Bill Payment Number`
3. กด Uninstall
4. Restart Odoo server (แนะนำ)

### ข้อควรรู้
- โมดูลนี้เป็นโมดูลเสริม (addon) ที่ทำงานด้วยการ:
  - เพิ่มฟิลด์ใหม่บน `account.move`
  - เพิ่ม view inheritance เพื่อแสดงฟิลด์ใน Vendor Bills
- การถอนติดตั้งจะไม่แก้ไขโค้ดของโมดูลหลัก `account`
- ฟิลด์ `payment_number` จะถูกถอดออกจาก registry เมื่อถอนติดตั้ง

### ตรวจสอบหลังถอนติดตั้ง
- เปิด Vendor Bills → เปิดเอกสาร Bill
- ตรวจสอบว่าไม่เห็นฟิลด์ `Payment Number` แล้ว

### ลบไฟล์บน Server (ทางเลือก)
- หากต้องการลบโค้ดออกจากเครื่อง:
  - ลบโฟลเดอร์ `C:\odoo\APPreadytouse\autoinfo_account_move_link_payment_number`
  - จากนั้น Restart Odoo และกด “Update Apps List”

### Credits

Development Team: The Auto-Info Co., Ltd. : Dev Team / Mr. Nattanon Vinyangkoon – Project conception, implementation, and thorough review of all deliverables.
AI Coding Assistant: TRAE SOLO / MICROSOFT 365 COPILOT - Utilized to support code generation and productivity improvements under human oversight (e.g., suggesting code snippets and optimizations).

