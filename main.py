import PySimpleGUI as sg
from openpyxl import load_workbook
from windows import window


def main():
    win1 = window()
    while True:
        ev1, vals1 = win1.read()
        if ev1 == sg.WIN_CLOSED:
            win1.close()
            break
        if


if __name__ == '__main__':
    main()
