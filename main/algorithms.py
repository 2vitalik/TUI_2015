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
    # total_resource_order = sum(resource_order.amount for resource_order in resource_orders)
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


def deikstra(graf, start, end):
    used = [False]*200000
    g = [1e9]*100000
    p = [0]*100000
    # p.append.(store_house.geography_point.pk)
    #todo: store_house.geography_point.pk, point_of_consuming.geography_point.pk
    # g[store_house.geography_point.pk] = 0
    g[start.geography_point.pk] = 0

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
    # if g[start.geography_point.pk] == 0:
    #     return pairs, g[end.geography_point.pk]
    cur_point = end.geography_point.pk
    while cur_point != start.geography_point.pk:
        if p[cur_point] == 0:
            return [], 1e9
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


# def create_roat(pairs, store_house, point_of_consuming, best_transport):
#     from main.models import Way
#     from main.models import Roat
#     roats = Roat.objects.create(name = "bla", storehouse_id=store_house, point_of_consuming_id=point_of_consuming, transport=best_transport)
#     print(roats)
#     # roat.storehouse_id = store_house
#         # roat.point_of_consuming_id = point_of_consuming
#         # roat.transport = best_transport
#
#     for pair in pairs:
#         way = Way.objects.get(point_from_id=pair[0], point_to_id=pair[1])
#         roats.wasys.add(way)
#
#     return roats

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
            if road.point_from == point and transport.kind_of_transport.passability >= road.passability:
                if road.point_from.pk in graf:
                    graf[road.point_from.pk].append((road.point_to.pk, road.roat_length*transport.kind_of_transport.expences_fuel))
                else:
                    graf[road.point_from.pk] = [(road.point_to.pk, road.roat_length*transport.kind_of_transport.expences_fuel)]

                if road.point_to.pk in graf:
                    graf[road.point_to.pk].append((road.point_from.pk, road.roat_length*transport.kind_of_transport.expences_fuel))
                else:
                    graf[road.point_to.pk] = [(road.point_from.pk, road.roat_length*transport.kind_of_transport.expences_fuel)]
    a = deikstra(graf, store_house, point_of_consuming)
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
    a  = None
    for point in points:
        for road in ways:
            if road.point_from.pk == point.pk and transport.kind_of_transport.passability >= road.passability:
                if road.point_from.pk in graf:
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

def create_graf_time(store_house,point_of_consuming,transport):
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
            if road.point_from == point and transport.kind_of_transport.passability >= road.passability:
                if road.point_from.pk in graf:
                    graf[road.point_from.pk].append((road.point_to.pk, (speed(transport, road)/road.load) * math.log(max(transport.kind_of_transport.passability - road.passability+2,5))/math.log(5)))
                else:
                    graf[road.point_from.pk] = [(road.point_to.pk, (speed(transport, road)/road.load) * math.log(max(transport.kind_of_transport.passability - road.passability+2,5)) / math.log(5))]

                if road.point_to.pk in graf:
                    graf[road.point_to.pk].append((road.point_from.pk, (speed(transport, road)/road.load) * math.log(max(transport.kind_of_transport.passability - road.passability+2,5))/math.log(5)))
                else:
                    graf[road.point_to.pk] = [(road.point_from.pk, (speed(transport, road)/road.load) * math.log(max(transport.kind_of_transport.passability - road.passability+2,5))/math.log(5))]

    # for n, data in graf_length.items():
    #     print n.pk
    #     for a, b in data:
    #         print (a, b)
    a = deikstra(graf, store_house, point_of_consuming)
    return a


def complacency(need):
    from main.models import Need
    from main.models import Resource
    if datetime.now().date() > need.date_recomended:
        comp = 0
    else:
        day_count = (need.date_recomended - datetime.now().date()).days
        comp = (need.resource.price_one_unit*need.priority)/math.log(min(5,day_count), 5)
    return comp


def speed(transport,way):
    from main.models import Way
    from main.models import Transport
    if transport.kind_of_transport.passability < way.passability:
        return 0
    general_speed = transport.kind_of_transport.speed * (transport.kind_of_transport.passability / way.passability / 5)
    return general_speed


def cost_res_in_store_house(stock, store_house):
    from main.models import StoreHouse
    from main.models import Stock
    cost = (stock.resource.volume_of_one_unit * store_house.rent)/store_house.volume
    return cost


