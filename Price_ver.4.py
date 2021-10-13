from tkinter import *
from tkinter import ttk

# CALCULATIONS FOR EACH ROOM BASED ON ENTERED VALUES, BOOKING.COM COPY BUTTONS:

def calculate(*args):
    try:
        value = float(mainprice.get())
        off = float((booking.get()) or 0)

        ones.set(round(1.2 * value))
        oneb.set(round((( 1.2 * value) / (1 - (off / 100)))))

        doub.set(round(2 * value))
        doub2.set(round(1.7 * value))
        doubb.set(round(((value) / (1 - (off / 100))) * 2))

        dbal.set((round(2 * value) + 30))  # Added balcony
        dbal2.set(round(1.7 * value) + 30)
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

    except ValueError:
        pass


# SETTING UP MAIN WINDOW

root = Tk()
root.title("Channel Price Calculator")
root.geometry('528x846')

mainframe = ttk.Frame(root, padding="10 8 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# SETTING UP VARIABLES (ALL TYPES OF ROOMS)

mainprice = StringVar()
booking = StringVar()

ones = StringVar()
oneb = StringVar()

doub = StringVar()
doub2 = StringVar()
doubb = StringVar()

dbal = StringVar()
dbal2 = StringVar()
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

# DISPLAY OF CALCULATED VALUES

feet_entry = ttk.Entry(mainframe, width=7, textvariable=mainprice)
feet_entry.grid(column=1, row=1, sticky=(W, E))
feet_entry2 = ttk.Entry(mainframe, width=7, textvariable=booking)
feet_entry2.grid(column=1, row=2, sticky=(W, E))

ttk.Label(mainframe, textvariable=ones, font=('Arial', 10, 'bold')).grid(column=1, row=5, sticky=W)
ttk.Label(mainframe, textvariable=oneb, font=('Arial', 10, 'bold')).grid(column=2, row=5, sticky=W)
ttk.Label(mainframe, textvariable=doub, font=('Arial', 10, 'bold')).grid(column=1, row=6, sticky=W)
ttk.Label(mainframe, textvariable=doub2).grid(column=1, row=7, sticky=W)
ttk.Label(mainframe, textvariable=doubb, font=('Arial', 10, 'bold')).grid(column=2, row=6, sticky=W)

ttk.Label(mainframe, textvariable=dbal, font=('Arial', 10, 'bold')).grid(column=1, row=8, sticky=W) ###
ttk.Label(mainframe, textvariable=dbal2).grid(column=1, row=9, sticky=W)
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


ttk.Label(mainframe, textvariable=stud, font=('Arial', 10, 'bold')).grid(column=1, row=18, sticky=W)
ttk.Label(mainframe, textvariable=studb, font=('Arial', 10, 'bold')).grid(column=2, row=18, sticky=W)
ttk.Label(mainframe, textvariable=stud31).grid(column=1, row=19, sticky=W)
ttk.Label(mainframe, textvariable=stud22).grid(column=1, row=20, sticky=W)
ttk.Label(mainframe, textvariable=stud13).grid(column=1, row=21, sticky=W)


ttk.Label(mainframe, textvariable=apa, font=('Arial', 10, 'bold')).grid(column=1, row=22, sticky=W)
ttk.Label(mainframe, textvariable=apab, font=('Arial', 10, 'bold')).grid(column=2, row=22, sticky=W)
ttk.Label(mainframe, textvariable=apa11).grid(column=1, row=23, sticky=W)
ttk.Label(mainframe, textvariable=apa4, font=('Arial', 10, 'bold')).grid(column=1, row=24, sticky=W)
ttk.Label(mainframe, textvariable=apa4b, font=('Arial', 10, 'bold')).grid(column=2, row=24, sticky=W)

ttk.Label(mainframe, textvariable=apa43d1).grid(column=1, row=25, sticky=W)
ttk.Label(mainframe, textvariable=apa42d2).grid(column=1, row=26, sticky=W)
ttk.Label(mainframe, textvariable=apa41d3).grid(column=1, row=27, sticky=W)

# LABELS

ttk.Label(mainframe, text="Cena podstawowa: ", font=('Helvetica', 12, 'bold')).grid(column=0, row=1, sticky=W)
ttk.Label(mainframe, text="Rabat na Booking.com:", font=('Helvetica', 12, 'bold')).grid(column=0, row=2, sticky=W)
ttk.Label(mainframe, text="% ", font=('Helvetica', 12, 'bold')).grid(column=2, row=2, sticky=W)
ttk.Label(mainframe, text="Ceny po przeliczeniu:", font=('Arial', 10, 'underline')).grid(column=0, row=4, sticky=W, pady=(100, 100))
ttk.Label(mainframe, text="Book. Engine:", font=('Arial', 10, 'underline')).grid(column=1, row=4, sticky=W)
ttk.Label(mainframe, text="Booking.com:", font=('Arial', 10, 'underline')).grid(column=2, row=4, sticky=W)
ttk.Label(mainframe, text="1 os. Standard: ").grid(column=0, row=5, sticky=W)
ttk.Label(mainframe, text="2 os. Standard: ").grid(column=0, row=6, sticky=W)
ttk.Label(mainframe, text="2 os. Standard, 1 os dorosła, 1 dziecko: ").grid(column=0, row=7, sticky=W)

ttk.Label(mainframe, text="2 os. Standard z balkonem: ").grid(column=0, row=8, sticky=W) # Tutaj skończyłem <- trzeba poprawić treść i rzędy
ttk.Label(mainframe, text="2 os. Standard z balkonem, 1 os dorosła, 1 dziecko: ").grid(column=0, row=9, sticky=W) # <--

ttk.Label(mainframe, text="2 os. Lux: ").grid(column=0, row=10, sticky=W)
ttk.Label(mainframe, text="2 os. Lux, 1 os dorosła, 1 dziecko: ").grid(column=0, row=11, sticky=W)

ttk.Label(mainframe, text="3 os. Standard: ").grid(column=0, row=12, sticky=W)
ttk.Label(mainframe, text="3 os. Standard, 2 os dorosłe, 1 dziecko: ").grid(column=0, row=13, sticky=W)
ttk.Label(mainframe, text="3 os. Standard, 1 os dorosła, 2 dzieci: ").grid(column=0, row=14, sticky=W)

ttk.Label(mainframe, text="3 os. Standard z balkonem: ").grid(column=0, row=15, sticky=W) ########
ttk.Label(mainframe, text="3 os. Standard z balkonem, 2 os dorosłe, 1 dziecko: ").grid(column=0, row=16, sticky=W)
ttk.Label(mainframe, text="3 os. Standard z balkonem, 1 os dorosła, 2 dzieci: ").grid(column=0, row=17, sticky=W)

ttk.Label(mainframe, text="4 os. Studio: ").grid(column=0, row=18, sticky=W)
ttk.Label(mainframe, text="4 os. Studio, 3 os dorosłe, 1 dziecko: ").grid(column=0, row=19, sticky=W)
ttk.Label(mainframe, text="4 os. Studio, 2 os dorosłe, 2 dzieci: ").grid(column=0, row=20, sticky=W)
ttk.Label(mainframe, text="4 os. Studio, 1 os dorosła, 3 dzieci: ").grid(column=0, row=21, sticky=W)

ttk.Label(mainframe, text="2 os. Apartament: ").grid(column=0, row=22, sticky=W)
ttk.Label(mainframe, text="2 os. Apartament, 1 os dorosła, 1 dziecko: ").grid(column=0, row=23, sticky=W)

ttk.Label(mainframe, text="4 os. Apartament: ").grid(column=0, row=24, sticky=W)
ttk.Label(mainframe, text="4 os. Apartament, 3 os dorosłe, 1 dziecko: ").grid(column=0, row=25, sticky=W)
ttk.Label(mainframe, text="4 os. Apartament, 2 os dorosłe, 2 dzieci: ").grid(column=0, row=26, sticky=W)
ttk.Label(mainframe, text="4 os. Apartament, 1 os dorosła, 1 dzieci: ").grid(column=0, row=27, sticky=W)

# BUTTON

ttk.Button(mainframe, text="Przelicz", command=calculate).grid(column=0, row=3, sticky=W)

# COPY FUNCTION

def copy(value):
    root.clipboard_clear()
    root.clipboard_append(value.get())
    root.update() # now it stays on the clipboard after the window is closed


# COPY BUTTONS
def show_buttons():
    Button(mainframe, text="⎘", borderwidth=0, font=('times bold', 12), command=lambda : copy(oneb)).grid(column=2, row=5, sticky=E)
    Button(mainframe, text="⎘", borderwidth=0, font=('times bold', 12), command=lambda : copy(doubb)).grid(column=2, row=6, sticky=E)
    Button(mainframe, text="⎘", borderwidth=0, font=('times bold', 12), command=lambda : copy(dbalb)).grid(column=2, row=8, sticky=E)
    Button(mainframe, text="⎘", borderwidth=0, font=('times bold', 12), command=lambda : copy(luxb)).grid(column=2, row=10, sticky=E)
    Button(mainframe, text="⎘", borderwidth=0, font=('times bold', 12), command=lambda : copy(trib)).grid(column=2, row=12, sticky=E)
    Button(mainframe, text="⎘", borderwidth=0, font=('times bold', 12), command=lambda : copy(tbalb)).grid(column=2, row=15, sticky=E)
    Button(mainframe, text="⎘", borderwidth=0, font=('times bold', 12), command=lambda : copy(studb)).grid(column=2, row=18, sticky=E)
    Button(mainframe, text="⎘", borderwidth=0, font=('times bold', 12), command=lambda : copy(apab)).grid(column=2, row=22, sticky=E)
    Button(mainframe, text="⎘", borderwidth=0, font=('times bold', 12), command=lambda : copy(apa4b)).grid(column=2, row=24, sticky=E)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()

