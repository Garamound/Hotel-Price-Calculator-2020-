from tkinter import *
from tkinter import ttk
import keyboard
from time import sleep
import clipboard as cb
import sys
import os

fill_on = True
# CALCULATIONS FOR EACH ROOM BASED ON ENTERED VALUES, BOOKING.COM COPY BUTTONS:

def calculate(*args):
    try:
        value = float(mainprice.get())
        off = float((booking.get()) or 0)

        ones.set(round(1.23 * value))
        oneb.set(round((( 1.23 * value) / (1 - (off / 100)))))

        double_standard.set(round(2 * value))
        double_standard_11.set(round(1.7 * value))
        doubb.set(round(((value) / (1 - (off / 100))) * 2))

        dbal.set((round(2 * value) + 30))  # Added balcony
        dbal_11.set(round(1.7 * value) + 30)
        dbalb.set(round(((value + 15) / (1 - (off / 100))) * 2))

        lux.set((round(2 * value) + 50))
        lux11.set(round(1.7 * value) + 50)
        luxb.set(round(((value + 25) / (1 - (off / 100))) * 2))

        tri2d1.set(round(2.7 * value))
        tri1d2.set(round(2.4 * value))

        tbal.set(round(3 * value) + 30)
        tbalb.set(round(((value + 30 / 3) / (1 - (off / 100))) * 3))

        tb2d1.set(round(2.7 * value) + 30)
        tb1d2.set(round(2.4 * value) + 30)

        stud.set((round(4 * value) + 50))
        tri.set(round(3 * value))
        trib.set(round(((value) / (1 - (off / 100))) * 3))

        quad_stand_bal.set((round(4 * value) + 30))
        quad_stand_bal_2a2k.set((round(3.4 * value) + 30))
        quad_stand_bal_3a1k.set((round(3.7 * value) + 30))
        quad_stand_bal_1a3k.set((round(3.1 * value) + 30))

        studb.set(round(((value + 12.5) / (1 - (off / 100))) * 4))
        stud22.set((round(3.4 * value) + 50))
        stud31.set((round(3.7 * value) + 50))
        stud13.set((round(3.1 * value) + 50))

        apa.set((round(2 * value) + 100))
        apab.set(round(((value + 50) / (1 - (off / 100))) * 2))
        apa11.set((round(1.7 * value) + 100))

        apa4.set((round(4 * value) + 100))
        apa4b.set(round(((value + 25) / (1 - (off / 100))) * 4))

        apa43d1.set(round(3.7 * value) + 100)
        apa42d2.set(round(3.4 * value) + 100)
        apa41d3.set(round(3.1 * value) + 100)

        show_buttons()
        global columns, price_set, days_set
        columns = int(chosen_column_nr.get())
        price_set = chosen_channel.get()
        days_set = [day1.get(), day2.get(), day3.get(), day4.get(), day5.get(), day6.get(), day7.get()]

    except ValueError:
        pass

def wait_key (times):
    for time in range(times):
        sleep(0.1)
        if keyboard.is_pressed('F8'):
            os.execl(sys.executable, sys.executable, *sys.argv)
            keyboard.release('shift')
            exit()

def broad_fill:

