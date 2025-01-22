from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
app.config['DATABASE'] = 'database.db'

# Dicionário de mapeamento de imagens para receitas
RECIPE_IMAGE_MAP = {
    "Arroz de couve-flor": "arroz_couveflor.jpg",
    "Aveia com maçã e canela": "aveia_maca.jpg",
    "Bolo de banana saudável": "bolo_banana.jpg",
    "Bowl de frutas vermelhas": "bowl_frutas.jpg",
    "Bowl de quinoa com legumes": "bowl_legumes.jpg",
    "Chá verde gelado com limão": "cha_verde.jpg",
    "Espaguete de abobrinha": "espaguete_abobrinha.jpg",
    "Frango grelhado com brócolis": "frango_brocolis.jpg",
    "Lentilha com legumes": "lentilha_legumes.jpg",
    "Mousse de morango saudável": "mousseu_morango.jpg",
    "Panqueca de banana e aveia": "panqueca_banana.jpg",
    "Peixe assado com legumes": "peixe_assado.jpg",
    "Peixe com arroz de quinoa": "peixe_arroz.jpg",
    "Quibe de abóbora com ricota": "quibe_abobora.jpg",
    "Salada de abacate com feijão preto": "salada_abacate_feijao.jpg",
    "Salada de grão-de-bico": "salada_grao_bico.jpg",
    "Sopa de lentilha com legumes": "sopa_lentilhas_legumes.jpg",
    "Sopa detox de abóbora": "sopa_detox_abobora.jpg",
    "Taco de peixe": "taco_peixe.jpg",
    "Torta de legumes": "torta_maca.jpg",
    "Torta de maçã sem açúcar": "torta_maca.jpg",
    "Wrap de frango com alface": "wrap_frango.jpg",

}

# Dicionário de mapeamento de imagens para alimentos
IMAGE_MAP = {
    "Abacate": "abacate.jpg",
    "Abacate hass": "abacate_hass.jpg",
    "Alface": "alface.jpg",
    "Abacaxi": "abacaxi.jpg",
    "Abóbora": "abobora.jpg",
    "Abóbora Cabotiá": "abobora_cambotia.jpg",
    "Abobrinha": "abobrinha.jpg",
    "Acelga": "acelga.jpg",
    "Alcachofra": "alcachofra.jpg",
    "Alcachofra de Jerusalém": "alcachofra_jerusalem.jpg",
    "Alecrim": "alecrim.jpg",
    "Alho": "alho.jpg",
    "Alho-poró": "alho_poro.jpg",
    "Amêndoas": "amendoas.jpg",
    "Amendoim": "amendoim.jpg",
    "Amora": "amora.jpg",
    "Arroz branco": "arroz_branco.jpg",
    "Arroz integral": "arroz_integral.jpg",
    "Aspargos": "aspargos.jpg",
    "Aveia": "aveia.jpg",
    "Banana madura": "banana_madura.jpg",
    "Batata inglesa": "batata_inglesa.jpg",
    "Batata yacon": "batata_yacon.jpg",
    "Batata-doce roxa": "batata_rocha.jpg",
    "Batata doce": "batata_doce.jpg",
    "Berinjela": "berinjela.jpg",
    "Berinjela japonesa": "berinjela_japonesa.jpg",
    "Beterraba": "beterraba1.jpg",
    "Beterraba dourada": "beterraba_dourada.jpg",
    "Broto de bambu": "broto_bambu.jpg",
    "Broto de feijão": "broto_feijao.jpg",
    "Brócolis": "brocolis.jpg",
    "Cacau cru": "cacau_cru.jpg",
    "Cacau em pó": "cacau_po.jpg",
    "Caju": "caju.jpg",
    "Canela": "canela.jpg",
    "Caqui": "caqui.jpg",
    "Cebola": "cebola.jpg",
    "Cebolinha": "cebolinha.jpg",
    "Cenoura": "cenoura.jpg",
    "Cenoura baby": "cenoura_baby.jpg",
    "Cevada": "cevada.jpg",
    "Chia": "chia.jpg",
    "Chuchu": "chuchu.jpg",
    "Cogumelo (champignon)": "cogumelo_champignon.jpg",
    "Couve": "couve.jpg",
    "Couve de Bruxelas": "couve_bruxelas.jpg",
    "Couve kale": "couve_kale.jpg",  
    "Couve-flor": "couve_flor.jpg",
    "Damascos secos": "damascos_secos.jpg",
    "Endívia": "endivia.jpg",
    "Ervilha torta": "ervilha_torta.jpg",
    "Ervilhas": "ervilhas.jpg",
    "Espinafre": "espinafre.jpg",
    "Feijão azuki": "feijao_azuki.jpg",
    "Feijão preto": "feijao_preto.jpg",
    "Figo": "figo.jpg",
    "Framboesa": "framboesa.jpg",
    "Fruta do dragão (pitaya branca)": "fruta_dragao.jpg",
    "Gengibre": "gengibre.jpg",
    "Gergelim": "gergelim.jpg",
    "Grão-de-bico": "grao_de_bico.jpg",
    "Grãos integrais (milho)": "graos_integrais.jpg",
    "Inhame": "inhame.jpg",
    "Iogurte natural sem açúcar": "iogurte_natural.jpg",
    "Jaca": "jaca.jpg",
    "Kiwi": "kiwi.jpg",
    "Laranja": "laranja.jpg",
    "Lentilha": "lentilha.jpg",
    "Linhaça": "linhaca.jpg",
    "Linhaça dourada": "linhaca_dourada.jpg",
    "Macarrão branco": "macarrao_branco.jpg",
    "Mamão": "mamao.jpg",
    "Mandioca": "mandioca.jpg",
    "Mandioca-brava": "mandioca_brava.jpg",
    "Mandioquinha": "mandioquinha.jpg",
    "Manga": "manga.jpg",
    "Manteiga de amendoim": "manteiga_amendoim.jpg",
    "Maracujá": "maracuja.jpg",
    "Maçã": "maca.jpg",
    "Melancia": "melancia.jpg",
    "Melão": "melao.jpg",
    "Mirtilo (Blueberry)": "mirtilio.jpg",
    "Moranga": "moranga.jpg",
    "Morango": "morango.jpg",
    "Nabo": "nabo.jpg",
    "Nozes": "nozes.jpg",
    "Ovo": "ovo.jpg",
    "Palmito": "palmito.jpg",
    "Pecã": "peca.jpg",
    "Peito de frango": "peito_frango.jpg",
    "Peixe (salmão ou tilápia)": "peixe.jpg",
    "Pepino": "pepino.jpg",
    "Pera": "pera.jpg",
    "Pimentão": "pimentao.jpg",
    "Pitaya": "pitaya.jpg",
    "Pão branco": "pao_branco.jpg",
    "Quiabo": "quiabo.jpg",
    "Quinoa": "quinoa.jpg",
    "Quiuí dourado": "quiui_dourado.jpg",
    "Rabanete": "rabanete.jpg",
    "Rabanete branco (daikon)": "rabanete_branco.jpg",
    "Ricota": "ricota.jpg",
    "Romã": "roma.jpg",
    "Rúcula": "rucula.jpg",
    "Salsinha": "salsinha.jpg", 
    "Semente de abóbora": "semente_abobora.jpg",
    "Semente de chia": "semente_chia.jpg",
    "Tomate": "tomate.jpg",
    "Tomate cereja": "tomate_cereja.jpg",
    "Uva": "uva.jpg",
}

