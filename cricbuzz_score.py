from playwright.sync_api import sync_playwright

with sync_playwright() as p:
 browser = p.chromium.launch(headless=False)
 page = browser.new_page()
 page.goto("https://www.cricbuzz.com/")
 #page.wait_for_selector("bg-white px-4 pb-2") # the selector you found")
 rows = page.locator(".flex.items-center.gap-4.justify-between")

 score = rows.nth(2).inner_text()

 print(score)
 #print(score)
 page.screenshot(path="score.png")
 browser.close()