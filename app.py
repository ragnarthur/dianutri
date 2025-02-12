from flask import Flask, render_template, request, redirect, url_for
import datetime
import sqlite3
from zoneinfo import ZoneInfo
import locale

app = Flask(__name__)
app.config['DATABASE'] = 'database.db'

# Dicionário de mapeamento de imagens para receitas
RECIPE_IMAGE_MAP = {
    "Abobrinha recheada com carne moída": "abobrinha_carne.jpg",
    "Arroz de brócolis com cogumelos": "arroz_brocolis_cogumelos.jpg",
    "Arroz de couve-flor": "arroz_couveflor.jpg",
    "Arroz integral com grão-de-bico e legumes": "arroz_integral_grao.jpg",
    "Aveia com maçã e canela": "aveia_maca.jpg",
    "Berinjela Recheada com Carne Moída Magra": "berinjela_recheada_carne_moida.jpg",
    "Bife grelhado com abobrinha e tomate": "bife_grelhado_abobrinha_tomate.jpg",
    "Biscoito de aveia e banana": "biscoito_aveia.jpg",
    "Biscoito Crocante de Aveia e Cacau": "biscoito_crocante_aveia.jpg",
    "Biscoito salgado de grão-de-bico": "biscoito_grao.jpg",
    "Bolinho de abóbora com carne moída": "bolinho_abobora_carne.jpg",
    "Bolinhos de Abobrinha e Queijo": "bolinho_abobrinha_queijo.jpg",
    "Bolinho de batata doce e frango": "bolinho_bata_frango.jpg",
    "Bolinho de batata doce e atum": "bolinho_batata_doce_atum.jpg",
    "Bolinhos de Batata Doce e Frango": "bolinho_batata_doce_frango.jpg",
    "Bolinho de espinafre com ricota": "bolinho_espinafre_ricota.jpg",
    "Bolo de cenoura com farinha de amêndoas": "bolo_cenoura_farinha_amendoas.jpg",
    "Bolo de chocolate com abacate": "bolo_chocolate_abacate.jpg",
    "Bolo de Chocolate com Abobrinha": "bolo_chocolate_abobrinha.jpg",
    "Bolo de maçã com farinha de coco": "bolo_maca_farinha_coco.jpg",
    "Bowl de quinoa com legumes": "bowl_legumes.jpg",
    "Cenoura assada com cúrcuma e alho": "cenoura_assada_curcuma.jpg",
    "Ceviche de tilápia": "ceviche_tilapia.jpg",
    "Chili de frango com abóbora": "chili_abobora.jpg",
    "Chili Vegetariano": "chili_vegetariano.jpg",
    "Chips de Batata Doce": "chips_batata_doce.jpg",
    "Creme de abacate com cacau": "creme_abacate_cacau.jpg",
    "Creme de brócolis e espinafre": "creme_brocolis_espinafre.jpg",
    "Creme de chuchu com alho-poró": "creme_chuchu_poro.jpg",
    "Creme de couve-flor com cebola": "creme_couve_flor_cebola.jpg",
    "Crepioca de Espinafre e Ricota": "crepioca_espinafre_ricota.jpg",
    "Crepioca recheada com frango e espinafre": "crepioca_recheada_frangoespinafre.jpg",
    "Cuscuz de quinoa com frango desfiado": "cuscuz_quinoa_frango.jpg",
    "Cuscuz de quinoa com legumes": "cuscuz_quinoa_legumes.jpg",
    "Espaguete de abobrinha": "espaguete_abobrinha.jpg",
    "Espetinhos de frango com vegetais": "espetinho_frango_legumes.jpg",
    "Espetinhos de Frango com Abacaxi": "espetinho_frango_abacaxi.jpg",
    "Frango ao curry com leite de coco": "frango_curry_coco.jpg",
    "Frango grelhado com brócolis": "frango_brocolis.jpg",
    "Gratinado de abóbora com cottage": "gratinado_abobora_cottage.jpg",
    "Hambúrguer de grão-de-bico": "hamburguer_grao.jpg",
    "Hambúrguer de lentilha": "hamburguer_lentilha.jpg",
    "Iogurte Caseiro com Frutas Vermelhas": "iogurte_caseiro_frutas_vermelhas.jpg",
    "Iogurte com frutas vermelhas e chia": "iogurte_frutas_chia.jpg",
    "Lasanha de Berinjela com Ricota e Molho de Tomate": "lasanha_berinjela_ricota.jpg",
    "Macarrão de abobrinha ao pesto": "macarrao_abobrinha_pesto.jpg",
    "Muffin de Abobrinha e Queijo": "muffin_abobrinha_queijo.jpg",
    "Muffin Integral de Banana": "muffin_banana.jpg",
    "Muffin de Maçã e Canela": "muffin_maca_canela.jpg",
    "Mousse de chocolate com abacate": "mousse_chocolate_abacate.jpg",
    "Omelete com legumes assados": "omelete_legumes_assados.jpg",
    "Omelete de claras com espinafre e cogumelos": "omelete_espinafre_cogumelos.jpg",
    "Omelete de espinafre com queijo branco": "omelete_espinafre_queijo.jpg",
    "Panqueca de abóbora": "panqueca_abobora.jpg",
    "Panqueca de banana e aveia": "panqueca_banana.jpg",
    "Panqueca de espinafre com cogumelos": "panqueca_espinafre_cogumelos.jpg",
    "Panqueca de espinafre com ricota": "panqueca_espinafre_ricota.jpg",
    "Panqueca de grão-de-bico": "panqueca_grao.jpg",
    "Pão de Abobrinha Low Carb": "pao_abobrinha_low.jpg",
    "Pasta de ricota com ervas": "pasta_ricota_ervas.jpg",
    "Patê de grão-de-bico com ervas": "pate_grao_bico.jpg",
    "Peito de Frango Grelhado com Molho de Iogurte": "peito_frango_molho_iogurte.jpg",
    "Peixe assado com legumes": "peixe_assado.jpg",
    "Peixe grelhado com molho de limão e alcaparras": "peixe_grelhado_alcaparas.jpg",
    "Pudim de Chia com Coco": "pudim_chia_coco.jpg",
    "Pudim de Chia com Frutas Vermelhas": "pudim_chia_frutas_vermelhas.jpg",
    "Purê de couve-flor": "pure_couve_flor.jpg",
    "Pão de aveia e linhaça": "pao_aveia_linhaca.jpg",
    "Pão de Farelo de Aveia e Linhaça": "pao_farelo_aveia.jpg",
    "Quibe assado de abóbora": "quibe_assado_abobora.jpg",
    "Risoto de quinoa com cogumelos": "risoto_quinoa_legumes.jpg",
    "Salada de abacate com feijão preto": "salada_abacate_feijao.jpg",
    "Salada de Abacate e Tomate": "salada_abacate_tomate.jpg",
    "Salada de Atum com Feijão Branco": "salada_atum_feijao_branco.jpg",
    "Salada de Beterraba e Laranja": "salada_beterra_laranja.jpg",
    "Salada de Couve com Grãos": "salada_couve_graos.jpg",
    "Salada de espinafre com morango": "salada_espinafre_morango.jpg",
    "Salada de folhas verdes com abacate e nozes": "salada_verde_legumes_abacate.jpg",
    "Salada de grãos com rúcula": "salada_graos_rucula.jpg",
    "Salada de Lentilhas com Legumes": "salada_lentilhas_legumes.jpg",
    "Salada de pepino com iogurte e hortelã": "salada_pepino_iogurte.jpg",
    "Salada de pepino com vinagrete de iogurte": "salada_pepino_vinagrete.jpg",
    "Salada de quinoa com abóbora assada": "salada_quinoa_abobora.jpg",
    "Salada de quinoa com grão-de-bico": "salada_quinoa_grao.jpg",
    "Salada de quinoa com legumes": "salada_quinoa_legumes.jpg",
    "Salada de rúcula com abacate e sementes de girassol": "salada_rucula_girassol.jpg",
    "Salada de Rúcula com Manga": "salada_rucula_manga.jpg",
    "Salada de Tofu com Legumes e Vinagrete de Limão": "salada_tofu.jpg",
    "Salada morna de grão-de-bico e abobrinha": "salada_morna_abobora.jpg",
    "Salmão ao forno com molho de mostarda e mel": "salmao_molho_mostarda_mel.jpg",
    "Salada morna de lentilha com espinafre": "salada_morna_lentilha.jpg",
    "Salmão ao Forno com Alho e Limão": "salmao_alho_limao.jpg",
    "Salmão grelhado com molho de limão": "salmao_grelhado_molholimao.jpg",
    "Salmão grelhado com molho de maracujá": "salmao_molhomaracuja.jpg",
    "Sanduíche de Pão Integral com Abacate e Ovo": "sanduiche_abacate_ovo.jpg",
    "Smoothie de abacate e espinafre": "smoothie_abacate_espinafre.jpg",
    "Smoothie verde detox": "smoothie_detox.jpg",
    "Sopa cremosa de abobrinha": "sopa_cremosa_abobrinha.jpg",
    "Sopa de abóbora com gengibre": "sopa_abobora_gengibre.jpg",
    "Sopa de Abóbora com Leite de Coco": "sopa_abobora_leite_coco.jpg",
    "Sopa de couve-flor com alho-poró": "sopa_couve_flor_alhoporo.jpg",
    "Sopa de Ervilha com Bacon de Peru": "sopa_ervilha_bacon.jpg",
    "Sopa de Ervilhas com Cenoura": "sopa_ervilha_cenoura.jpg",
    "Sopa de Legumes com Carne Moída": "sopa_legumes_carne_moida.jpg",
    "Sopa de Legumes com Frango Desfiado": "sopa_legumes_frango.jpg",
    "Sopa de lentilha com legumes": "sopa_lentilha_legumes.jpg",
    "Sopa de Tomate e Manjericão": "sopa_tomate_manjericao.jpg",
    "Sorvete Caseiro de Banana e Morango": "sorvete_banana_morango.jpg",
    "Strogonoff de Frango Low Carb": "strogonoff_frango.jpg",
    "Taco de alface com carne moída": "taco_alface_carne_moida.jpg",
    "Tabule de couve-flor": "tabule_couve_flor.jpg",
    "Tapioca de Frango com Requeijão Light": "tapioca_frango_light.jpg",
    "Tartar de atum com abacate": "tartar_atum_abacate.jpg",
    "Torta de berinjela com queijo": "torta_berinjela_queijo.jpg",
    "Torta de Espinafre com Tomate e Queijo Branco": "torta_espinafre_queijo.jpg",
    "Torta salgada de legumes com farinha de aveia": "torta_farinha_aveia.jpg",
    "Wrap de alface com abacate e frango": "wrap_alface_frango_abacate.jpg",
    "Wrap de Alface com Frango": "wrap_alface_frango_folha.jpg",
    "Wrap de alface com frango desfiado": "wrap_alface_frango.jpg",
}

