## Troubleshooting — autoinfo_account_move_link_payment_number (Odoo 15)

### 1) ฟิลด์ Payment Number ว่าง ทั้งที่มีการจ่ายแล้ว
สาเหตุที่พบบ่อย:
- Payment ยังไม่ posted
- Payment posted แล้วแต่ยังไม่ reconcile กับ bill

แนวทางตรวจสอบ:
1. เปิด Vendor Bill
2. ตรวจสอบสถานะ (posted) และตรวจสอบรายการ payments ที่เกี่ยวข้อง
3. ตรวจสอบว่า Bill และ Payment ถูก reconcile กันจริง

### 2) แสดงเลข Payment หลายรายการ
เป็นพฤติกรรมปกติ หากมีการจ่ายหลายครั้ง/หลาย payment แล้ว reconcile กับ bill เดียวกัน

### 3) ไม่เห็นฟิลด์ใน Vendor Bills
แนวทางแก้:
1. ตรวจสอบว่าโมดูลติดตั้งแล้ว (Apps)
2. เปิด Developer Mode แล้วไปที่ Settings → Technical → User Interface → Views
3. ตรวจสอบว่า view ไม่ได้ถูก archive
4. ลอง Upgrade โมดูลอีกครั้ง แล้ว refresh หน้าจอ

### 4) ต้องการหยุดใช้งานชั่วคราว (ไม่ uninstall)
ทำตามขั้นตอนใน `docs/usage_guide.md` หัวข้อ “ปิดใช้งานชั่วคราว (ไม่ถอนโมดูล)”

### Known Limitations
- โมดูลนี้แสดง `name` ของ payment ตามที่ระบบสร้าง (เลขเอกสารของ payment) และขึ้นกับการ reconcile
- หากองค์กรใช้ flow จ่ายเงินแบบอื่นที่ไม่ reconcile กับ vendor bill โดยตรง ฟิลด์อาจไม่แสดงค่า

### Credits

Development Team: The Auto-Info Co., Ltd. : Dev Team / Mr. Nattanon Vinyangkoon – Project conception, implementation, and thorough review of all deliverables.
AI Coding Assistant: TRAE SOLO / MICROSOFT 365 COPILOT - Utilized to support code generation and productivity improvements under human oversight (e.g., suggesting code snippets and optimizations).

