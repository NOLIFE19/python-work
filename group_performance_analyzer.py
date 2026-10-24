#შექმენი პროგრამა, რომელიც საშუალებას აძლევს მასწავლებელს შეიყვანოს კლასის სტუდენტების ქულები.


# scores = []

# while True:
#     teacher_input = input("შეიყვანე ქულა ან stop: ")

#     if teacher_input.lower() == "stop":
#         break

#     try:
#         score = int(teacher_input)

#         if 0 <= score <= 10:
#             scores.append(score)
#         else:
#             print("შეიყვანე  ქულა 0 დან 10 ჩათვლით")

#     except ValueError:
#         print("გთხოვ სწორი რიცხვი შეიყვანე ან stop'.")


# if len(scores) > 0:
#     minimum = min(scores)
#     maximum = max(scores)
#     average = sum(scores) / len(scores)


#     print(f"min: {minimum:g}")
#     print(f"max: {maximum:g}")
#     print(f"average: {average:.2f}")

#     print(sorted(scores))

    
# checked = []

# for score in scores:
#     if score not in checked:
#         print(f"ქულა {score:g} — {scores.count(score)}-ჯერ")
#         checked.append(score)

