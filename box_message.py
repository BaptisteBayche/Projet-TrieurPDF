import tkinter
import tkinter.messagebox


class Message():
    def __init__(self):
        self.filename = ''
        self.root = tkinter.Tk()
        self.root.overrideredirect(1)
        self.root.withdraw()
    def set_namefile(self,filename):
        self.filename = filename

    def box_succes(self):
        tkinter.messagebox.showinfo(title='Succés! ',
                                    message='Le fichier '+ self.filename + ' a bien était trié!')

    def box_error(self):
        tkinter.messagebox.showerror(title='Erreur!',
                                     message='Le fichier '+ self.filename + ' ne peut pas être trié!')




if __name__ == '__main__':
    message = Message()
    message.box_succes()