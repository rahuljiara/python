char = input("Enter Character to Check Vowel/Consonent: ")
print("Data type of ", char, "is :- ", type(char))

if char.isalpha():
  
  if(char=='a' or char=='A' or char=='e' or char=='E'or char=='i' or char=='I'or char=='o' or char=='O'or char=='u' or char=='U'):
    print("Vowel")
  else:
    print("Consonent")
    
else:
  print("Invalid Input!")