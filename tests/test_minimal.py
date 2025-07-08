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
    def __init__(self):
        self.keyboard = MockKeyboard()
        self.mouse = MockMouse()
        self.consumer_control = MockConsumerControl()
        self.menu_stack = ['main']
        self.current_menu = self.get_menu('main')
        self.current_index = 0

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
        print("=== Menu Passpartout ===")
        print(f"\nMenu: {' -> '.join(self.menu_stack)}")
        print("\nOptions:")
        for i, option in enumerate(self.current_menu):
            if i == self.current_index:
                print(f">> {i + 1}. {option}")
            else:
                print(f"   {i + 1}. {option}")

    def handle_input(self, key):
        if key == 'up':
            self.current_index = max(0, self.current_index - 1)
        elif key == 'down':
            self.current_index = min(len(self.current_menu) - 1, self.current_index + 1)
        elif key == 'enter':
            self.select_option()
        elif key == 'back':
            self.go_back()

    def select_option(self):
        selected = self.current_menu[self.current_index]
        
        if selected in self.get_menu('os'):
            self.menu_stack.append(f"{selected.lower()}_payloads")
            self.current_menu = self.get_menu(f"{selected.lower()}_payloads")
            self.current_index = 0
            return
            
        print(f"Option sélectionnée: {selected}")
        time.sleep(1)

    def go_back(self):
        if len(self.menu_stack) > 1:
            self.menu_stack.pop()
            self.current_menu = self.get_menu(self.menu_stack[-1])
            self.current_index = 0

    def run(self):
        print("=== Test interactif Passpartout ===")
        print("Commandes:")
        print("↑/↓ : Navigation dans le menu")
        print("Enter : Sélectionner une option")
        print("B : Retourner au menu précédent")
        print("Q : Quitter")
        print("\nAppuyez sur une touche pour commencer...")

        while True:
            self.show_menu()
            
            key = input("\nChoisissez une option (↑/↓/Enter/B/Q): ").lower()
            
            if key == 'q':
                print("\nAu revoir!")
                break
                
            self.handle_input(key)

def main():
    test = TestMenu()
    test.run()

if __name__ == "__main__":
    main()