# Dicionário de mapeamento de imagens para alimentos
IMAGE_MAP = {
    "Abacate": "abacate.jpg",
    "Abacate hass": "abacate_hass.jpg",
    "Alface": "alface.jpg",
    "Abacaxi": "abacaxi.jpg",
    "Abiu": "abiu.jpg",
    "Abóbora": "abobora.jpg",
    "Abóbora Cabotiá": "abobora_cambotia.jpg",
    "Abobrinha": "abobrinha.jpg",
    "Acelga": "acelga.jpg",
    "Agrião": "agriao.jpg",
    "Alcachofra": "alcachofra.jpg",
    "Alcachofra de Jerusalém": "alcachofra_jerusalem.jpg",
    "Alecrim": "alecrim.jpg",
    "Alho": "alho.jpg",
    "Alho-poró": "alho_poro.jpg",
    "Amaranto": "amaranto.jpg",
    "Amêndoas": "amendoas.jpg",
    "Araticum": "araticum.jpg",
    "Amendoim": "amendoim.jpg",
    "Amora": "amora.jpg",
    "Arroz branco": "arroz_branco.jpg",
    "Arroz integral": "arroz_integral.jpg",
    "Aspargos": "aspargos.jpg",
    "Aveia": "aveia.jpg",
    "Açaí (sem açúcar)": "acai_sem_acucar.jpg",
    "Bacaba": "bacaba.jpg",
    "Banana madura": "banana_madura.jpg",
    "Baru": "baru.jpg",
    "Batata inglesa": "batata_inglesa.jpg",
    "Batata yacon": "batata_yacon.jpg",
    "Batata-doce roxa": "batata_rocha.jpg",
    "Bergamota": "bergamota.jpg",
    "Batata doce": "batata_doce.jpg",
    "Beldroega": "beldroegas.jpg",
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
    "Camu-camu": "camu_camu.jpg",
    "Canela": "canela.jpg",
    "Canola": "canola.jpg",
    "Caqui": "caqui.jpg",
    "Carambola": "carambola.jpg",
    "Cará": "cara.jpg",
    "Cará roxo": "cara_roxo.jpg",
    "Castanha-do-Pará": "castanha_para.jpg",
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
    "Coco seco": "coco_seco.jpg",
    "Cogumelo (champignon)": "cogumelo_champignon.jpg",
    "Couve": "couve.jpg",
    "Couve de Bruxelas": "couve_bruxelas.jpg",
    "Couve kale": "couve_kale.jpg",  
    "Couve-flor": "couve_flor.jpg",
    "Cupuaçu": "cupuacu.jpg",
    "Damascos secos": "damascos_secos.jpg",
    "Dendê": "dende.jpg",
    "Endívia": "endivia.jpg",
    "Ervilha torta": "ervilha_torta.jpg",
    "Ervilhas": "ervilhas.jpg",
    "Escarola": "escarola.jpg",
    "Espinafre": "espinafre.jpg",
    "Farinha de banana verde": "farinha_banana.jpg",
    "Farinha de castanha": "farinha_castanha.jpg",
    "Farinha de centeio": "farinha_centeio.jpg",
    "Farinha de coco": "farinha_coco.jpg",
    "Fava": "fava.jpg",
    "Feijão azuki": "feijao_azuki.jpg",
    "Feijão preto": "feijao_preto.jpg",
    "Feijão rosinha": "feijao_rosinha.jpg",
    "Feijão verde": "feijao_verde.jpg",
    "Figo": "figo.jpg",
    "Figo turco (seco)": "figo_turco.jpg",
    "Figo-da-índia": "figo_india.jpg",
    "Framboesa": "framboesa.jpg",
    "Fruta do dragão (pitaya branca)": "fruta_dragao.jpg",
    "Gengibre": "gengibre.jpg",
    "Gergelim": "gergelim.jpg",
    "Gergelim preto": "gergelim_preto.jpg",
    "Graptopetalum paraguayense": "graptopetalum_paraguayense.jpg",
    "Graviola": "graviola.jpg",
    "Grão-de-bico": "grao_de_bico.jpg",
    "Grãos integrais (milho)": "graos_integrais.jpg",
    "Inhame": "inhame.jpg",
    "Iogurte natural sem açúcar": "iogurte_natural.jpg",
    "Jabuticaba": "jabuticaba.jpg",
    "Jaca": "jaca.jpg",
    "Jambo": "jambo.jpg",
    "Jambú": "jambu.jpg",
    "Jatobá": "jatoba.jpg",
    "Jojoba": "jojoba.jpg",
    "Kiwano": "kiwano.jpg",
    "Kiwi": "kiwi.jpg",
    "Laranja": "laranja.jpg",
    "Lentilha": "lentilha.jpg",
    "Linhaça": "linhaca.jpg",
    "Linhaça dourada": "linhaca_dourada.jpg",
    "Lúpulo (em pó)": "lupulo_po.jpg",
    "Macarrão branco": "macarrao_branco.jpg",
    "Mamão": "mamao.jpg",
    "Mandioca": "mandioca.jpg",
    "Mandioca-brava": "mandioca_brava.jpg",
    "Mandioquinha": "mandioquinha.jpg",
    "Manga": "manga.jpg",
    "Mangostão": "mangostao.jpg",
    "Manteiga de amendoim": "manteiga_amendoim.jpg",
    "Maracujá": "maracuja.jpg",
    "Mascarpone": "mascarpone.jpg",
    "Maxixe": "maxixe.jpg",
    "Maçã": "maca.jpg",
    "Melancia": "melancia.jpg",
    "Melão": "melao.jpg",
    "Mirtilo (Blueberry)": "mirtilio.jpg",
    "Moranga": "moranga.jpg",
    "Morango": "morango.jpg",
    "Murici": "murici.jpg",
    "Nabo": "nabo.jpg",
    "Noni": "noni.jpg",
    "Nozes": "nozes.jpg",
    "Ovo": "ovo.jpg",
    "Painço": "painco.jpg",
    "Palmito": "palmito.jpg",
    "Pecã": "peca.jpg",
    "Peito de frango": "peito_frango.jpg",
    "Peixe (salmão ou tilápia)": "peixe.jpg",
    "Pepino": "pepino.jpg",
    "Pequi": "pequi.jpg",
    "Pera": "pera.jpg",
    "Pimentão": "pimentao.jpg",
    "Pitaya": "pitaya.jpg",
    "Pupunha": "pupunha.jpg",
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
    "Semente de girassol": "semente_girassol.jpg",
    "Seriguela": "seriguela.jpg",
    "Sorgo": "sorgo.jpg",
    "Tamarindo": "tamarindo.jpg",
    "Tayberry": "tayberry.jpg",
    "Tomate": "tomate.jpg",
    "Tomate cereja": "tomate_cereja.jpg",
    "Trigo sarraceno (buckwheat)": "trigo_sarraceno.jpg",
    "Tucumã": "tucuma.jpg",
    "Uva": "uva.jpg",
    "Uva-passa": "uva_passa.jpg",
}