def auto_fill():
    root.wm_state('iconic')

    while True:
        sleep(0.01)
        if keyboard.is_pressed('F4'):
            break
        sleep(0.01)
        if keyboard.is_pressed('F8'):
            keyboard.release('shift')
            os.execl(sys.executable, sys.executable, *sys.argv)
            exit()

    offer_price_list = [
        ones.get(),
        double_standard.get(),
        double_standard_11.get(),
        lux11.get(),
        lux.get(),
        tri1d2.get(),
        tri2d1.get(),
        tri.get(),
        stud22.get(),
        stud31.get(),
        stud.get(),
        stud13.get(),
        apa.get(),
        apa11.get(),
        dbal_11.get(),
        dbal.get(),
        tb1d2.get(),
        tb2d1.get(),
        tbal.get(),
        quad_stand_bal_2a2k.get(),
        quad_stand_bal_3a1k.get(),
        quad_stand_bal.get(),
        quad_stand_bal_1a3k.get(),
        apa41d3.get(),
        apa42d2.get(),
        apa43d1.get(),
        apa4.get()]
    booking_price_list = [
        oneb.get(),
        doubb.get(),
        trib.get(),
        studb.get(),
        apab.get(),
        luxb.get(),
        dbalb.get(),
        tbalb.get(),
        apa4b.get(), ]

    print(days_set)

    while fill_on:
        price_list = []
        nearest_columns = []
        if price_set == 'Oferty': price_list = offer_price_list
        if price_set == 'Booking.com': price_list = booking_price_list

        if not all(days_set):
            list3 = []
            for index in range(columns):
                list3.append((index + 1) * days_set[index % len(days_set)])
            print(list3)

        for item in price_list:
            cb.copy(item)
            keyboard.press('shift')
            for column in range(columns-1):
                wait_key(2)
                keyboard.press_and_release('Right')

            keyboard.release('shift')
            wait_key(3)
            keyboard.press_and_release('ctrl+v')
            wait_key(10)
            keyboard.press_and_release('Down')
            wait_key(10)
        break


# SETTING UP MAIN WINDOW

root = Tk()
root.title("Channel Price Calculator 4.0")
root.geometry('490x792')
#root.iconbitmap('calc.ico')

