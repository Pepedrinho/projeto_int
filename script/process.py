
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.ie.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select 


class Processo:
    def __init__(self, url_sistema, usuario, senha, emp=None, estado_sistema=None, data=None, headless = False, codigo=None):
        self.url = url_sistema
        self.usuario = usuario
        self.secret = codigo
        self.ultimo_codigo = None
        self.senha = senha
        self.emp = emp
        self.uf = estado_sistema
        self.data = data
        self.processos = []

        self.download_path = join(os.getcwd(), 'rpa_pje','arquivos', self.emp, self.data, self.uf)
        os.makedirs(self.download_path, exist_ok=True)

        self.user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
        
        #-------------------------------------------
        # self.options = uc.ChromeOptions() #undetected-chromedriver
        # self.options.add_argument("--no-sandbox")
        # self.options.add_argument("--disable-dev-shm-usage")
        # self.options.add_argument("--disable-blink-features=AutomationControlled")
        #self.options.add_argument("--headless=new")   # se quiser headless
        #------------------------------------------------------------
        self.options = Options()
        self.options.add_argument("--start-maximized")  
        self.options.add_argument("--disable-popup-blocking")
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--disable-blink-features")
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        self.options.add_argument("--disable-infobars")
        self.options.add_argument("--kiosk-printing")
        self.options.add_argument("--no-sandbox")
        #self.options.add_argument("--headless=new")   # modo headless
        self.options.add_argument("--disable-dev-shm-usage")
        #self.options.add_argument("--headless=new")
        if self.url.startswith("https://pje1g.tjrn.jus.br"):
            self.options.add_argument(f'user-agent={self.user_agent}')
        prefs = {
            "download.default_directory": self.download_path,
            "download.prompt_for_download": False,  
            "download.directory_upgrade": True,
            "plugins.always_open_pdf_externally": True,
            "safebrowsing.enabled": True
        }
        self.options.add_experimental_option("prefs", prefs)
    
        self.service = Service(executable_path='/opt/drivers/chromedriver')
        #self.service = Service("/usr/bin/chromedriver") #DOCKERFILE

        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        #self.driver = uc.Chrome(options=self.options)  #undetected-chromedriver

        self.wait = WebDriverWait(self.driver, 10)        
        self.actions = ActionChains(self.driver)
        self.keys = Keys()
        self.driver.maximize_window()
        #Acessa a URL
        self.driver.get(self.url) 

        self.solver = TwoCaptcha('8db3590b458b4ee53d6c9f209e16d4c2')
   
        # self.oracle_db = ClassOracle.Oracle()
        self.s3ibm = ClassS3IBM.S3()
    
    # def to_base64(self, path):
    #     with open(path, "rb") as f:
    #         return base64.b64encode(f.read()).decode("utf-8")