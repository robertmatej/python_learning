"""
Kalkulator kosztu przejazdy na zadanym oddzinku przy podanyn spalaniu samochou
posiada dwie opcje wskazania ceny paliwa,
- ręcznie wprowadzenie do pola Entry
- wrapping aktualnej ceny z Inetrnetu poprzez wskazanie Buttona z rodzajem paliwa (obsłużyć błąd połączenia z Netem)

wrapping aktuanych cen paliw ze strony Autocentrum, wykonano wyłącznie w celach dydaktycznych
"""

from tkinter import Tk, Button, Label, Entry, Frame, X, Y, LEFT, CENTER
from bs4 import BeautifulSoup
from requests import get, exceptions

# Zmienne globalne
reczna_cena = False
podana_cena = 0
rodzaj_paliwa = 'darmowe'


# Obliczenie i wyświetlenie kosztu przejazdu
def licz_koszt(lbl_wynik333, get_trasa, get_spalanie):
    global rodzaj_paliwa
    spalanie = get_spalanie.get()
    dlugosc_trasy = get_trasa.get()
    print_paliwa = {'pb':'PB95', 'pbp':'PB98', 'on':'ON+', 'onp':'ON', 'lpg':'LPG'}

    # obsługa błędów wprowadzenia niewłaściwych danych lub nie wskazania rodzaju paliwa
    try:
        if reczna_cena:
            cena = float(reczna_cena_paliwa(ent_cena_paliwa))
            koszt_przejazdu = cena * float(spalanie) * float(dlugosc_trasy) * 0.01
            lbl_wynik.configure(text=f'Koszt przejazdu {dlugosc_trasy}km przy cenie {cena}PLN wyniesie {round(koszt_przejazdu, 2)}PLN', font=35, fg='darkgreen', bg='lightgreen', wraplength=200)
        else:
            koszt_przejazdu = pobierz_cenę_paliwa()[rodzaj_paliwa] * float(spalanie) * float(dlugosc_trasy) * 0.01
            lbl_wynik.configure(text=f'Koszt przejazdu {dlugosc_trasy}km na {print_paliwa[rodzaj_paliwa]} wyniesie {round(koszt_przejazdu, 2)}PLN', font=35, fg='darkgreen',bg='lightgreen', wraplength=200)
    except ValueError:
        lbl_wynik.configure(text=f'Proszę wprowadzić właściwe parametry', font=80, bg='pink', fg='red')
    except KeyError:
        lbl_wynik.configure(text=f'Wskaż rodzaj paliwa', font=80, fg='red')
    except TypeError:
        #pass
        lbl_wynik.configure(text=f'Problem z dostępem do źródła cen, strona nie odpowiada, wprowadź cenę ręcznie', font=80, fg='red', bg='pink', wraplength=200)

# wrapping aktuanych cen paliw ze strony Autocentrum, wykonano wyłącznie w celach dydaktycznych
def pobierz_cenę_paliwa():
    URL = 'https://www.autocentrum.pl/paliwa/ceny-paliw/'
    try:
        page = get(URL)
        bs = BeautifulSoup(page.content, 'html.parser')
        matryca_paliw = ['pb', 'pbp', 'on', 'onp', 'lpg']
        slownik_cen_paliw = dict()

        for paliwo in matryca_paliw:
            paliwa = bs.find('a', class_=f"station-detail-wrapper {paliwo} text-center active")
            cena = paliwa.find('div', class_="price")
            final_cena = (cena.contents[0].get_text(strip=True))
            slownik_cen_paliw[paliwo] = float(final_cena.replace(',', '.'))
        return slownik_cen_paliw
    # Błąd nie zostanie wyświetlony gdyż wcześniej zgłosi się błąd warości w słowniku, obsługa usuwa błąd połączenia w terminalu, przy pass też obsugiwało błąd
    except exceptions.ConnectionError:
        lbl_wynik.configure(text=f'Źródło cen nie odpowiada, sprawdz połączenie Internetowe', font=80, fg='red', wraplength=200)
        
# obsługa przycisku ręcznej ceny
def reczna_cena_paliwa(get_cena_paliwa):
    global reczna_cena
    global podana_cena
    reczna_cena = True

    podana_cena = get_cena_paliwa.get()
    return podana_cena.replace(',', '.')

# obsługa przycisków z rodzajem paliwa
def wybor_paliwa_button(paliwo):
    global rodzaj_paliwa
    global reczna_cena
    reczna_cena = False
    rodzaj_paliwa = paliwo


