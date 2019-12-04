#交互动作（将动作附加到动作链中串行执行）模拟将一个模块拖拽至另一个区域等
from selenium import webdriver
from selenium.webdriver import ActionChains     #ActionChains

browser = webdriver.Chrome()
url = "https://www.runoob.com/try/try.php?filename=jqueryul-api-droppable"
browser.get(url)
browser.switch_to.frame('iframeResult')
source = browser.find_element_by_css_selector('#draggable')  #获取原始位置
target = browser.find_element_by_css_selector('#droppable')  #获取目标位置
actions = ActionChains(browser)                              #声明动作链操作
actions.drag_and_drop(source.target)
actions.perform()                                            #执行操作