# Função para obter a conexão com o banco de dados
def get_db_connection():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/foods')
def list_foods():
    """
    Lista de alimentos, com funcionalidade de busca por 'search' (GET).
    """
    search_query = request.args.get('search', '').strip()
    with get_db_connection() as conn:
        cursor = conn.cursor()
        if search_query:
            foods = cursor.execute('''
                SELECT * FROM foods
                WHERE name LIKE ?
                ORDER BY name
            ''', (f"%{search_query}%",)).fetchall()
        else:
            foods = cursor.execute('SELECT * FROM foods ORDER BY name').fetchall()
    return render_template('list_foods.html', foods=foods, image_map=IMAGE_MAP)

@app.route('/food/<int:food_id>')
def food_detail(food_id):
    """
    Detalhes de um alimento específico.
    """
    with get_db_connection() as conn:
        food = conn.execute('SELECT * FROM foods WHERE id = ?', (food_id,)).fetchone()
    if food is None:
        return render_template('404.html', message="Alimento não encontrado."), 404
    return render_template('food_detail.html', food=food, image_map=IMAGE_MAP)

@app.route('/recipes')
def list_recipes():
    """
    Lista de receitas com imagens.
    """
    with get_db_connection() as conn:
        recipes = conn.execute('SELECT * FROM recipes ORDER BY title ASC').fetchall()
    return render_template('list_recipes.html', recipes=recipes, image_map=RECIPE_IMAGE_MAP)

@app.route('/recipe/<int:recipe_id>')
def recipe_detail(recipe_id):
    """
    Detalhes de uma receita específica com imagem.
    """
    with get_db_connection() as conn:
        recipe = conn.execute('SELECT * FROM recipes WHERE id = ?', (recipe_id,)).fetchone()
    if recipe is None:
        return render_template('404.html', message="Receita não encontrada."), 404
    image = RECIPE_IMAGE_MAP.get(recipe["title"], "default.jpg")  # Usar imagem padrão se não houver mapeamento
    return render_template('recipe_detail.html', recipe=recipe, image=image)

if __name__ == '__main__':
    app.run(debug=True)
