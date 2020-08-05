from selenium import webdriver


driver = webdriver.Chrome()
driver.get('https://www.google.com/')

#that string is the xpath
driver.implicitly_wait(10)
print('finding serachbox');
#searchbox = driver.find_element_by_xpath('//*[@id="search"]')
searchbox = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
#searchbox = driver.find_element_by_id('search')
print('found...waitiong')
driver.implicitly_wait(3)
print(searchbox)
print('sendimng keys..')
searchbox.send_keys('cricket highlights')
print('keys sent')
print('getting search button')
#searchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
searchButton = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
print('clicking search....')
searchButton.click()
