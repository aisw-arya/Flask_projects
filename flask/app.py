import flask
from flask import request,jsonify
from models import *
from sqlalchemy import select
from flask_cors import CORS,cross_origin



app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:1234@localhost:5432/flaskdb"
CORS(app)
db.init_app(app)



@app.route("/")
def home():
    return "Hello, world"


@app.route("/product")
def product_list():
    product_list = db.select(Image).order_by(Image.image_id.desc())
    product = db.session.execute(product_list).scalars()
    resp=[]
    for item in product:
        list ={
        "product_id":item.product.product_id,
        "product_name":item.product.product_name,
        "price":item.product.price,
        "category_id" :item.product.category_id,
        "category_name":item.product.category.category_name,
        "image":item.image
        }
        resp.append(list)
    return flask.jsonify(resp)


@app.route("/category")
def category_list():
    Category_select_query = db.select(Category).order_by(Category.id.desc())
    category = db.session.execute(Category_select_query).scalars()
    resp =[]
    for item in  category:
        list={"id":item.id,
        "category_name": item.category_name}

        resp.append(list)
    return flask.jsonify(resp)

@app.route("/categories" ,methods=['POST'])
def add_category():
    data = request.get_json()
    id = data.get("id")
    category_name = data.get("category_name")
    new_category =Category(id=id,category_name=category_name)
    db.session.add(new_category)
    db.session.commit()
    return flask.jsonify("resp")

@app.route("/products",methods=['POST'])
@cross_origin()
def add_products():
    data=request.get_json()
    product_name = data['data']['product_name']
    price = data['data']['price']
    category_name = data['data']['category_name']
    image = data['data']['image']
    
    print(product_name)
    print(price)
    print(category_name)
    print(image)
    if any(value is None for value in [ product_name, price,category_name, image]):
        return jsonify({'error': "Missing or invalid data"}), 400

    category = db.session.query(Category).filter_by(category_name = category_name).first()
    if category == None :
        new_category= Category( category_name=category_name)
        db.session.add(new_category)
        db.session.commit()
    new_product=Product(product_name=product_name,price=price,category_id=category.id)
    db.session.add(new_product)
    db.session.commit()
    new_image =Image(image=image,p_id=new_product.product_id)
    db.session.add(new_image)
    db.session.commit()
    return jsonify({'message':"Product added successfully"})


    
with app.app_context():
    db.create_all()

if __name__ == "__main__":
  init_db()
  app.run(port=5000)