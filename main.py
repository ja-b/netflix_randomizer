import random
from selenium import webdriver

def login(driver):
    driver.get("http://www.netflix.com/Login")
    driver.find_element_by_id('email').send_keys("")
    driver.find_element_by_id('password').send_keys("")
    driver.find_element_by_id('login-form-contBtn').click()
    driver.find_element_by_xpath('//li[@class="profile"][1]/a[1]/div[1]').click()

def set_drm_plugin_on(driver):

    #driver.get("chrome://plugins")
    #driver.find_element_by_id("libwidevinecdmadapter.so-always-allowed").click()
    driver.get("chrome://components")
    driver.find_element_by_id("oimompecagnajdejgnnjijobebaeigek").click()
    import time; time.sleep(10)

def go_to_browse(driver):

    driver.get("http://www.netflix.com/Browse")

def select_random_from_screen(driver):

    import time; time.sleep(10)
    rows = driver.find_element_by_xpath('//div[@class="lolomo"]').find_elements_by_xpath('./div')
    shows_on_row = random.choice(rows).find_element_by_xpath('./div[1]/div[1]/div[1]/div[1]/div[1]/div[1]').find_elements_by_xpath('./div')
    not_selected = True; parsed_id = ''
    while not_selected:
        selected_show_id = random.choice(shows_on_row).get_attribute('data-reactid')
        if "$title_" in selected_show_id:
            parsed_id = selected_show_id.split("$title_")[1].split('_')[0]
            not_selected = False
    driver.get('http://www.netflix.com/title/{}'.format(parsed_id))
    driver.find_element_by_xpath('//div[@class="playRing"]').click()

if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_extension("chrome_cast.crx")
    options.add_experimental_option("excludeSwitches", ["disable-component-update"])
    #options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(chrome_options=options)
    driver.maximize_window()
    driver.implicitly_wait(time_to_wait=25)
    set_drm_plugin_on(driver=driver)
    login(driver=driver)
    while True:
        go_to_browse(driver=driver)
        select_random_from_screen(driver=driver)
        import time; time.sleep(60 * 1)
