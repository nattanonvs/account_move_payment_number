## Usage Guide — autoinfo_account_move_link_payment_number (Odoo 15)

### ภาพรวมการทำงาน
โมดูลนี้แสดงฟิลด์ `Payment Number` บนเอกสาร Vendor Bill เพื่อให้เห็นเลขที่เอกสาร Payment ที่ถูก reconcile เข้ากับ Bill นั้น ๆ

ค่าที่แสดง:
- ว่าง (empty) หากยังไม่มีการ reconcile payment กับ bill
- เป็นรายการเลขที่ Payment หลายรายการได้ โดยคั่นด้วย `, `

### ผู้ใช้ทั่วไป (Basic User)
#### เป้าหมาย
- ตรวจสอบว่า Bill ใดถูกจ่ายด้วย Payment ใบไหน

#### ขั้นตอนใช้งาน
1. ไปที่ Accounting → Vendors → Bills (Vendor Bills)
2. เปิดเอกสาร Bill ที่ต้องการตรวจสอบ
3. ดูฟิลด์ `Payment Number`

### ผู้ใช้ระดับกลาง (Accounting User)
#### Flow แนะนำ (ตรวจสอบสถานะการจ่าย)
1. เปิด Vendor Bills แบบรายการ (list)
2. ใช้ช่องค้นหา/กรองตาม vendor, วันที่, due date
3. เปิด Bill ที่ต้องการ และตรวจสอบ `Payment Number`
4. หาก `Payment Number` ว่าง ให้ตรวจสอบว่า Payment ถูกโพสต์และ reconcile แล้วหรือไม่

### ผู้ดูแลระบบ (Administrator)
#### ตรวจสอบว่าฟิลด์แสดงเฉพาะ Vendor Bills
- ในหน้ารายการ/หน้าฟอร์มของ Customer Invoices จะไม่แสดง `Payment Number` (โมดูลตั้งค่าให้ซ่อนตาม move type)

#### ปิดใช้งานชั่วคราว (ไม่ถอนโมดูล)
กรณีต้องการ “หยุดใช้งานชั่วคราว” แต่ไม่ uninstall:
1. เปิด Developer Mode
2. ไปที่ Settings → Technical → User Interface → Views
3. ค้นหา view ที่ชื่อใกล้เคียง:
   - `account.move.vendor.bill.payment.number`
   - `account.move.vendor.bill.tree.payment.number`
4. ปิดการใช้งาน (archive) view record ทั้ง 2 รายการ
5. Refresh หน้าจอ Vendor Bills

### Credits

Development Team: The Auto-Info Co., Ltd. : Dev Team / Mr. Nattanon Vinyangkoon – Project conception, implementation, and thorough review of all deliverables.
AI Coding Assistant: TRAE SOLO / MICROSOFT 365 COPILOT - Utilized to support code generation and productivity improvements under human oversight (e.g., suggesting code snippets and optimizations).

