"""
program requesting many times exteranl HTTP service using HTTP protoco.
Compare runing time with one thread and many threads.
Use threading module.
"""

import requests
import threading
import datetime


# Function gets currency exchanges from NBP API, exchange course of xx to PLN
def get_exchange_rate(currency):
    currency_exchange_rate_source = f"http://api.nbp.pl/api/exchangerates/rates/a/{currency}/?format=json"

    response = requests.get(currency_exchange_rate_source)
    data = response.json()
    # getting currency exchange
    currency_exchange_rate = data['rates'][0]['mid']
    # getting exchanged currency name
    currency_name = data['currency']

    print(f'{currency_name}: {currency_exchange_rate}')

#    return currency_exchange_rate

# defining threads for currencies
t_eur = threading.Thread(target=get_exchange_rate, args=('eur',))
t_usd = threading.Thread(target=get_exchange_rate, args=('usd',))
t_jpy = threading.Thread(target=get_exchange_rate, args=('jpy',))
t_chf = threading.Thread(target=get_exchange_rate, args=('chf',))
t_huf = threading.Thread(target=get_exchange_rate, args=('huf',))
t_try = threading.Thread(target=get_exchange_rate, args=('try',))
t_sek = threading.Thread(target=get_exchange_rate, args=('sek',))
t_nok = threading.Thread(target=get_exchange_rate, args=('nok',))


# starting threads nad measuring duration time for one and multi thread
start_time_multi_thread = datetime.datetime.now()
t_eur.start()
t_usd.start()
t_jpy.start()
t_chf.start()
t_huf.start()
t_try.start()
t_sek.start()
start_time_one_thread = datetime.datetime.now()
t_nok.start()


# printing results
program_duration_multi_thread = datetime.datetime.now() - start_time_multi_thread
program_duration_one_thread = datetime.datetime.now() - start_time_one_thread
print('Foreign currency exchange rates to PLN')
print(f'Multi thread working time: {program_duration_multi_thread.microseconds}')
print(f'One thread working time: {program_duration_one_thread.microseconds}\n')