from splinter import Browser


if __name__ == "__main__":
    browser = Browser()
    browser.visit("https://bratislava.pyladies.com")
    browser.quit()
