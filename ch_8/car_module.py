def build_car(manufacturer, model, **info):
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for k,v in info.items():
        car[k] = v
    return car