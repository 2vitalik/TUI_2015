# coding: utf-8
import math
from datetime import timedelta, datetime



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

# volonters = Volonter.objects.filter(fio__contains='')


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
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
    needs_1 = Need.objects.filter(resource=need.resource)
    needs_2 = need.resource.need_set.all()
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
#todo:fill_store_houses()
# virtual_stocks = Stock.objects.filter(store_house__isnull=True)
#  for stock in virtual_stocks:
#      fill_store_houses(stock)


def create_stock(resource_order):
    from main.models import Stock
    Stock.objects.create(resource=resource_order.resource, amount=resource_order.amount)


def deikstra(graf,start,end):
    used = [False]*200000
    g = [1e9]*100000
    p = [0]*100000
    # p.append.(store_house.geography_point.pk)
    #todo: store_house.geography_point.pk, point_of_consuming.geography_point.pk
    # g[store_house.geography_point.pk] = 0
    g[start] = 0

    for l in range(len(graf)):
        index = -1
        curres = 1e9
        for j in graf:
                if (used[j] == False) and ((index == -1) or (g[j] < g[index])):
                    index = j
        if g[index] == curres:
            break
        used[index] = True
        for (u,w) in graf[index]:
            if g[u] > g[index]+w:
                 g[u] = g[index]+w
                 p[u] = index

    pairs = []
    if p[start] == 0:
        return pairs
    cur_point = end
    while cur_point != start:
        pairs.append((p[cur_point],cur_point))
        cur_point = p[cur_point]
    pairs.reverse()
    # p_sort = []
    # pairs = []
    # for lu in p:
    #     # if lu != point_of_consuming.geography_point.pk
    #         p_sort.append(lu)
    # p_sort.reverse()
    # for i in range(len(p_sort)-1):
    #         pairs.append((p[i],p[i+1]))
    #         # print(pairs[i])
    return pairs, g[end.geography_point.pk]

def create_graf_chip(store_house, point_of_consuming,transport):
    from main.models import Way
    from main.models import PointOfConsuming
    from main.models import GeographyPoint
    from main.models import StoreHouse
    ways = Way.objects.all()
    points = GeographyPoint.objects.all()
# /////////////////////////1////////////////////////////////////////////////////////////////////////////////////////////
    graf = dict()
    for point in points:
        for road in ways:
            if road.point_from == point and transport.passability >= road.passability:
                if road.point_from in graf:
                    graf[road.point_from.pk].append((road.point_to.pk, road.roat_length/transport.expences_fuel))
                else:
                    graf[road.point_from.pk] = [(road.point_to.pk, road.roat_length/transport.expences_fuel)]

                if road.point_to in graf:
                    graf[road.point_to.pk].append((road.point_from.pk, road.roat_length/transport.expences_fuel))
                else:
                    graf[road.point_to.pk] = [(road.point_from.pk, road.roat_length/transport.expences_fuel)]
    a = deikstra(graf,store_house,point_of_consuming)
    return a
    # for n, data in graf_length.items():
    #     print n.pk
    #     for a, b in data:
    #         print (a, b)

#///////////////////////////////////////2///////////////////////////////////////////////////////////////////////////////
def create_graf_danger(store_house, point_of_consuming, transport):
    from main.models import Way
    from main.models import PointOfConsuming
    from main.models import GeographyPoint
    from main.models import StoreHouse
    ways = Way.objects.all()
    points = GeographyPoint.objects.all()
    graf = dict()
    for point in points:
        for road in ways:
            if road.point_from.pk == point.pk and transport.passability >= road.passability:
                if road.point_from in graf:
                    graf[road.point_from.pk].append((road.point_to.pk, round(-1.0 * math.log(1-road.danger),4)))
                else:
                    graf[road.point_from.pk] = [(road.point_to.pk, round(-1.0 * math.log(1-road.danger),4))]

                if road.point_to.pk in graf:
                    graf[road.point_to.pk].append((road.point_from.pk, round(-1.0 * math.log(1-road.danger),4)))
                else:
                    graf[road.point_to.pk] = [(road.point_from.pk, round(-1.0 * math.log(1-road.danger),4))]
    a = deikstra(graf, store_house, point_of_consuming)
    return a

    # for n, data in graf_danger.items():
    #     print n
    #     for a, b in data:
    #         print (a, b)

