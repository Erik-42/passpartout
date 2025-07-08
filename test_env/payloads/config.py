# Configuration des payloads

# Payloads par défaut
DEFAULT_PAYLOADS = {
    'windows': {
        'recovery': {
            'name': 'Windows Recovery',
            'actions': [
                {'type': 'key', 'keys': ['windows', 'r']},
                {'type': 'write', 'text': 'shutdown /r /o /t 0'},
                {'type': 'key', 'keys': ['enter']}
            ]
        },
        'task_manager': {
            'name': 'Task Manager',
            'actions': [
                {'type': 'key', 'keys': ['windows', 'shift', 'esc']}
            ]
        }
    },
    'linux': {
        'terminal': {
            'name': 'Terminal',
            'actions': [
                {'type': 'key', 'keys': ['ctrl', 'alt', 't']}
            ]
        },
        'update': {
            'name': 'System Update',
            'actions': [
                {'type': 'write', 'text': 'sudo apt update && sudo apt upgrade -y'},
                {'type': 'key', 'keys': ['enter']}
            ]
        }
    },
    'macos': {
        'force_quit': {
            'name': 'Force Quit',
            'actions': [
                {'type': 'key', 'keys': ['command', 'option', 'esc']}
            ]
        },
        'reboot': {
            'name': 'Reboot',
            'actions': [
                {'type': 'key', 'keys': ['command', 'control', 'alt', 'power']}
            ]
        }
    }
}

# Configuration pour le payload auto-exécuté
AUTO_EXECUTE = {
    'enabled': False,
    'payload': None,
    'os': None
}

# Sauvegarde de la configuration
def save_config():
    import json
    with open('payloads/config.json', 'w') as f:
        json.dump({
            'auto_execute': AUTO_EXECUTE
        }, f)

# Chargement de la configuration
def load_config():
    import json
    try:
        with open('payloads/config.json', 'r') as f:
            config = json.load(f)
            AUTO_EXECUTE.update(config.get('auto_execute', {}))
    except:
        pass
