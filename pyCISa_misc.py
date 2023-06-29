import webbrowser
from tkinter import messagebox

def openweb():
    webbrowser.open('http://servcis.pwa.co.th:8001/CISSupport/AuditReport')


def credit():
    messagebox.showinfo(title='ผู้พัฒนา',message='นายชัชพล นุโยค\nนายเอกพจน์ ศักดิ์เรืองฤทธิ์\nนายศิริชัย แก่นไชย\nVersion 2.00 วันที่ xx xxxx 2566')
    
table_neme=('1. ผู้ใช้น้ำทั้งหมด',
            '2. การรับเงินค่าติดตั้ง',
            '3. การรับเงินรายได้ค่าน้ำ',
            '4. รายได้อื่น ๆ',
            '_4.1 เกียวกับผู้ใช้น้ำ',
            '_4.2 ไม่เกี่ยวกับผู้ใช้น้ำ',
            '5. ฝากมาตรครบกำหนด',
            '6. ทะเบียนคุมน้ำท่อธาร',
            '7. ตั้งหนี้ประจำเดือน',
            '_7.1 ตั้งหนี้ประจำเดือน',
            '_7.2 ตั้งหนี้ผู้ใช้น้ำ',
            '8. หลักประกันสัญญา',
            '9. หนี้ค้างชำระ',
            '11. ประวัติการเปลี่ยนสถานะมาตร',
            '12. มาตรตาย',
            '13. ยกเลิกใบเสร็จรับเงินค่าน้ำ')