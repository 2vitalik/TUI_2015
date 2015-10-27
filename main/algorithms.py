# coding: utf-8
import math
from datetime import timedelta,datetime


def fill_store_houses(stock):
    from main.models import StoreHouse
    from main.models import Stock

    if stock.store_house:
        return

    resource = stock.resource
    unit_volume = resource.volume_of_one_unit

    store_houses = StoreHouse.objects.all()
    sorted_store_houses = sorted(store_houses, key=lambda x: x.rent)

    for store in sorted_store_houses:
        if unit_volume * stock.amount <= store.free_volume:
            # запас полностью помещается на этот склад
            stock.store_house = store
            stock.save()
            store.free_volume -= unit_volume * stock.amount
            store.save()
            return
        elif unit_volume > store.free_volume:
            continue  # даже минимальная единица объёма не помещается на этом складе
        else:
            current_amount = int(math.floor(store.free_volume / unit_volume))
            Stock.objects.create(store_house=store,
                                 resource=resource,
                                 amount=current_amount)
            stock.amount -= current_amount
            stock.save()
            store.free_volume -= unit_volume * current_amount
            store.save()

#     volonters = Volonter.objects.filter(fio__contains='')


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def create_resource_orders(need):
    pass
    from main.models import Stock
    from main.models import Need
    from main.models import ResourceOrder


    # stocks = Stock.objects.filter(resource=need.resource).exclude(store_house=None)
    # stores = []
    # for stock in stocks:
    #     if stock.store_house not in stores:
    #         stores.append(stock.store_house)
    #
    # needs = Need.objects.filter(resource=need.resource)
    # resource_orders = ResourceOrder.objects.filter(resource = need.resource).exclude(finished = True)
    #
    # total_stock_amount = sum([stock.amount for stock in stocks])
    # # cуммируем кол-во запасов
    # total_need_amount = sum([need.amount for need in needs])
    # # суммируем кол-во потребностей
    # total_resorce_order = sum(resource_order.amount for resource_order in resource_orders)
    # # суммируем кол-во заказов
    #
    #
    # # если нужно создаем ResourceOrder
    # if total_stock_amount < total_need_amount:

    ResourceOrder.objects.create(
            resource=need.resource,
            amount=need.amount,
            finished=False,
            date_created = datetime.now(),
            date_finished= datetime.now() + timedelta(days=1),
        )

 #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def shipment_store_houses():
    pass
#     from datetime import timedelta,datetime
#     from main.models import Stock
#     from main.models import Need
#     from main.models import ResourceOrder
#     from main.models import StoreHouse
#     from main.models import Resource
#     stocks = Stock.objects.filter(resource=need.resource).exclude(store_house=None)
#     stores = []
#     for stock in stocks:
#         if stock.store_house not in stores:
#             stores.append(stock.store_house)
#     # сортируем склады начиная с самого дорогого
#     sorted_stores = sorted(stores, key=lambda x: x.rent, reverse=True)
#     resource = need.resource
#     # пробегаемся начиная с самого дорого склада, и любого запаса с этого склада, удаляем нулевые запасы
#     count = need.amount
#     break_count = False
#     for store in sorted_stores:
#         for stock in stocks:
#             break_count = False
#             delete_stock = False
#             if store == stock.store_house:
#                 if count < stock.amount:
#                     stock.amount -= count
#                     stock.save()
#                     store.free_volume += count * resource.volume_of_one_unit
#                     store.save()
#                     break_count = True
#                 elif count == stock.amount:
#                     store.free_volume += count * resource.volume_of_one_unit
#                     store.save()
#                     stock.delete()
#                     break_count = True
#                 else:
#                     count -= stock.amount
#                     store.free_volume += stock.amount * resource.volume_of_one_unit
#                     store.save()
#                     delete_stock = True
#             if delete_stock is True:
#                 stock.delete()
#             if break_count is True:
#                 break
#         if break_count is True:
#             break

def create_stock(resource_order):
    from main.models import Stock
    Stock.objects.create(resource=resource_order.resource, amount=resource_order.amount)