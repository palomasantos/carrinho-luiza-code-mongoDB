async def create_address(address_collection,address,email,users_collection,):
    try:
        
        user = await users_collection.find_one({"email": email})
        address_user = await address_collection.find_one(({"user._id": user["_id"]}))
        if address_user == None:
            address = await address_collection.insert_one(address)
            if address.inserted_id:
                address = await get_address(address_collection, address.inserted_id)
                return user
        else: address = address_collection.update_one(
            
            {"_id": "{address_user._id}"},
        {
        "$addToSet": {
            "email": 'joaquina@gmail.com',
        "address": {
          "street": "Rua Quarenta e Sete, Numero 3",
              "cep": "8465312",
              "district": "São Paulo",
              "city": "São Paulo",
              "state": "São Paulo",
              "is_delivery": True
           }
        }
    }

);
        endereco = await address_collection.find_one({"email": email})        
        return endereco
    except Exception as e:
        print(f'create_address.error: {e}')

async def get_address(address_collection, address_id):
    try:
        data = await address_collection.find_one({'_id': address_id})
        if data:
            return data
    except Exception as e:
        print(f'get_address.error: {e}')

async def get_addresses(address_collection,email, skip, limit):
    try:
        address_cursor = address_collection.find({"email": email}).skip(int(skip)).limit(int(limit))
        address = await address_cursor.to_list(length=int(limit))
        return address
    except Exception as e:
        print(f'get_adress.error: {e}')
        
async def delete_address(address_collection, email):
    try:
        address = await address_collection.delete_one(
            {'email': email}
        )
        if address.deleted_count:
            return {'status': 'Address deleted'}
    except Exception as e:
        print(f'delete_address.error: {e}')