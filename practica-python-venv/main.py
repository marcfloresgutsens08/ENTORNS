import requests
from colorama import Fore, Style, init

# Inicialitza colorama
init()

print(Fore.CYAN + "=== Provant l'entorn virtual de Python ===" + Style.RESET_ALL)

# Petició a una API pública
response = requests.get("https://api.github.com")

if response.status_code == 200:
    print(Fore.GREEN + f"[ÈXIT] Connectat a GitHub API. Codi: {response.status_code}" + Style.RESET_ALL)
else:
    print(Fore.RED + f"[ERROR] No s'ha pogut connectar. Codi: {response.status_code}" + Style.RESET_ALL)
