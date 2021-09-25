import PySimpleGUI as sg

def window():
    layout = [
        [sg.Text("Excel Margenrechner", justification="center", size=(10, 2))],
        [],
        [sg.Text("Dateinamen eingeben: "), sg.InputText(key="_FILENAME_"), sg.FileBrowse()],
        [sg.Text("ProduktName: "), sg.InputText(key="_PRODUCNAME_"), sg.OK()]
    ]

    return sg.Window("Margenrechner", layout, return_keyboard_events=True, finalize=True)