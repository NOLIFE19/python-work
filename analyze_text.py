# შექმენით ფუნქცია სახელად analyze_text, რომელიც იღებს ტექსტს და აანალიზებს მის სტრუქტურას.

def analyze_text(text: str,target_word: str):
    
    quantity = text.split()
    quantity_1 = len(quantity)

    target= target_word.lower()
    count_word=0
    for target_word in quantity:
        if target_word.lower()==target:
            count_word +=1


    longtext=max(quantity, key=len)
    return quantity_1 , count_word, longtext
     


print(analyze_text("Python is fun and Python is useful", "python"))

print(analyze_text("I love coding because coding is interesting", "coding"))

print(analyze_text("Apple banana apple orange apple", "apple"))

print(analyze_text("Today is a beautiful day and tomorrow is beautiful", "beautiful"))

print(analyze_text("Java Python C++ Python JavaScript", "java"))


