print ("Привет,я словарик ,давай учить язык вместе :)")


def loe_rus(f):
    fail=open(f,'r',encoding="utf-8-sig")
    mas=[] 
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas
def salvesta_failisse(f,text):
 fail=open(f,'a',"encoding=utf-8-sig")
 fail.write(text+"\n")
 fail.close()
 mas=[]
 mas=loe_rus(f)
 return mas
def tolkimine():
  pass
rus_list=loe_rus("rus.txt")
ing_list=loe_rus("ing.txt")

print(rus_list)
print(ing_list)
print("Я тут создал пару функций,выбери то что тебе больше нравится \n Нажми  ")
while True:
 ot=input("1-Перевод слов\n2-Добавить новое слово\n3-Исправить ошибку\n4-Тест на проверку знаний\n")
 if ot=="1":
  tolkimine()
 elif ot=="2":
  rus_word=input("Введи слово на русском:\n")
  ing_word=input("Введи слово на английском:\n")
  rus_list=salvesta_failisse("rus.txt",rus_word)
  ing_list=salvesta_failisse("ing.txt",ing_word)
  print(rus_list)
  print(ing_list)


 
