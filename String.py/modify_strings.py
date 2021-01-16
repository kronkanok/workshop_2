string = " Hello, World! "

print(string.upper()) #Output : "Hello, World!"
print(string.lower()) #Output : "hello, world!"
print(string.strip()) #Output : "Hello, World!" #แก้ไขคำที่error
print(string.replace("H","J")) #Output : "Jello World! " แก้ไขคำ #ลบข้อความที่ไม่มีspace ได้เช่น   I love you เป็น Iloveyou
print(string.split(",")) #Output :  ['Hello', ' World! '] ตัดหัวท้ายทิ้ง
print(len(string))  #15