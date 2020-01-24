from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import subprocess
import sys

import time

import certifi
import urllib3
http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where())


reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]


def format_url(url):
    return url.replace('.', '_').replace('https://', '').replace('/', '_')


print(format_url('https://webbutik.comviq.se/samsung-galaxy-s10.html'))
# SETTINGS


abtool = 'optimize'
landing_url = 'https://webbutik.comviq.se/samsung-galaxy-s10.html'
experimentid = 'HIwkAaZfQtKhfjINaTpiTg'
var = '1'


experimentcookie_value_to_set = 'GAX1.2.' + experimentid + '.18371.'+var
previewcookie_value_to_set = 'abpreviewcookiea'


# Test starts here
# Instruction how to write selenium tests: https://selenium-python.readthedocs.io/api.html

testname = 'T51 Hardware Priceplans'


def run_test(testname, landing_url, var, device, os_version, remote=False, ):

    if (remote == True):

        desired_cap = {
            'project': testname,
            'device': device,
            'os_version': os_version,
            'realMobile': 'true',
            'name': format_url(landing_url) + ' - ' + var,
            'browserstack.debug': 'true',
            'browserstack.console': 'errors'
        }

        driver = webdriver.Remote(
            command_executor='https://jonathankuronen1:wxhSDATwLPpk7KsxMTQF@hub-cloud.browserstack.com/wd/hub',
            desired_capabilities=desired_cap)

    if (remote == False):
        driver = webdriver.Chrome('/Users/erikohlen/C_local/chromedriver')

    driver.get(landing_url)
    driver.implicitly_wait(5)
    time.sleep(5)
    experimentcookie_value_to_set = 'GAX1.2.' + experimentid + '.18371.'+var
    driver.add_cookie(
        {'name': '_gaexp',
         'value': experimentcookie_value_to_set,
         'domain': '.comviq.se'}
    )
    driver.add_cookie(
        {'name': 'abpreviewcookiea',
         'value': 'true',
         'domain': '.comviq.se'}
    )

    driver.get(landing_url)

    scroll_down_pixels = 500
    print('scrolling down... ' + str(scroll_down_pixels) + 'px')
    driver.execute_script(
        "window.scrollTo(0, " + str(scroll_down_pixels) + ")")
    time.sleep(5)
    if (remote == False):

        """  url_to_filename = landing_url.replace(
             '.', '_').replace('https://', '').replace('/', '_') """
        print('trying to take screenshot: ' + testname +
              ' - ' + format_url(landing_url) + var + '.png')
        driver.save_screenshot(
            testname + ' - ' + format_url(landing_url) + ' - ' + var + '.png')
        """ driver.save_screenshot(
            'T51 Hardware Priceplans - webbutik_comviq_sesamsung-galaxy-s10_html1.png') """

    if (remote == True):
        driver.quit()


landing_urls = [
    'https://webbutik.comviq.se/samsung-galaxy-s10.html',
    'https://webbutik.comviq.se/apple-iphone-11.html',
    'https://webbutik.comviq.se/apple-iphone-xs.html',
]

variations = [
    # '0',
    # '1',
    '3'  # ,
    # '3'
]

devices = [
    # Small list recommended by BrowserStack
    {"os_version": "11",
     "device": "iPhone 8"},

    {"os_version": "9.0",
     "device": "Google Pixel 3"},

    {"os_version": "9.0",
     "device": "Samsung Galaxy S9 Plus"},

    {"os_version": "7.0",
     "device": "Samsung Galaxy S8"},

    {"os_version": "11",
     "device": "iPad 6th"}

]


def run_many_tests(remote):
    for variation in variations:
        for url in landing_urls:
            for item in devices:
                run_test(testname, url, variation, os_version=item['os_version'],
                         device=item['device'], remote=remote)


# run_many_tests(remote=False)


run_test(testname, 'https://webbutik.comviq.se/samsung-galaxy-s10.html',
         '2', remote=True, os_version='11', device='iPhone 8 Plus'
         )
