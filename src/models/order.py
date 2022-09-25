async def create_order(order_collection,order,email):
    try:
        
        order_user = await order_collection.find_one({"email": email})
        if order_user == None:
            order = await order_collection.insert_one(order)
            if order.inserted_id:
                order = await get_order(order_collection,order.inserted_id)
                return order
        else: 
                    
            return f'Já existe um carrinho cadastrado para esse usuário' 
    except Exception as e:
        print(f'create_order.error: {e}')

async def get_order(order_collection, order_id):
    try:
        data = await order_collection.find_one({'_id': order_id})
        if data:
            return data
    except Exception as e:
        print(f'get_order.error: {e}')

async def get_orders(order_collection,email, skip, limit):
    try:
        address_cursor = order_collection.find({"email": email}).skip(int(skip)).limit(int(limit))
        address = await address_cursor.to_list(length=int(limit))
        return address
    except Exception as e:
        print(f'get_adress.error: {e}')

async def delete_order(order_collection, email):
    try:
        order = await order_collection.delete_one(
            {}
        )
        if order.deleted_count:
            return {'status': 'Order deleted'}
    except Exception as e:
        print(f'delete_order.error: {e}')