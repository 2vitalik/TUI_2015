from _ast import Store
from setuptools.command.saveopts import saveopts



def fill_store_houses(stock):

    from main.models import StoreHouse
    from main.models import Stock

    store_houses = StoreHouse.objects.all()
    sort_store_houses = sorted(store_houses, key = lambda x: x.rent)
    resource = stock.resource
    storehouses_params = []
    for store in sort_store_houses:
        storehouses_params.append((store.pk, store.free_volume))


    # to_add = []
    # virtual_stocks = Stock.objects.filter(store_house__isnull=True)

    for id, free_volume in storehouses_params:
        volume = resource.volume_of_one_unit
        amount = stock.amount
        if volume*amount <= free_volume:
            stock.store_house = id
            stock.save()
            free_volume -= volume*amount
            break
        elif volume > free_volume:
            stock.store_house = None
            continue
        else:
            cur_amount = int(free_volume/volume)
            residual_amount = amount - cur_amount
            # to_add.append([store, resource, cur_amount])
            Stock.objects.create(store_house=id, resource=resource, amount=cur_amount)
            stock.amount = residual_amount
            stock.save()
            free_volume -= volume * cur_amount

    for i in range(len(sort_store_houses)):
        sort_store_houses[i].free_volume = storehouses_params[i][[1]]
    sort_store_houses.save()

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