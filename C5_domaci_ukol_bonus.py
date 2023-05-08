teploty = [
    ["pondělí", 2.1, 5.2, 6.1, -0.1],
    ["úterý", 2.2, 4.8, 5.6, -1.0],
    ["středa", 3.3, 6.5, 5.9, 1.2],
    ["čtvrtek", 2.9, 5.6, 6.0, 0.0],
    ["pátek", 2.0, 4.6, 5.5, -1.2],
    ["sobota", 1.0, 3.2, 2.1, -2.0],
    ["neděle", 0.4, 2.7, 1.3, -2.8]
]

""" oprava bonusu: """

prum_teploty = {item[0]: float(f"{round(sum(item[1:]) / len(item[1:]), 1)}") for item in teploty}
print(prum_teploty)



""" 
původní nedokonalé řešení:

prum_teploty = {item[0]: f"{round(sum(item[1:]) / len(item[1:]), 1)}" for item in teploty}
print(prum_teploty) 

"""
