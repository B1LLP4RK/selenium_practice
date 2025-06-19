import selenium.webdriver as webdriver

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
title = driver.title
driver.quit()