# Função para obter a conexão com o banco de dados
def get_db_connection():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

# Dicionário de palavras-chave para cada tipo de refeição (todos em minúsculas)
MEAL_KEYWORDS = {
    "Café da Manhã": ["panqueca", "muffin", "omelete", "biscoito", "crepioca", "iogurte", "pão"],
    "Almoço": ["arroz", "salada", "frango", "peixe", "risoto", "cuscuz", "lasanha", "bife", "chili", "bolinho", "hambúrguer", "taco", "quibe"],
    "Café da Tarde": ["smoothie", "pudim", "mousse", "sanduíche", "wrap"],
    "Janta": ["sopa", "torta", "strogonoff", "wrap", "tartar", "salada morna", "salmão", "ceviche", "creme", "gratinado", "quinoa"]
}

# Função auxiliar para obter uma receita aleatória filtrada pelas palavras-chave
def get_recipe_for_meal(cursor, meal_type):
    keywords = MEAL_KEYWORDS.get(meal_type, [])
    if not keywords:
        return None
    conditions = " OR ".join(["LOWER(title) LIKE ?" for _ in keywords])
    query = f"SELECT * FROM recipes WHERE {conditions} ORDER BY RANDOM() LIMIT 1"
    params = [f"%{kw}%" for kw in keywords]
    return cursor.execute(query, params).fetchone()

