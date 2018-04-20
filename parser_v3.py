from selenium import webdriver

driver = webdriver.Chrome('chromedriver')

driver.implicitly_wait(3)

driver.get('https://nid.naver.com/nidlogin.login')

driver.find_element_by_name('id').send_keys('naver_id')
driver.find_element_by_name('pw').send_keys('naver_password')

driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

