
def get_population(data,country):
    result = list(filter(lambda item: item['Country'] == data,country))
    return result
    
    