import platform
import os
import sys
import locale
import subprocess


class OSDetector:
    def __init__(self):
        self.os_info = self.detect_os()
        self.system_info = self.get_system_info()

    def detect_os(self):
        """Détection du système d'exploitation"""
        os_info = {
            'name': platform.system(),
            'version': platform.version(),
            'release': platform.release(),
            'machine': platform.machine(),
            'processor': platform.processor()
        }
        
        # Détection spécifique pour Windows
        if os_info['name'] == 'Windows':
            os_info['edition'] = self.get_windows_edition()
            os_info['build'] = self.get_windows_build()
            os_info['language'] = self.get_windows_language()
            os_info['architecture'] = self.get_windows_architecture()
            
        # Détection spécifique pour Linux
        elif os_info['name'] == 'Linux':
            os_info['distribution'] = self.get_linux_distribution()
            os_info['kernel'] = self.get_linux_kernel()
            os_info['language'] = self.get_linux_language()
            os_info['architecture'] = self.get_linux_architecture()
            
        # Détection spécifique pour MacOS
        elif os_info['name'] == 'Darwin':  # Darwin est le nom interne de MacOS
            os_info['name'] = 'MacOS'
            os_info['version'] = self.get_macos_version()
            os_info['language'] = self.get_macos_language()
            os_info['architecture'] = self.get_macos_architecture()
            
        return os_info

    def get_system_info(self):
        """Récupération des informations système"""
        return {
            'username': os.getlogin(),
            'hostname': platform.node(),
            'locale': locale.getlocale()[0],
            'timezone': time.tzname[0],
            'encoding': sys.getdefaultencoding()
        }

    # Windows-specific methods
    def get_windows_edition(self):
        try:
            cmd = 'wmic os get Caption /value'
            result = subprocess.check_output(cmd, shell=True).decode()
            return result.split('=')[1].strip()
        except:
            return 'Unknown Edition'

    def get_windows_build(self):
        try:
            cmd = 'wmic os get BuildNumber /value'
            result = subprocess.check_output(cmd, shell=True).decode()
            return result.split('=')[1].strip()
        except:
            return 'Unknown Build'

    def get_windows_language(self):
        try:
            cmd = 'wmic os get MUILanguages /value'
            result = subprocess.check_output(cmd, shell=True).decode()
            return result.split('=')[1].strip()
        except:
            return 'Unknown Language'

    def get_windows_architecture(self):
        return platform.architecture()[0]

    # Linux-specific methods
    def get_linux_distribution(self):
        try:
            with open('/etc/os-release', 'r') as f:
                for line in f:
                    if line.startswith('PRETTY_NAME='):
                        return line.split('=')[1].strip().strip('"')
            return 'Unknown Distribution'
        except:
            return 'Unknown Distribution'

    def get_linux_kernel(self):
        return platform.uname().release

    def get_linux_language(self):
        try:
            return locale.getdefaultlocale()[0]
        except:
            return 'Unknown Language'

    def get_linux_architecture(self):
        return platform.machine()

    # MacOS-specific methods
    def get_macos_version(self):
        try:
            cmd = 'sw_vers'
            result = subprocess.check_output(cmd, shell=True).decode()
            return result.strip()
        except:
            return 'Unknown Version'

    def get_macos_language(self):
        try:
            cmd = 'defaults read NSGlobalDomain AppleLanguages'
            result = subprocess.check_output(cmd, shell=True).decode()
            return result.strip()[1:-1]  # Remove brackets
        except:
            return 'Unknown Language'

    def get_macos_architecture(self):
        try:
            cmd = 'uname -m'
            result = subprocess.check_output(cmd, shell=True).decode()
            return result.strip()
        except:
            return 'Unknown Architecture'

    def get_os_parameters(self):
        """Retourne tous les paramètres du système"""
        return {
            'os_info': self.os_info,
            'system_info': self.system_info
        }

    def get_compatible_payloads(self, payloads):
        """Retourne les payloads compatibles avec le système détecté"""
        compatible_payloads = []
        
        # Filtrer les payloads selon le système d'exploitation
        for payload in payloads:
            if 'os' in payload:
                if payload['os'] == self.os_info['name']:
                    compatible_payloads.append(payload)
            elif 'os_version' in payload:
                if payload['os_version'] == self.os_info['version']:
                    compatible_payloads.append(payload)
            elif 'os_distribution' in payload:
                if payload['os_distribution'] == self.system_info['distribution']:
                    compatible_payloads.append(payload)
        
        return compatible_payloads
