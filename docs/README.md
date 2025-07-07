# Passpartout

Clé USB d'accès et de dépannage d'urgence pour systèmes bloqués

## Description

Passpartout est un outil de dépannage et d'accès d'urgence qui transforme votre Raspberry Pi Pico en une clé USB capable de prendre le contrôle de n'importe quel ordinateur Windows/Linux. Conçu pour les situations d'urgence où l'accès normal au système est impossible, Passpartout permet d'exécuter automatiquement des séquences de commandes pour :

- Débloquer des systèmes bloqués
- Accéder aux modes de récupération
- Exécuter des commandes de dépannage
- Contourner des blocages d'accès

Ce projet utilise la bibliothèque Adafruit HID pour communiquer avec votre ordinateur via USB.

## Fonctionnalités

- Simulation de touches clavier
- Simulation de clics de souris
- Contrôle du volume
- Support de plusieurs layouts clavier (US, CRO, UK)
- Gestion des combinaisons de touches
- Support des commandes de défilement
- Détecteur de bouton intégré

## Installation

1. Préparez votre Raspberry Pi Pico
   - Téléchargez CircuitPython depuis https://circuitpython.org/downloads
   - Copiez le fichier .uf2 sur votre Raspberry Pi Pico

2. Configuration du système
   - Mettez votre Raspberry Pi Pico en mode CIRCUITPY
   - Copiez tous les fichiers du projet sur le périphérique CIRCUITPY
   - Assurez-vous que les bibliothèques Adafruit HID sont installées

3. Configuration des bibliothèques
   - Téléchargez la bibliothèque Adafruit HID depuis la CircuitPython Library Bundle
   - Copiez les fichiers nécessaires dans le dossier lib/
   - Les fichiers requis sont :
     - adafruit_hid
     - adafruit_keyboard
     - adafruit_keyboard_layout_us

## Utilisation

## Mode d'emploi en situation d'urgence

1. Insérez la clé USB dans le port USB de l'ordinateur bloqué
2. Le système détecte automatiquement la clé et affiche le menu de configuration
3. Utilisez les touches directionnelles pour naviguer dans le menu
4. Sélectionnez les options appropriées pour votre système
5. Confirmez l'exécution des séquences de dépannage

## Menu de configuration

Le menu de configuration permet de :

1. Identifier le système cible

   - Sélectionner le système d'exploitation (Windows/Linux/Mac)
   - Spécifier la version du système
   - Configurer les paramètres régionaux

2. Personnaliser les séquences de dépannage

   - Choisir les commandes à exécuter
   - Définir l'ordre des opérations
   - Ajuster les délais entre les actions

3. Configurer les options d'exécution

   - Activer/désactiver les messages de confirmation
   - Définir les combinaisons de touches spécifiques
   - Configurer les actions de déblocage

4. Sauvegarder les paramètres
   - Enregistrer la configuration pour les futures utilisations
   - Créer des profils de dépannage personnalisés
   - Exporter/importer les configurations

Le menu est accessible via les touches directionnelles et la touche Entrée pour la sélection.

## Fonctionnalités avancées

- Exécution automatique de séquences de dépannage
- Support de multiples scénarios de dépannage
- Gestion des modes de récupération Windows/Linux
- Support des commandes de déblocage spécifiques
- Interface USB HID complètement silencieuse

- DELAY : Pause en secondes
- PRESS : Appuyer sur des touches
- WRITE : Écrire du texte
- HOLD : Maintenir des touches
- RELEASE : Relâcher toutes les touches
- MOVE : Déplacer la souris
- SCROLL : Défiler la page
- CLICK : Cliquer avec la souris
- VOLUME : Contrôler le volume

## Configuration des scénarios de dépannage

- Le fichier `layout.txt` définit le layout clavier à utiliser
- Le fichier `settings.toml` configure les paramètres de dépannage
- Les fichiers d'exemple (`example-1.txt`) montrent des scénarios de dépannage courants
- Les séquences de commandes peuvent être personnalisées selon le système cible

## Structure du projet

- `code.py` : Programme principal
- `boot.py` : Script de démarrage
- `layout.txt` : Configuration du layout clavier
- `lib/` : Bibliothèques nécessaires
- `example-1.txt` : Exemple de configuration

## Dépendances

- Adafruit CircuitPython
- Adafruit HID Library
- Python Standard Library

## Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

## Tests et validation

Pour tester le système et ses fonctionnalités :

1. Test simplifié (recommandé avant la mise sur clé)
   - Exécutez le test simplifié
   ```bash
   cd /chemin/vers/le/projet
   python3 test_menu.py
   ```
   - Ce test ne nécessite aucune installation
   - Vérifiez la navigation dans le menu
   - Testez les commandes de base (DELAY, PRESS, WRITE)
   - Vérifiez les séquences de déblocage

2. Test avec VMware (pour tests réels)
   - Créez une nouvelle machine virtuelle dans VMware
   - Configurez les paramètres :
     - Mémoire : 2Go minimum
     - Disque dur : 20Go minimum
     - Processeurs : 2 cores minimum
     - USB 2.0 (la clé RP2040 est compatible USB 2.0)
   - Préparer la clé USB RP2040 :
     - Assurez-vous que votre clé USB RP2040 est bien formatée
     - Copiez tous les fichiers du projet sur le dossier CIRCUITPY de la clé
     - Vérifiez que le dossier `lib/` contient toutes les bibliothèques Adafruit HID
     - Assurez-vous que `code.py` est présent à la racine
   - Dans VMware :
     - Allez dans Paramètres > USB
     - Activez "Connecter automatiquement ce périphérique USB au démarrage"
     - Connectez votre clé USB RP2040
     - Redémarrez la machine virtuelle
   - La clé USB sera détectée au démarrage et vous pourrez tester toutes les fonctionnalités
   - Note : La clé USB RP2040 est un microcontrôleur avec 4Mo de mémoire Flash, assurez-vous de ne pas dépasser cette capacité

