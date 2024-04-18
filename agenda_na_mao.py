AGENDA = {
    "Guilherme": {
        "Telefone": "(61)9 9999-0000",
        "Email": "email@email.com",
        "Endereço": "Av.0"
    },

    "Joaquim": {
        "Telefone": "(61)9 9999-0001",
        "Email": "email@email.com",
        "Endereço": "Av.01"
    },

    "João": {
        "Telefone": "(61)9 9999-0002",
        "Email": "email@email.com",
        "Endereço": "Av.02"
    },

    "Beto": {
        "Telefone": "(61)9 9999-0003",
        "Email": "email@email.com",
        "Endereço": "Av.03"
    },

    "Allan": {
        "Telefone": "(61)9 9999-0004",
        "Email": "email@email.com",
        "Endereço": "Av.04"
    },

    "Moisés": {
        "Telefone": "(61)9 9999-0005",
        "Email": "email@email.com",
        "Endereço": "Av.05"
    },
}

AGENDA["Guilherme"]["Endereço"] = "Rua das nações"

AGENDA["Lucas"] = {
    "Telefone": "(61)9 9999-0006",
    "Email": "email@email.com",
    "Endereço": "Av.10",
}

AGENDA.pop("Guilherme")

for contato in AGENDA:
    print(AGENDA)
