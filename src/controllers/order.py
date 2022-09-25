from src.models.order import (
    create_order,
    delete_order,
    get_orders
)

from src.server.database import connect_db, db, disconnect_db


async def order_crud():
    option = input("Entre com a opção de CRUD: \n 1 - Criar carrinho \n 2 - Ver carrinhos já existentes \n 3 - Apagar carrinho ")
    
    await connect_db()
    
    order_collection = db.order_collection


    order =  {
       "email": 'ludomagalu@gmail.com',
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

    if option == '1':
      
        order = await create_order(
            order_collection,
            order,
            order["email"],
        
        
        )
        print(order)
    elif option == '2':
        
        orders= await get_orders(
            order_collection,
            order["email"],
            skip=0,
            limit=20,
            
        )
        print(orders)
    if option == '3':
       
        result = await delete_order(
            order_collection,
            order["email"],
        )
        print(result)
    await disconnect_db()
        
