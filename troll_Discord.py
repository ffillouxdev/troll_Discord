from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time


def troll_max(link, fichier):
    # Chemin vers le pilote Chrome et le dossier de données utilisateur
    chromeDriverPath = "C:/Users/fillo/OneDrive/Documents/PERSONNEL/projet python/Projets/troll/chromedriver.exe"
    userdatadir = "C:/Users/fillo/AppData/Local/Google/Chrome/User Data"

    # Options du navigateur Chrome
    ouvrir_chrome = Options()
    ouvrir_chrome.add_argument(f"--user-data-dir={userdatadir}")
    ouvrir_chrome.add_argument("--profile-directory=Profile 2")

    # Créer un objet Service avec le chemin du pilote Chrome
    service = Service(chromeDriverPath)

    # Ouvrir une session de navigateur Chrome avec les options configurées et le service
    driver = webdriver.Chrome(options=ouvrir_chrome, service=service)
    driver.maximize_window()

    # Ouvrir le lien spécifié
    driver.get(link)

    time.sleep(2)

    # Récupérer les phrases du fichier texte
    with open(fichier, "r") as file:
        phrases = file.readlines()

    for phrase in phrases:
        # Suppression des caractères de saut de ligne
        phrase = phrase.strip()

        time.sleep(4)
        # Publier la phrase dans la discussion en appuyant sur la touche Entrée
        input_text = driver.find_element(
            By.XPATH,
            '/html/body/div[1]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[3]/div[3]/main/form/div/div/div/div[3]/div/div[2]',
        )
        input_text.send_keys(phrase)
        input_text.send_keys(Keys.RETURN)

        # Attendre un certain temps avant d'afficher la prochaine phrase
        time.sleep(2)

    # Attendre un certain temps pour permettre l'envoi du dernier message
    time.sleep(2)

    # Fermer le navigateur
    driver.quit()


# Exemple d'utilisation de la fonction troll_max avec un lien et un fichier spécifiés
link = "your_link_here"
fichier = "fic.txt"

if __name__ == "__main__":
    for i in range (0, 10): #vous pouvez changer les valeurs pour augmenter le nombre de fois que le spam sera envoyé
        troll_max(link, fichier)
