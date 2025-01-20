from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/foods')
def list_foods():
    """
    Lista de alimentos, com funcionalidade de busca por 'search' (GET).
    E atribui imagem para cada 'name'.
    """
    search_query = request.args.get('search', '').strip()
    conn = get_db_connection()
    cursor = conn.cursor()

    if search_query:
        foods = cursor.execute('''
            SELECT * FROM foods
            WHERE name LIKE ?
            ORDER BY name
        ''', (f"%{search_query}%",)).fetchall()
    else:
        foods = cursor.execute('SELECT * FROM foods ORDER BY name').fetchall()

    conn.close()

    # Crie um dicionário de mapeamento: {nome_do_alimento: nome_do_arquivo}
    image_map = {
        "Abacate": "abacate.jpg",
        "Alface": "alface.jpg",
        "Abacaxi": "abacaxi.jpg",
        "Abobrinha": "abobrinha.jpg",
        "Alecrim": "alecrim.jpg",
        "Alface": "alface.jpg",
        "Amêndoas": "amendoas.jpg",
        "Amendoim": "amendoim.jpg",
        "Arroz branco": "arroz_branco.jpg",
        "Arroz integral": "arroz_integral.jpg",
        "Aveia": "aveia.jpg",
        "Banana (madura)": "banana_madura1.jpg",
        "Batata inglesa": "batata_inglesa.jpg",
        "Batata yacon": "batata_yacon.jpg",
        "Batata doce": "batata_doce.jpg",
        "Beterraba (crua ou assada)": "beterraba1.jpg",
        "Bolos e biscoitos refinados": "bolos_biscoitos.jpg",
        "Bŕocolis": "brocolis.jpg",
        "Canela": "canela",
        "Caqui": "caqui.jpg",
        "Cenoura": "cenoura.jpg",
        "Chá verde": "cha_verde.jpg",
        "Couve": "couve.jpg",
        "Doces industrializados": "doces.jpg",
        "Ervilhas": "ervilhas.jpg",
        "Feijão preto": "feijao_preto.jpg",
        "Figo": "figo.jpg",
        "Framboesa": "framboesa.jpg",
        "Gengibre": "gengibre.jpg",
        "Gergelim": "gergelim.jpg",
        "Grão-de-bico": "grao_de_bico.jpg",
        "Inhame (cozido ou assado)": "inhame.jpg",
        "Iogurte natural sem açúcar": "iogurte_natural.jpg",
        "Jaca": "jaca.jpg",
        "Lentilha": "lentilha.jpg",
        "Linhaça": "linhaca.jpg",
        "Macarrão branco": "macarrao_branco.jpg",
        "Mandioca (cozida)": "mandioca.jpg",
        "Manga": "manga.jpg",
        "Manteiga de amendoim (100% integral)": "manteiga_amendoim.jpg",
        "Maçã": "maca.jpg",
        "Melancia": "melancia.jpg",
        "Mirtilio (Blueberry)": "mirtilio.jpg",
        "Morango": "morango.jpg",
        "Nozes": "nozes.jpg",
        "Ovo": "ovo.jpg",
        "Peito de frango": "peito_frango.jpg",
        "Peixe (salmão ou tilápia)": "peixe.jpg",
        "Pera": "pera.jpg",
        "Pão branco": "pao_branco.jpg",
        "Quinoa": "quinoa.jpg",
        "Refrigerante comum": "refrigerante.jpg",
        "Ricota": "ricota.jpg",
        "Semente de abóbora": "semente_abobora.jpg",
        "Suco artificial (de caixinha)": "suco,jpg",
        "Tomate": "tomate.jpg",
        "Uva": "uva.jpg",
        
    }

    # Agora passamos esse dicionário para o template
    return render_template('list_foods.html', foods=foods, image_map=image_map)

