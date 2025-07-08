import sys

class MockSupervisor:
    @staticmethod
    def reload():
        print("Redémarrage du programme...")
        # Dans un vrai environnement CircuitPython, cela redémarre le programme
        # Ici, on simule simplement le redémarrage
        raise SystemExit(0)

# Remplacer le module supervisor par notre mock
sys.modules['supervisor'] = MockSupervisor()