def create_graf_time(store_house, point_of_consuming,transport):
    # def create_graf_chip(store_house, point_of_consuming):
    from main.models import Way
    from main.models import PointOfConsuming
    from main.models import GeographyPoint
    from main.models import StoreHouse
    ways = Way.objects.all()
    points = GeographyPoint.objects.all()
# /////////////////////////3////////////////////////////////////////////////////////////////////////////////////////////
    graf = dict()

    for point in points:
        for road in ways:
            if road.point_from == point:
                if road.point_from in graf and transport.passability >= road.passability:
                    graf[road.point_from.pk].append((road.point_to.pk, speed(transport, road) * math.log(min(transport.passability),5)/math.log(5)))
                else:
                    graf[road.point_from.pk] = [(road.point_to.pk, speed(transport, road) * math.log(min(transport.passability),5)/math.log(5))]

                if road.point_to in graf:
                    graf[road.point_to.pk].append((road.point_from.pk, speed(transport, road) * math.log(min(transport.passability),5)/math.log(5)))
                else:
                    graf[road.point_to.pk] = [(road.point_from.pk, speed(transport, road) * math.log(min(transport.passability),5)/math.log(5))]

    # for n, data in graf_length.items():
    #     print n.pk
    #     for a, b in data:
    #         print (a, b)
    a = deikstra(graf, store_house, point_of_consuming)
    return a

def complacency(need):
    from main.models import Need
    from main.models import Resource
    if datetime.now() > need.date_recomended:
        comp = 0
    else:
        comp = (need.resource.price_one_unit*need.priority)/math.log(min(5,need.date_recomended - datetime.now()), 5)
    return comp


def speed(transport,way):
    from main.models import Way
    from main.models import Transport
    general_speed = transport.speed/(transport.passability - way.passability)
    return general_speed


def cost_res_in_store_house(stock, store_house):
    from main.models import StoreHouse
    from main.models import Stock
    cost = (stock.resource.volume_of_unit * store_house.rent)/store_house.volume
    return cost


def general_algo():
    pass


def K_func(transport, store_house, point_of_consuming):
    pass


def algo_2(transport, store_house, point_of_consuming):
    from main.models import KindOfTransport
    from main.models import StoreHouse
    from main.models import PointOfConsuming
    from main.models import Need
    from main.models import Stock
    from main.models import Transport
    from main.models import Resource
    from main.models import Order
    from main.models import ShippingDetalization

    orders = Order.objects.filter(point_of_consuming=point_of_consuming)
    diction = {Resource.objects.all(): {orders: 0}}

    volume_cur = transport.volume_transport
    sum_opt = 0
    coef_best = 1

    while coef_best != 0:
        coef_best = 0
        need_best = None
        stock_best = None
        order_best = None
        complacency_max = 0
        for order in orders:
            needs = order.need_set.all()
            for need in needs:
                if need.amount == 0:
                    continue
                stocks = Stock.objects.filter(resource=need.resorce, store_house=store_house)
                amount = 0
                for stock in stocks:
                    amount += stock.amount

                if stock.resource.volume_of_unit <= volume_cur and amount > 0:
                    if complacency(need)/need.resource.volume_of_one_unit > coef_best:
                        stock_best = stock
                        order_best = order
                        need_best = need
                        coef_best = complacency(need)/need.resource.volume_of_one_unit
                        complacency_max = complacency(need)

        sum_opt = sum_opt + stock_best.resource.volume_of_one_unit*cost_res_in_store_house(stock_best, store_house) + complacency_max
        volume_cur -= stock_best.resource.volume_of_one_unit
        diction[stock_best.resource.pk][order_best.pk] += 1
        need_best.amount -= 1
        need_best.save()

    sum_opt -= K_func(transport, store_house, point_of_consuming)
    return sum_opt, diction



