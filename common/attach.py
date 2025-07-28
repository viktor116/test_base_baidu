import allure
from playwright.sync_api import Page


#截图结果与Allure提取
def readAttach(page: Page, paths, fileName):
    page.screenshot(path = paths + fileName + '.png')
    with open(paths + fileName + ".png", 'rb') as file:
        allure.attach(file.read(), name = fileName, attachment_type = allure.attachment_type.PNG)