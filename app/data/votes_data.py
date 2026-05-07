PRIMARY_QUESTIONS = [
    {
        "id": "environment",
        "question": "Você prefere um destino urbano, natural ou misto?",
        "options": ["Urbano", "Natural", "Misto"]
    }
]


SECONDARY_QUESTIONS = {
    "Urbano": {
        "id": "urban_preference",
        "question": "Que tipo de cidade você prefere?",
        "options": ["Cidade grande", "Cidade histórica", "Cidade cultural"]
    },

    "Natural": {
        "id": "nature_preference",
        "question": "Que tipo de natureza você prefere?",
        "options": ["Praias", "Montanhas", "Rios"]
    },

    "Misto": {
        "id": "mixed_preference",
        "question": "Você prefere mais descanso, agitação ou equilíbrio?",
        "options": ["Descanso", "Agitação", "Equilíbrio"]
    }
}


DESTINATIONS_BY_SECONDARY_ANSWER = {
    "Cidade grande": ["São Paulo", "Rio de Janeiro", "Belo Horizonte"],
    "Cidade histórica": ["Ouro Preto", "Paraty", "Petrópolis"],
    "Cidade cultural": ["Curitiba", "Recife", "Salvador"],

    "Praias": ["Florianópolis", "Maragogi", "Fernando de Noronha"],
    "Montanhas": ["Gramado", "Campos do Jordão", "Chapada Diamantina"],
    "Rios": ["Bonito", "Jalapão", "Foz do Iguaçu"],

    "Descanso": ["João Pessoa", "Maceió", "Porto Seguro"],
    "Agitação": ["Salvador", "Rio de Janeiro", "Recife"],
    "Equilíbrio": ["Florianópolis", "Curitiba", "Fortaleza"]
}