@app.route('/food/<int:food_id>')
def food_detail(food_id):
    """
    Detalhes de um alimento específico.
    """
    conn = get_db_connection()
    food = conn.execute('SELECT * FROM foods WHERE id = ?', (food_id,)).fetchone()
    conn.close()
    if food is None:
        return "Alimento não encontrado.", 404

    # Criando o dicionário de mapeamento para as imagens
    image_map = {
        "Abacate": "abacate.jpg",
        "Alface": "alface.jpg",
        "Abacaxi": "abacaxi.jpg",
        "Abobrinha": "abobrinha.jpg",
        "Alecrim": "alecrim.jpg",
        "Amêndoas": "amendoas.jpg",
        "Amendoim": "amendoim.jpg",
        "Arroz integral": "arroz_integral.jpg",
        "Aveia": "aveia.jpg",
        "Banana (madura)": "banana_madura1.jpg",
        "Batata inglesa": "batata_inglesa.jpg",
        "Batata yacon": "batata_yacon.jpg",
        "Beterraba (crua ou assada)": "beterraba1.jpg",
        "Brócolis": "brocolis.jpg",
        "Canela": "canela.jpg",
        "Cenoura": "cenoura.jpg",
        "Chá verde": "cha_verde.jpg",
        "Couve": "couve.jpg",
        "Ervilhas": "ervilhas.jpg",
        "Feijão preto": "feijao_preto.jpg",
        "Framboesa": "framboesa.jpg",
        "Gengibre": "gengibre.jpg",
        "Gergelim": "gergelim.jpg",
        "Grão-de-bico": "grao_de_bico.jpg",
        "Iogurte natural sem açúcar": "iogurte_natural.jpg",
        "Lentilha": "lentilha.jpg",
        "Maçã": "maca.jpg",
        "Mirtilo (Blueberry)": "mirtilio.jpg",
        "Morango": "morango.jpg",
        "Peixe (salmão ou tilápia)": "peixe.jpg",
        "Pera": "pera.jpg",
        "Quinoa": "quinoa.jpg",
        "Ricota": "ricota.jpg",
        "Semente de abóbora": "semente_abobora.jpg",
        "Tomate": "tomate.jpg",
        "Uva": "uva.jpg"
    }

    # Passa a imagem do alimento para o template
    return render_template('food_detail.html', food=food, image_map=image_map)

@app.route('/food/add', methods=['GET', 'POST'])
def add_food():
    """
    Adicionar novo alimento (opcional).
    """
    if request.method == 'POST':
        name = request.form['name']
        category = request.form['category']
        glycemic_index = request.form['glycemic_index']
        description = request.form['description']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO foods (name, category, glycemic_index, description)
            VALUES (?, ?, ?, ?)
        ''', (name, category, glycemic_index, description))
        conn.commit()
        conn.close()

        return redirect(url_for('list_foods'))

    return render_template('add_food.html')

@app.route('/recipes')
def list_recipes():
    """
    Lista de receitas.
    """
    conn = get_db_connection()
    recipes = conn.execute('SELECT * FROM recipes ORDER BY id DESC').fetchall()
    conn.close()
    return render_template('list_recipes.html', recipes=recipes)

@app.route('/recipe/<int:recipe_id>')
def recipe_detail(recipe_id):
    """
    Detalhes de uma receita específica.
    """
    conn = get_db_connection()
    recipe = conn.execute('SELECT * FROM recipes WHERE id = ?', (recipe_id,)).fetchone()
    conn.close()
    if recipe is None:
        return "Receita não encontrada.", 404
    return render_template('recipe_detail.html', recipe=recipe)

@app.route('/recipe/add', methods=['GET', 'POST'])
def add_recipe():
    """
    Adicionar nova receita (opcional).
    """
    if request.method == 'POST':
        title = request.form['title']
        ingredients = request.form['ingredients']
        instructions = request.form['instructions']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO recipes (title, ingredients, instructions)
            VALUES (?, ?, ?)
        ''', (title, ingredients, instructions))
        conn.commit()
        conn.close()

        return redirect(url_for('list_recipes'))
    return render_template('add_recipe.html')

if __name__ == '__main__':
    app.run(debug=True)