mainframe = ttk.Frame(root, padding="8 6 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# SETTING UP VARIABLES (ALL TYPES OF ROOMS)

mainprice = StringVar()
booking = StringVar()
channel = StringVar()
chosen_column_nr = StringVar()

ones = StringVar()
oneb = StringVar()

double_standard = StringVar()
double_standard_11 = StringVar()
doubb = StringVar()

dbal = StringVar()
dbal_11 = StringVar()
dbalb = StringVar()

lux = StringVar()
lux11 = StringVar()
luxb = StringVar()

tri = StringVar()
trib = StringVar()
tri2d1 = StringVar()
tri1d2 = StringVar()

tbal = StringVar()
tbalb = StringVar()
tb2d1 = StringVar()
tb1d2 = StringVar()

quad_stand_bal = StringVar()
quad_stand_bal_2a2k = StringVar()
quad_stand_bal_3a1k = StringVar()
quad_stand_bal_1a3k = StringVar()

stud = StringVar()
studb = StringVar()
stud22 = StringVar()
stud31 = StringVar()
stud13 = StringVar()

apa = StringVar()
apab = StringVar()
apa11 = StringVar()
apa4 = StringVar()
apa4b = StringVar()

apa43d1 = StringVar()
apa42d2 = StringVar()
apa41d3 = StringVar()

day1 = IntVar()
day2 = IntVar()
day3 = IntVar()
day4 = IntVar()
day5 = IntVar()
day6 = IntVar()
day7 = IntVar()
day1.set(1)
day2.set(1)
day3.set(1)
day4.set(1)
day5.set(1)
day6.set(1)
day7.set(1)

chosen_channel = ttk.Combobox(mainframe, width=9, textvariable='channel')
chosen_channel['values'] = ('Oferty', 'Booking.com')
chosen_channel.grid(column=2, row=3, sticky=E)
chosen_channel.current(0)

# DISPLAY OF CALCULATED VALUES

feet_entry = ttk.Entry(mainframe, width=8, textvariable=mainprice)
feet_entry.grid(column=0, row=1, sticky=(E))
feet_entry2 = ttk.Entry(mainframe, width=8, textvariable=booking)
feet_entry2.grid(column=0, row=2, sticky=(E))
feet_entry3 = ttk.Entry(mainframe, width=4, textvariable=chosen_column_nr)
feet_entry3.grid(column=2, row=1, sticky=(E))

ttk.Label(mainframe, textvariable=ones, font=('Arial', 10, 'bold')).grid(column=1, row=6, sticky=W)
ttk.Label(mainframe, textvariable=oneb, font=('Arial', 10, 'bold')).grid(column=2, row=6, sticky=W)
ttk.Label(mainframe, textvariable=double_standard, font=('Arial', 10, 'bold')).grid(column=1, row=7, sticky=W)
ttk.Label(mainframe, textvariable=double_standard_11).grid(column=1, row=8, sticky=W)
ttk.Label(mainframe, textvariable=doubb, font=('Arial', 10, 'bold')).grid(column=2, row=7, sticky=W)

ttk.Label(mainframe, textvariable=dbal, font=('Arial', 10, 'bold')).grid(column=1, row=8, sticky=W) ###
ttk.Label(mainframe, textvariable=dbal_11).grid(column=1, row=9, sticky=W)
ttk.Label(mainframe, textvariable=dbalb, font=('Arial', 10, 'bold')).grid(column=2, row=8, sticky=W)

ttk.Label(mainframe, textvariable=lux, font=('Arial', 10, 'bold')).grid(column=1, row=10, sticky=W)
ttk.Label(mainframe, textvariable=luxb, font=('Arial', 10, 'bold')).grid(column=2, row=10, sticky=W)
ttk.Label(mainframe, textvariable=lux11).grid(column=1, row=11, sticky=W)

ttk.Label(mainframe, textvariable=tri, font=('Arial', 10, 'bold')).grid(column=1, row=12, sticky=W)
ttk.Label(mainframe, textvariable=trib, font=('Arial', 10, 'bold')).grid(column=2, row=12, sticky=W)
ttk.Label(mainframe, textvariable=tri2d1).grid(column=1, row=13, sticky=W)
ttk.Label(mainframe, textvariable=tri1d2).grid(column=1, row=14, sticky=W)

ttk.Label(mainframe, textvariable=tbal, font=('Arial', 10, 'bold')).grid(column=1, row=15, sticky=W) ###
ttk.Label(mainframe, textvariable=tbalb, font=('Arial', 10, 'bold')).grid(column=2, row=15, sticky=W)
ttk.Label(mainframe, textvariable=tb2d1).grid(column=1, row=16, sticky=W)
ttk.Label(mainframe, textvariable=tb1d2).grid(column=1, row=17, sticky=W)

ttk.Label(mainframe, textvariable=quad_stand_bal, font=('Arial', 10, 'bold')).grid(column=1, row=18, sticky=W)
ttk.Label(mainframe, textvariable=quad_stand_bal_3a1k).grid(column=1, row=19, sticky=W)
ttk.Label(mainframe, textvariable=quad_stand_bal_2a2k).grid(column=1, row=20, sticky=W)
ttk.Label(mainframe, textvariable=quad_stand_bal_1a3k).grid(column=1, row=21, sticky=W)

ttk.Label(mainframe, textvariable=stud, font=('Arial', 10, 'bold')).grid(column=1, row=22, sticky=W)
ttk.Label(mainframe, textvariable=studb, font=('Arial', 10, 'bold')).grid(column=2, row=22, sticky=W)
ttk.Label(mainframe, textvariable=stud31).grid(column=1, row=23, sticky=W)
ttk.Label(mainframe, textvariable=stud22).grid(column=1, row=24, sticky=W)
ttk.Label(mainframe, textvariable=stud13).grid(column=1, row=25, sticky=W)


ttk.Label(mainframe, textvariable=apa, font=('Arial', 10, 'bold')).grid(column=1, row=26, sticky=W)
ttk.Label(mainframe, textvariable=apab, font=('Arial', 10, 'bold')).grid(column=2, row=26, sticky=W)
ttk.Label(mainframe, textvariable=apa11).grid(column=1, row=27, sticky=W)
ttk.Label(mainframe, textvariable=apa4, font=('Arial', 10, 'bold')).grid(column=1, row=28, sticky=W)
ttk.Label(mainframe, textvariable=apa4b, font=('Arial', 10, 'bold')).grid(column=2, row=28, sticky=W)

ttk.Label(mainframe, textvariable=apa43d1).grid(column=1, row=29, sticky=W)
ttk.Label(mainframe, textvariable=apa42d2).grid(column=1, row=30, sticky=W)
ttk.Label(mainframe, textvariable=apa41d3).grid(column=1, row=31, sticky=W)

# LABELS

ttk.Label(mainframe, text="Cena podstawowa:", font=('Helvetica', 12, 'bold')).grid(column=0, row=1, sticky=W)
ttk.Label(mainframe, text="Ilość kolumn: ", font=('Helvetica', 12, 'bold')).grid(column=1, row=1, columnspan=2)
ttk.Label(mainframe, text="Rabat na Booking.com:", font=('Helvetica', 12, 'bold')).grid(column=0, row=2, sticky=W)
ttk.Label(mainframe, text="% ", font=('Helvetica', 12, 'bold')).grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="Ceny po przeliczeniu:", font=('Arial', 10, 'underline')).grid(column=0, row=5, sticky=W, pady=(100, 100))
ttk.Label(mainframe, text="Book. Engine:", font=('Arial', 10, 'underline')).grid(column=1, row=5, sticky=W)
ttk.Label(mainframe, text="Booking.com:", font=('Arial', 10, 'underline')).grid(column=2, row=5, sticky=W)
ttk.Label(mainframe, text="1 os. Standard: ").grid(column=0, row=6, sticky=W)
ttk.Label(mainframe, text="2 os. Standard: ").grid(column=0, row=7, sticky=W)
ttk.Label(mainframe, text="2 os. Standard, 1 os dorosła, 1 dziecko: ").grid(column=0, row=8, sticky=W)

