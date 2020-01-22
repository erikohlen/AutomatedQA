from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import subprocess
import sys

import certifi
import urllib3
http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where())


reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]


desired_cap = {
    'browserName': 'iPhone',
    'device': 'iPhone 8 Plus',
    'realMobile': 'true',
    'os_version': '11',
    'name': 'Bstack-[Python] Sample Test'
}

driver = webdriver.Remote(
    command_executor='https://jonathankuronen1:wxhSDATwLPpk7KsxMTQF@hub-cloud.browserstack.com/wd/hub',
    desired_capabilities=desired_cap)

driver = webdriver.Chrome(
    '/Users/erikohlen/C_local/chromedriver')


# Test starts here
# Instruction how to write selenium tests: https://selenium-python.readthedocs.io/api.html

# driver.get("https://comviq5.comviq.pp.ciklum.com/")
driver.get("https://www.comviq.se")
# if not "Google" in driver.title:
#    raise Exception("Unable to load google page!")

#elem = driver.find_element_by_tag_name('body')

driver.add_cookie({"_gaexp": "GAX1.2.Fa6s-00FTIS_gAg5MxoMqg.18371.1"})

driver.get("https://www.comviq.se")

#elem = driver.find_element_by_name("q")
# elem.send_keys("BrowserStack")
# elem.submit()
print(driver.title)
# driver.quit()
