from random import randint
import csv

row_list = [
    ["perninha_curta", "pelo_longo", "faz_auau", "qual_animal"]
    ]

for x in range(1, 11):
    row_list.append(
        [int(randint(0, 1)), int(randint(0, 1)), int(randint(0, 1)), int(randint(0, 1))]
    )

with open('dados_comprar.csv', 'w', newline='') as file:
    write = csv.writer(file)
    write.writerows(row_list)


# with open('dados_comprar.csv', 'r') as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#         print(row)