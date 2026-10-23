from flask import Flask, render_template
app = Flask(__name__)
PRODUCTS = [
    {"id":1,"name":"Rizwan Store T-Shirt","price":499,"image":"https://via.placeholder.com/400"},
    {"id":2,"name":"FamGateway Hoodie","price":999,"image":"https://via.placeholder.com/400"},
    {"id":3,"name":"Stylish Cap","price":299,"image":"https://via.placeholder.com/400"},
]
@app.route('/')
def home():
    return render_template('index.html', products=PRODUCTS)
@app.route('/order', methods=['POST'])
def order():
    return "Order Received! <a href='/'>Back</a>"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
