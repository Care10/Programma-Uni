import os, shutil
nome=input("Inserisci nome: ")
cognome=input("Inserisci cognome: ")
indirizzo=input("Inserisci indirizzo: ")
bonus=input("Inserisci bonus: ")

numero=len([number for number in os.listdir(os.getcwd()) if os.path.isdir(number)])

#if os.path.isfile(number)

def autoIncrement():
    global numero
    pStart = 1
    pInterval = 1
    if (numero == 0):
        numero = pStart
    else:
        numero += pInterval
    return numero

numero=autoIncrement()

#numero=autoIncrement()

#Creazione root
os.makedirs("{}_{}_{}_{}_{}".format(numero,nome,cognome,indirizzo,bonus))
#Entrata in root
os.chdir("{}_{}_{}_{}_{}".format(numero,nome,cognome,indirizzo,bonus))
root=os.getcwd()

#01 FASE PRELIMINARE
os.makedirs("01_Fase Preliminare/01_Documento di riconoscimento")
os.makedirs("01_Fase Preliminare/02_Licenze o concessioni edilizie o PDC")
os.makedirs("01_Fase Preliminare/03_Visure catastali PRE")
os.makedirs("01_Fase Preliminare/04_PLN Catastali PRE")
os.makedirs("01_Fase Preliminare/05_Libretto caldaia climatizzatori e impianti")
os.makedirs("01_Fase Preliminare/06_Atto di proprietà")
os.makedirs("01_Fase Preliminare/07_Fattura")
os.makedirs("01_Fase Preliminare/08_Bonifico")
#02 FASE CONTRATTUALE
os.makedirs("02_Fase Contrattuale/01_Contratto preliminare-PRE fattibilità (DOC A)")
#03 FASE PROGETTUALE
os.makedirs("03_Fase Progettuale/01_Rilievo/01_Rilievo fotografico")
os.makedirs("03_Fase Progettuale/01_Rilievo/02_Rilievo grafico")
os.makedirs("03_Fase Progettuale/01_Rilievo/03_Rilievo energetico")

os.makedirs("03_Fase Progettuale/02_Post rilievo/01_Scansione foglio campagna")
os.makedirs("03_Fase Progettuale/02_Post rilievo/02_Scansione copia in bella")

os.makedirs("03_Fase Progettuale/03_Grafico rilievo in DWG-Termus")

os.makedirs("03_Fase Progettuale/04_Invio catasto/01_DOCFA Catasto")
os.makedirs("03_Fase Progettuale/04_Invio catasto/02_Visure Catastali post")
os.makedirs("03_Fase Progettuale/04_Invio catasto/03_PLN Catastali post")


os.makedirs("03_Fase Progettuale/05_Pratica energetica/01_Modello in termus/01_Ante/01_Procedura termus ante")
os.makedirs("03_Fase Progettuale/05_Pratica energetica/01_Modello in termus/01_Ante/02_File ante termus")
os.makedirs("03_Fase Progettuale/05_Pratica energetica/01_Modello in termus/02_Post/01_Procedura termus post")
os.makedirs("03_Fase Progettuale/05_Pratica energetica/01_Modello in termus/02_Post/02_File post termus")
os.makedirs("03_Fase Progettuale/05_Pratica energetica/01_Modello in termus/02_Post/03_Impianto fotovoltaico")
os.makedirs("03_Fase Progettuale/05_Pratica energetica/01_Modello in termus/02_Post/04_Impianto solare")
os.makedirs("03_Fase Progettuale/05_Pratica energetica/01_Modello in termus/02_Post/05_Impianto riscaldamento raffrescamento ACS")

os.makedirs("03_Fase Progettuale/05_Pratica energetica/02_APE ante operam non convenzionale/01_Annullamento APE SID/01_Vecchio APE")
os.makedirs("03_Fase Progettuale/05_Pratica energetica/02_APE ante operam non convenzionale/01_Annullamento APE SID/02_Auto dichiarazione DASN")
os.makedirs("03_Fase Progettuale/05_Pratica energetica/02_APE ante operam non convenzionale/01_Annullamento APE SID/03_PRO forma PEC invio")
os.makedirs("03_Fase Progettuale/05_Pratica energetica/02_APE ante operam non convenzionale/01_Annullamento APE SID/04_PEC Invio")

os.makedirs("03_Fase Progettuale/05_Pratica energetica/02_APE ante operam non convenzionale/02_Procedura SID")
os.makedirs("03_Fase Progettuale/05_Pratica energetica/02_APE ante operam non convenzionale/03_APE ante non convenzionale")
os.makedirs("03_Fase Progettuale/05_Pratica energetica/02_APE ante operam non convenzionale/04_Attestazione energetica ANTE")
os.makedirs("03_Fase Progettuale/05_Pratica energetica/02_APE ante operam non convenzionale/05_Ricevuta di presentazione APE ANTE al SID")
os.makedirs("03_Fase Progettuale/05_Pratica energetica/02_APE ante operam non convenzionale/06_Procedura plico consegna APE ANTE")

