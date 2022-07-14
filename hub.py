import tkinter
import options
import tkinter.font
import tkinter.messagebox
from tkinter.filedialog import askopenfilename , askdirectory
from file_management import file_management

import os

class Interface():
    def __init__(self):
        self.fenetre = tkinter.Tk()
        self.fenetre.iconphoto(False, tkinter.PhotoImage(file='icone.png'))
        self.fenetre.title('Trieur PDF')




        self.path = ''
        self.FILETYPES = [("fichier PDF", "*.pdf")]
        font_copyright = tkinter.font.Font(size=8)
        self.create_MenuBar()

        self.filename = tkinter.StringVar(self.fenetre)
        self.l_titre = tkinter.Label(self.fenetre, text='Trieur de PDF')
        self.l_selec_fichier = tkinter.Label(self.fenetre, text='Selectionner un fichier')
        self.l_rename1 = tkinter.Label(self.fenetre, text='Vous pouvez renomer')
        self.l_rename2 = tkinter.Label(self.fenetre, text='le PDF (falcultatif)')
        self.l_copyright = tkinter.Label(self.fenetre, text='by Baptiste.B', font = font_copyright)
        self.e_selec_fichier = tkinter.Entry(self.fenetre, textvariable=self.filename)
        self.b_close = tkinter.Button(self.fenetre, text='Fermer', command=self.fenetre.quit)
        self.b_open = tkinter.Button(self.fenetre, text='Ouvrir', command=self.set_filename)
        self.b_valider = tkinter.Button(self.fenetre, text='Valider', command=self.valider)




        self.l_selec_fichier.grid(padx = 50)
        self.b_open.grid(pady = 2)
        self.e_selec_fichier.grid(pady = 2)
        self.l_rename1.grid()
        self.l_rename2.grid()
        self.b_valider.grid(pady= 2)
        self.b_close.grid(pady = 10)
        self.l_copyright.grid(sticky = 'se')




        self.fenetre.mainloop()

    def set_filename(self):
        global path
        self.path  = askopenfilename(filetypes=self.FILETYPES)
        file = os.path.split(self.path)
        self.filename.set((file[1]))

    def get_filename(self):
        return self.filename.get()

    def get_path(self):
        return self.path

    def valider(self):
         file_management(self.get_path(),options.get_path(),self.get_filename())


    def box_succes(self):
        tkinter.messagebox.showinfo(title= 'Succés! ', message='Le fichier ' + self.get_filename() + 'à bien était trié!')

    def create_MenuBar(self):

        self.menuBar = tkinter.Menu(self.fenetre)
        self.fenetre.config(menu=self.menuBar)

        self.menuFile = tkinter.Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label='Fichier', menu=self.menuFile)
        self.menuAbout = tkinter.Menu(self.menuBar, tearoff=0)
        self.menuBar.add_command(label='A propos', command=self.fenetre_about)

        self.menuFile.add_command(label='Option', command=self.fenetre_option)
        self.menuFile.add_command(label='Fermer', command=self.fenetre.quit)

    def fenetre_option(self):
        self.fenetreOption = tkinter.Toplevel(self.fenetre)
        self.fenetreOption.grab_set()
        self.fenetreOption.title('Options')
        self.fenetreOption.iconphoto(False, tkinter.PhotoImage(file='icone.png'))
        self.pathname = tkinter.StringVar(self.fenetreOption)
        self.pathname.set(options.get_path())


        self.l_option = tkinter.Label(self.fenetreOption,text='Options')
        self.l_change = tkinter.Label(self.fenetreOption,text='Changer le chemin de direction')
        self.b_change = tkinter.Button(self.fenetreOption, text='Changer', command=self.select_dossier)
        self.b_left = tkinter.Button(self.fenetreOption, text='Quitter', command=self.fenetreOption.destroy)
        self.e_path = tkinter.Entry(self.fenetreOption, textvariable=self.pathname)

        self.l_option.grid(pady=2)
        self.l_change.grid(pady=1)
        self.e_path.grid(pady=1)
        self.b_change.grid(pady=3)
        self.b_left.grid(pady=2)


    def select_dossier(self):
        dirname = askdirectory()
        self.set_pathselect(dirname)
    def get_pathselect(self):
        return self.pathname.get()

    def set_pathselect(self,path):
        options.set_path(path)
        self.pathname.set(options.get_path())

    def fenetre_about(self):
        self.fenetreAbout = tkinter.Toplevel(self.fenetre)
        self.fenetreAbout.title('A propos')
        self.fenetreAbout.iconphoto(False, tkinter.PhotoImage(file='icone.png'))

        self.l_about1 = tkinter.Label(self.fenetreAbout, text='Logiciel de trie de PDF automatique !')
        self.l_about2 = tkinter.Label(self.fenetreAbout, text='')
        self.l_about3 = tkinter.Label(self.fenetreAbout, text='Crée par Baptiste')

        self.l_about1.grid()
        self.l_about2.grid()
        self.l_about3.grid()





















if __name__ == '__main__':
    root = Interface()