# Função auxiliar para obter a próxima receita (em ordem de id) para o ciclo do tipo de refeição
def get_next_recipe_for_meal(cursor, meal_type):
    keywords = MEAL_KEYWORDS.get(meal_type, [])
    if not keywords:
        return None
    conditions = " OR ".join(["LOWER(title) LIKE ?" for _ in keywords])
    query_all = f"SELECT * FROM recipes WHERE {conditions} ORDER BY id ASC"
    params = [f"%{kw}%" for kw in keywords]
    recipes = cursor.execute(query_all, params).fetchall()
    
    # Buscar o registro mais recente para este tipo na tabela daily_recipes
    record = cursor.execute(
        "SELECT recipe_id FROM daily_recipes WHERE meal_type = ? ORDER BY date DESC LIMIT 1",
        (meal_type,)
    ).fetchone()
    
    if record:
        last_recipe_id = record['recipe_id']
        # Procura a próxima receita cujo id seja maior que a última usada
        for r in recipes:
            if r['id'] > last_recipe_id:
                return r
        # Se todas já foram utilizadas, reinicia o ciclo
        if recipes:
            return recipes[0]
        return None
    else:
        if recipes:
            return recipes[0]
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/foods')
def list_foods():
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
    with get_db_connection() as conn:
        food = conn.execute('SELECT * FROM foods WHERE id = ?', (food_id,)).fetchone()
    if food is None:
        return render_template('404.html', message="Alimento não encontrado."), 404
    return render_template('food_detail.html', food=food, image_map=IMAGE_MAP)

