from appium import webdriver
import time, traceback

#怎么配置
desired_caps= {}
desired_caps['platformName']='Android'
desired_caps['appPackage']='io.manong.developerdaily'
desired_caps['appActivity']='io.toutiao.android.ui.activity.LaunchActivity'
desired_caps['unicodeKeyboard']=True
desired_caps['noReset']=True
desired_caps['newCommandTimeout']=6000
desired_caps['deviceName']='huawei'



driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


try:
    driver.implicitly_wait(10)
#怎么找到手机端id
    driver.find_element_by_id("io.manong.developerdaily:id/tab_bar_plus").click()
    time.sleep(1)
    driver.find_element_by_id("io.manong.developerdaily:id/btn_email").click()


except:
    #traceback什么意思
    print(traceback.format_exc())

