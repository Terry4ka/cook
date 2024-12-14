from flask import Flask, render_template, request

app = Flask(__name__)

# Пример базы данных рецептов
recipes = [
    {
        'name': 'Салат Цезарь',
        'description': 'Классический салат с курицей и сыром пармезан.',
        'ingredients': 'Курица, листья салата, сыр пармезан, сухарики, соус цезарь.',
        'instructions': 'Обжарить курицу, нарезать салат, добавить сыр и сухарики, заправить соусом.',
        'category': 'appetizers',
        'difficulty': 'easy'
    },
    {
        'name': 'Борщ',
        'description': 'Традиционный украинский борщ с мясом и свеклой.',
        'ingredients': 'Свекла, капуста, картофель, мясо, морковь, лук, томатная паста.',
        'instructions': 'Отварить мясо, добавить нарезанные овощи, варить до готовности.',
        'category': 'soup',
        'difficulty': 'medium'
    }
]

@app.route('/')
def index():
    return render_template('templates/index.html')

@app.route('/search', methods=['GET'])
def search():
    ingredients = request.args.get('ingredients').split(',')
    category = request.args.get('category')
    difficulty = request.args.get('difficulty')

    filtered_recipes = []
    for recipe in recipes:
        if all(ingredient.lower() in recipe['ingredients'].lower() for ingredient in ingredients):
            if category and category != '' and category == recipe['category']:
                if difficulty and difficulty != '' and difficulty == recipe['difficulty']:
                    filtered_recipes.append(recipe)

    return render_template('templates/results.html', recipes=filtered_recipes)

if __name__ == '__main__':
    app.run(debug=True)
