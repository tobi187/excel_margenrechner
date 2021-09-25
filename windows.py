import PySimpleGUI as sg


def window():
    layout = [
        [sg.Text("Excel Margenrechner", pad=(140, 0), font=("Courier", 20, "bold"))],
        [sg.Text("")],
        [sg.Text("Dateinamen eingeben: "), sg.InputText(key="_FILENAME_"), sg.FileBrowse()],
        [],
        [sg.Text("ProduktName: "), sg.InputText(key="_PRODUCTNAME_"), sg.Text("Anzahl"),
         sg.InputText(key="_AMOUNT_", size=(10, 1))],
        [sg.Text("            Fehler: Ungültige Eingabe", text_color="red", visible=False, key="_ERROR_")],
        [sg.Text("Marge: ", font=("Courier", 15, "normal")), sg.Text("0.0", key="_MARGE_"), sg.Button("Kopieren")],
        [],
        [sg.Button("Berechnen", key="_OK_", pad=(200, 0))]
    ]

    return sg.Window("Margenrechner", layout, return_keyboard_events=True, finalize=True)
