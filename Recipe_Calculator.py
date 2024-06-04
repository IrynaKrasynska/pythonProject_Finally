import json


def pr_num(b):
    try:
        b = int(b)
        if b == 0 or b < 0:
            print("You cannot prepare this dish, choose another recipe")
            exit()
        else:
            print("We calculate the amount of ingredients!")
        a = rec[ingridient]
        k = b / a
        my_recipe = {}
        for x, i in rec.items():
            i = i * k
            print(x, i)
            my_recipe[x] = i
        new_recipe = input("Enter name new recipe: ")
        cooking_book[new_recipe] = my_recipe
        for num, key in enumerate(cooking_book, 1):
            print(f"{num}.{key}")
    except ValueError:
        print("You must enter the amount of ingridient in grams!")
        exit()


with open("cookbook.json", "r") as f:
    cooking_book = json.load(f)

print("Recipe names: ")
for num, key in enumerate(cooking_book, 1):
    print(f"{num}.{key}")
choice = input("Choose your recipe(name): ")
if choice in cooking_book:
    print("You choosed")
else:
    print("Recipe not found")
    exit()

print("Ingridients: ")
rec = cooking_book.get(choice)
for num, key in enumerate(rec, 1):
    print(f"{num}.{key:}")
ingridient = input("Enter the name of the missing ingridient: ")
if ingridient in rec:
        print("You choosed")
else:
    print("Ingridient not found")
    exit()
b = input("Enter quantity in grams: ")
pr_num(b)

with open("cookbook.json", "w") as f:
    json.dump(cooking_book,f, ensure_ascii=True, indent=4)
    print("Succses!")







