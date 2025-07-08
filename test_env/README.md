# Environnement de test Passpartout

## Structure du projet
```
test_env/
├── src/
│   ├── main.py          # Code principal
│   ├── menu.py         # Interface menu
│   ├── mock_supervisor.py  # Mock pour le module supervisor
│   └── payloads/       # Gestionnaire de payloads
├── payloads/
│   ├── config.py      # Configuration des payloads
│   └── test_payloads.json  # Payloads de test
└── test_circuit.py    # Script de test
```

## Fonctionnalités implémentées

1. **Détection du système**
   - Détection automatique du système d'exploitation
   - Affichage des informations système
   - Configuration des paramètres système

2. **Gestion des payloads**
   - Sélection de payloads par système
   - Configuration de l'auto-exécution
   - Sauvegarde des configurations

3. **Interface utilisateur**
   - Menu interactif avec sélection par numéro
   - Indicateurs LED pour le statut
   - Bouton pour accéder au menu

## À faire demain

1. Finaliser les mocks CircuitPython
2. Implémenter la détection du système
3. Ajouter plus de payloads de test
4. Améliorer l'interface utilisateur
5. Ajouter des tests unitaires