def general_algo():
    from main.models import Employment
    from main.models import Transport
    from main.models import Roat, Way, StoreHouse, PointOfConsuming, Stock, Shipping, ShippingDetalization
    transports = Transport.objects.all()
    free_transports = []
    for transport in transports:
        try:
            employment = transport.employment_set.order_by('-date_finish')[0]
        except IndexError:
            employment = None
        if employment and employment.date_finish > datetime.now().date():
            pass  # transport занят
        else:
            free_transports.append(transport)
    store_houses = StoreHouse.objects.all()
    point_of_consumings = PointOfConsuming.objects.all()
    max_sum = 0
    cur_obj_diction = None

    transport_best = None
    store_house_best = None
    point_of_consuming_best = None
    cur_obj_best = None
    for transport in free_transports:
        for store_house in store_houses:
            for point_of_consuming in point_of_consumings:
                print datetime.now(), transport, store_house, point_of_consuming
                cur_sum, cur_dict = algo_2(transport, store_house, point_of_consuming)
                if cur_sum > max_sum:
                    max_sum = cur_sum
                    transport_best = transport
                    store_house_best = store_house
                    point_of_consuming_best = point_of_consuming
                    cur_obj_diction = cur_dict
                # orders = Order.objects.all(point_consuming = point_of_consuming)
                # for res, data in cur_dict.items():
                #     for order_m,amount in data.items():
                #         if amount == 0:
                #             continue
                #         else:
                #             needs = order_m.need_set.all()
                #             need = needs.get(resource=res.pk)# or resoure = res
                #             need.amount += amount
                #             need.save()

    print datetime.now(), 'second step'
    if max_sum == 0:
        return
    else:

        cur_dict = cur_obj_diction
        date_need = (datetime.now() + timedelta(days=100)).date()
        for res, data in cur_dict.items():
            for order_m, amount in data.items():
                if amount == 0:
                    continue
                else:
                    needs = order_m.need_set.all()
                    need = needs.get(resource=res.pk)# or resoure = res
                    need.amount -= amount
                    need.save()
                    if date_need > need.date_recomended:
                        date_need = need.date_recomended
        Employment.objects.create(transport=transport_best, date_finish=date_need)
        shipping = Shipping.objects.create(date_recomended=datetime.now())
        for res, data in cur_dict.items():
            for order_m, amount in data.items():
                if amount <= 0:
                    continue
                else:
                    stocks = Stock.objects.filter(store_house=store_house_best, resource=res)# or resoure = res
                    for stock in stocks:
                        if amount <= stock.amount:
                            ShippingDetalization.objects.create(shipping=shipping, stock=stock, amount=amount)
                            stock.amount -= amount
                            stock.save()
                            store_house_best.free_volume += amount * res.volume_of_one_unit
                            store_house_best.save()
                            break
                        else:
                            amount -= stock.amount
                            ShippingDetalization.objects.create(shipping=shipping, stock=stock, amount=amount)
                            stock.amount -= amount
                            stock.save()
                            store_house_best.free_volume += stock.amount * res.volume_of_one_unit
                            store_house_best.save()

        a = create_graf_time(store_house_best, point_of_consuming_best, transport_best)
        best_pairs = a[0]
        roat = Roat(name=store_house_best.geography_point.address,storehouse=store_house_best,
                    transport=transport_best, point_consuming= point_of_consuming_best)
        roat.save()
        for pair in best_pairs:
            way = Way.objects.get(point_from_id=pair[0], point_to_id=pair[1])
            roat.wasys.add(way.pk)

        print datetime.now(), 'finished'


# todo:fill_store_houses()
    virtual_stocks = Stock.objects.filter(store_house__isnull=True)
    for stock in virtual_stocks:
        fill_store_houses(stock)




def K_func(transport, store_house, point_of_consuming):
    from main.models import Way
    from main.models import PointOfConsuming
    from main.models import GeographyPoint
    from main.models import StoreHouse
    ways = Way.objects.all()
    points = GeographyPoint.objects.all()
    graf = dict()
    for point in points:
        for road in ways:
            if road.point_from.pk == point.pk and transport.kind_of_transport.passability >= road.passability:
                if road.point_from in graf:
                    graf[road.point_from.pk].append((road.point_to.pk, road.roat_length*transport.kind_of_transport.expences_fuel))
                else:
                    graf[road.point_from.pk] = [(road.point_to.pk, road.roat_length*transport.kind_of_transport.expences_fuel)]

                if road.point_to.pk in graf:
                    graf[road.point_to.pk].append((road.point_from.pk,road.roat_length*transport.kind_of_transport.expences_fuel))
                else:
                    graf[road.point_to.pk] = [(road.point_from.pk, road.roat_length*transport.kind_of_transport.expences_fuel)]
    a = deikstra(graf, store_house, point_of_consuming)
    return a[1]


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

    orders = list(Order.objects.filter(point_consuming=point_of_consuming))
    diction = {}
    for resource in Resource.objects.all():
        diction[resource] = {}
        for order in orders:
            diction[resource][order] = 0

    volume_cur = transport.kind_of_transport.volume_transport
    sum_opt = 0
    coef_best = 1

    for order in orders:
        order.needs = list(order.need_set.all().prefetch_related('resource'))

    stock_by_resource = {}
    for order in orders:
        for need in order.needs:
            stock_by_resource[need.resource] = \
                list(Stock.objects.filter(resource=need.resource, store_house=store_house).prefetch_related('resource'))

    while coef_best != 0:
        coef_best = 0
        need_best = None
        stock_best = None
        order_best = None
        complacency_max = 0
        for order in orders:
            for need in order.needs:
                if need.amount == 0:
                    continue
                # stocks = Stock.objects.filter(resource=need.resource, store_house=store_house).prefetch_related('resource')
                stocks = stock_by_resource[need.resource]
                amount = 0
                for stock in stocks:
                    amount += stock.amount

                for stock in stocks:
                    if stock.resource.volume_of_one_unit <= volume_cur and amount > 0:
                        if coef_best is None or complacency(need)/need.resource.volume_of_one_unit > coef_best:
                            stock_best = stock
                            order_best = order
                            need_best = need
                            coef_best = complacency(need)/need.resource.volume_of_one_unit
                            complacency_max = complacency(need)

        if stock_best is None:
            return sum_opt, diction
            # break
        sum_opt += stock_best.resource.volume_of_one_unit*cost_res_in_store_house(stock_best, store_house) + complacency_max
        volume_cur -= stock_best.resource.volume_of_one_unit
        diction[stock_best.resource][order_best] += 1
        need_best.amount -= 1
        # need_best.save()

    sum_opt -= K_func(transport, store_house, point_of_consuming)
    return sum_opt, diction



