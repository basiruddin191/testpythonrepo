a=["hello","world"]
final_text=""
for i in a:
  final_text=final_text+" "+i
print(final_text)
print(final_text+"Basir")
list1=final_text.split(" ")
for i in list1:
  if(i=="world"):
    print(True,i)
  else:
   print(False,i)