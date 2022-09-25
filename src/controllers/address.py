from src.models.address import(
    create_address,
    get_addresses,
    delete_address    )

from src.server.database import connect_db, db, disconnect_db

async def address_crud():
    option = input("Entre com a opção de CRUD: ")
    
    await connect_db()
    address_collection =db.address_collection
    users_collection = db.users_collection

    address =  {
       "email": 'paloma@gmail.com',
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
        # get user
        address = await create_address(
            address_collection,
            address,
            address["email"],
            users_collection,
        )
        print(address)
    elif option == '2':
        # pagination
        users = await get_addresses(
            address_collection,
            address["email"],
            skip=0,
            limit=20,
            
        )
        print(users)
    elif option == '3':
        # delete
     
        result = await delete_address(
            address_collection,
            address["email"]
        )

        print(result)

    await disconnect_db()

