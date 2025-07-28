def click_fill(page,local,fills):
    page.locator(local).click()
    page.locator(local).fill(fills)