@app.route('/recipes')
def list_recipes():
    with get_db_connection() as conn:
        recipes = conn.execute('SELECT * FROM recipes ORDER BY title ASC').fetchall()
    return render_template('list_recipes.html', recipes=recipes, image_map=RECIPE_IMAGE_MAP)

@app.route('/recipe/<int:recipe_id>')
def recipe_detail(recipe_id):
    with get_db_connection() as conn:
        recipe = conn.execute('SELECT * FROM recipes WHERE id = ?', (recipe_id,)).fetchone()
        next_recipe = conn.execute('''
            SELECT * FROM recipes
            WHERE id > ?
            ORDER BY id ASC LIMIT 1
        ''', (recipe_id,)).fetchone()
    if recipe is None:
        return render_template('404.html', message="Receita não encontrada."), 404
    image = RECIPE_IMAGE_MAP.get(recipe["title"], "default.jpg")
    return render_template('recipe_detail.html', recipe=recipe, image=image, next_recipe=next_recipe)

@app.route('/daily-schedule')
def daily_schedule():
    # Define o fuso horário para São Paulo e a localidade para pt_BR
    now = datetime.datetime.now(ZoneInfo("America/Sao_Paulo"))
    today = now.date()
    locale.setlocale(locale.LC_TIME, "pt_BR.utf8")
    display_date = now.strftime("%A, %d de %B")
    current_time = now.strftime("%H:%M")
    
    # Define os tipos de refeição para o período atual
    if now.hour < 12:
        meals = ["Café da Manhã", "Almoço"]
    elif 12 <= now.hour < 18:
        meals = ["Café da Tarde"]
    else:
        meals = ["Janta"]
    
    schedule = []
    with get_db_connection() as conn:
        cursor = conn.cursor()
        for meal in meals:
            # Verifica se já existe uma receita para hoje para este tipo de refeição
            record = cursor.execute(
                "SELECT recipe_id FROM daily_recipes WHERE date = ? AND meal_type = ?",
                (today.strftime("%Y-%m-%d"), meal)
            ).fetchone()
            if record:
                recipe = cursor.execute(
                    "SELECT * FROM recipes WHERE id = ?",
                    (record['recipe_id'],)
                ).fetchone()
            else:
                # Obtém a próxima receita no ciclo para o tipo de refeição
                recipe = get_next_recipe_for_meal(cursor, meal)
                if recipe:
                    cursor.execute(
                        "INSERT INTO daily_recipes (date, meal_type, recipe_id) VALUES (?, ?, ?)",
                        (today.strftime("%Y-%m-%d"), meal, recipe['id'])
                    )
                    conn.commit()
            schedule.append({"meal": meal, "recipe": recipe})
    
    return render_template('daily_schedule.html',
                           schedule=schedule,
                           date=display_date,
                           current_time=current_time,
                           image_map=RECIPE_IMAGE_MAP)

if __name__ == '__main__':
    app.run(debug=True)
