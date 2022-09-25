from ast import Return
from itertools import product


async def add_item(order_items_collection,order_item,product_collection,product,order_collection,order):
    try:
    
        product = await product_collection.find_one(product)
        order = await order_collection.find_one(order)
        
        if product == None:
            return f"produto não cadastrado"
        elif order == None:
            return f'usuário n possui carrinho'
        
        else:
                 
            order_item = await order_items_collection.insert_one(
                    product)
            if order_item.inserted_id:
                order_item = await get_order(order_items_collection,order_item.inserted_id)
                return order_item
    except Exception as e:
        print(f'create_order_item.error: {e}')

async def get_order(order_items_collection, order_item_id):
    try:
        data = await order_items_collection.find_one({'_id': order_item_id})
        if data:
            return data   
    except Exception as e:
        print(f'create_order_item.error: {e}')


async def delete_product(order_items_collection, produto):
    try:
        address = await order_items_collection.delete_one(
            produto
        )
        if address.deleted_count:
            return {'status': 'Product deleted'}
    except Exception as e:
        print(f'delete_address.error: {e}')

async def get_products(order_items_collection,order,order_collection, skip, limit):
    try:

        products_cursor = order_items_collection.find().skip(int(skip)).limit(int(limit))
        products = await products_cursor.to_list(length=int(limit))
        return products
    except Exception as e:
        print(f'get_products.error: {e}')




