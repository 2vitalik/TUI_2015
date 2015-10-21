from _ast import Store
from setuptools.command.saveopts import saveopts
from main.models import Volonter
from main.models import StoreHouse
from main.models import Stock
from main.models import Resource

def fill_store_houses():
    store_houses = StoreHouse.objects.all()
    sort_store_houses = sorted(store_houses, key = lambda x: x.rent)

    for store in sort_store_houses:
        free = StoreHouse.free_volume.store
        volume = Resource.volume_of_one_unit.self
        amount = Stock.amount.self
        if volume*amount <= free:
            Stock.storeHouseId.self = StoreHouse.store.pk
            free -= volume*amount
        elif volume > free:
            continue
        else:
            cur_amount = int(free/volume)
            residual_amount = amount - cur_amount
            Stock.objects.create(storeHouseId = StoreHouse.store.pk, resource = Stock.storeHouseId.self, amount = cur_amount )
            Stock.amount.self = residual_amount
            free -= volume * cur_amount

        StoreHouse.free_volume.store = free

########################################################################################################################
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