ttk.Label(mainframe, text="2 os. Standard z balkonem: ").grid(column=0, row=9, sticky=W) # Tutaj skończyłem <- trzeba poprawić treść i rzędy
ttk.Label(mainframe, text="2 os. Standard z balkonem, 1 os dorosła, 1 dziecko: ").grid(column=0, row=10, sticky=W) # <--

ttk.Label(mainframe, text="2 os. Lux: ").grid(column=0, row=11, sticky=W)
ttk.Label(mainframe, text="2 os. Lux, 1 os dorosła, 1 dziecko: ").grid(column=0, row=12, sticky=W)

ttk.Label(mainframe, text="3 os. Standard: ").grid(column=0, row=13, sticky=W)
ttk.Label(mainframe, text="3 os. Standard, 2 os dorosłe, 1 dziecko: ").grid(column=0, row=14, sticky=W)
ttk.Label(mainframe, text="3 os. Standard, 1 os dorosła, 2 dzieci: ").grid(column=0, row=15, sticky=W)

ttk.Label(mainframe, text="3 os. Standard z balkonem: ").grid(column=0, row=16, sticky=W) ########
ttk.Label(mainframe, text="3 os. Standard z balkonem, 2 os dorosłe, 1 dziecko: ").grid(column=0, row=17, sticky=W)
ttk.Label(mainframe, text="3 os. Standard z balkonem, 1 os dorosła, 2 dzieci: ").grid(column=0, row=18, sticky=W)

ttk.Label(mainframe, text="4 os. Standard: ").grid(column=0, row=19, sticky=W)
ttk.Label(mainframe, text="4 os. Standard, 3 os dorosłe, 1 dziecko: ").grid(column=0, row=20, sticky=W)
ttk.Label(mainframe, text="4 os. Standard, 2 os dorosłe, 2 dzieci: ").grid(column=0, row=21, sticky=W)
ttk.Label(mainframe, text="4 os. Standard, 1 os dorosła, 3 dzieci: ").grid(column=0, row=22, sticky=W)

ttk.Label(mainframe, text="4 os. Studio: ").grid(column=0, row=23, sticky=W)
ttk.Label(mainframe, text="4 os. Studio, 3 os dorosłe, 1 dziecko: ").grid(column=0, row=24, sticky=W)
ttk.Label(mainframe, text="4 os. Studio, 2 os dorosłe, 2 dzieci: ").grid(column=0, row=25, sticky=W)
ttk.Label(mainframe, text="4 os. Studio, 1 os dorosła, 3 dzieci: ").grid(column=0, row=26, sticky=W)

ttk.Label(mainframe, text="2 os. Apartament: ").grid(column=0, row=27, sticky=W)
ttk.Label(mainframe, text="2 os. Apartament, 1 os dorosła, 1 dziecko: ").grid(column=0, row=28, sticky=W)

