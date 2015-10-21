from _ast import Store
from setuptools.command.saveopts import saveopts
from main.models import Volonter
from main.models import StoreHouse
from main.models import Stock
from main.models import Resource

def fill_store_houses():

    store_houses = StoreHouse.objects.all()
    resource_stock = Stock.objects.all()

    sort_store_houses = sorted(store_houses,key = StoreHouse.rent)
    sort_stock = sorted(resource_stock, key = Resource.volume_of_one_unit, reverse=True)

    for store in sort_store_houses:
        free = StoreHouse.free_volume.store
        for res in sort_stock:
            volume = Resource.volume_of_one_unit.res
            amount = Stock.amount.res
            if volume*amount <= free:
                Stock.storeHouseId.res = StoreHouse.store.pk
                free -= volume*amount
            elif volume > free:
                continue
            else:
                cur_amount = int(free/volume)
                residual_amount = amount - cur_amount
                Stock.objects.create(storeHouseId = None, resource = Stock.storeHouseId.res, amount = residual_amount )
                #create new stock with (amount = cur_amount) and id = StoreHouse.store.pk
                #update current stock set amount = residual_amount
                Stock.amount.res = residual_amount
                free -= volume*cur_amount

        StoreHouse.free_volume.store = free

def create_resource_orders(need):
    volonters = Volonter.objects.filter(fio__contains='')
    count = len(volonters)
    for volonter in volonters:
        print volonter.fio

   # ResourceOrder.objects.create(
        # priority=0.5,
        # date_of_starting = datetime.now(),
        # date_of_finish = datetime.now() + timedelta(days=1),
   # )