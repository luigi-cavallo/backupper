'''
    Autore : Cavallo Luigi
    Descrizione:
    Questo programma permette di effettuare facilmente backup di file su disco o su altri
    dispositivi di memorizzazione.
    Per adesso è supportato solo su window
'''
import os.path as op
import os

def main():
    welcome()
    exec_command()

def print_file(directory):
    ''' print a list of directories '''
    for file in os.listdir(directory):
        print("**" + file +"**")


def exec_command():
    ''' comandi per l'utente '''
    directory = None        #directory di cui effettuare il backup
    device = None           #device selezionato per il backup dei dati
    ask = ""                #domande all'utente
    param = ()              #cattura eventuali parametri
    all_parameters = 0      #somma dei parametri
    try :

        os.chdir("C:\\")    #path di default
    except:
        print("errore inspiegabile contattare il programmatore")
        exit(1)

    print("Type help for a list of all commands")

    while True:
        cmd = input("->")
        '''param = (cmd.split())
        param = param[1:]
        all_parameters = len(param)'''
        if cmd.strip() == "help":
            list_of_commands()

        elif cmd.strip() == "copy":
            copy(device,directory)

        elif cmd.strip() == "chdir":
            ask = str(input("percorso nuovo directory di cui effettuare il backup: "))
            chdir(ask)

        elif cmd.strip() == "target":
            if directory:
                target(directory)
            else:
                print("nessuna directory scelta per il backup")

        elif cmd.strip() == "path":
            #print("percorso corrente: ", os.getcwd())
            path()

        elif cmd.strip() == "device":
            if device :
                dev(device)
            else:
                print("device non ancora selezionato")

        elif cmd.strip() == "rmdevice":
            device = rmdevice(device)

        elif cmd.strip() == "log":
            print("Non ancora implementata")

        elif cmd.strip() == "setdevice":
            if not device:
                device = str(input("Device: "))
                if os.path.lexists(device):
                    print("device selezionato per il backup: ",device)
                else:
                    print("device non disponibile")
                    device = None
            else:
                print("device già selezionato, utilizzare il comando 'device'per visualizzare il device corrente")

        elif cmd.strip() == "setdir":
            if not directory:
                directory = str(input("directory di cui effettuare il backup: "))
                if os.path.exists(directory):
                    print("directory scelta [%s]" %(directory))
                    os.chdir(directory)
                else:
                    print("directory inesistente o nome directory errato")
                    directory = None
            else:
                print("directory già settata")

        elif cmd.strip() == "listfile":
            if not directory:
                print("devi settare prima una directory usando il comando 'setdir'")
            else:
                print_file(directory)

        elif cmd.strip() == "clear":
            os.system("cls")

        elif cmd.strip() == "exit":
            print("Grazie per aver usato Backupper!!")
            os.system("cls")
            break
        else:
            print("comando errato")

################################################################## FUZIONALITA' IMPLEMENTATE ##########################################################################
def copy(dev, directory, param = None):
    ''' permette la copia di file '''
    #TODO: DA IMPLEMENTARE ESCLUSIONE DI DETERMINATI FILE PER LA COPIA, E IL PASSAGGIO DI EVENTUALI PARAMETRI
    ask = ""        #domande ad utente
    exclude = ""    #eslusione file
    new = ""        #name new dir

    if dev != None and directory != None:
        ask = str(input("Vuoi creare un cartella con il nome di quella di cui effettui il backup?(s/n): "))
        if ask == "si" or ask == "no" or ask == "s" or ask == "n":
            if ask == "si" or ask == "s":
                try:
                    os.chdir(dev)
                    new = directory.split("\\")[-1]
                    os.mkdir(new)
                    os.system("xcopy %s /E %s"%(directory, r"%s%s"%(dev,new)))
                    os.system("pause")
                except:
                    print("errore imprevisto")
            else:
                os.system("xcopy %s /E %s"%(directory, dev))
                os.system("pause")
        else:
            print("Opzione non valida")
    else:
        print("nessun device o directory selezionata")

def rmdevice(dev):
    ''' rimuove il device precedente '''
    if not dev:
        print("device già rimosso")
    dev = None
    print("device precedente rimosso con successo")
    return dev

def chdir(directory, param = None):
    ''' permette di cambiare directory corrente '''
    d = ""      #nome directory
    if os.path.exists(directory):
        d = directory
        try:
            os.chdir(d)
            print("directory di lavoro corrente : %s" %(os.getcwd()))
        except:
            print("non è stato possibile impostare la nuova destinazione")
    else:
        print("percorso directory errata")

def target(directory):
    print("directory : [%s]" %(directory))

def path():
    print("percorso corrente: ", os.getcwd())

def dev(device):
    print("device selezionato per il backup : ",device)

def tmp_log(list_of_file):
    ''' salva i nomi dei file prima di effettuare una determinata operazione '''
    log_folder = "C:\\Users\caval"
    try:
        os.chdir(log_folder)
    except:
        print("errore fatale!!")
        exit(1)
    file = open("log.txt","a")
    for f in list_of_file:
        #scrive nel log i file prima di effettuare un operazione
        file.write(f+"\n")

def list_of_commands():
    print('''
    COMANDI:
        copy -> copia tutti i file nella directory corrente
        setdir -> imposta la directory su cui effettuare il backup
        listfile -> visualizza i file della directory impostata come backup
        chdir -> cambia la directory di lavoro
        target -> mostra la directory scelta per il backup
        dev -> mostra il device che è stato selezionato per il backup
        setdevice -> setta il device per il backup
        rmdevice -> rimuove il device precedentemente selezionato
        path -> mostra il percorso di lavoro corrente
        log -> avvia o disatttiva i file di log
        clear -> cancella schermo
        exit -> chiude backupper
    ''')

######################################################################################################################################################################
def welcome():
    print('''

    Benvenuto su backupper, inizia il tuo backup ^-^

    ''')
if __name__ == "__main__":
    main()
