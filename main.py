import asyncio

from src.controllers.users import users_crud
from src.controllers.products import products_crud
from src.controllers.address import address_crud
from src.controllers.order import order_crud
from src.controllers.ordem_items import order_items_crud

loop = asyncio.get_event_loop()
loop.run_until_complete(users_crud())
loop.run_until_complete(products_crud())
loop.run_until_complete(address_crud())
loop.run_until_complete(order_crud())
loop.run_until_complete(order_items_crud())


