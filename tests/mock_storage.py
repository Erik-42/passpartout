class MockStorage:
    """Simule le stockage USB"""
    def __init__(self):
        self._enabled = True
        
    def disable_usb_drive(self):
        """Simule la désactivation du lecteur USB"""
        self._enabled = False
        print("Lecteur USB désactivé")
        
    def enable_usb_drive(self):
        """Simule la réactivation du lecteur USB"""
        self._enabled = True
        print("Lecteur USB réactivé")

# Remplacer le module storage par notre mock
storage = MockStorage()
