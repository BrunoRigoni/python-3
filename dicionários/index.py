clients = []


users = [
    {
        "nome": "Bruno",
        "idade": 24,
        "nacionalidade": "brasileiro",
        "estoque": ["uva", "pera", "maçã"]
    }
]

new_users = {
    "nome": "Ana",
    "idade": 30,
    "nacionalidade": "brasileira",
    "estoque": ["abacaxi"]
}

users.append(new_users)

clients.append(users)
print(clients)
