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


# def Add(to_add):
#     from main.models import Stock
#     for add in to_add:
#         Stock.objects.create(store_house = add[0], resource = add[1], amount = add[2])

########################################################################################################################
# def create_resource_orders(need):
#     volonters = Volonter.objects.filter(fio__contains='')
#     count = len(volonters)
#     for volonter in volonters:
#         print volonter.fio

   # ResourceOrder.objects.create(
        # priority=0.5,
        # date_of_starting = datetime.now(),
        # date_of_finish = datetime.now() + timedelta(days=1),
   # )