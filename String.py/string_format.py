age = 21
txt = "My name is Chompoo, and I am {}"

result = txt.format(age) #การต่อstr(txt.format)ที่สามารถกำหนดอกิวเม้นได้

print("result", result) #Output: "My name is Chompoo, and I am 21
 
#txt.format สามารถใช้ string+intได้ เช่น ชมพู่ + 21 จะได้ ชมพู่21