3. Test avancé (optionnel)
   - Exécutez le test avancé
   ```bash
   cd /chemin/vers/le/projet
   python3 test_virtual.py
   ```
   - Ce test simule l'environnement CircuitPython complet
   - Vérifiez toutes les fonctionnalités HID
   - Testez l'intégration avec Adafruit HID
   - Vérifiez la gestion des entrées/sorties

2. Test sur clé USB
   - Préparez votre environnement
   - Assurez-vous que votre Raspberry Pi Pico est en mode CIRCUITPY
   - Les fichiers du projet doivent être copiés sur CIRCUITPY
   - Les bibliothèques Adafruit doivent être installées dans le dossier lib/

2. Exécution des tests
   - Branchez votre Raspberry Pi Pico à l'ordinateur
   - Le menu de configuration s'affichera automatiquement
   - Utilisez les touches directionnelles pour naviguer
   - Testez les différentes commandes et séquences

3. Tests spécifiques
   - Vérifiez que le menu s'affiche correctement
   - Testez la navigation entre les différents menus
   - Vérifiez les combinaisons de touches
   - Testez les délais de réponse
   - Vérifiez la détection automatique du système

## Installation des bibliothèques

Pour installer les bibliothèques nécessaires :

1. Exécutez le script d'installation
```bash
python3 install_libs.py
```

2. Les bibliothèques requises seront automatiquement téléchargées et installées
3. Les fichiers seront copiés dans le dossier lib/

Note : Assurez-vous d'avoir Internet pour télécharger le bundle Adafruit.

## Sécurité et responsabilité

Ce projet est destiné uniquement à des fins de dépannage et d'accès d'urgence légitimes. Son utilisation doit se faire dans le respect des politiques de sécurité et des lois applicables. Les développeurs ne sont pas responsables de l'utilisation abusive de cet outil.

## Crédits

Ce projet utilise la bibliothèque HID d'Adafruit et est conçu pour être un outil de dépannage professionnel.

## Contact

<div align="center">
Pour toute question ou suggestion, n'hésitez pas à ouvrir une issue sur le dépôt GitHub.
<br/>
<br/>

[![GitHub followers][github followers-shield]][github followers-url]
[![Stargazers][stars-shield]][stars-url]
[![GitHub repo][github repo-shield]][github repo-url]
[![wakatime][wakatime-shield]][wakatime-url]

[![Github Badge][github badge-shield]][github badge-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<a href = 'https://basillecorp.dev'> <img width = '32px' align= 'center' src="https://raw.githubusercontent.com/rahulbanerjee26/githubAboutMeGenerator/main/icons/portfolio.png"/> basillecorp.dev</a>

Portfolio:<br/>
https://bash-cv.vercel.app/

Mon CV:
<br/>
[version Figma](https://www.figma.com/design/H17d3Plq2fxppmKcQXfB0p/Cv-Eric-Breteau?m=auto&t=enkiu3089axN0tBm-1)<br/>
[version PDF](assets/Cv-Erik_Mesen.pdf)

[https://buymeacoffee.com/meseneriko](https://buymeacoffee.com/meseneriko)

<a href="https://buymeacoffee.com/meseneriko">
    <img src="./assets/img/bmc_qr.png" alt="Buy My Coffee" width="100" style="background-color:grey">
</a>

Contactez moi: [erik.mesen@basillecorp.dev](mailto:erik.mesen@basillecorp.dev)

[<img src="./assets/img/logo-Erik-42-souris-v1.jpg" alt="logo Erik-42" width="75">](https://bash-cv.vercel.app/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[wakatime-shield]: https://wakatime.com/badge/user/f84d00d8-fee3-4ca3-803d-3daa3c7053a5.svg
[wakatime-url]: https://wakatime.com/@f84d00d8-fee3-4ca3-803d-3daa3c7053a5
[github badge-shield]: https://img.shields.io/badge/Github-Erik--42-155?style=for-the-badge&logo=github
[github badge-url]: https://github.com/Erik-42
[github repo-shield]: https://img.shields.io/badge/Repositories-68-blue
[github repo-url]: https://github.com/Erik-42/Erik-42?tab=repositories
[github followers-shield]: https://img.shields.io/github/followers/Erik-42
[github followers-url]: https://github.com/followers/Erik-42
[contributors-shield]: https://img.shields.io/github/contributors/Erik-42/export-project-structure
[contributors-url]: https://github.com/Erik-42/export-project-structure/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Erik-42/export-file-structure
[forks-url]: https://github.com/Erik-42/export-file-structure/forks
[issues-shield]: https://img.shields.io/github/issues-raw/Erik-42/export-file-structure
[issues-url]: https://github.com/Erik-42/export-file-structure/issues
[stars-shield]: https://img.shields.io/github/stars/Erik-42
[stars-url]: https://github.com/Erik-42?tab=stars
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/erik-mesen/
[html-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[html-url]: https://html.spec.whatwg.org/
[css-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[css-url]: https://www.w3.org/TR/CSS/#css
[javascript-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555

[logo-Erik-42-souris-v1.jpg]: ./assets/img/logo-Erik-42-souris-v1.jpg
