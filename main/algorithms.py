from _ast import Store
from setuptools.command.saveopts import saveopts



def fill_store_houses(stock):

    from main.models import Resource
    from main.models import StoreHouse
    from main.models import Stock


    store_houses = StoreHouse.objects.all()
    sort_store_houses = sorted(store_houses, key = lambda x: x.rent)
    resource = stock.resource

    for store in sort_store_houses:
        free = store.free_volume
        volume = resource.volume_of_one_unit
        amount = stock.amount
        if volume*amount <= free:
            stock.store_house = store
            stock.save()
            free -= volume*amount
        elif volume > free:
            continue
        else:
            cur_amount = int(free/volume)
            residual_amount = amount - cur_amount
            Stock.objects.create(store_house=store, resource=stock.store_house, amount=cur_amount)
            stock.amount = residual_amount
            stock.save()
            free -= volume * cur_amount

        store.free_volume = free
        store.save()

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