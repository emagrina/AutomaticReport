from datetime import datetime

# chromedriver.exe rute
_driver_path = '#'

my_name = '#'

_addressee = {
    'name': '#',
    'email': '#',
}

date_today = datetime.today().strftime('%Y/%m/%d')

_preference = {
    'title': 'Reporte ' + date_today,
    'header': 'Buenas ' + _addressee['name'] + ',\n\n',
    'content': 'En el día de hoy he hecho lo siguiente:\n\n\n',
    'footer': '\nAtentamente ' + my_name + '.',
}

__all__ = ['_driver_path', '_addressee', '_preference']
