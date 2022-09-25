from turtle import pen
from src.models.product import (
    create_product,
    get_product_by_name,
    update_product,
    delete_product,
    get_products
)

from src.server.database import connect_db, db, disconnect_db

async def products_crud():
    option = input("Entre com a opção de CRUD: \n 1 -Criar produto \n 2 - Pesquisar produto \n 3 - Atualizar produto \n 4 -Deletar produto\n ")
    
    await connect_db()
    product_collection = db.product_collection

    product =  {
        "name": "melissa",
        "description": "cheirinho de chiclete",
        "price": 10000,
        "image": "Imagine uma foto bonita",
        "Code": 123
    }

    if option == '1':
        # create user

        product = await create_product(
            product_collection,
            product
        )
        print(product)
    elif option == '2':
        # get user
        product = await get_product_by_name(
            product_collection,
            product["name"]
        )
        print(product)
    elif option == '3':
        # update
        product = await get_product_by_name(
            product_collection,
            product["name"]
        )

        product_data = {
            "price": 123
        }

        is_updated, numbers_updated = await update_product(
            product_collection,
            product["_id"],
            product_data
        )
        if is_updated:
            print(f"Atualização realizada com sucesso, número de documentos alterados {numbers_updated}")
        else:
            print("Atualização falhou!")

    elif option == '4':
        # delete
        product = await get_product_by_name(
            product_collection,
            product["name"]
        )

        result = await delete_product(
            product_collection,
            product["_id"]
        )

        print(result)
    elif option == '5':
        # pagination
        product = await get_products(
            product_collection,
            skip=0,
            limit=2
        )
        print(product)

    await disconnect_db()
