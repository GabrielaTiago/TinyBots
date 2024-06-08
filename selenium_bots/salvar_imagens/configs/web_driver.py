from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def config_web_driver():
    # Configurações do Chrome
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1050,700', '--disable-notifications' , '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    # Configurações experimentais
    chrome_options.add_experimental_option('prefs', {
        'download.default_directory': 'C:\\Users\gabri\\Documents\\Projects\\TinyBots\\downloads',
        'download.directory_upgrade': True,
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,
    })

    # Instanciando o serviço do Chrome
    service = ChromeService(ChromeDriverManager().install())

    # Instanciando o driver do Chrome
    driver = webdriver.Chrome(service=service, options=chrome_options)

    return driver