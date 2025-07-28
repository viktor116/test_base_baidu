import allure
from common.attach import readAttach
from playwright.sync_api import Page


@allure.epic("采购模块")
@allure.title("搜索playwright")
def test_playwright(page: Page):
    page.goto("https://www.baidu.com/")
    page.locator("#kw").click()
    page.locator("#kw").fill("playwright")
    page.get_by_role("button", name="百度一下").click()
    readAttach(page, "./log/screenshot/", "test_playwright")