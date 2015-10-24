# coding: utf-8
import math



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
def create_resource_orders(need):
    from datetime import timedelta,datetime
    from main.models import Stock
    from main.models import Need
    from main.models import ResourceOrder
    from main.models import StoreHouse
    from main.models import Resource

    stocks = Stock.objects.all()
    filter_stocks = stocks.filter(resource=need.resource).exclude(store_house = None)
    store_houses = StoreHouse.objects.all()
    filter_store_houses=[]
    for store in store_houses:
        for stock in filter_stocks:
            if store == stock.store_house:
                filter_store_houses.append(store)
            else:
                continue
    # фильтруем склады начиная с самого дорогого
    sorted_stores = sorted(filter_store_houses, key=lambda x: x.rent, reverse=True)
    # сумируем кол-во ресурсов
    count_stock_res = sum([res.amount for res in filter_stocks])
    # если нужно создаем ResourceOrder
    if count_stock_res < need.amount:
        ResourceOrder.objects.create(
            resource = need.resource,
            amount = need.amount - count_stock_res,
            finished = False,
            date_finished = datetime.now() + timedelta(days=1),
        )
        need.amount = count_stock_res
        need.save()
    resource = need.resource
    # пробегамся начиная с самого дорого склада, и любого запаса с этого склада, удаляем нулевые запасы
    count = need.amount
    for store in sorted_stores:
        for stock in filter_stocks:
            break_count = False
            delete_stock = False
            if store == stock.store_house:
                if count < stock.amount:
                    stock.amount -= count
                    stock.save()
                    store.free_volume += count * resource.volume_of_one_unit
                    store.save()
                    break_count = True
                elif count == stock.amount:
                    store.free_volume += count * resource.volume_of_one_unit
                    store.save()
                    stock.delete()
                    break_count = True
                else:
                    count -= stock.amount
                    store.free_volume += stock.amount * resource.volume_of_one_unit
                    store.save()
                    delete_stock = True
            if delete_stock is True:
                stock.delete()
            if break_count is True:
                break
        if break_count is True:
                break
