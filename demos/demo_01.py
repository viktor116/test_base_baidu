import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://fat-home.z9soft.cn/login?redirect=/purchase/purchasemgt/purchaseorder")
    page.get_by_role("textbox", name="请输入账号/手机号").click()
    page.get_by_role("textbox", name="请输入账号/手机号").click()
    page.get_by_role("textbox", name="请输入账号/手机号").fill("18565764872")
    page.get_by_role("textbox", name="请输入登录密码").click()
    page.get_by_role("textbox", name="请输入登录密码").fill("Aqfbui1iq123%")
    page.get_by_role("button", name="登 录").click()
    page.get_by_text("草稿").click()
    with page.expect_popup() as page1_info:
        page.locator("div").filter(has_text=re.compile(r"^13:3901:39 工作台 企业服务项目服务产品服务账号店铺服务目标计划供应商服务采购服务质量服务仓储服务$")).get_by_role("img").click()
    page1 = page1_info.value
    page1.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