ttk.Label(mainframe, text="4 os. Apartament: ").grid(column=0, row=29, sticky=W)
ttk.Label(mainframe, text="4 os. Apartament, 3 os dorosłe, 1 dziecko: ").grid(column=0, row=30, sticky=W)
ttk.Label(mainframe, text="4 os. Apartament, 2 os dorosłe, 2 dzieci: ").grid(column=0, row=31, sticky=W)
ttk.Label(mainframe, text="4 os. Apartament, 1 os dorosła, 1 dzieci: ").grid(column=0, row=32, sticky=W)

# BUTTON
ttk.Button(mainframe, text="Przelicz", command=calculate).grid(column=1, row=2, sticky=E, padx = 4, pady = 12, columnspan=2)

ttk.Button(mainframe, text=" Tryb autouzupełniania ", command=auto_fill)\
    .grid(column=0, row=3, sticky=W, padx = 4, pady = 12, columnspan=2)


# COPY FUNCTION
def copy(value):
    root.clipboard_clear()
    root.clipboard_append(value.get())
    root.update() # now it stays on the clipboard after the window is closed


# COPY BUTTONS
def show_buttons():
    Button(mainframe, text="⎘", borderwidth=0, font=('times bold', 10), command=lambda : copy(oneb)).grid(column=2, row=6)
    Button(mainframe, text="⎘", borderwidth=0, font=('times bold', 10), command=lambda : copy(doubb)).grid(column=2, row=7)
    Button(mainframe, text="⎘", borderwidth=0, font=('times bold', 10), command=lambda : copy(dbalb)).grid(column=2, row=9)
    Button(mainframe, text="⎘", borderwidth=0, font=('times bold', 10), command=lambda : copy(luxb)).grid(column=2, row=11)
    Button(mainframe, text="⎘", borderwidth=0, font=('times bold', 10), command=lambda : copy(trib)).grid(column=2, row=13)
    Button(mainframe, text="⎘", borderwidth=0, font=('times bold', 10), command=lambda : copy(tbalb)).grid(column=2, row=16)
    Button(mainframe, text="⎘", borderwidth=0, font=('times bold', 10), command=lambda : copy(studb)).grid(column=2, row=23)
    Button(mainframe, text="⎘", borderwidth=0, font=('times bold', 10), command=lambda : copy(apab)).grid(column=2, row=27)
    Button(mainframe, text="⎘", borderwidth=0, font=('times bold', 10), command=lambda : copy(apa4b)).grid(column=2, row=29)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=2)

ttk.Checkbutton(mainframe, text="1", variable=day1).grid(column=0, row=4, sticky=W, columnspan=3, padx=5)

ttk.Checkbutton(mainframe, text="2", variable=day2).grid(column=0, row=4, sticky=W, columnspan=3, padx=35)
ttk.Checkbutton(mainframe, text="3", variable=day3).grid(column=0, row=4, sticky=W, columnspan=3, padx=65)
ttk.Checkbutton(mainframe, text="4", variable=day4).grid(column=0, row=4, sticky=W, columnspan=3, padx=95)
ttk.Checkbutton(mainframe, text="5", variable=day5).grid(column=0, row=4, sticky=W, columnspan=3, padx=125)
ttk.Checkbutton(mainframe, text="6", variable=day6).grid(column=0, row=4, sticky=W, columnspan=3, padx=155)
ttk.Checkbutton(mainframe, text="7", variable=day7).grid(column=0, row=4, sticky=W, columnspan=3, padx=185)

ttk.Label(mainframe, text=" Start: F4   |   Pauza: F8", font=('Helvetica', 10))\
    .grid(column=0, row=3, sticky=W, columnspan=3, pady = 10, padx = 145)
ttk.Label(mainframe, text="Cennik:", font=('Helvetica', 10))\
    .grid(column=0, row=3, sticky=E, columnspan=2, pady = 10, padx = 5)


feet_entry.focus()
root.bind('<Return>', calculate)
root.mainloop()