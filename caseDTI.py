import calendar
from datetime import datetime

print("*Kennel BH*")

date = input("Informe a data (DD/MM/AAAA): ")
date = datetime.strptime(date,"%d/%m/%Y")
days = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')

day = calendar.weekday(date.year, date.month, date.day)
print("Dia: ",days[day])

small_dogs = int(input("Informe a quantidade de cães pequenos: "))
big_dogs = int(input("Informe a quantidade de cães grandes: "))

#dicionarios para armazenar dados e valores dos canis
my_happy_canine ={"distance": 2, "smalldogs": 20, "bigdogs": 40}
go_rex = {"distance": 1.7, "smalldogs": 15, "bigdogs": 50, "smalldogsweekend": 20, "bigdogsweekend": 55}
chowChawgas = {"distance": 0.8, "smalldogs": 30, "bigdogs": 45}

def calculate_price(pet_shop):
    return (pet_shop["smalldogs"] * small_dogs) + (pet_shop["bigdogs"] * big_dogs)

final_price1 = {"name":"My Happy Canine", "total": calculate_price(my_happy_canine)}

final_price2 = {"name": "Go Rex", "total": calculate_price(go_rex)}

final_price3 = {"name": "Chow Chawgas", "total": calculate_price(chowChawgas)}

equal = False

if days[day] == "Sábado" or days[day] == "Domingo":

	# calcula porcentagem de taxa de aumento
	rate1 = my_happy_canine["smalldogs"] * 0.2
	#soma porcentagem com o valor semanal e multiplica pela quantidade de caes
	price_smalldogs1 = (my_happy_canine["smalldogs"] + rate1) * small_dogs
	rate2 = my_happy_canine["bigdogs"] * 0.2
	price_bigdogs1 = (my_happy_canine["bigdogs"] + rate2) * big_dogs
	final_price1["total"] = price_smalldogs1 + price_bigdogs1

	price_smalldogs2 = go_rex["smalldogsweekend"] * small_dogs
	price_bigdogs2 = go_rex["bigdogsweekend"] * big_dogs
	final_price2["total"] = price_smalldogs2 + price_bigdogs2

# caso seja valores iguais pega menor distancia. Como já é fixa já sei que é o vai rex.
elif final_price1["total"] == final_price2["total"]:
    print("O melhor canil é o VaiRex e o preço total é R$", final_price2["total"])
    equal = True
elif final_price1["total"] == final_price3["total"]:
    print("O melhor canil é o Chow Chawgas e o preço total é R$", final_price3["total"])
    equal = True
elif final_price2["total"] == final_price3["total"]:
    print("O melhor canil é o Chow Chawgas e o preço total é R$", final_price3["total"])
    equal = True
elif final_price1["total"] == final_price2["total"] and final_price1["total"] == final_price3["total"]:
    print("O melhor canil é o Chow Chawgas e o preço total é R$", final_price3["total"])
    equal = True

#lista de melhor preço 
if not equal:
    price = []
    price.append(final_price1)
    price.append(final_price2)
    price.append(final_price3)
    best_price = min(price, key=lambda x:x["total"]) # pega o valor minimo pela chave "total" do dicionario
    print("O melhor petshop é",best_price["name"], " e o valor total dos banhos é R$", best_price["total"])