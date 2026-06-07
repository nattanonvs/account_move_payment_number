## autoinfo_account_move_link_payment_number (Odoo 15)

โมดูลเพิ่มฟิลด์ `Payment Number` บน Vendor Bill (account.move) เพื่อแสดงเลขที่เอกสาร Payment ที่ถูก reconcile กับบิลนั้น ช่วยให้ทีมบัญชีตรวจสอบการจ่ายได้สะดวกขึ้นทั้งในหน้าฟอร์มและรายการบิล

### Dependencies
- account

### Documentation
- Installation: [installation_guide.md](docs/installation_guide.md)
- Uninstallation: [uninstallation_guide.md](docs/uninstallation_guide.md)
- Update/Changelog: [update_guide.md](docs/update_guide.md)
- Usage: [usage_guide.md](docs/usage_guide.md)
- Configuration: [configuration_guide.md](docs/configuration_guide.md)
- Troubleshooting: [troubleshooting.md](docs/troubleshooting.md)

### Usage (สรุป)
1. ไปที่ Vendor Bills
2. เปิดบิลที่มีการ Register Payment และ reconcile แล้ว
3. ระบบจะแสดงฟิลด์ `Payment Number` เป็นรายการเลขที่ Payment (คั่นด้วยเครื่องหมาย ,)

### Value (คุณค่าต่อธุรกิจ/การใช้งาน)
- ลดเวลาตรวจสอบการจ่ายเงินของ Vendor Bills (เห็นเลข Payment ที่ reconcile ได้ทันที)
- ช่วยลดความผิดพลาดจากการอ้างอิงเลขเอกสารผิด และช่วย trace การจ่ายในงานบัญชี

### Scope (ขอบเขตการเปลี่ยนแปลง)
- เป็นโมดูลเสริมเพียง 1 โมดูล ไม่แก้ไขโค้ดของโมดูลหลัก `account`
- สามารถติดตั้ง/ถอนการติดตั้งได้โดยไม่กระทบโมดูลหลัก (ยกเว้นการแสดงผลฟิลด์/วิวที่เพิ่มเข้ามา)

### Known Limitations
- แสดงเลข Payment ตาม `name` ของเอกสาร Payment และขึ้นกับการ reconcile
- หากใช้งาน flow การจ่ายที่ไม่ทำ reconcile กับ Vendor Bill โดยตรง อาจไม่แสดงค่า

### Credits

Development Team: The Auto-Info Co., Ltd. : Dev Team / Mr. Nattanon Vinyangkoon – Project conception, implementation, and thorough review of all deliverables.
AI Coding Assistant: TRAE SOLO / MICROSOFT 365 COPILOT - Utilized to support code generation and productivity improvements under human oversight (e.g., suggesting code snippets and optimizations).
