import string 
    
# An input string.
Sentence = "Hey, Geeks !, How are you?"
  
for i in Sentence:
      
    # checking whether the char is punctuation.
    if i in string.punctuation:
        print("Punctuation: " + i)
   