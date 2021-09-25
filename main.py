import PySimpleGUI as sg
from calc import calc_marge
from windows import window


def main():
    win1 = window()
    while True:
        ev1, vals1 = win1.read()
        if ev1 == sg.WIN_CLOSED:
            win1.close()
            break
        if ev1 == "_OK_":
            if vals1["_FILENAME_"] == "" or vals1["_PRODUCTNAME_"] == "" or int(vals1["_AMOUNT_"] < 0):
                vals1["_ERROR_"].update(visible=True)
                continue
            vals1["_ERROR_"].update(visible=False)
            marge = calc_marge(vals1["_FILENAME_"], vals1["_PRODUCTNAME_"], int(vals1["_AMOUNT_"]))
            vals1["_MARGE_"].update(marge)
        if ev1 == "Kopieren":
            sg.clipboard_set(vals1["_MARGE_"])


if __name__ == '__main__':
    main()
