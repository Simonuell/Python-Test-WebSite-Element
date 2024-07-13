# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image
import os
if os.path.exists("DevicesScreenshots") is False:
    os.mkdir("DevicesScreenshots")

List_Of_Devices =[
{
    'device': 'Apple iPhone 12 mini',
    'width': 375,
    'height': 812,
    'pixel_ratio': 3.0
},
{
    'device': 'Apple iPad Mini',
    'width': 768,
    'height': 1024,
    'pixel_ratio': 2.0
},
{
    'device': 'Apple iPhone 15',
    'width': 393,
    'height': 852,
    'pixel_ratio': 2.75
},
{
    'device': 'Honor 8X',
    'width': 360,
    'height': 780,
    'pixel_ratio': 2.75
},
{
    'device': 'Huawei P40 Pro',
    'width': 400,
    'height': 880,
    'pixel_ratio': 3
},
{
    'device': 'LG G Pad 5 10.1',
    'width': 600,
    'height': 960,
    'pixel_ratio': 2.5
},
{
    'device': 'LG G5',
    'width': 360,
    'height': 640,
    'pixel_ratio': 2
},
{
    'device': 'MacBook Pro 13.3',
    'width': 1280,
    'height': 800,
    'pixel_ratio': 2.75
}
]

for device in List_Of_Devices:
    try:
        browser = webdriver.ChromeOptions()
        browser.add_argument('--headless')
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=browser)

        driver.set_window_size(device['width'], device['height'])

        driver.get("https://undergroundcoffee.ru/")

        button = driver.find_element(By.CSS_SELECTOR, ".t-body .t-records.t-records_animated.t-records_visible .r.t-rec.t-rec_pt_75.t-rec_pt-res-480_30 .t396")
        assert button.is_displayed(), f"button is not displayed on {device['device']}!"
        driver.execute_script("return arguments[0].scrollIntoView(true);", button)
        print(button)
        screenshot_path = f"DevicesScreenshots/{device['device']}.png"
        driver.save_screenshot(screenshot_path)
    finally:
        driver.quit()

