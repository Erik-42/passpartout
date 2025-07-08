from typing import Dict, List, Any
import json
import os

class PayloadManager:
    """Gestionnaire des payloads pour Passpartout"""
    
    def __init__(self, payloads_dir: str = "payloads"):
        """Initialise le gestionnaire de payloads"""
        self.payloads_dir = payloads_dir
        self.payloads: Dict[str, Dict[str, Any]] = {}
        self.payloads_by_os: Dict[str, List[Dict[str, Any]]] = {
            'Windows': [],
            'Linux': [],
            'MacOS': []
        }
        self.load_payloads()
    
    def load_payloads(self):
        """Charge tous les payloads disponibles"""
        try:
            # Charger les payloads par système d'exploitation
            for os_dir in ['windows', 'linux', 'mac']:
                os_path = os.path.join(self.payloads_dir, os_dir)
                if os.path.exists(os_path):
                    # Charger les fichiers JSON dans le dossier
                    for filename in os.listdir(os_path):
                        if filename.endswith('.json'):
                            payload_id = filename[:-5]  # Retirer l'extension .json
                            with open(os.path.join(os_path, filename), 'r') as f:
                                payload_data = json.load(f)
                                payload_data['os'] = os_dir.title()
                                self.payloads[payload_id] = payload_data
                                self.payloads_by_os[os_dir.title()].append(payload_data)
                    
                    # Charger les payloads Python si présents
                    for filename in os.listdir(os_path):
                        if filename.endswith('.py'):
                            payload_id = filename[:-3]  # Retirer l'extension .py
                            # Créer un payload minimal pour les fichiers Python
                            self.payloads[payload_id] = {
                                'id': payload_id,
                                'name': filename,
                                'description': f"Script Python pour {os_dir.title()}",
                                'os': os_dir.title(),
                                'type': 'python'
                            }
                            self.payloads_by_os[os_dir.title()].append(self.payloads[payload_id])
        except Exception as e:
            print(f"Erreur lors du chargement des payloads: {str(e)}")
    
    def get_payloads(self) -> List[Dict[str, Any]]:
        """Retourne la liste de tous les payloads disponibles"""
        return list(self.payloads.values())
    
    def get_payloads_by_os(self, os_name: str) -> List[Dict[str, Any]]:
        """Retourne les payloads pour un système d'exploitation spécifique"""
        return self.payloads_by_os.get(os_name, [])
    
    def get_payload(self, payload_id: str) -> Dict[str, Any]:
        """Retourne un payload spécifique"""
        return self.payloads.get(payload_id, None)
    
    def execute_payload(self, payload_id: str, keyboard, mouse, consumer_control):
        """Exécute un payload spécifique"""
        payload = self.get_payload(payload_id)
        if not payload:
            print(f"Payload {payload_id} non trouvé")
            return False
            
        print(f"\n=== Exécution du payload: {payload['name']} ===")
        print(f"Description: {payload['description']}")
        print(f"Système d'exploitation: {payload['os']}")
        
        try:
            if payload.get('type') == 'python':
                # Pour les scripts Python, exécuter le fichier
                script_path = os.path.join(
                    self.payloads_dir,
                    payload['os'].lower(),
                    f"{payload_id}.py"
                )
                if os.path.exists(script_path):
                    print("\nExécution du script Python...")
                    exec(open(script_path).read())
                else:
                    print(f"Erreur: Le script {script_path} n'existe pas")
                    return False
            else:
                # Pour les payloads JSON, exécuter les actions
                for action in payload['actions']:
                    action_type = action['type'].lower()
                    
                    if action_type == 'delay':
                        print(f"\nAttente de {action['duration']} secondes")
                        time.sleep(action['duration'])
                        
                    elif action_type == 'press':
                        print(f"\nAppui sur touches: {action['keys']}")
                        keyboard.send(*action['keys'])
                        
                    elif action_type == 'write':
                        print(f"\nÉcriture: {action['text']}")
                        keyboard.write(action['text'])
                        
                    elif action_type == 'click':
                        print(f"\nClic de la souris: {action['button']}")
                        mouse.click(action['button'])
                        
                    elif action_type == 'volume':
                        print(f"\nContrôle du volume: {action['action']}")
                        if action['action'] == 'increase':
                            consumer_control.send(102)
                        elif action['action'] == 'decrease':
                            consumer_control.send(96)
                        elif action['action'] == 'mute':
                            consumer_control.send(97)
                        
                    time.sleep(0.5)  # Pause entre les actions
            
            print("\n=== Payload exécuté avec succès ===")
            return True
            
        except Exception as e:
            print(f"Erreur lors de l'exécution du payload: {str(e)}")
            return False

def load_payloads():
    """Charge et retourne le gestionnaire de payloads"""
    return PayloadManager()