os.makedirs("03_Fase Progettuale/05_Pratica energetica/03_Relazione ex legge 10/01_Procedura ex legge 10")
os.makedirs("03_Fase Progettuale/05_Pratica energetica/03_Relazione ex legge 10/02_APE ante superbonus")
os.makedirs("03_Fase Progettuale/05_Pratica energetica/03_Relazione ex legge 10/03_APE post superbonus")
os.makedirs("03_Fase Progettuale/05_Pratica energetica/03_Relazione ex legge 10/04_Relazione di raffronto")
os.makedirs("03_Fase Progettuale/05_Pratica energetica/03_Relazione ex legge 10/05_Grafici esecutivi energetici")
os.makedirs("03_Fase Progettuale/05_Pratica energetica/03_Relazione ex legge 10/06_Schede tecniche")
os.makedirs("03_Fase Progettuale/05_Pratica energetica/03_Relazione ex legge 10/07_Relazione tecnica")

os.makedirs("03_Fase Progettuale/05_Pratica energetica/04_APE post operam non convenzionale/01_Annullamento APE SID/01_Vecchio APE")
os.makedirs("03_Fase Progettuale/05_Pratica energetica/04_APE post operam non convenzionale/01_Annullamento APE SID/02_Autocertificazione DASN")
os.makedirs("03_Fase Progettuale/05_Pratica energetica/04_APE post operam non convenzionale/01_Annullamento APE SID/03_PRO forma PEC invio")
os.makedirs("03_Fase Progettuale/05_Pratica energetica/04_APE post operam non convenzionale/01_Annullamento APE SID/04_PEC Invio")
os.makedirs("03_Fase Progettuale/05_Pratica energetica/04_APE post operam non convenzionale/02_Procedura SID")
os.makedirs("03_Fase Progettuale/05_Pratica energetica/04_APE post operam non convenzionale/03_APE post non convenzionale")
os.makedirs("03_Fase Progettuale/05_Pratica energetica/04_APE post operam non convenzionale/04_Attestazione energetica post")
os.makedirs("03_Fase Progettuale/05_Pratica energetica/04_APE post operam non convenzionale/05_Ricevuta di presentazione APE post al SID")
os.makedirs("03_Fase Progettuale/05_Pratica energetica/04_APE post operam non convenzionale/06_Procedura plico consegna APE post")

os.makedirs("03_Fase Progettuale/06_SCIA (Ordinaria-Sanatoria)/01_Bollettino diritti di segreteria")
os.makedirs("03_Fase Progettuale/06_SCIA (Ordinaria-Sanatoria)/02_Bollettino oneri concessori")
os.makedirs("03_Fase Progettuale/06_SCIA (Ordinaria-Sanatoria)/03_Modulistica")
os.makedirs("03_Fase Progettuale/06_SCIA (Ordinaria-Sanatoria)/04_Relazioni")
os.makedirs("03_Fase Progettuale/06_SCIA (Ordinaria-Sanatoria)/05_OSP")
os.makedirs("03_Fase Progettuale/06_SCIA (Ordinaria-Sanatoria)/06_Grafici")
os.makedirs("03_Fase Progettuale/06_SCIA (Ordinaria-Sanatoria)/07_Protocollo SUE e UTC - SCIA e Legge 10")
os.makedirs("03_Fase Progettuale/06_SCIA (Ordinaria-Sanatoria)/08_Inizio dei lavori/01_DURC Impresa")
os.makedirs("03_Fase Progettuale/06_SCIA (Ordinaria-Sanatoria)/08_Inizio dei lavori/02_Visura camerale impresa")
os.makedirs("03_Fase Progettuale/06_SCIA (Ordinaria-Sanatoria)/08_Inizio dei lavori/03_Documento amministratore impresa")
os.makedirs("03_Fase Progettuale/06_SCIA (Ordinaria-Sanatoria)/08_Inizio dei lavori/04_PSC Impresa")
os.makedirs("03_Fase Progettuale/06_SCIA (Ordinaria-Sanatoria)/08_Inizio dei lavori/05_POS Impresa")
os.makedirs("03_Fase Progettuale/06_SCIA (Ordinaria-Sanatoria)/08_Inizio dei lavori/06_Modulo inizio lavori")
os.makedirs("03_Fase Progettuale/06_SCIA (Ordinaria-Sanatoria)/09_Contratto esecutivo tecnico")
os.makedirs("03_Fase Progettuale/06_SCIA (Ordinaria-Sanatoria)/10_Parcella tecnica")
os.makedirs("03_Fase Progettuale/06_SCIA (Ordinaria-Sanatoria)/11_Contratto esecutivo impresa")
os.makedirs("03_Fase Progettuale/06_SCIA (Ordinaria-Sanatoria)/12_Computo lavori impresa")
#04 FASE IN CORSO D'OPERA
os.makedirs("04_Fase in corso d'opera/01_Controllo qualità/01_Fotografie in corso d'opera")
os.makedirs("04_Fase in corso d'opera/01_Controllo qualità/02_Schede tecniche")
os.makedirs("04_Fase in corso d'opera/01_Controllo qualità/03_Dichiarazione di conformità")

os.makedirs("04_Fase in corso d'opera/02_Trasmissione del credito/01_Asseverazione ENEA")
os.makedirs("04_Fase in corso d'opera/02_Trasmissione del credito/02_Comunicazione della cessione agenzia entrate")
#05 FASE FINALE
os.makedirs("05_Fase Finale/01_Chiusura lavori")
os.makedirs("05_Fase Finale/02_APE post operam al SID")
