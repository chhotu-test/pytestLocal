# from playwright.sync_api import sync_playwright

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False, slow_mo=500, args=["--start-maximized"])
#     context = browser.new_context(no_viewport=True)
#     page = context.new_page()
#     page.goto(Config.URL, wait_until="domcontentloaded", timeout=60000)
#     page.wait_for_timeout(5000)
#     page.screenshot(path="screenshots/preprod_login.png", full_page=True)
#     print("PAGE URL:", page.url)
#     print("PAGE TITLE:", page.title())
#     inputs = page.query_selector_all("input")
#     for i in inputs:
#         print("INPUT:", i.get_attribute("type"), i.get_attribute("id"), i.get_attribute("name"), i.get_attribute("placeholder"))
#     buttons = page.query_selector_all("button")
#     for b in buttons:
#         print("BUTTON:", b.text_content().strip(), b.get_attribute("type"), b.get_attribute("class"))
#     forms = page.query_selector_all("form")
#     for f in forms:
#         print("FORM:", f.get_attribute("id"), f.get_attribute("class"))
#     print("BODY HTML (first 3000 chars):")
#     print(page.inner_html("body")[:3000])
#     page.wait_for_timeout(3000)
#     browser.close()
