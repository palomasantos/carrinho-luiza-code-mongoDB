from src.models.order_items import (
   add_item,
   delete_product
)

from src.server.database import connect_db, db, disconnect_db


async def order_items_crud():
    option = input("Entre com a opção de CRUD: \n 1 - Adicionar produto ao carrinho \n 2 - Remover produto \n ")
    
    await connect_db()
    
    order_items_collection = db.order_items_collection
    order_collection = db.order_collection
    product_collection = db.product_collection

    order_item = {
    "order":{
       "email": 'palomattss@gmail.com',
       "price": 1796.4,
       "paid" : False,
        "address":[ 
        {
          "street": "Rua Quarenta e Sete, Numero 3",
              "cep": "8465312",
              "district": "São Paulo",
              "city": "São Paulo",
              "state": "São Paulo",
              "is_delivery": True
           }
        ]
    }
    ,
    "product":{
        "name": "calça",
        "description": "Um celular digno de um rico",
        "price": 10000,
        "image": "Imagine uma foto bonita",
        "Code": 123
    }
 
    }
    if option == '1':
        # get user
        order = await add_item(
            order_items_collection,
            order_item,
            product_collection, 
            order_item["product"],
            order_collection,
            order_item["order"],
            
                   
        )
        print(order)    
    elif option == '2':
        # delete
        result = await delete_product(
            order_items_collection,
            order_item["product"]
        )
        print(result)
    await disconnect_db()
        
