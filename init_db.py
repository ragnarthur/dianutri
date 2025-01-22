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

        ("Abacaxi", "Fruta", 66,
         "Fruta tropical rica em vitamina C, melhora a digestão e acelera o metabolismo.",
         "Auxilia na digestão devido à bromelina e é ótima para o sistema imunológico.",
         "Ideal em sucos, saladas ou como sobremesa.",
         "100g de abacaxi contém 50 calorias, 13g de carboidratos, 0,5g de proteína, 0,1g de gordura, 1g de fibra."),
        
        ("Alecrim", "Erva", 0,
         "Erva aromática que melhora a digestão e tem propriedades antioxidantes.",
         "Ajuda a combater dores de estômago e melhora a memória.",
         "Pode ser usado em carnes, sopas e chás.",
         "100g de alecrim contém 131 calorias, 21g de carboidratos, 3g de proteína, 5g de gordura, 14g de fibra."),

        ("Amendoim", "Oleaginosa", 14,
         "Rico em gorduras saudáveis e proteínas. Baixo impacto glicêmico.",
         "Ajuda no controle da glicemia e é uma boa fonte de energia.",
         "Pode ser consumido como lanche ou adicionado a pratos.",
         "100g de amendoim contém 567 calorias, 16g de carboidratos, 25g de proteína, 49g de gordura."),

        ("Alface", "Vegetal", 10,
         "Rica em água e fibras, boa para hidratação e controle do apetite.",
         "Auxilia na digestão e na redução de peso devido ao seu baixo valor calórico.",
         "Ideal em saladas, como acompanhamento ou em wraps.",
         "100g de alface contém 15 calorias, 3g de carboidratos, 1g de proteína, 0g de gordura, 1g de fibra."),

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

         ("Batata inglesa", "Tubérculo", 70,
         "Rica em carboidratos complexos, ajuda a repor energia.",
         "Ideal para treinos e recuperação muscular, porém com moderação devido ao alto índice glicêmico.",
         "Pode ser cozida, assada ou utilizada em purês.",
         "100g de batata inglesa contém 77 calorias, 17g de carboidratos, 2g de proteína, 0g de gordura."),

        ("Batata doce", "Tubérculo", 54,
         "Fonte de carboidratos de baixo índice glicêmico, rica em fibras.",
         "Ajuda no controle de glicose e na saúde intestinal.",
         "Pode ser consumida cozida, assada ou em purês.",
         "100g de batata doce contém 86 calorias, 20g de carboidratos, 1g de proteína, 0g de gordura."),

         ("Batata yacon", "Tubérculo", 38,
         "Possui baixo índice glicêmico, rica em fibras e com baixo valor calórico.",
         "Auxilia no controle de glicose, melhora a digestão e contribui para a saúde intestinal.",
         "Ideal para ser consumida cozida, assada ou em saladas.",
         "100g de batata yacon contém 37 calorias, 9g de carboidratos, 0g de proteína, 0g de gordura, 3g de fibra."),

        ("Banana madura", "Fruta", 51,
         "Fonte de carboidratos rápidos, rica em potássio e vitamina B6.",
         "Ajuda na recuperação muscular, melhora a digestão e fornece energia de forma rápida.",
         "Ideal como lanche, em vitaminas ou adicionada em sobremesas.",
         "100g de banana madura contém 89 calorias, 23g de carboidratos, 1g de proteína, 0g de gordura, 2,6g de fibra."),

        ("Beterraba", "Vegetal", 64,
         "Rica em fibras e antioxidantes, ajuda no controle do colesterol.",
         "Melhora a circulação sanguínea e combate a anemia.",
         "Ideal em saladas, sucos ou como acompanhamento.",
         "100g de beterraba contém 43 calorias, 10g de carboidratos, 2g de proteína, 0g de gordura."),

        ("Canela", "Especiaria", 0,
         "Possui propriedades antioxidantes, ajuda a controlar os níveis de glicose.",
         "Auxilia na melhora da digestão e pode ser usada em diversas preparações.",
         "Pode ser adicionada em chás, doces, mingaus ou pratos salgados.",
         "100g de canela contém 247 calorias, 81g de carboidratos, 4g de proteína, 1g de gordura."),

        ("Caqui", "Fruta", 55,
         "Rico em fibras e antioxidantes, ajuda a melhorar a digestão.",
         "Auxilia no controle da glicemia e combate radicais livres.",
         "Ideal em sobremesas ou consumido in natura.",
         "100g de caqui contém 81 calorias, 22g de carboidratos, 0g de proteína, 0g de gordura."),   

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

        ("Inhame", "Tubérculo", 51,
         "Rico em carboidratos de baixo índice glicêmico, ajuda na digestão.",
         "Auxilia na saúde intestinal e controle da glicemia.",
         "Pode ser consumido cozido, assado ou em purês.",
         "100g de inhame contém 118 calorias, 27g de carboidratos, 2g de proteína, 0,2g de gordura."),

        ("Iogurte natural sem açúcar", "Laticínio", 14, 
         "Rico em probióticos, proteínas e cálcio. Ajuda a controlar o açúcar no sangue.",
         "Ajuda na digestão e promove uma flora intestinal saudável.",
         "Pode ser consumido com frutas ou usado em preparações como smoothies.",
         "100g de iogurte natural sem açúcar contém 59 calorias, 3g de carboidratos, 10g de proteína, 3g de gordura."),

        ("Jaca", "Fruta", 55,
         "Fruta tropical rica em fibras e vitaminas. Boa para a saúde digestiva.",
         "Auxilia na digestão e no controle da glicemia.",
         "Ideal em sobremesas ou como lanche.",
         "100g de jaca contém 95 calorias, 23g de carboidratos, 1g de proteína, 0g de gordura."),

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

        ("Macarrão branco", "Cereal", 70,
         "Alimento rico em carboidratos simples, com alto índice glicêmico.",
         "Consumo moderado é recomendado para quem controla a glicemia.",
         "Ideal em pratos simples como macarrão ao sugo.",
         "100g de macarrão branco contém 158 calorias, 31g de carboidratos, 5g de proteína, 1g de gordura."),

        ("Mandioca", "Tubérculo", 58,
         "Rica em carboidratos e fibras. Fornece energia e é fonte de cálcio.",
         "Melhora a digestão e é ótima para quem pratica atividades físicas.",
         "Pode ser consumida cozida ou frita.",
         "100g de mandioca contém 160 calorias, 38g de carboidratos, 1g de proteína, 0,2g de gordura."),

        ("Manga", "Fruta", 51,
         "Rica em vitamina C e fibras. Melhora a digestão e imunidade.",
         "Auxilia no combate ao envelhecimento precoce e melhora a saúde da pele.",
         "Ideal consumida fresca ou em sucos.",
         "100g de manga contém 60 calorias, 15g de carboidratos, 0,8g de proteína, 0,4g de gordura."),

        ("Melancia", "Fruta", 72,
         "Alimento hidratante e refrescante, bom para quem pratica atividades físicas.",
         "Auxilia na recuperação pós-treino e é rica em licopeno.",
         "Ideal em sucos ou como sobremesa.",
         "100g de melancia contém 30 calorias, 8g de carboidratos, 1g de proteína, 0g de gordura."),

        ("Manteiga de amendoim", "Oleaginosa", 14,
         "Rica em gorduras saudáveis, pode ser uma excelente fonte de energia.",
         "Auxilia no controle da glicemia e melhora a saciedade.",
         "Ideal para comer com pães integrais ou em smoothies.",
         "100g de manteiga de amendoim contém 588 calorias, 20g de carboidratos, 25g de proteína, 50g de gordura."),

        ("Melão", "Fruta", 65,
         "Fruta refrescante, boa para hidratação e controle do colesterol.",
         "Ideal para emagrecimento e controle da glicemia.",
         "Pode ser consumido in natura ou em sucos.",
         "100g de melão contém 34 calorias, 8g de carboidratos, 1g de proteína, 0g de gordura."),

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

        ("Nozes", "Oleaginosa", 15,
         "Ricas em antioxidantes, ômega-3 e fibras.",
         "Auxiliam no controle da glicemia e da pressão arterial.",
         "Pode ser consumida como lanche ou adicionada a saladas e sobremesas.",
         "100g de nozes contém 654 calorias, 14g de carboidratos, 15g de proteína, 65g de gordura."),

         ("Ovo", "Proteína animal", 0,
         "Fonte de proteína de alto valor biológico e rico em nutrientes essenciais.",
         "Melhora a construção muscular e auxilia na saciedade.",
         "Pode ser consumido cozido, frito ou em preparações diversas.",
         "100g de ovo contém 155 calorias, 1g de carboidratos, 13g de proteína, 11g de gordura."),

        ("Peixe (salmão ou tilápia)", "Proteína animal", 0, 
         "Fonte de proteína e gorduras boas (ex.: ômega-3 no salmão).",
         "Promove a saúde cardiovascular e ajuda a reduzir os níveis de colesterol.",
         "Ideal grelhado, assado ou em sopas.",
         "100g de salmão contém 206 calorias, 0g de carboidratos, 22g de proteína, 12g de gordura."),

        ("Pão branco", "Industrializado", 70,
         "Fonte de carboidratos simples, com alto índice glicêmico.",
         "Evitar o consumo excessivo, principalmente para diabéticos.",
         "Ideal para sanduíches simples.",
         "100g de pão branco contém 265 calorias, 49g de carboidratos, 8g de proteína, 3g de gordura."),

        ("Peito de frango", "Proteína animal", 0,
         "Alto teor de proteínas magras, ideal para dietas de emagrecimento.",
         "Auxilia na construção muscular e recuperação pós-treino.",
         "Ideal grelhado, assado ou cozido.",
         "100g de peito de frango contém 165 calorias, 0g de carboidratos, 31g de proteína, 3g de gordura."),

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
        
        ("Espinafre", "Vegetal", 15, 
        "Rico em ferro, cálcio e antioxidantes. Auxilia no controle de glicemia e na saúde cardiovascular.",
        "Ajuda a reduzir inflamações e melhora a saúde óssea devido ao alto teor de cálcio e vitamina K.",
        "Pode ser consumido cru em saladas, refogado ou em sopas.",
        "100g de espinafre contém 23 calorias, 3,6g de carboidratos, 2,9g de proteína e 0,4g de gordura."),

        ("Rúcula", "Vegetal", 15, 
        "Fonte de antioxidantes, rica em vitaminas A e K, e com baixíssimo índice glicêmico.",
        "Melhora a digestão e promove saúde óssea devido ao alto teor de cálcio.",
        "Ideal em saladas ou como complemento de sanduíches e pratos principais.",
        "100g de rúcula contém 25 calorias, 3,6g de carboidratos, 2,6g de proteína, 0,7g de gordura."),

        ("Pimentão", "Vegetal", 10, 
        "Rico em vitamina C, antioxidantes e fibras. Auxilia na saúde do coração e no controle de glicemia.",
        "Promove a saúde imunológica e reduz inflamações.",
        "Pode ser consumido cru, grelhado ou em refogados.",
        "100g de pimentão contém 31 calorias, 6g de carboidratos, 1g de proteína e 0,3g de gordura."),

        ("Berinjela", "Vegetal", 15, 
        "Baixo índice glicêmico, rica em fibras e antioxidantes, auxilia no controle do colesterol e glicemia.",
        "Promove saciedade e melhora a digestão devido ao alto teor de fibras.",
        "Pode ser consumida assada, grelhada ou em ensopados.",
        "100g de berinjela contém 25 calorias, 5,9g de carboidratos, 1g de proteína e 0,2g de gordura."),

        ("Abóbora", "Vegetal", 22, 
        "Rica em betacaroteno, fibras e com baixo índice glicêmico.",
        "Auxilia na saúde ocular, melhora a digestão e ajuda no controle de glicemia.",
        "Pode ser consumida cozida, assada ou em sopas.",
        "100g de abóbora contém 26 calorias, 6,5g de carboidratos, 1g de proteína, 0,1g de gordura."),

        ("Linhaça", "Semente", 15, 
        "Rica em fibras solúveis e ômega-3, ajuda no controle da glicemia e colesterol.",
        "Auxilia na saúde intestinal e promove saciedade.",
        "Pode ser adicionada a sucos, iogurtes ou usada em receitas de pães e bolos.",
        "100g de linhaça contém 534 calorias, 28g de carboidratos, 18g de proteína, 42g de gordura (30g poli-insaturada)."),

        ("Couve-flor", "Vegetal", 15, 
        "Baixo índice glicêmico, rica em fibras, vitaminas C e K. Auxilia no controle de glicemia.",
        "Ajuda na saúde óssea e promove saciedade.",
        "Pode ser consumida crua, cozida ou como substituto do arroz e purês.",
        "100g de couve-flor contém 25 calorias, 5g de carboidratos, 2g de proteína, 0,3g de gordura."),

        ("Cebolinha", "Vegetal", 15, 
        "Rica em antioxidantes e vitamina K, melhora a saúde óssea e cardiovascular.",
        "Ajuda na digestão e no controle da glicemia.",
        "Pode ser usada como tempero em saladas, sopas e pratos quentes.",
        "100g de cebolinha contém 32 calorias, 4,3g de carboidratos, 1,8g de proteína, 0,7g de gordura."),

        ("Alho", "Especiaria", 0, 
        "Possui propriedades anti-inflamatórias, antioxidantes e ajuda no controle da pressão arterial.",
        "Melhora a imunidade e auxilia no controle de glicemia.",
        "Pode ser usado como tempero em diversas preparações.",
        "100g de alho contém 149 calorias, 33g de carboidratos, 6,4g de proteína e 0,5g de gordura."),

        ("Pepino", "Vegetal", 15, 
        "Alimento hidratante, rico em fibras e com baixíssimo índice glicêmico.",
        "Promove saúde da pele e melhora a digestão.",
        "Pode ser consumido cru em saladas ou em sucos detox.",
        "100g de pepino contém 16 calorias, 3,6g de carboidratos, 0,7g de proteína, 0,1g de gordura."),

        ("Cebola", "Vegetal", 15, 
        "Rica em compostos antioxidantes e com propriedades anti-inflamatórias.",
        "Auxilia no controle de glicemia e melhora a circulação sanguínea.",
        "Pode ser consumida crua, refogada ou em sopas e ensopados.",
        "100g de cebola contém 40 calorias, 9g de carboidratos, 1,1g de proteína, 0,1g de gordura."),

        ("Moranga", "Vegetal", 30, 
        "Rica em fibras e betacaroteno, com baixo impacto glicêmico.",
        "Auxilia na saúde ocular e no controle de glicemia.",
        "Pode ser consumida cozida, assada ou em sopas.",
        "100g de moranga contém 26 calorias, 6g de carboidratos, 1g de proteína, 0g de gordura."),

        ("Alcachofra", "Vegetal", 20, 
        "Rica em fibras e antioxidantes, com baixo índice glicêmico.",
        "Ajuda na digestão, controle de glicemia e saúde do fígado.",
        "Pode ser consumida cozida ou em saladas.",
        "100g de alcachofra contém 47 calorias, 10g de carboidratos, 3g de proteína, 0,1g de gordura."),

        ("Quiabo", "Vegetal", 15, 
        "Rico em fibras e antioxidantes, melhora a digestão e o controle da glicemia.",
        "Auxilia na saúde cardiovascular e no controle de colesterol.",
        "Pode ser consumido cozido ou refogado.",
        "100g de quiabo contém 33 calorias, 7g de carboidratos, 1,9g de proteína, 0,2g de gordura."),

        ("Palmito", "Vegetal", 35, 
        "Baixo índice glicêmico, rico em fibras e minerais como potássio e ferro.",
        "Promove saciedade e melhora a digestão.",
        "Pode ser consumido em saladas ou refogados.",
        "100g de palmito contém 28 calorias, 4,6g de carboidratos, 1,8g de proteína, 0,2g de gordura."),

        ("Cogumelo (champignon)", "Vegetal", 15, 
        "Rico em proteínas, vitaminas do complexo B e antioxidantes.",
        "Ajuda na saúde cerebral, imunológica e controle de glicemia.",
        "Pode ser consumido grelhado, refogado ou em saladas.",
        "100g de cogumelo contém 22 calorias, 3,3g de carboidratos, 3,1g de proteína, 0,3g de gordura."),

        ("Salsinha", "Erva", 0, 
        "Rica em antioxidantes, vitamina C e ferro, ajuda na digestão e na imunidade.",
        "Auxilia no controle de glicemia e promove desintoxicação.",
        "Pode ser usada como tempero ou em sucos detox.",
        "100g de salsinha contém 36 calorias, 6g de carboidratos, 3g de proteína, 0,8g de gordura."),

        ("Rabanete", "Vegetal", 15, 
        "Rico em fibras e antioxidantes, com baixíssimo índice glicêmico.",
        "Promove saúde intestinal e ajuda no controle de glicemia.",
        "Pode ser consumido cru em saladas ou como acompanhamento.",
        "100g de rabanete contém 16 calorias, 3,4g de carboidratos, 0,7g de proteína, 0,1g de gordura."),

        ("Chuchu", "Vegetal", 15, 
        "Rico em fibras e com baixíssimo índice glicêmico.",
        "Auxilia na saúde digestiva e no controle de glicemia.",
        "Pode ser consumido cozido ou em refogados.",
        "100g de chuchu contém 19 calorias, 4,5g de carboidratos, 0,8g de proteína, 0,1g de gordura."),

        ("Nabo", "Vegetal", 30, 
        "Rico em fibras, vitaminas C e B6, com baixo impacto glicêmico.",
        "Promove saciedade e melhora a digestão.",
        "Pode ser consumido cru, em saladas, ou cozido.",
        "100g de nabo contém 28 calorias, 6,4g de carboidratos, 0,9g de proteína, 0,1g de gordura."), 
    
        ("Aspargos", "Vegetal", 15,
        "Rico em fibras, vitaminas A, C, E e K. Possui propriedades antioxidantes e anti-inflamatórias.",
        "Ajuda a melhorar a digestão, controlar a glicemia e promover a saúde cardiovascular.",
        "Pode ser consumido grelhado, cozido ou em saladas.",
        "100g de aspargos contém 20 calorias, 3,9g de carboidratos, 2,2g de proteína, 0,1g de gordura."),

        ("Cacau em pó", "Alimento", 20,
        "Rico em antioxidantes e flavonoides, que ajudam no controle da glicemia e da pressão arterial.",
        "Melhora o humor e promove a saúde cardiovascular.",
        "Pode ser usado em bebidas, receitas doces ou como tempero.",
        "100g de cacau em pó contém 228 calorias, 58g de carboidratos, 19g de proteína, 14g de gordura."),

        ("Endívia", "Vegetal", 15,
        "Rica em fibras, vitaminas A e K, com baixo índice glicêmico.",
        "Auxilia na digestão e promove a saúde intestinal.",
        "Pode ser consumida em saladas ou levemente grelhada.",
        "100g de endívia contém 17 calorias, 3,3g de carboidratos, 1,3g de proteína, 0,2g de gordura."),

        ("Acelga", "Vegetal", 15,
        "Fonte de fibras, vitaminas A e C, e antioxidantes que ajudam a reduzir a inflamação.",
        "Promove a saúde ocular e auxilia no controle de glicemia.",
        "Pode ser consumida crua em saladas ou refogada.",
        "100g de acelga contém 19 calorias, 3,7g de carboidratos, 1,8g de proteína, 0,2g de gordura."),

        ("Laranja", "Fruta", 45,
        "Rica em vitamina C, antioxidantes e fibras solúveis.",
        "Ajuda a fortalecer o sistema imunológico e controlar a glicemia.",
        "Pode ser consumida in natura ou como suco natural (sem açúcar).",
        "100g de laranja contém 47 calorias, 12g de carboidratos, 0,9g de proteína, 0,1g de gordura."),

        ("Kiwi", "Fruta", 50,
        "Rico em vitamina C, fibras e antioxidantes. Ajuda a controlar os níveis de glicose no sangue.",
        "Promove a saúde digestiva e melhora a imunidade.",
        "Ideal para consumo in natura, em saladas de frutas ou smoothies.",
        "100g de kiwi contém 61 calorias, 15g de carboidratos, 1,1g de proteína, 0,5g de gordura."),

        ("Couve de Bruxelas", "Vegetal", 20,
        "Rica em fibras, vitaminas C e K, com propriedades antioxidantes.",
        "Auxilia na digestão e no controle de glicemia.",
        "Pode ser consumida assada, cozida no vapor ou refogada.",
        "100g de couve de Bruxelas contém 43 calorias, 9g de carboidratos, 3,4g de proteína, 0,3g de gordura."),

        ("Abóbora Cabotiá", "Vegetal", 30,
        "Rica em fibras e betacaroteno, com baixo impacto glicêmico.",
        "Ajuda no controle da glicemia e promove a saúde ocular.",
        "Pode ser consumida assada, cozida ou em sopas.",
        "100g de abóbora cabotiá contém 34 calorias, 8g de carboidratos, 1g de proteína, 0,2g de gordura."),

        ("Alho-poró", "Vegetal", 15,
        "Fonte de fibras, vitaminas A, C e K. Possui propriedades antioxidantes.",
        "Promove a digestão e ajuda a controlar os níveis de glicose no sangue.",
        "Pode ser usado em sopas, refogados e como tempero em pratos.",
        "100g de alho-poró contém 61 calorias, 14g de carboidratos, 1,5g de proteína, 0,3g de gordura."),

        ("Mandioca-brava", "Tubérculo", 45,
        "Rica em carboidratos complexos e fibras, com índice glicêmico moderado.",
        "Ajuda a manter a energia e promove a saúde digestiva.",
        "Pode ser consumida cozida, assada ou em purês.",
        "100g de mandioca-brava contém 119 calorias, 28g de carboidratos, 1,2g de proteína, 0,2g de gordura."),

        ("Pitaya", "Fruta", 25,
        "Rica em fibras, vitamina C e antioxidantes, com baixo índice glicêmico.",
        "Ajuda na digestão e promove a saúde intestinal.",
        "Pode ser consumida in natura, em sucos ou smoothies.",
        "100g de pitaya contém 50 calorias, 11g de carboidratos, 1,2g de proteína, 0,4g de gordura."),

        ("Caju", "Fruta", 35,
        "Rico em vitamina C, antioxidantes e fibras, com índice glicêmico moderado.",
        "Ajuda na digestão e melhora a imunidade.",
        "Pode ser consumido in natura ou em sucos sem adição de açúcar.",
        "100g de caju contém 43 calorias, 9,2g de carboidratos, 1,5g de proteína, 0,1g de gordura."),

        ("Broto de feijão", "Vegetal", 15,
        "Rico em fibras, proteínas e antioxidantes, com baixo índice glicêmico.",
        "Ajuda na digestão e promove a saúde cardiovascular.",
        "Pode ser consumido cru em saladas ou levemente refogado.",
        "100g de broto de feijão contém 31 calorias, 6g de carboidratos, 3,2g de proteína, 0,1g de gordura."),

        ("Maracujá", "Fruta", 30,
        "Rico em fibras solúveis, vitamina C e antioxidantes.",
        "Ajuda a controlar os níveis de glicose e promove a saúde cardiovascular.",
        "Pode ser consumido in natura ou como suco natural sem açúcar.",
        "100g de maracujá contém 36 calorias, 9g de carboidratos, 1g de proteína, 0,4g de gordura."),

        ("Mamão", "Fruta", 60,
        "Rico em fibras, vitamina C e antioxidantes. Promove a saúde digestiva.",
        "Ajuda a controlar os níveis de glicemia e fortalece a imunidade.",
        "Pode ser consumido in natura ou em saladas de frutas.",
        "100g de mamão contém 43 calorias, 11g de carboidratos, 0,5g de proteína, 0,1g de gordura."),

        ("Semente de chia", "Semente", 15,
        "Rica em ômega-3, fibras e proteínas, com propriedades anti-inflamatórias.",
        "Promove a saciedade e ajuda no controle dos níveis de glicose.",
        "Pode ser usada em sucos, mingaus, iogurtes e receitas diversas.",
        "100g de semente de chia contém 486 calorias, 42g de carboidratos, 17g de proteína, 31g de gordura."),

        ("Beterraba dourada", "Vegetal", 25,
        "Fonte de antioxidantes, fibras e vitaminas, com índice glicêmico moderado.",
        "Ajuda na digestão e no controle dos níveis de glicose no sangue.",
        "Pode ser consumida assada, cozida ou em saladas.",
        "100g de beterraba dourada contém 43 calorias, 10g de carboidratos, 1,6g de proteína, 0,2g de gordura."),

        ("Mandioquinha", "Tubérculo", 60,
        "Rica em carboidratos complexos e fibras, com índice glicêmico moderado.",
        "Promove energia e melhora a saúde digestiva.",
        "Pode ser consumida cozida, assada ou em purês.",
        "100g de mandioquinha contém 101 calorias, 24g de carboidratos, 1,2g de proteína, 0,3g de gordura."),

        ("Romã", "Fruta", 35,
        "Rica em antioxidantes, vitamina C e fibras, com baixo índice glicêmico.",
        "Ajuda a controlar os níveis de glicose e melhora a saúde cardiovascular.",
        "Pode ser consumida in natura ou como suco natural.",
        "100g de romã contém 83 calorias, 19g de carboidratos, 1,7g de proteína, 1,2g de gordura."),

        ("Figo", "Fruta", 35,
        "Rico em fibras, antioxidantes e com índice glicêmico moderado.",
        "Ajuda a controlar os níveis de glicose e promove a saúde digestiva.",
        "Pode ser consumido in natura ou como complemento em saladas.",
        "100g de figo contém 74 calorias, 19g de carboidratos, 0,8g de proteína, 0,3g de gordura."),

        ("Couve kale", "Vegetal", 15,
        "Rica em fibras, antioxidantes e vitaminas A, C e K, com baixo índice glicêmico.",
        "Auxilia na saúde cardiovascular, controle da glicemia e digestão.",
        "Pode ser consumida em saladas, refogada ou em smoothies.",
        "100g de couve kale contém 49 calorias, 9g de carboidratos, 4g de proteína, 0,9g de gordura."),

        ("Amora", "Fruta", 25,
        "Rica em fibras, antioxidantes e vitamina C, com baixo índice glicêmico.",
        "Ajuda no controle da glicemia e combate os radicais livres.",
        "Pode ser consumida in natura, em sucos ou como topping para sobremesas.",
        "100g de amora contém 43 calorias, 10g de carboidratos, 1g de proteína, 0,4g de gordura."),

        ("Damascos secos", "Fruta", 40,
        "Fonte de fibras, potássio e ferro, com baixo índice glicêmico.",
        "Promove saciedade e ajuda na saúde cardiovascular.",
        "Pode ser consumido como lanche ou adicionado a saladas e sobremesas.",
        "100g de damascos secos contém 241 calorias, 63g de carboidratos, 3,4g de proteína, 0,5g de gordura."),

        ("Cevada", "Cereal", 55,
        "Rica em fibras solúveis, ajuda a estabilizar os níveis de açúcar no sangue.",
        "Promove saciedade, melhora a saúde digestiva e cardiovascular.",
        "Pode ser usada em sopas, saladas ou como substituto de arroz.",
        "100g de cevada contém 354 calorias, 73g de carboidratos, 12g de proteína, 2,3g de gordura."),

        ("Pecã", "Oleaginosa", 15,
        "Rica em gorduras monoinsaturadas, fibras e antioxidantes.",
        "Ajuda no controle da glicemia e na saúde cardiovascular.",
        "Pode ser consumida como lanche ou adicionada a sobremesas.",
        "100g de pecã contém 691 calorias, 14g de carboidratos, 9g de proteína, 72g de gordura."),

        ("Abacate hass", "Fruta", 15,
        "Rico em gorduras saudáveis, fibras e vitaminas, com baixíssimo índice glicêmico.",
        "Ajuda no controle de glicemia, saúde cardiovascular e saciedade.",
        "Pode ser consumido in natura, em saladas ou smoothies.",
        "100g de abacate hass contém 160 calorias, 9g de carboidratos, 2g de proteína, 15g de gordura."),

        ("Quiuí dourado", "Fruta", 45,
        "Rico em fibras, vitamina C e antioxidantes, com baixo índice glicêmico.",
        "Ajuda no controle de glicemia e promove a saúde digestiva.",
        "Ideal para consumo in natura ou em saladas de frutas.",
        "100g de quiuí dourado contém 60 calorias, 15g de carboidratos, 1,2g de proteína, 0,4g de gordura."),

        ("Grãos integrais (milho)", "Cereal", 55,
        "Rico em fibras, vitaminas do complexo B e antioxidantes.",
        "Ajuda no controle de glicemia e na saúde digestiva.",
        "Pode ser consumido cozido, em saladas ou sopas.",
        "100g de milho integral contém 96 calorias, 21g de carboidratos, 3g de proteína, 1g de gordura."),

        ("Batata-doce roxa", "Tubérculo", 54,
        "Fonte de carboidratos de baixo índice glicêmico, rica em fibras e antioxidantes.",
        "Ajuda na saúde intestinal e no controle de glicemia.",
        "Pode ser consumida cozida, assada ou em purês.",
        "100g de batata-doce roxa contém 86 calorias, 20g de carboidratos, 1,2g de proteína, 0,1g de gordura."),

        ("Cacau cru", "Alimento", 20,
        "Rico em antioxidantes e flavonoides, com baixo índice glicêmico.",
        "Promove a saúde cardiovascular e ajuda no controle da glicemia.",
        "Pode ser usado em smoothies, sobremesas ou bebidas.",
        "100g de cacau cru contém 228 calorias, 57g de carboidratos, 19g de proteína, 14g de gordura."),

        ("Feijão azuki", "Leguminosa", 35,
        "Rico em proteínas, fibras e antioxidantes, com baixo índice glicêmico.",
        "Ajuda no controle de glicemia e melhora a saúde digestiva.",
        "Pode ser usado em sopas, saladas ou como acompanhamento.",
        "100g de feijão azuki contém 329 calorias, 63g de carboidratos, 20g de proteína, 0,1g de gordura."),

        ("Ervilha torta", "Leguminosa", 32,
        "Rica em fibras, proteínas e vitaminas, com baixo índice glicêmico.",
        "Auxilia no controle de glicemia e promove a saúde cardiovascular.",
        "Pode ser consumida crua, cozida ou em saladas.",
        "100g de ervilha torta contém 42 calorias, 7g de carboidratos, 2,8g de proteína, 0,2g de gordura."),

        ("Alcachofra de Jerusalém", "Vegetal", 20,
        "Rica em fibras e prebióticos, ajuda no controle de glicemia e saúde intestinal.",
        "Promove a digestão e melhora a imunidade.",
        "Pode ser consumida cozida, assada ou em saladas.",
        "100g de alcachofra de Jerusalém contém 73 calorias, 17g de carboidratos, 2g de proteína, 0,1g de gordura."),

        ("Tomate cereja", "Vegetal", 15,
        "Baixo índice glicêmico, rico em antioxidantes e licopeno.",
        "Ajuda a combater inflamações e promove a saúde cardiovascular.",
        "Pode ser consumido cru, em saladas ou como snack saudável.",
        "100g de tomate cereja contém 18 calorias, 3,9g de carboidratos, 0,9g de proteína, 0,2g de gordura."),

        ("Cenoura baby", "Vegetal", 35,
        "Rica em fibras e betacaroteno, com índice glicêmico moderado.",
        "Ajuda na saúde ocular e no controle de glicemia.",
        "Pode ser consumida crua, cozida ou como snack.",
        "100g de cenoura baby contém 35 calorias, 8g de carboidratos, 1g de proteína, 0,2g de gordura."),

        ("Linhaça dourada", "Semente", 15,
        "Rica em ômega-3, fibras e antioxidantes, com baixo índice glicêmico.",
        "Ajuda no controle de glicemia e promove a saúde cardiovascular.",
        "Pode ser consumida em sucos, iogurtes ou pães.",
        "100g de linhaça dourada contém 534 calorias, 29g de carboidratos, 18g de proteína, 42g de gordura."),

        ("Fruta do dragão (pitaya branca)", "Fruta", 25,
        "Rica em fibras, vitamina C e antioxidantes, com baixo índice glicêmico.",
        "Promove a digestão e melhora a saúde intestinal.",
        "Pode ser consumida in natura ou em smoothies.",
        "100g de pitaya branca contém 50 calorias, 11g de carboidratos, 1,2g de proteína, 0,4g de gordura."),

        ("Rabanete branco (daikon)", "Vegetal", 15,
        "Rico em fibras, antioxidantes e vitamina C, com baixo índice glicêmico.",
        "Ajuda na digestão e promove a saúde cardiovascular.",
        "Pode ser consumido cru, ralado ou em refogados.",
        "100g de rabanete branco contém 18 calorias, 4g de carboidratos, 0,6g de proteína, 0,1g de gordura."),

        ("Berinjela japonesa", "Vegetal", 15,
        "Baixíssimo índice glicêmico, rica em fibras e antioxidantes.",
        "Promove a saciedade e melhora o controle de glicemia.",
        "Pode ser consumida assada, grelhada ou em refogados.",
        "100g de berinjela japonesa contém 24 calorias, 5,5g de carboidratos, 1g de proteína, 0,2g de gordura."),

        ("Broto de bambu", "Vegetal", 15,
        "Baixo índice glicêmico, rico em fibras e antioxidantes.",
        "Auxilia na saúde digestiva e no controle de glicemia.",
        "Pode ser consumido em saladas ou refogados.",
        "100g de broto de bambu contém 27 calorias, 5g de carboidratos, 2,6g de proteína, 0,3g de gordura.")
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
     """1. Corte o abacate em cubos médios.
        2. Pique o tomate e a cebola roxa em pedaços pequenos.
        3. Em uma tigela, misture o feijão preto cozido com o abacate, o tomate e a cebola.
        4. Regue com azeite e suco de limão. Tempere com sal e pimenta a gosto.
        5. Mexa delicadamente para não amassar o abacate. Sirva imediatamente.""",
     "Uma refeição saudável, rica em fibras e antioxidantes, ideal para o controle de glicemia."),

    ("Aveia com maçã e canela",
     "Aveia, Maçã, Leite desnatado (ou bebida vegetal), Canela em pó",
     """1. Em uma panela, coloque a aveia e o leite. Cozinhe em fogo médio, mexendo ocasionalmente, até atingir a consistência desejada.
        2. Enquanto a aveia cozinha, lave e pique a maçã em cubos pequenos.
        3. Quando a aveia estiver pronta, coloque em um prato ou tigela. Adicione a maçã por cima.
        4. Polvilhe canela em pó e, se desejar, acrescente mel ou adoçante natural. Sirva quente.""",
     "Uma excelente opção para o café da manhã, promovendo saciedade e controle glicêmico."),

    ("Sopa de lentilha com legumes",
     "Lentilha, Cenoura, Abobrinha, Cebola, Alho, Caldo de legumes sem sal, Temperos a gosto",
     """1. Lave a lentilha e deixe de molho por 1 hora para reduzir o tempo de cozimento.
        2. Pique a cenoura, a abobrinha e a cebola em cubos pequenos.
        3. Em uma panela grande, aqueça azeite e refogue o alho e a cebola até dourarem levemente.
        4. Adicione a lentilha escorrida, a cenoura, a abobrinha e o caldo de legumes.
        5. Cozinhe em fogo médio até que a lentilha esteja macia. Ajuste o tempero com sal, pimenta e ervas a gosto. Sirva quente.""",
     "Uma refeição leve, rica em proteínas vegetais e fibras, ideal para o controle glicêmico."),

    ("Frango grelhado com brócolis",
     "Peito de frango, Brócolis, Azeite, Alho, Sal, Pimenta",
     """1. Tempere os filés de frango com sal, pimenta e um fio de azeite. Deixe marinar por 20 minutos.
        2. Aqueça uma frigideira ou grelha e cozinhe os filés por 4-5 minutos de cada lado, até dourar.
        3. Lave o brócolis e cozinhe no vapor por 5 minutos, até ficar al dente.
        4. Em uma frigideira, aqueça azeite e refogue o alho picado. Misture o brócolis com o alho refogado.
        5. Sirva o frango grelhado acompanhado do brócolis.""",
     "Frango magro, combinado com brócolis, é uma refeição rica em proteínas e antioxidantes."),

    ("Bowl de quinoa com legumes",
     "Quinoa, Tomate-cereja, Alface, Cenoura ralada, Pepino, Azeite, Limão, Sal",
     """1. Lave a quinoa em água corrente. Cozinhe em uma panela com água e sal por 15 minutos ou até a água secar.
        2. Enquanto isso, corte o tomate-cereja ao meio, rale a cenoura e fatie o pepino em rodelas finas.
        3. Em uma tigela grande, misture a quinoa cozida com os legumes e as folhas de alface.
        4. Tempere com azeite, suco de limão, sal e pimenta a gosto. Misture bem e sirva.""",
     "Uma refeição leve, rica em fibras, que promove saciedade e controle glicêmico."),

    ("Peixe assado com legumes",
     "Peixe (salmão ou tilápia), Abobrinha, Cenoura, Cebola, Azeite, Ervas finas, Sal",
     """1. Tempere o peixe com sal, ervas finas e um fio de azeite. Deixe descansar por 15 minutos.
        2. Lave e corte a abobrinha e a cenoura em rodelas finas. Corte a cebola em fatias.
        3. Em uma assadeira, disponha os legumes e coloque o peixe por cima.
        4. Regue com mais azeite e cubra a assadeira com papel alumínio.
        5. Asse em forno preaquecido a 200°C por 20 minutos. Remova o papel alumínio e asse por mais 5 minutos para dourar.
        6. Sirva quente.""",
     "Rico em ômega-3 e antioxidantes, este prato ajuda a melhorar a saúde cardiovascular e controlar a glicemia."),

    ("Panqueca de banana e aveia",
     "1 banana madura, 2 colheres (sopa) de aveia, 1 ovo, Canela a gosto",
     """1. Amasse bem a banana com um garfo até formar um purê.
        2. Misture a banana amassada com o ovo e a aveia até obter uma massa homogênea.
        3. Adicione canela a gosto e misture bem.
        4. Aqueça uma frigideira antiaderente em fogo médio e unte com um fio de óleo, se necessário.
        5. Coloque pequenas porções da massa na frigideira e cozinhe por 2-3 minutos de cada lado, até dourar.
        6. Sirva quente, acompanhado de frutas ou mel.""",
     "Uma refeição rápida e saudável, ótima para o café da manhã."),

    ("Arroz de couve-flor",
     "Couve-flor, Alho, Cebola, Azeite, Sal",
     """1. Lave bem a couve-flor e seque-a com papel-toalha para remover o excesso de umidade.
        2. Corte a couve-flor em pedaços pequenos e coloque no processador de alimentos. Triture até obter uma textura semelhante a grãos de arroz.
        3. Pique finamente o alho e a cebola.
        4. Em uma frigideira grande, aqueça o azeite em fogo médio. Refogue o alho e a cebola até dourarem levemente e liberarem aroma.
        5. Adicione a couve-flor triturada à frigideira e misture bem.
        6. Refogue por cerca de 5-7 minutos, mexendo ocasionalmente, até que a couve-flor esteja cozida, mas ainda firme.
        7. Tempere com sal a gosto. Se desejar, adicione ervas frescas ou outros temperos para realçar o sabor.
        8. Sirva quente como acompanhamento ou substituto do arroz em pratos principais.""",
     "Uma ótima substituição para o arroz branco, com baixo impacto glicêmico."),

    ("Espaguete de abobrinha",
     "Abobrinha, Alho, Azeite, Manjericão, Tomate-cereja",
     """1. Lave bem a abobrinha e seque-a com papel-toalha.
        2. Usando um espiralizador ou um ralador de legumes, corte a abobrinha em tiras finas para formar o "espaguete".
        3. Corte os tomates-cereja ao meio e pique finamente o alho.
        4. Em uma frigideira grande, aqueça o azeite em fogo médio. Refogue o alho até dourar levemente, tomando cuidado para não queimar.
        5. Adicione o "espaguete" de abobrinha à frigideira e misture bem. Refogue por 2-3 minutos, mexendo ocasionalmente, para aquecer e amolecer levemente, sem deixar que os fios de abobrinha percam a textura.
        6. Acrescente os tomates-cereja e misture rapidamente para aquecê-los.
        7. Rasgue as folhas de manjericão fresco com as mãos e adicione à frigideira.
        8. Tempere com sal e pimenta a gosto. Se desejar, finalize com um fio de azeite extra virgem antes de servir.
        9. Sirva imediatamente como prato principal ou acompanhamento saudável.""",
     "Uma alternativa saudável ao espaguete tradicional, com menos carboidratos."),

     ("Salada de quinoa com legumes",
     "Quinoa, Cenoura, Pepino, Tomate-cereja, Cebola roxa, Azeite, Limão, Sal, Salsinha",
     """1. Lave bem a quinoa em água corrente e cozinhe em água fervente com uma pitada de sal por 12-15 minutos ou até que os grãos estejam macios.
        2. Escorra a quinoa, deixe esfriar e transfira para uma tigela grande.
        3. Corte a cenoura e o pepino em cubos pequenos, e os tomates-cereja ao meio. Pique finamente a cebola roxa e a salsinha.
        4. Adicione os legumes e a salsinha à tigela com a quinoa.
        5. Misture o azeite, o suco de limão e o sal em um recipiente separado para fazer o molho.
        6. Regue a salada com o molho, misture bem e sirva imediatamente.""",
     "Uma refeição leve, rica em fibras e proteínas vegetais, com baixo impacto glicêmico."),

    ("Omelete de espinafre com queijo branco",
     "Ovos, Espinafre, Queijo branco, Azeite, Sal, Pimenta-do-reino",
     """1. Bata os ovos em uma tigela com sal e pimenta a gosto.
        2. Lave e pique as folhas de espinafre. Corte o queijo branco em cubos pequenos.
        3. Aqueça o azeite em uma frigideira antiaderente em fogo médio e refogue o espinafre até murchar.
        4. Adicione os ovos batidos à frigideira, espalhando uniformemente.
        5. Distribua os cubos de queijo branco sobre o omelete.
        6. Cozinhe em fogo baixo até que os ovos estejam firmes. Dobre ao meio e sirva quente.""",
     "Uma opção rica em proteínas e com baixo impacto glicêmico, ideal para o café da manhã ou jantar."),

    ("Sopa cremosa de abobrinha",
     "Abobrinha, Cebola, Alho, Caldo de legumes sem sal, Azeite, Sal, Pimenta",
     """1. Lave e corte a abobrinha em pedaços médios. Pique a cebola e o alho.
        2. Aqueça o azeite em uma panela e refogue a cebola e o alho até ficarem macios.
        3. Adicione a abobrinha e refogue por mais 3 minutos.
        4. Acrescente o caldo de legumes até cobrir os ingredientes e deixe cozinhar por 15 minutos.
        5. Bata a sopa no liquidificador até obter um creme homogêneo.
        6. Tempere com sal e pimenta a gosto. Volte à panela para aquecer e sirva.""",
     "Uma sopa leve e nutritiva, perfeita para o jantar ou dias mais frios."),

    ("Bolo de cenoura com farinha de amêndoas",
     "Cenoura, Farinha de amêndoas, Ovos, Adoçante culinário, Fermento em pó, Canela",
     """1. Rale a cenoura finamente e reserve.
        2. Em uma tigela, bata os ovos com o adoçante até obter uma mistura homogênea.
        3. Adicione a cenoura ralada, a farinha de amêndoas e uma pitada de canela. Misture bem.
        4. Acrescente o fermento em pó e mexa delicadamente.
        5. Despeje a massa em uma forma untada e asse em forno pré-aquecido a 180°C por 30-40 minutos.
        6. Retire do forno, deixe esfriar e sirva.""",
     "Uma opção saudável e sem açúcar refinado para sobremesas ou lanches."),

    ("Hambúrguer de grão-de-bico",
     "Grão-de-bico cozido, Cebola, Alho, Salsinha, Azeite, Sal, Pimenta, Farinha de aveia",
     """1. No processador, triture o grão-de-bico até obter uma pasta grossa.
        2. Pique finamente a cebola, o alho e a salsinha. Adicione à mistura de grão-de-bico.
        3. Tempere com sal, pimenta e um fio de azeite. Misture bem.
        4. Acrescente a farinha de aveia aos poucos até dar liga.
        5. Molde hambúrgueres e leve à frigideira antiaderente com azeite, dourando dos dois lados.
        6. Sirva no pão integral com salada ou como acompanhamento.""",
     "Um hambúrguer nutritivo, rico em proteínas vegetais e fibras."),

    ("Smoothie verde detox",
     "Espinafre, Abacaxi, Limão, Gengibre, Água de coco, Adoçante opcional",
     """1. Lave bem as folhas de espinafre. Descasque o abacaxi e corte em pedaços.
        2. No liquidificador, adicione o espinafre, o abacaxi, o suco de limão e um pedaço pequeno de gengibre.
        3. Acrescente a água de coco e bata até obter uma mistura homogênea.
        4. Prove e, se necessário, adicione adoçante.
        5. Sirva imediatamente em copos altos.""",
     "Uma bebida refrescante e cheia de nutrientes, ideal para começar o dia."),

    ("Quibe assado de abóbora",
     "Abóbora, Trigo para quibe, Hortelã, Cebola, Sal, Azeite",
     """1. Cozinhe a abóbora até ficar macia e amasse formando um purê.
        2. Hidrate o trigo para quibe conforme as instruções da embalagem e escorra bem.
        3. Misture o trigo com o purê de abóbora, a hortelã picada, a cebola ralada e o sal.
        4. Unte uma assadeira com azeite, despeje a mistura e alise a superfície.
        5. Asse em forno pré-aquecido a 200°C por 30 minutos ou até dourar.
        6. Sirva quente com uma salada fresca.""",
     "Uma alternativa saudável e deliciosa ao quibe tradicional."),

    ("Pasta de ricota com ervas",
     "Ricota, Salsinha, Cebolinha, Manjericão, Azeite, Sal",
     """1. Esfarele a ricota em uma tigela.
        2. Pique finamente a salsinha, a cebolinha e o manjericão.
        3. Misture as ervas com a ricota, adicionando azeite aos poucos até obter uma consistência cremosa.
        4. Tempere com sal a gosto.
        5. Sirva como acompanhamento para pães integrais ou torradas.""",
     "Uma pasta leve e saudável, rica em proteínas e fácil de preparar."),

    ("Salmão grelhado com molho de limão",
     "Filé de salmão, Limão, Alho, Azeite, Sal, Pimenta, Ervas frescas",
     """1. Tempere o filé de salmão com sal, pimenta, alho picado e suco de limão. Deixe marinar por 15 minutos.
        2. Aqueça uma frigideira antiaderente com um fio de azeite.
        3. Grelhe o salmão por 3-4 minutos de cada lado, até dourar.
        4. Retire o salmão e reserve. Na mesma frigideira, adicione mais suco de limão e ervas frescas, mexendo rapidamente para formar o molho.
        5. Sirva o salmão com o molho por cima.""",
     "Rico em ômega-3, este prato é perfeito para a saúde cardiovascular."),

    ("Biscoito de aveia e banana",
     "Banana madura, Aveia em flocos, Canela, Essência de baunilha, Coco ralado (opcional)",
     """1. Amasse a banana até formar um purê.
        2. Misture a banana amassada com a aveia em flocos, a canela e a essência de baunilha.
        3. Adicione coco ralado se desejar.
        4. Modele pequenos biscoitos e disponha em uma assadeira untada ou forrada com papel manteiga.
        5. Asse em forno pré-aquecido a 180°C por 15-20 minutos, até dourarem levemente.
        6. Retire do forno, deixe esfriar e sirva.""",
     "Biscoitos simples e saudáveis, perfeitos para lanches rápidos."),

     ("Cuscuz de quinoa com legumes",
     "Quinoa, Cenoura, Abobrinha, Tomate, Cebola, Azeite, Limão, Salsinha, Sal",
     """1. Lave bem a quinoa e cozinhe em água com uma pitada de sal por 12-15 minutos. Escorra e reserve.
        2. Rale a cenoura, corte a abobrinha em cubos pequenos e o tomate em pedaços.
        3. Em uma frigideira, aqueça o azeite e refogue a cebola até ficar macia.
        4. Adicione os legumes, refogue por 5 minutos e misture a quinoa.
        5. Tempere com limão, sal e salsinha picada. Sirva quente ou frio.""",
     "Uma refeição nutritiva e leve, com baixo impacto glicêmico."),

    ("Salada de folhas verdes com abacate e nozes",
     "Alface, Rúcula, Espinafre, Abacate, Nozes, Azeite, Limão, Sal",
     """1. Lave bem as folhas verdes e seque com cuidado.
        2. Corte o abacate em fatias finas e pique as nozes.
        3. Em uma tigela, misture as folhas, o abacate e as nozes.
        4. Tempere com azeite, suco de limão e sal a gosto. Sirva imediatamente.""",
     "Rica em fibras e gorduras boas, ideal para uma refeição leve."),

    ("Torta salgada de legumes com farinha de aveia",
     "Farinha de aveia, Ovos, Abobrinha, Cenoura, Tomate, Azeite, Sal, Fermento",
     """1. Rale a abobrinha e a cenoura. Corte o tomate em cubos pequenos.
        2. Em uma tigela, bata os ovos e misture com a farinha de aveia, formando uma massa homogênea.
        3. Adicione os legumes e tempere com sal.
        4. Acrescente o fermento e misture delicadamente.
        5. Despeje a mistura em uma forma untada e asse em forno pré-aquecido a 180°C por 30 minutos.
        6. Retire do forno, deixe esfriar levemente e sirva.""",
     "Uma torta prática, rica em fibras e com baixo índice glicêmico."),

    ("Patê de grão-de-bico com ervas",
     "Grão-de-bico cozido, Alho, Limão, Azeite, Salsinha, Sal, Pimenta",
     """1. No processador, bata o grão-de-bico com alho, suco de limão e azeite até obter uma pasta.
        2. Adicione a salsinha picada, sal e pimenta a gosto.
        3. Misture bem e sirva com torradas integrais ou vegetais crus.""",
     "Um patê rico em proteínas vegetais e com baixo impacto glicêmico."),

    ("Salada morna de lentilha com espinafre",
     "Lentilha, Espinafre, Alho, Azeite, Sal, Pimenta, Suco de limão",
     """1. Cozinhe a lentilha em água com sal até ficar macia, mas firme. Escorra e reserve.
        2. Aqueça o azeite em uma frigideira e refogue o alho picado.
        3. Adicione o espinafre e mexa até murchar levemente.
        4. Misture a lentilha cozida, tempere com sal, pimenta e suco de limão. Sirva morno.""",
     "Uma refeição leve e rica em fibras e proteínas vegetais."),

    ("Panqueca de espinafre com ricota",
     "Farinha de aveia, Espinafre, Ricota, Ovo, Leite desnatado, Azeite, Sal",
     """1. Bata o espinafre, o ovo, o leite e a farinha de aveia no liquidificador até obter uma massa homogênea.
        2. Aqueça uma frigideira antiaderente com um fio de azeite e despeje uma porção da massa, espalhando bem.
        3. Cozinhe até dourar dos dois lados e repita com o restante da massa.
        4. Recheie as panquecas com ricota temperada com sal e azeite.
        5. Dobre as panquecas e sirva quente.""",
     "Uma opção leve e nutritiva para refeições principais."),

    ("Bolinho de batata-doce com frango",
     "Batata-doce, Peito de frango, Azeite, Cebola, Alho, Sal, Pimenta",
     """1. Cozinhe a batata-doce até ficar macia e amasse formando um purê.
        2. Cozinhe o peito de frango, desfie e tempere com cebola, alho, sal e pimenta.
        3. Misture o purê de batata-doce com o frango desfiado até formar uma massa.
        4. Modele bolinhos e asse em forno pré-aquecido a 200°C por 20 minutos ou até dourar.
        5. Sirva com uma salada fresca.""",
     "Uma opção rica em proteínas e com carboidratos de baixo índice glicêmico."),

    ("Creme de abacate com cacau",
     "Abacate, Cacau em pó, Adoçante, Essência de baunilha",
     """1. Corte o abacate ao meio, retire o caroço e retire a polpa com uma colher.
        2. No liquidificador, bata o abacate com cacau em pó, adoçante e essência de baunilha até obter um creme homogêneo.
        3. Transfira para tigelas individuais e leve à geladeira por 30 minutos antes de servir.""",
     "Uma sobremesa saudável, rica em gorduras boas e sem açúcar refinado."),

    ("Abobrinha recheada com carne moída",
     "Abobrinha, Carne moída magra, Tomate, Cebola, Alho, Azeite, Sal, Pimenta",
     """1. Corte a abobrinha ao meio no sentido do comprimento e retire parte da polpa, formando barquinhas.
        2. Refogue a carne moída com alho, cebola, tomate picado, sal e pimenta.
        3. Recheie as abobrinhas com a carne moída e disponha em uma assadeira.
        4. Regue com azeite e leve ao forno pré-aquecido a 180°C por 20 minutos.
        5. Sirva quente com uma salada verde.""",
     "Uma refeição completa, rica em proteínas e com baixo impacto glicêmico."),

    ("Iogurte com frutas vermelhas e chia",
     "Iogurte natural sem açúcar, Morango, Mirtilo, Chia, Adoçante",
     """1. Lave e corte os morangos em pedaços pequenos.
        2. Em um recipiente, misture o iogurte natural com os morangos, mirtilos e sementes de chia.
        3. Adicione adoçante a gosto, misture bem e deixe descansar por 10 minutos para a chia hidratar.
        4. Sirva como café da manhã ou lanche.""",
     "Rico em fibras, antioxidantes e proteínas, perfeito para o dia a dia."),

     ("Salada de rúcula com abacate e sementes de girassol",
     "Rúcula, Abacate, Sementes de girassol, Limão, Azeite, Sal, Pimenta",
     """1. Lave e seque as folhas de rúcula.
        2. Corte o abacate em fatias ou cubos pequenos.
        3. Em uma tigela, misture a rúcula, o abacate e as sementes de girassol.
        4. Tempere com suco de limão, azeite, sal e pimenta a gosto. Sirva imediatamente.""",
     "Uma salada leve, rica em gorduras boas e fibras."),

    ("Sopa de couve-flor com alho-poró",
     "Couve-flor, Alho-poró, Caldo de legumes sem sal, Azeite, Sal, Pimenta",
     """1. Lave e corte a couve-flor em pedaços pequenos.
        2. Fatie o alho-poró e refogue em azeite até dourar levemente.
        3. Adicione a couve-flor e o caldo de legumes, cozinhando até amaciar.
        4. Bata no liquidificador até obter um creme homogêneo.
        5. Tempere com sal e pimenta a gosto. Sirva quente.""",
     "Uma sopa nutritiva e cremosa, perfeita para jantares leves."),

    ("Panqueca de espinafre com cogumelos",
     "Farinha de aveia, Espinafre, Cogumelos, Ovos, Leite desnatado, Azeite, Sal, Pimenta",
     """1. Bata o espinafre, os ovos, o leite e a farinha de aveia no liquidificador.
        2. Aqueça uma frigideira e prepare as panquecas.
        3. Refogue os cogumelos fatiados com azeite, sal e pimenta.
        4. Recheie as panquecas com os cogumelos e sirva.""",
     "Rico em fibras e proteínas, ideal para refeições rápidas."),

    ("Arroz integral com grão-de-bico e legumes",
     "Arroz integral, Grão-de-bico, Cenoura, Brócolis, Alho, Azeite, Sal",
     """1. Cozinhe o arroz integral conforme as instruções da embalagem.
        2. Cozinhe o grão-de-bico e os legumes no vapor.
        3. Refogue o alho no azeite, misture o arroz, o grão-de-bico e os legumes.
        4. Tempere com sal a gosto e sirva quente.""",
     "Um prato completo, rico em fibras e proteínas vegetais."),

    ("Smoothie de abacate e espinafre",
     "Abacate, Espinafre, Leite de amêndoas, Limão, Gengibre, Adoçante",
     """1. Coloque todos os ingredientes no liquidificador e bata até obter uma consistência cremosa.
        2. Ajuste o adoçante a gosto e sirva gelado.""",
     "Uma bebida nutritiva e rica em gorduras saudáveis."),

    ("Frango ao curry com leite de coco",
     "Peito de frango, Leite de coco, Curry, Cebola, Alho, Azeite, Sal",
     """1. Corte o frango em cubos e tempere com sal e curry.
        2. Refogue a cebola e o alho no azeite.
        3. Adicione o frango e cozinhe até dourar.
        4. Acrescente o leite de coco e cozinhe por mais 10 minutos.
        5. Sirva com legumes no vapor.""",
     "Um prato aromático e rico em proteínas, com baixo índice glicêmico."),

    ("Pão de aveia e linhaça",
     "Farinha de aveia, Linhaça, Ovos, Iogurte natural, Fermento, Sal",
     """1. Misture todos os ingredientes em uma tigela até formar uma massa homogênea.
        2. Despeje em uma forma e asse em forno pré-aquecido a 180°C por 30 minutos.
        3. Deixe esfriar antes de servir.""",
     "Uma alternativa saudável ao pão tradicional, rico em fibras."),

    ("Salada de quinoa com abóbora assada",
     "Quinoa, Abóbora, Azeite, Salsinha, Sal, Pimenta",
     """1. Cozinhe a quinoa conforme as instruções da embalagem.
        2. Asse a abóbora com azeite, sal e pimenta até dourar.
        3. Misture a quinoa, a abóbora e a salsinha. Sirva morno ou frio.""",
     "Uma salada equilibrada, rica em fibras e nutrientes."),

    ("Macarrão de abobrinha ao pesto",
     "Abobrinha, Manjericão, Azeite, Nozes, Alho, Sal",
     """1. Corte a abobrinha em formato de macarrão usando um espiralizador.
        2. Prepare o molho pesto batendo o manjericão, as nozes, o alho e o azeite no processador.
        3. Misture o molho com a abobrinha e sirva.""",
     "Uma alternativa de baixa caloria e rica em gorduras boas ao macarrão tradicional."),

    ("Bolo de maçã com farinha de coco",
     "Maçã, Farinha de coco, Ovos, Canela, Adoçante, Fermento",
     """1. Bata os ovos com o adoçante e a canela.
        2. Adicione a farinha de coco e misture bem.
        3. Acrescente o fermento e as maçãs em pedaços.
        4. Asse em forno pré-aquecido a 180°C por 30 minutos.""",
     "Uma sobremesa saudável e sem glúten, com baixo índice glicêmico."),

    ("Crepioca recheada com frango e espinafre",
     "Farinha de tapioca, Ovo, Frango desfiado, Espinafre, Azeite, Sal",
     """1. Misture a tapioca com o ovo até formar uma massa homogênea.
        2. Cozinhe a massa em uma frigideira para formar a crepioca.
        3. Recheie com frango desfiado e espinafre refogado.""",
     "Uma refeição leve e prática, rica em proteínas."),

    ("Mousse de chocolate com abacate",
     "Abacate, Cacau em pó, Adoçante, Essência de baunilha",
     """1. Bata todos os ingredientes no liquidificador até obter uma mistura cremosa.
        2. Leve à geladeira por 2 horas antes de servir.""",
     "Uma sobremesa rica em gorduras boas e antioxidantes."),

    ("Tartar de atum com abacate",
     "Atum fresco, Abacate, Limão, Azeite, Sal, Pimenta",
     """1. Corte o atum e o abacate em cubos pequenos.
        2. Tempere com limão, azeite, sal e pimenta.
        3. Misture delicadamente e sirva.""",
     "Uma entrada sofisticada e saudável, rica em ômega-3."),

    ("Salada de pepino com iogurte e hortelã",
     "Pepino, Iogurte natural, Hortelã, Azeite, Sal",
     """1. Corte o pepino em rodelas finas.
        2. Misture com o iogurte, hortelã picada, azeite e sal.
        3. Sirva gelado.""",
     "Uma salada refrescante e leve, perfeita para dias quentes."),

    ("Hambúrguer de lentilha",
     "Lentilha, Cebola, Alho, Azeite, Sal, Farinha de aveia",
     """1. Cozinhe a lentilha até ficar macia.
        2. Bata no processador com os temperos e a farinha de aveia.
        3. Modele os hambúrgueres e asse ou grelhe.""",
     "Uma alternativa vegetariana rica em proteínas e fibras."),

    ("Salmão grelhado com molho de maracujá",
     "Salmão, Maracujá, Adoçante, Azeite, Sal",
     """1. Tempere o salmão com sal e grelhe até dourar.
        2. Prepare o molho reduzindo o suco de maracujá com adoçante.
        3. Sirva o salmão com o molho por cima.""",
     "Rico em ômega-3, ideal para a saúde cardiovascular."),

    ("Wrap de alface com frango desfiado",
     "Folhas de alface, Frango desfiado, Cenoura ralada, Azeite, Limão, Sal",
     """1. Recheie as folhas de alface com o frango e a cenoura.
        2. Tempere com azeite, limão e sal antes de enrolar.""",
     "Um lanche prático, leve e nutritivo."),

    ("Biscoito salgado de grão-de-bico",
     "Grão-de-bico, Azeite, Sal, Ervas",
     """1. Bata o grão-de-bico no processador até formar uma massa.
        2. Misture azeite, sal e ervas.
        3. Modele os biscoitos e asse.""",
     "Um snack saudável e rico em proteínas vegetais."),

    ("Purê de couve-flor",
     "Couve-flor, Azeite, Alho, Sal",
     """1. Cozinhe a couve-flor até ficar macia.
        2. Bata no processador com azeite, alho e sal.""",
     "Um acompanhamento leve e com baixo índice glicêmico."),

    ("Risoto de quinoa com cogumelos",
     "Quinoa, Cogumelos, Alho, Caldo de legumes, Azeite, Sal",
     """1. Cozinhe a quinoa no caldo de legumes.
        2. Refogue os cogumelos no azeite com alho.
        3. Misture a quinoa com os cogumelos e sirva.""",
     "Um prato sofisticado, rico em proteínas e fibras.")

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
