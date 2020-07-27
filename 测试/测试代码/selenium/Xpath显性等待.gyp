# 导入封装的driver初始化参数
from init_driver.Init_driver import init_driver
# 导入显性等待的包
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import time
#from selenium.webdriver.common.by import By  (locator = (By.ID,"kw"))

driver = init_driver()

try:
    #隐性等待,在webdrive包里
    driver.implicity_wait(30)
    # 定位单个元素
    driver.find_element_by_id("com.android.settings:id/search").click()
    time.sleep(10)
    driver.find_element_by_class_name("android.widget.ImageButton").click()
    time.sleep(5)

    # 定位一组元素
    ele_list_id = driver.find_elements_by_id("android:id/title")
    ele_list_cl = driver.find_elements_by_class_name("android.widget.TextView")

    # 使用xpath定位
    xpath_val = "//*[contains(@class, 'android.widget.TextView')]"
    xpath_list = driver.find_elements_by_xpath(xpath_val)
    for i in xpath_list:
        if "个人" in i.text:
            i.click()
            break

    # 当前时间
    print(time.strftime("%H:%M:%S", time.localtime()))
    # 显性等待 WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(locator)),要导入包
    #WebDriverWait(driver, 超时时长, 调用频率, 忽略异常).until(可执行方法, 超时时返回的信息)
    #可执行方法，不是find_element，要有参数，可用expected_conditions(from selenium.webdriver.support import expected_conditions as EC)或者is_displayed(),is_enabled(),is_selected()
    ele_list = WebDriverWait(driver, timeout=5, poll_frequency=0.5).until(lambda x: x.find_element_by_xpath("//*[contains(@text, 'WLAN')]"))
    ele_list.click()
    time.sleep(10)

    # 练习
    driver.find_element_by_xpath("//*[contains(@text, '更多')]").click()
    driver.find_element_by_xpath("//*[contains(@text, '无线显示')]").click()
    driver.find_element_by_id("android:id/switchWidget").click()
    time.sleep(2)
    driver.find_element_by_class_name("android.widget.ImageButton").click()
    driver.find_element_by_class_name("android.widget.ImageButton").click()

except Exception as e:
    print(e)
finally:
    # 当前时间
    print(time.strftime("%H:%M:%S", time.localtime()))
    # 退出驱动
    driver.quit()