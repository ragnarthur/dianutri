from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
app.config['DATABASE'] = 'database.db'

# Dicionário de mapeamento de imagens para receitas
RECIPE_IMAGE_MAP = {
    "Abobrinha recheada com carne moída": "abobrinha_carne.jpg",
    "Arroz de couve-flor": "arroz_couveflor.jpg",
    "Arroz integral com grão-de-bico e legumes": "arroz_integral_grao.jpg",
    "Aveia com maçã e canela": "aveia_maca.jpg",
    "Biscoito de aveia e banana": "biscoito_aveia.jpg",
    "Biscoito salgado de grão-de-bico": "biscoito_grao.jpg",
    "Bolinho de abóbora com carne moída": "bolinho_abobora_carne.jpg",
    "Bolinho de batata doce e frango": "bolinho_bata_frango.jpg",
    "Bolinho de espinafre com ricota": "bolinho_espinafre_ricota.jpg",
    "Bolo de cenoura com farinha de amêndoas": "bolo_cenoura_farinha_amendoas.jpg",
    "Bolo de maçã com farinha de coco": "bolo_maca_farinha_coco.jpg",
    "Bowl de quinoa com legumes": "bowl_legumes.jpg",
    "Ceviche de tilápia": "ceviche_tilapia.jpg",
    "Creme de abacate com cacau": "creme_abacate_cacau.jpg",
    "Creme de brócolis e espinafre": "creme_brocolis_espinafre.jpg",
    "Creme de chuchu com alho-poró": "creme_chuchu_poro.jpg",
    "Crepioca recheada com frango e espinafre": "crepioca_recheada_frangoespinafre.jpg",
    "Cuscuz de quinoa com frango desfiado": "cuscuz_quinoa_frango.jpg",
    "Cuscuz de quinoa com legumes": "cuscuz_quinoa_legumes.jpg",
    "Espaguete de abobrinha": "espaguete_abobrinha.jpg",
    "Espetinhos de frango com vegetais": "espetinho_frango_legumes.jpg",
    "Frango ao curry com leite de coco": "frango_curry_coco.jpg",
    "Frango grelhado com brócolis": "frango_brocolis.jpg",
    "Gratinado de abóbora com cottage": "gratinado_abobora_cottage.jpg",
    "Hambúrguer de grão-de-bico": "hamburguer_grao.jpg",
    "Hambúrguer de lentilha": "hamburguer_lentilha.jpg",
    "Iogurte com frutas vermelhas e chia": "iogurte_frutas_chia.jpg",
    "Macarrão de abobrinha ao pesto": "macarrao_abobrinha_pesto.jpg",
    "Mousse de chocolate com abacate": "mousse_chocolate_abacate.jpg",
    "Omelete com legumes assados": "omelete_legumes_assados.jpg",
    "Omelete de claras com espinafre e cogumelos": "omelete_espinafre_cogumelos.jpg",
    "Omelete de espinafre com queijo branco": "omelete_espinafre_queijo.jpg",
    "Panqueca de banana e aveia": "panqueca_banana.jpg",
    "Panqueca de espinafre com cogumelos": "panqueca_espinafre_cogumelos.jpg",
    "Panqueca de espinafre com ricota": "panqueca_espinafre_ricota.jpg",
    "Pasta de ricota com ervas": "pasta_ricota_ervas.jpg",
    "Patê de grão-de-bico com ervas": "pate_grao_bico.jpg",
    "Peixe assado com legumes": "peixe_assado.jpg",
    "Purê de couve-flor": "pure_couve_flor.jpg",
    "Pão de aveia e linhaça": "pao_aveia_linhaca.jpg",  
    "Quibe assado de abóbora": "quibe_assado_abobora.jpg",
    "Risoto de quinoa com cogumelos": "risoto_quinoa_legumes.jpg",
    "Salada de abacate com feijão preto": "salada_abacate_feijao.jpg",
    "Salada de folhas verdes com abacate e nozes": "salada_verde_legumes_abacate.jpg",
    "Salada de grãos com rúcula": "salada_graos_rucula.jpg",
    "Salada de pepino com iogurte e hortelã": "salada_pepino_iogurte.jpg",
    "Salada de quinoa com abóbora assada": "salada_quinoa_abobora.jpg",
    "Salada de quinoa com legumes": "salada_quinoa_legumes.jpg",
    "Salada de rúcula com abacate e sementes de girassol": "salada_rucula_girassol.jpg",
    "Salada morna de grão-de-bico e abobrinha": "salada_morna_abobora.jpg", 
    "Salada morna de lentilha com espinafre": "salada_morna_lentilha.jpg",
    "Salmão grelhado com molho de limão": "salmao_grelhado_molholimao.jpg",
    "Salmão grelhado com molho de maracujá": "salmao_molhomaracuja.jpg",
    "Smoothie de abacate e espinafre": "smoothie_abacate_espinafre.jpg",
    "Smoothie verde detox": "smoothie_detox.jpg",
    "Sopa cremosa de abobrinha": "sopa_cremosa_abobrinha.jpg",
    "Sopa de couve-flor com alho-poró": "sopa_couve_flor_alhoporo.jpg",
    "Sopa de lentilha com legumes": "sopa_lentilha_legumes.jpg",
    "Tabule de couve-flor": "tabule_couve_flor.jpg",
    "Tartar de atum com abacate": "tartar_atum_abacate.jpg",
    "Torta de berinjela com queijo": "torta_berinjela_queijo.jpg",
    "Torta salgada de legumes com farinha de aveia": "torta_farinha_aveia.jpg",
    "Wrap de alface com frango desfiado": "wrap_alface_frango.jpg",
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
    "Araticum": "araticum.jpg",
    "Amendoim": "amendoim.jpg",
    "Amora": "amora.jpg",
    "Arroz branco": "arroz_branco.jpg",
    "Arroz integral": "arroz_integral.jpg",
    "Aspargos": "aspargos.jpg",
    "Aveia": "aveia.jpg",
    "Bacaba": "bacaba.jpg",
    "Banana madura": "banana_madura.jpg",
    "Batata inglesa": "batata_inglesa.jpg",
    "Batata yacon": "batata_yacon.jpg",
    "Batata-doce roxa": "batata_rocha.jpg",
    "Bergamota": "bergamota.jpg",
    "Batata doce": "batata_doce.jpg",
    "Berinjela": "berinjela.jpg",
    "Berinjela japonesa": "berinjela_japonesa.jpg",
    "Beterraba": "beterraba1.jpg",
    "Beterraba dourada": "beterraba_dourada.jpg",
    "Brambleberry": "brambleberry.jpg",
    "Broto de bambu": "broto_bambu.jpg",
    "Broto de feijão": "broto_feijao.jpg",
    "Brócolis": "brocolis.jpg",
    "Cabeludinha": "cabeludinha.jpg",
    "Cacau cru": "cacau_cru.jpg",
    "Cacau em pó": "cacau_po.jpg",
    "Caju": "caju.jpg",
    "Canela": "canela.jpg",
    "Canola": "canola.jpg",
    "Caqui": "caqui.jpg",
    "Cebola": "cebola.jpg",
    "Cebolinha": "cebolinha.jpg",
    "Cenoura": "cenoura.jpg",
    "Cenoura baby": "cenoura_baby.jpg",
    "Cenoura roxa": "cenoura_roxa.jpg",
    "Cevada": "cevada.jpg",
    "Chia": "chia.jpg",
    "Chuchu": "chuchu.jpg",
    "Chá de hibisco": "cha_hibisco.jpg",
    "Cipó de São João": "cipo_sao_joao.jpg",
    "Cogumelo (champignon)": "cogumelo_champignon.jpg",
    "Couve": "couve.jpg",
    "Couve de Bruxelas": "couve_bruxelas.jpg",
    "Couve kale": "couve_kale.jpg",  
    "Couve-flor": "couve_flor.jpg",
    "Damascos secos": "damascos_secos.jpg",
    "Dendê": "dende.jpg",
    "Endívia": "endivia.jpg",
    "Ervilha torta": "ervilha_torta.jpg",
    "Ervilhas": "ervilhas.jpg",
    "Escarola": "escarola.jpg",
    "Espinafre": "espinafre.jpg",
    "Feijão azuki": "feijao_azuki.jpg",
    "Feijão preto": "feijao_preto.jpg",
    "Feijão verde": "feijao_verde.jpg",
    "Figo": "figo.jpg",
    "Figo-da-índia": "figo_india.jpg",
    "Framboesa": "framboesa.jpg",
    "Fruta do dragão (pitaya branca)": "fruta_dragao.jpg",
    "Gengibre": "gengibre.jpg",
    "Gergelim": "gergelim.jpg",
    "Graptopetalum paraguayense": "graptopetalum_paraguayense.jpg",
    "Graviola": "graviola.jpg",
    "Grão-de-bico": "grao_de_bico.jpg",
    "Grãos integrais (milho)": "graos_integrais.jpg",
    "Inhame": "inhame.jpg",
    "Iogurte natural sem açúcar": "iogurte_natural.jpg",
    "Jabuticaba": "jabuticaba.jpg",
    "Jaca": "jaca.jpg",
    "Jambú": "jambu.jpg",
    "Jojoba": "jojoba.jpg",
    "Kiwano": "kiwano.jpg",
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
    "Sacha Inchi": "sacha_inchi.jpg",
    "Salsinha": "salsinha.jpg", 
    "Semente de abóbora": "semente_abobora.jpg",
    "Semente de chia": "semente_chia.jpg",
    "Tamarindo": "tamarindo.jpg",
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
    Detalhes de uma receita específica com imagem e botão "Próximo".
    """
    with get_db_connection() as conn:
        recipe = conn.execute('SELECT * FROM recipes WHERE id = ?', (recipe_id,)).fetchone()

        # Buscar a próxima receita com base no ID
        next_recipe = conn.execute('''
            SELECT * FROM recipes
            WHERE id > ?
            ORDER BY id ASC LIMIT 1
        ''', (recipe_id,)).fetchone()

    if recipe is None:
        return render_template('404.html', message="Receita não encontrada."), 404

    image = RECIPE_IMAGE_MAP.get(recipe["title"], "default.jpg")  # Usar imagem padrão se não houver mapeamento

    # Passar a próxima receita (se houver) para o template
    return render_template('recipe_detail.html', recipe=recipe, image=image, next_recipe=next_recipe)

if __name__ == '__main__':
    app.run(debug=True)