root = Tk()
root.title('Kalkulator kosztów przejazdu samochodem')
#root.geometry('450x550')


lbl_instruction = Label(text='Wprowadź spalanie samochodu', fg="green", font=30)
lbl_instruction.pack(fill=X, expand=True)

# pobranie spalania
ent_spalanie = Entry(text='Wprowadź średnie spalanie', fg='blue', font=25, bg='lightgrey', width=25, justify=CENTER)
ent_spalanie.pack(padx=15, pady=5)
ent_spalanie.insert(0, '')

lbl_instr_trasa = Label(text='Wprowadź długość trasy', fg="green", font=30)
lbl_instr_trasa.pack(fill=X, expand=True)

# pobranie długości trasy
ent_trasa = Entry(fg='blue', font=25, bg='lightgrey', width=20, justify=CENTER)
ent_trasa.pack(padx=15, pady=5)

# ramka dla paliw
frm_paliwa = Frame(master=root, width=300, height=400, bg='navy')
frm_paliwa.pack(padx=15, pady=15)

# przyciski wyboru paliwa
btn_paliwo_ON = Button(master=frm_paliwa, text='ON', relief='groove', bd=4, bg='black', fg='white', font=25, width=5, height=2)
btn_paliwo_95 = Button(master=frm_paliwa, text='95', relief='groove', bd=4, bg='green', fg='white', font=25, width=5, height=2)
btn_paliwo_98 = Button(master=frm_paliwa, text='98', relief='groove', bd=4, bg='green', fg='white', font=25, width=5, height=2)
btn_paliwo_ONp = Button(master=frm_paliwa, text='ON+', relief='groove', bd=4, bg='black', fg='white', font=25, width=5, height=2)
btn_paliwo_LPG = Button(master=frm_paliwa, text='LPG', relief='groove', bd=4, bg='blue', fg='white', font=25, width=5, height=2)
btn_paliwo_ON.pack(fill=X, side=LEFT, padx=10, pady=10)
btn_paliwo_ONp.pack(fill=X, side=LEFT, padx=10, pady=10)
btn_paliwo_95.pack(fill=X, side=LEFT, padx=10, pady=10)
btn_paliwo_98.pack(side=LEFT, padx=10, pady=10)
btn_paliwo_LPG.pack(side=LEFT, padx=10, pady=10)

# ramka dla ręcznej ceny
frm_reczna_cena = Frame(master=root, width=450, height=200, bg='navy')
frm_reczna_cena.pack()
frm_reczna_cena.rowconfigure(0, minsize=50)
frm_reczna_cena.columnconfigure([0, 1], minsize=50)

# formularz ręcznej ceny
ent_cena_paliwa = Entry(master=frm_reczna_cena, fg="blue", font=25, bg='lightgrey', width=5, justify=CENTER)
#ent_cena_paliwa.place(x=10, y=0)
#ent_cena_paliwa.pack(side=LEFT)
ent_cena_paliwa.grid(row=0, column=0, sticky='e', padx=5, pady=10)

# button ręcnzej ceny
btn_podaj_cene_paliwa = Button(master=frm_reczna_cena, text="Własna cena", font=25, fg="orange", bg='purple', width=11, height=2)
#btn_podaj_cene_paliwa.place(x=30, y=100)
#btn_podaj_cene_paliwa.pack(side=RIGHT)
btn_podaj_cene_paliwa.grid(row=0, column=1, sticky='w', padx=5, pady=15)

# button obliczający koszt przejazdu
licz = Button(text="Kalkuluj koszt", font=25, fg='blue', bg='gold', width=13, height=2)
licz.pack(expand=True, pady=15)

lbl_wynik = Label(text='koszt przejazdu PLN', font=35, fg='red', width=40, bg='lavender')
lbl_wynik.pack(expand=True, pady=20)

btn_podaj_cene_paliwa.configure(command=lambda: reczna_cena_paliwa(ent_cena_paliwa))
licz.configure(command=lambda:licz_koszt(lbl_wynik, ent_trasa, ent_spalanie))

# obsługa przycisków wyboru palwa
btn_paliwo_ON.configure(command=lambda: wybor_paliwa_button('onp'))
btn_paliwo_ONp.configure(command=lambda: wybor_paliwa_button('on'))
btn_paliwo_95.configure(command=lambda: wybor_paliwa_button('pb'))
btn_paliwo_98.configure(command=lambda: wybor_paliwa_button('pbp'))
btn_paliwo_LPG.configure(command=lambda: wybor_paliwa_button('lpg'))


root.mainloop()

