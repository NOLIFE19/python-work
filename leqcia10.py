#ნაწილი 1
# თოთოეული ხაზის ახნა 
def factorial_recursive(n):  #აქ  შექმენით ფუნქცია   ფატორიალი რეკურსიული
    if n < 0:     # აქ ვამოწმედ იმას რომ თუ  შეყვანილი რიცხვი არის უარყოფითი, თუ უარყოფითია აბრუნებს ქვემოთ მოყვანილი მშნიშველობას
        return "Factorial is not defined for negative numbers."  
   
    if n == 0 or n == 1:  # ეს არის base case ეს ყველაზე მნშვნელოვანია ნაწილია ეს პირობა აჩერებს რეკურსიას, ეს რომ არი იყოს ფუნქცია საკუთარ თავას გამოიძახებს სულ  
        return 1             # აქ ამოწმებს  თუ n=1  და n=0  დააბრუნოს 1    აქ ჩერდება ფუნქცია აღარ იძახებს საკუთარ თავს 
    
    return n * factorial_recursive(n - 1)    #ეს არის რეკურსიის ნაწილი როცა  n იღებს მნიშვნელობას  და  ამრავლებს სანამ n 1 ან 0 არ გაუტოლდება.  მანამდე ხდება ფუნქციის გამოძახება

print(factorial_recursive(5))  #  აქ ვუთითებთ   არგუმენტს რომელიც  მიეწდოება ფუნქციას პარამეტრის სახით და ტერმინალში გამომგვაქვს


# ნაწილი 2 
 

def calculate_cart_total(discount_rate, *prices):
     result=[]
     for price in prices:
          discount=price*discount_rate/100
          final_price=price-discount
          result.append(final_price)
          
     return sum(result)



print(calculate_cart_total(10,16,30,40))


# ნაწილი 3 
def filter_and_sort_products(**products):
    filtered_products = filter(
        lambda item: item[1] >= 100,
        products.items()
    )

    return sorted(filtered_products, key=lambda item: item[1])


print(filter_and_sort_products(
    laptop=2500,
    mouse=50,
    keyboard=150,
    monitor=500
))


from functools import reduce

names = ["Ana", "Nino", "Luka", "Giorgi", "Mariam"]
scores = [45, 82, 91, 38, 74]


def pair_students(names_list, scores_list):
    return list(zip(names_list, scores_list))


def get_passed_students(paired_data, passing_score=60):
    return list(filter(lambda student: student[1] >= passing_score, paired_data))


def calculate_average_of_passed(passed_students):
    scores = list(map(lambda student: student[1], passed_students))
    total = reduce(lambda a, b: a + b, scores)
    return total / len(scores)


paired_data = pair_students(names, scores)

passed_students = get_passed_students(paired_data)

average = calculate_average_of_passed(passed_students)


print( paired_data)
print( passed_students)
print( average)




