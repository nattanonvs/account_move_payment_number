## Configuration Guide — autoinfo_account_move_link_payment_number (Odoo 15)

### ค่าตั้งค่า (Parameters/Settings)
โมดูลนี้ไม่มีหน้า setting และไม่มี `ir.config_parameter` ใด ๆ

### แนวทางตั้งค่า/ปรับแต่ง (Best Practices)
- ถ้าต้องการเปลี่ยนตำแหน่งการแสดงผลฟิลด์ `Payment Number`
  - แนะนำสร้างโมดูลเสริมอีกตัว (autoinfo_addon) เพื่อ inherit view อีกชั้น
  - หลีกเลี่ยงการแก้ไขไฟล์ในโมดูลนี้โดยตรงบน production

### การจำกัดสิทธิ์การมองเห็น (Optional)
หากต้องการให้เฉพาะกลุ่มบัญชีเห็นฟิลด์:
1. สร้างโมดูลเสริมและ inherit view เดิม
2. ใส่ `groups="account.group_account_user"` หรือกลุ่มที่ต้องการใน field ของ view

### Credits

Development Team: The Auto-Info Co., Ltd. : Dev Team / Mr. Nattanon Vinyangkoon – Project conception, implementation, and thorough review of all deliverables.
AI Coding Assistant: TRAE SOLO / MICROSOFT 365 COPILOT - Utilized to support code generation and productivity improvements under human oversight (e.g., suggesting code snippets and optimizations).

