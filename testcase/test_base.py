import allure
import pytest

from common.action import click_fill
from common.attach import readAttach
from common.read_file import read_yaml
from playwright.sync_api import Page


@allure.epic("基础数据")
@allure.title("搜索pytest")
def test_pytest(page: Page):
    # 读取yaml文件
    dbinfo = read_yaml("/data/base.yaml")
    # 打开地址
    page.goto(dbinfo["test_pytest"]["goto"])
    # 搜索框输入内容
    click_fill(page, "#kw", dbinfo["test_pytest"]["fills"])
    # 点击'百度一下'
    page.get_by_role("button", name="百度一下").click()
    # 截图结果并保存到log与allure
    readAttach(page, dbinfo["test_pytest"]["path"], dbinfo["test_pytest"]["fileName"])


@allure.epic("基础数据")
@allure.title("搜索allure")
def test_allure(page: Page):
    dbinfo = read_yaml("/data/base.yaml")
    page.goto(dbinfo["test_allure"]["goto"])
    click_fill(page, "#kw", dbinfo["test_allure"]["fills"])
    page.get_by_role("button", name="百度一下").click()
    readAttach(page, dbinfo["test_allure"]["path"], dbinfo["test_allure"]["fileName"])