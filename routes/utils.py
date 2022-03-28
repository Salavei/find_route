from trains.models import Train


def dfs_paths(graph, start, goal):
    """Функция поиска всех возможных маршрутов
        из одного города в другой. Вариант посещения
        одного и того же города более одного раза,
        не рассматривается.
        """
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        if vertex in graph.keys():
            for next_ in graph[vertex] - set(path):
                if next_ == goal:
                    yield path + [next_]
                else:
                    stack.append((next_, path + [next_]))


def get_graph(qs):
    graph = {}
    for q in qs:
        graph.setdefault(q.from_city_id, set())
        graph[q.from_city_id].add(q.to_city_id)
    return graph


def get_routes(request, form) -> dict:
    context = {'form': form}
    data = form.cleaned_data
    # экземпляры, получаем id по точечной анатации
    all_ways = list(dfs_paths(get_graph(Train.objects.all()), data['from_city'].id, data['to_city'].id))
    if not len(all_ways):
        raise ValueError('Маршрута, удовлетворяющего условиям не существует')
    if data['cities']:
        _cities = [city.id for city in data['cities']]
        right_ways = []
        for route in all_ways:
            if all(city in route for city in _cities):
                right_ways.append(route)
        if not right_ways:
            raise ValueError('Маршрут, через эти города невозможен')
    else:
        right_ways = all_ways
    routes = []
    all_trains = {}
    for q in Train.objects.all():
        all_trains.setdefault((q.from_city_id, q.to_city_id), [])
        all_trains[(q.from_city_id, q.to_city_id)].append(q)
    for route in right_ways:
        tmp = {}
        tmp['trains'] = []
        total_time = 0
        for i in range(len(route) - 1):
            total_time += all_trains[(route[i], route[i + 1])][0].travel_time
            tmp['trains'].append(all_trains[(route[i], route[i + 1])][0])
        tmp['total_time'] = total_time
        if total_time <= data['travelling_time']:
            routes.append(tmp)
    if not routes:
        raise ValueError('Время в пути больше заданного')
    print(routes)
    sorted_routes = []
    if len(routes) == 1:
        sorted_routes = routes
    else:
        times = list(set(r['total_time'] for r in routes))
        times = sorted(times)
        for time in times:
            for route in routes:
                if time == route['total_time']:
                    sorted_routes.append(route)
    context['routes'] = sorted_routes
    context['cities'] = {'from_city': data['from_city'].name, 'to_city': data['to_city'].name}
    print(context)
    return context
