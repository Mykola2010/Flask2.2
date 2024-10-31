from flask import Flask, render_template

app = Flask(__name__)

@app.get("/home/")
def home():
    return render_template('index.html')

@app.get('/order/')
def order():
    pizzas = [
        {
            'name': 'Папероні',
            'description': 'Класична піца з тонкими шматочками пікантної ковбаски папероні, соусом з томатів та сиром моцарела. Ідеальний вибір для любителів гострих страв!',
            'price': 29.99,
            'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Pepperoni_pizza.jpg/330px-Pepperoni_pizza.jpg'
        },
        {
            'name': 'Чотири сири',
            'description':"Делікатесний продукт виготовляють з якісного коров'ячого молока, в яке додається благородна блакитна цвіль. У піці даний сорт сиру розкриває всю гаму свого смаку: солонуватий, гіркий, молочний і пряний присмак. Фета належить до напівм'якого сорта сиру. На смак сир трохи солонуватий і володіє ненав'язливою кислинкою.",
            'price': 39.99,
            'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Pizza_quattro_formaggi_at_restaurant%2C_Chalk_Farm_Road%2C_London.jpg/330px-Pizza_quattro_formaggi_at_restaurant%2C_Chalk_Farm_Road%2C_London.jpg'
        },
        {
            'name': 'Маргарита',
            'description': 'Піца "Маргарита" - це одна з найпопулярніших піц у світі. Назва цієї піци було надано на честь королеви Італії Маргарити Савойської, яка відвідала Неаполь у 1889 році.Саме цю піццу обожнювали Черепашки-ніндзя',
            'price': 24.99,
            'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Pizza_Margherita_stu_spivack.jpg/411px-Pizza_Margherita_stu_spivack.jpg'
        },
        {
            'name': 'Гавайська',
            'description': 'Гавайську піцу винайдено Семом Панопулосом, який відкрив піцерію в Канаді. Цікавий і той факт, що самі італійці не люблять цей різновид страви, і в Італії купити гавайську варіацію практично неможливо.',
            'price': 32.99,
            'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Pizza_Hawaii_02.jpg/330px-Pizza_Hawaii_02.jpg'
        }
    ]

    return render_template('order.html', pizzas=pizzas)

if __name__ == '__main__':
    app.run(port=6969, debug=True)