a=["hello","world"]
final_text=""
for i in a:
  final_text=final_text+" "+i
print(final_text)
print(final_text+"Basir")
for i in final_text:
  if(i=="world"):
    print(True)
  else:
    print(False)
