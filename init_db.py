import sqlite3

def create_tables():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Criação da tabela de alimentos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS foods (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT,
            glycemic_index INTEGER,
            description TEXT,
            benefits TEXT,
            suggestions TEXT,
            nutritional_info TEXT
        )   
    ''')

    # Criação da tabela de receitas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS recipes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            ingredients TEXT NOT NULL,
            instructions TEXT NOT NULL,
            additional_info TEXT
        )
    ''')

    conn.commit()
    conn.close()

def seed_data():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Alimentos com informações detalhadas e dados nutricionais
    foods_data = [
        ("Abacate", "Fruta", 15, 
         "Rico em gorduras monoinsaturadas. Ajuda no controle da glicemia e promove saciedade. Fonte de vitaminas e minerais.",
         "Ajuda a melhorar o controle do colesterol, promovendo a saúde cardiovascular. Ideal para dietas de controle de peso.",
         "Pode ser consumido em saladas, smoothies, ou até como substituto de manteiga em receitas.",
         "100g de abacate contém cerca de 160 calorias, 9g de carboidratos, 2g de proteína e 15g de gordura (9g monoinsaturada)."),

        ("Abobrinha", "Vegetal", 15, 
         "Baixíssimo índice glicêmico, rica em fibras e versátil no preparo.",
         "Auxilia na digestão e promove a sensação de saciedade. Boa para controle de peso e saúde intestinal.",
         "Pode ser consumida crua em saladas, cozida ou assada com temperos variados.",
         "100g de abobrinha contém 17 calorias, 3g de carboidratos, 1g de proteína, 0,3g de gordura, 1g de fibra."),

        ("Amêndoas", "Oleaginosa", 15, 
         "Ricas em gorduras saudáveis, proteínas e fibras. Auxiliam no controle do açúcar no sangue.",
         "Além de controlar a glicemia, as amêndoas têm propriedades antioxidantes e anti-inflamatórias.",
         "São ótimas como lanche, em smoothies, ou adicionadas em pratos doces e salgados.",
         "100g de amêndoas contém 576 calorias, 22g de carboidratos, 21g de proteína, 49g de gordura (31g monoinsaturada)."),

        ("Arroz integral", "Cereal", 50, 
         "Versão integral do arroz, com mais fibras e menor impacto na glicemia.",
         "Melhora a saúde digestiva e mantém os níveis de glicose estáveis. Auxilia no controle de peso.",
         "Ideal para substituição do arroz branco em pratos principais, acompanhando legumes ou proteínas.",
         "100g de arroz integral contém 111 calorias, 23g de carboidratos, 2g de proteína, 1g de gordura, 1g de fibra."),

        ("Aveia", "Cereal", 55, 
         "Rica em betaglucana, fibra solúvel que retarda a digestão e absorção de glicose. Ajuda a controlar picos de açúcar.",
         "A aveia ajuda na redução do colesterol e no controle do apetite, promovendo sensação de saciedade.",
         "Consumida em mingaus, granolas ou como base para bolos e panquecas saudáveis.",
         "100g de aveia contém 389 calorias, 66g de carboidratos, 16g de proteína, 7g de gordura, 10g de fibra."),

        ("Brócolis", "Vegetal", 10, 
         "Rico em sulforafano, fibras, vitaminas e minerais. Ajuda a controlar o açúcar no sangue.",
         "É antioxidante, combate a inflamação e pode ajudar na prevenção do câncer.",
         "Ótimo como acompanhamento de proteínas magras, refogado, cozido no vapor ou em sopas.",
         "100g de brócolis contém 34 calorias, 7g de carboidratos, 3g de proteína, 0,4g de gordura, 2,4g de fibra."),

        ("Cenoura", "Vegetal", 35, 
         "Baixo índice glicêmico, rica em betacaroteno e fibras. Pode ser consumida crua ou cozida.",
         "Auxilia na saúde ocular e no controle do colesterol.",
         "Ideal em saladas, sucos ou como acompanhamento de pratos.",
         "100g de cenoura contém 41 calorias, 10g de carboidratos, 1g de proteína, 0,2g de gordura, 2,8g de fibra."),

        ("Chia", "Semente", 15, 
         "Rica em fibras, auxilia no controle da glicemia e saciedade. Boa fonte de ômega-3.",
         "Ajuda a melhorar a digestão, controla o colesterol e promove saciedade.",
         "Pode ser adicionada a sucos, saladas, iogurtes ou ser usada na preparação de pudins.",
         "100g de chia contém 486 calorias, 42g de carboidratos, 17g de proteína, 31g de gordura, 34g de fibra."),

        ("Couve", "Vegetal", 10, 
         "Folha verde rica em ferro, cálcio e com baixo impacto glicêmico.",
         "Ajuda na digestão, previne doenças cardiovasculares e melhora a função hepática.",
         "Pode ser consumida crua em saladas ou refogada com outros legumes.",
         "100g de couve contém 49 calorias, 9g de carboidratos, 4g de proteína, 0,9g de gordura, 2,5g de fibra."),

        ("Ervilhas", "Leguminosa", 32, 
         "Boa fonte de proteínas e fibras, auxilia no controle do açúcar no sangue.",
         "Além de controlar o açúcar, as ervilhas ajudam na saúde digestiva.",
         "São ótimas em sopas, saladas, refogados ou como acompanhamento.",
         "100g de ervilhas contém 81 calorias, 15g de carboidratos, 5g de proteína, 0,4g de gordura, 5g de fibra."),

        ("Feijão preto", "Leguminosa", 30, 
         "Fonte de proteínas e fibras, reduzindo picos de glicemia.",
         "Auxilia na saúde digestiva, controla a glicemia e melhora a saciedade.",
         "Ideal em feijoadas, saladas ou como acompanhamento de carnes magras.",
         "100g de feijão preto contém 339 calorias, 62g de carboidratos, 21g de proteína, 0,8g de gordura, 16g de fibra."),

         ("Framboesa", "Fruta", 25, 
         "Baixo índice glicêmico, rica em antioxidantes e vitaminas.",
         "Auxilia na melhora da saúde cardiovascular e no controle de glicose.",
         "Ideal em sobremesas, sucos, ou consumida como snack.",
         "100g de framboesa contém 52 calorias, 12g de carboidratos, 1g de proteína, 0,7g de gordura, 6,5g de fibra."),

        ("Gengibre", "Especiaria", 0, 
         "Estimula a produção de insulina, reduz níveis de açúcar no sangue e inflamação.",
         "Auxilia no controle de glicemia e digestão.",
         "Ideal para chás, sucos ou adicionado em temperos de pratos.",
         "100g de gengibre contém 80 calorias, 18g de carboidratos, 2g de proteína, 0,7g de gordura, 2g de fibra."),

        ("Gergelim", "Semente", 14, 
         "Semente rica em gorduras boas e micronutrientes. Usada em pães e saladas.",
         "Melhora a saúde cardiovascular, ajuda a controlar os níveis de colesterol.",
         "Pode ser consumido em saladas, sopas ou como recheio de pães.",
         "100g de gergelim contém 573 calorias, 23g de carboidratos, 18g de proteína, 49g de gordura (sesquiterpenos)."),

        ("Grão-de-bico", "Leguminosa", 30, 
         "Fonte de proteínas, fibras e minerais. Ajuda na saciedade e controle glicêmico.",
         "Além de controlar o açúcar, o grão-de-bico também ajuda na digestão e no controle do colesterol.",
         "Ideal em sopas, saladas, ou misturado em pratos principais.",
         "100g de grão-de-bico contém 164 calorias, 27g de carboidratos, 9g de proteína, 2g de gordura, 8g de fibra."),

        ("Iogurte natural sem açúcar", "Laticínio", 14, 
         "Rico em probióticos, proteínas e cálcio. Ajuda a controlar o açúcar no sangue.",
         "Ajuda na digestão e promove uma flora intestinal saudável.",
         "Pode ser consumido com frutas ou usado em preparações como smoothies.",
         "100g de iogurte natural sem açúcar contém 59 calorias, 3g de carboidratos, 10g de proteína, 3g de gordura."),

        ("Lentilha", "Leguminosa", 28, 
         "Proteína vegetal, rica em fibras e micronutrientes. Baixo IG.",
         "Auxilia na saciedade e no controle glicêmico, além de ser uma excelente fonte de ferro.",
         "Ideal em sopas, saladas ou como acompanhamento.",
         "100g de lentilha contém 116 calorias, 20g de carboidratos, 9g de proteína, 0,4g de gordura, 8g de fibra."),

        ("Maçã", "Fruta", 38, 
         "Rica em pectina (fibra solúvel) que retarda a digestão de glicose. Baixo IG.",
         "Auxilia no controle de colesterol e glicemia.",
         "Ideal como lanche, em sucos ou sobremesas.",
         "100g de maçã contém 52 calorias, 14g de carboidratos, 0g de proteína, 0g de gordura, 2,4g de fibra."),

        ("Mirtilo (Blueberry)", "Fruta", 53, 
         "Antioxidante poderoso, índice glicêmico moderado.",
         "Rico em antioxidantes, o mirtilo ajuda a proteger contra doenças cardíacas.",
         "Ideal em sucos, iogurtes ou como topping para sobremesas.",
         "100g de mirtilo contém 57 calorias, 14g de carboidratos, 1g de proteína, 0,3g de gordura, 2g de fibra."),

        ("Morango", "Fruta", 40, 
         "Baixo IG, rico em vitamina C e antioxidantes.",
         "Auxilia na saúde da pele e no fortalecimento do sistema imunológico.",
         "Ideal como sobremesa, em sucos ou misturado com iogurte.",
         "100g de morango contém 32 calorias, 7g de carboidratos, 0g de proteína, 0g de gordura, 2g de fibra."),

        ("Peixe (salmão ou tilápia)", "Proteína animal", 0, 
         "Fonte de proteína e gorduras boas (ex.: ômega-3 no salmão).",
         "Promove a saúde cardiovascular e ajuda a reduzir os níveis de colesterol.",
         "Ideal grelhado, assado ou em sopas.",
         "100g de salmão contém 206 calorias, 0g de carboidratos, 22g de proteína, 12g de gordura."),

        ("Pera", "Fruta", 38, 
         "Rica em fibras e vitaminas. Ajuda no controle da glicemia.",
         "Auxilia na digestão e é rica em antioxidantes.",
         "Ideal como lanche, em saladas ou sobremesas.",
         "100g de pera contém 57 calorias, 15g de carboidratos, 1g de proteína, 0g de gordura, 3g de fibra."),

        ("Quinoa", "Cereal", 53, 
         "Rica em proteínas e fibras, índice glicêmico moderado.",
         "A quinoa é uma excelente fonte de proteína e possui todos os aminoácidos essenciais.",
         "Pode ser consumida como prato principal ou salada.",
         "100g de quinoa contém 120 calorias, 21g de carboidratos, 4g de proteína, 2g de gordura, 2g de fibra."),

        ("Ricota", "Laticínio", 0, 
         "Baixo teor de carboidratos e gorduras, rica em proteínas.",
         "Ideal para dietas de controle de peso e ajuda na recuperação muscular.",
         "Pode ser usada em receitas salgadas ou doces, como recheio.",
         "100g de ricota contém 150 calorias, 6g de carboidratos, 11g de proteína, 9g de gordura."),

        ("Semente de abóbora", "Semente", 10, 
         "Boa fonte de magnésio, ferro e gorduras boas.",
         "Auxilia no controle de glicemia e na saúde do coração.",
         "Pode ser consumida como lanche ou adicionada a saladas.",
         "100g de semente de abóbora contém 559 calorias, 10g de carboidratos, 30g de proteína, 49g de gordura."),

        ("Tomate", "Vegetal", 15, 
         "Rico em licopeno e vitaminas, baixíssimo índice glicêmico.",
         "Auxilia na prevenção do câncer e melhora a saúde ocular.",
         "Ideal em saladas, molhos ou como acompanhamento de pratos.",
         "100g de tomate contém 18 calorias, 4g de carboidratos, 1g de proteína, 0g de gordura, 1g de fibra."),

        ("Uva", "Fruta", 59, 
         "IG moderado, mas alta carga glicêmica em grandes quantidades. Moderação.",
         "Rica em antioxidantes e ajuda na saúde cardiovascular.",
         "Ideal como lanche ou adicionada a sucos e sobremesas.",
         "100g de uva contém 69 calorias, 18g de carboidratos, 0g de proteína, 0g de gordura, 0g de fibra."),
    
    ]

    # Inserindo alimentos no banco
    cursor.executemany('''
        INSERT INTO foods (name, category, glycemic_index, description, benefits, suggestions, nutritional_info)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', foods_data)

    # Receitas com exemplos mais detalhados
    recipes_data = [
        ("Salada de abacate com feijão preto",
         "Abacate, Feijão preto cozido, Cebola roxa, Tomate, Azeite, Limão, Sal, Pimenta",
         "1. Corte o abacate em cubos. 2. Misture com feijão preto cozido, cebola e tomate picados. 3. Tempere com azeite, limão, sal e pimenta.",
         "Uma refeição saudável, rica em fibras e antioxidantes, ideal para o controle de glicemia."),
        
        ("Aveia com maçã e canela",
         "Aveia, Maçã, Leite desnatado (ou bebida vegetal), Canela em pó",
         "1. Cozinhe a aveia com o leite até atingir a consistência desejada. 2. Adicione maçã picada e canela por cima.",
         "Uma excelente opção para o café da manhã, promovendo saciedade e controle glicêmico."),
        
        ("Sopa de lentilha com legumes",
         "Lentilha, Cenoura, Abobrinha, Cebola, Alho, Caldo de legumes sem sal, Temperos a gosto",
         "1. Refogue cebola e alho. 2. Acrescente lentilha, cenoura, abobrinha e o caldo de legumes. 3. Cozinhe até ficar macia.",
         "Uma refeição leve, rica em proteínas vegetais e fibras, ideal para o controle glicêmico."),
        
        ("Frango grelhado com brócolis",
         "Peito de frango, Brócolis, Azeite, Alho, Sal, Pimenta",
         "1. Tempere o frango e grelhe. 2. Cozinhe o brócolis no vapor. 3. Sirva com azeite e alho refogado.",
         "Frango magro, combinado com brócolis, é uma refeição rica em proteínas e antioxidantes."),
        
        ("Bowl de quinoa com legumes",
         "Quinoa, Tomate-cereja, Alface, Cenoura ralada, Pepino, Azeite, Limão, Sal",
         "1. Cozinhe a quinoa conforme instruções. 2. Misture com tomate-cereja, alface, cenoura, pepino. 3. Tempere.",
         "Uma refeição leve, rica em fibras, que promove saciedade e controle glicêmico."),
        
        ("Peixe assado com legumes",
         "Peixe (salmão ou tilápia), Abobrinha, Cenoura, Cebola, Azeite, Ervas finas, Sal",
         "1. Tempere o peixe com sal e ervas. 2. Corte os legumes em tiras. 3. Asse tudo em forno a 200°C por ~20 min.",
         "Rico em ômega-3 e antioxidantes, este prato ajuda a melhorar a saúde cardiovascular e controlar a glicemia."),
        
        # Mais 15 receitas adicionadas
        ("Panqueca de banana e aveia",
         "1 banana madura, 2 colheres (sopa) de aveia, 1 ovo, Canela a gosto",
         "1. Amasse a banana e misture com o ovo e a aveia. 2. Adicione canela. 3. Despeje em frigideira antiaderente até dourar.",
         "Uma refeição rápida e saudável, ótima para o café da manhã."),
        
        ("Torta de maçã sem açúcar",
         "Maçã, Farinha integral, Ovos, Canela, Adoçante, Fermento",
         "1. Misture todos os ingredientes e despeje em uma forma untada. 2. Asse em forno médio por 30 minutos.",
         "Uma alternativa saudável para quem adora tortas doces."),
        
        ("Sopa detox de abóbora",
         "Abóbora, Cebola, Alho, Caldo de legumes, Gengibre, Pimenta",
         "1. Cozinhe a abóbora com cebola e alho. 2. Bata no liquidificador e leve ao fogo para aquecer.",
         "Sopa leve e detox, ideal para ajudar na digestão e desintoxicação."),
        
        ("Quibe de abóbora com ricota",
         "Abóbora cozida, Trigo para quibe, Ricota, Cebola, Hortelã, Sal, Pimenta",
         "1. Hidrate o trigo para quibe. 2. Amasse a abóbora e misture com a ricota e temperos. 3. Leve ao forno até dourar.",
         "Uma opção saudável e saborosa de quibe, ideal para o almoço."),
        
        ("Arroz de couve-flor",
         "Couve-flor, Alho, Cebola, Azeite, Sal",
         "1. Processe a couve-flor até virar ‘arroz’. 2. Refogue com alho e cebola até dourar.",
         "Uma ótima substituição para o arroz branco, com baixo impacto glicêmico."),
        
        ("Taco de peixe",
         "Peixe grelhado, Tortilhas integrais, Alface, Tomate, Abacate, Limão",
         "1. Grelhe o peixe e monte os tacos com alface, tomate, abacate e limão.",
         "Uma refeição rica em proteínas e gorduras boas, excelente para o almoço."),
        
        ("Salada de grão-de-bico",
         "Grão-de-bico, Tomate, Pepino, Cebola roxa, Azeite, Limão, Sal",
         "1. Misture todos os ingredientes. 2. Tempere com azeite, limão, e sal.",
         "Salada fresca e nutritiva, rica em fibras e proteínas vegetais."),
        
        ("Bolo de banana saudável",
         "Bananas maduras, Farinha de aveia, Ovos, Canela, Fermento",
         "1. Amasse as bananas e misture com os outros ingredientes. 2. Asse em forno médio por 40 minutos.",
         "Uma alternativa saudável e sem açúcar para os amantes de bolos doces."),
        
        ("Wrap de frango com alface",
         "Peito de frango grelhado, Alface, Tomate, Abacate, Tortilhas integrais",
         "1. Grelhe o frango e coloque nos wraps com os outros ingredientes.",
         "Uma refeição rápida e rica em proteínas."),
        
        ("Bowl de frutas vermelhas",
         "Framboesa, Morango, Mirtilo, Iogurte natural sem açúcar, Mel",
         "1. Misture as frutas com o iogurte e adicione mel a gosto.",
         "Uma refeição leve e cheia de antioxidantes."),
        
        ("Chá verde gelado com limão",
         "Chá verde, Limão, Gelo, Adoçante",
         "1. Prepare o chá verde e deixe esfriar. 2. Sirva com limão e gelo.",
         "Uma bebida refrescante e cheia de antioxidantes."),
        
        ("Torta de legumes",
         "Cenoura, Abobrinha, Ervilhas, Alho-poró, Ovo, Queijo",
         "1. Misture todos os legumes e ovos. 2. Asse a mistura em forma untada até dourar.",
         "Uma refeição rica em fibras e com baixo impacto glicêmico."),
        
        ("Espaguete de abobrinha",
         "Abobrinha, Alho, Azeite, Manjericão, Tomate-cereja",
         "1. Corte a abobrinha em tiras finas e refogue com alho e azeite. 2. Sirva com tomate e manjericão.",
         "Uma alternativa saudável ao espaguete tradicional, com menos carboidratos."),
        
        ("Mousse de morango saudável",
         "Morango, Iogurte grego, Adoçante, Essência de baunilha",
         "1. Bata os ingredientes no liquidificador até ficar cremoso. 2. Sirva gelado.",
         "Uma sobremesa saudável e cheia de vitaminas."),
        
        ("Lentilha com legumes",
         "Lentilha, Cenoura, Batata-doce, Tomate, Alho, Ervas finas",
         "1. Cozinhe as lentilhas e depois misture com os legumes cozidos.",
         "Uma refeição rica em proteínas vegetais, ideal para vegetarians e vegans."),
        
        ("Peixe com arroz de quinoa",
         "Peixe (tilápia ou salmão), Quinoa, Alho, Limão, Azeite",
         "1. Cozinhe a quinoa. 2. Grelhe o peixe e sirva com a quinoa e molho de limão.",
         "Um prato completo e cheio de ômega-3 e fibras."),
    ]

    # Inserindo receitas no banco
    cursor.executemany('''
        INSERT INTO recipes (title, ingredients, instructions, additional_info)
        VALUES (?, ?, ?, ?)
    ''', recipes_data)

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()
    seed_data()
    print("Banco de dados criado e populado com sucesso!")
