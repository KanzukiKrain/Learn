from selenium import webdriver

# 关闭Chrome正受到自动化软件的控制

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('useAutomationExtension',False)
chrome_options.add_experimental_option("excludeSwitches",['enable-automation'])

chrome_options.add_argument("--no-sandbox") #有时浏览器有问题需要加入 --no-sandbox

driver = webdriver.Chrome(options=chrome_options) #新版selenium参数名options


driver.get("https://www.baidu.com")
