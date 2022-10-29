from unittest import result
from webbrowser import get
import population
def run(): 

    data = [{'Country': 'Bolivia',
    'population': 500}]
    country = input('Pais:')

    result = population.get_population(data,country)

    print(result)
        
if __name__ == "__main__":
        run()