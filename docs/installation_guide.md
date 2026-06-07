## Installation Guide — autoinfo_account_move_link_payment_number (Odoo 15)

### Prerequisites
- Odoo 15
- ต้องติดตั้งโมดูล `account` ก่อน
- ต้องวางโฟลเดอร์โมดูลไว้ใน addons path ของระบบ
  - สำหรับเครื่องนี้กำหนดศูนย์กลางไว้ที่ `C:\odoo\APPreadytouse`

### Install (ผ่านหน้า Odoo)
1. วางโฟลเดอร์โมดูล `autoinfo_account_move_link_payment_number` ไว้ใน `C:\odoo\APPreadytouse`
2. ตรวจสอบไฟล์ config ของ Odoo ว่ามี `C:\odoo\APPreadytouse` อยู่ใน `addons_path`
3. Restart Odoo service / odoo server
4. เปิด Odoo → Apps
5. เปิด Developer Mode (ถ้ายังไม่เปิด)
6. กด “Update Apps List”
7. ค้นหา `Vendor Bill Payment Number` แล้วกด Install

### Install/Upgrade (ผ่านคำสั่ง)
- Install:
  - `-i autoinfo_account_move_link_payment_number`
- Upgrade:
  - `-u autoinfo_account_move_link_payment_number`

### Post-install checklist
- เปิด Vendor Bills → เปิดเอกสาร Bill ใด ๆ
- ตรวจสอบว่ามีฟิลด์ `Payment Number` แสดงในหน้า Bill (เฉพาะฝั่ง Vendor Bills)

### Credits

Development Team: The Auto-Info Co., Ltd. : Dev Team / Mr. Nattanon Vinyangkoon – Project conception, implementation, and thorough review of all deliverables.
AI Coding Assistant: TRAE SOLO / MICROSOFT 365 COPILOT - Utilized to support code generation and productivity improvements under human oversight (e.g., suggesting code snippets and optimizations).

