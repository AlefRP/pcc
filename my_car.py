def make_car(manufacturer, model, **car_info):
    """
    A function to create a car with the given manufacturer, model, and additional car information.
    :param manufacturer: the manufacturer of the car
    :param model: the model of the car
    :param car_info: additional information about the car (kwargs)
    :return: a dictionary containing the car information
    """
    """"""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

make_car('Toyota', 'Camry', color='red', year=2020)