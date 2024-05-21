from time import sleep
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)
    page = browser.new_page(locale="pt-br")
    page.goto("https://wol.jw.org")

    # Access Menu Today
    page.locator('#menuToday').click()
    page.locator('h2[data-pid="2"] strong').click()

    # Get Content
    text_day = page.locator('#article').text_content().strip()
    sleep(5)

    # Access ChatGPT
    page.goto('https://chatgpt.com')
    page.fill('#prompt-textarea',
              text_day + '- o que posso aprender com esse texto? Quais pontos posso tirar de proveito?')
    sleep(5)
    page.keyboard.press("Enter")
    sleep(30)

    print(page.locator('.markdown').text_content())
