#!/usr/bin/env python3

import curses
import sys
import time

class MockKeyboard:
    def __init__(self):
        self.keys_pressed = []

    def send(self, *keys):
        print(f"Appuyant sur les touches: {keys}")
        self.keys_pressed.extend(keys)

    def release_all(self):
        print("Libération de toutes les touches")
        self.keys_pressed.clear()

class MockMouse:
    def click(self, button):
        print(f"Clic sur le bouton {button}")

class MockConsumerControl:
    def send(self, code):
        codes = {
            96: "Volume down",
            97: "Volume mute",
            102: "Volume up"
        }
        print(f"Contrôle: {codes.get(code, 'Code inconnu')}")

class TestMenu:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.keyboard = MockKeyboard()
        self.mouse = MockMouse()
        self.consumer_control = MockConsumerControl()
        self.menu_stack = ['main']
        self.current_menu = self.get_menu('main')
        self.current_index = 0
        self.stdscr.keypad(True)
        curses.curs_set(0)
        self.stdscr.clear()

    def get_menu(self, menu_name):
        menus = {
            'main': [
                "Système d'exploitation",
                "Séquences de dépannage",
                "Payloads",
                "Options d'exécution",
                "Sauvegarder",
                "Exécuter"
            ],
            'os': [
                "Windows",
                "Linux",
                "MacOS",
                "Version...",
                "Paramètres régionaux..."
            ],
            'windows_payloads': [
                "HackyPi_AccessCamera.py",
                "HackyPi_CoolFake_Hacking.py",
                "HackyPi_CreateFile.py"
            ],
            'linux_payloads': [
                "linux_recovery.json"
            ],
            'mac_payloads': [
                "mac_recovery.json"
            ]
        }
        return menus.get(menu_name, [])

    def show_menu(self):
        self.stdscr.clear()
        self.stdscr.addstr(0, 0, "=== Menu Passpartout ===")
        self.stdscr.addstr(1, 0, "\nMenu: " + ' -> '.join(self.menu_stack))
        self.stdscr.addstr(2, 0, "\nOptions:")
        
        # Afficher les options avec un espacement fixe
        for i, option in enumerate(self.current_menu):
            prefix = "-> " if i == self.current_index else "   "
            try:
                self.stdscr.addstr(4 + i, 0, prefix + str(i + 1) + ". " + option[:30])
            except curses.error:
                self.stdscr.addstr(4 + i, 0, prefix + str(i + 1) + ". " + option[:30].encode('ascii', 'replace').decode())
        
        self.stdscr.addstr(10, 0, "\nCommandes:")
        self.stdscr.addstr(11, 0, "↑/↓ : Navigation")
        self.stdscr.addstr(12, 0, "Enter/Numéro : Sélection")
        self.stdscr.addstr(13, 0, "B : Retour")
        self.stdscr.addstr(14, 0, "Q : Quitter")
        self.stdscr.refresh()

    def handle_input(self, key):
        if key == curses.KEY_UP:
            self.current_index = max(0, self.current_index - 1)
        elif key == curses.KEY_DOWN:
            self.current_index = min(len(self.current_menu) - 1, self.current_index + 1)
        elif key == curses.KEY_ENTER or key in [10, 13]:  # Enter
            self.select_option()
        elif key == ord('b') or key == ord('B'):  # B ou b
            self.go_back()
        elif key == ord('q') or key == ord('Q'):  # Q ou q
            return False
        elif key >= ord('1') and key <= ord('9'):  # Numéro
            num = key - ord('0') - 1
            if 0 <= num < len(self.current_menu):
                self.current_index = num
                self.select_option()
        return True

    def select_option(self):
        selected = self.current_menu[self.current_index]
        
        if selected in ['Windows', 'Linux', 'MacOS']:
            self.menu_stack.append(f"{selected.lower()}_payloads")
            self.current_menu = self.get_menu(f"{selected.lower()}_payloads")
            self.current_index = 0
            return
            
        self.stdscr.addstr(16, 0, f"\nOption sélectionnée: {selected}")
        self.stdscr.refresh()
        time.sleep(1)

    def go_back(self):
        if len(self.menu_stack) > 1:
            self.menu_stack.pop()
            self.current_menu = self.get_menu(self.menu_stack[-1])
            self.current_index = 0

    def run(self):
        while True:
            self.show_menu()
            key = self.stdscr.getch()
            if not self.handle_input(key):
                break

def main(stdscr):
    test = TestMenu(stdscr)
    test.run()

if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        print("\nAu revoir!")
    except Exception as e:
        print(f"\nUne erreur est survenue : {str(e)}")
