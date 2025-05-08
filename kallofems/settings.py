# Scrapy settings for kallofems project

BOT_NAME = "kallofems"
# Spider modulok
SPIDER_MODULES = ["kallofems.spiders"]
NEWSPIDER_MODULE = "kallofems.spiders"

# A spider middleware-hez és a downloader middleware-hez fontos:
ROBOTSTXT_OBEY = False

# Playwright használata a JavaScript által generált tartalomhoz
PLAYWRIGHT_ENABLED = True

# Scrapy-Playwright integráció engedélyezése
DOWNLOAD_HANDLERS = {
    "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
    "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}

# Playwright beállítások
PLAYWRIGHT_BROWSER_TYPE = "chromium"
PLAYWRIGHT_LAUNCH_OPTIONS = {
    "headless": True,
}
PLAYWRIGHT_DEFAULT_NAVIGATION_TIMEOUT = 30000  # 30 másodperc


# Kimeneti fájl formátuma és neve
FEEDS = {
    "products.json": {
        "format": "json",
        "encoding": "utf8",
        "overwrite": True,
    }
}

# Log szint (hasznos hibakereséshez)
LOG_LEVEL = "INFO"

# AsyncIO alapú Twisted reaktor (Playwright-hoz kötelező)
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"

# UTF-8 kódolás a kimeneti fájlhoz
FEED_EXPORT_ENCODING = "utf-8"
