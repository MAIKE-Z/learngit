# UI自动化
> 在可以写出来一些简单的脚本之后，这时候就要学习selenium或appium 一些常用的api，了解显式等待、xpath的高级定位等各种用法，还要学习pytest，unittest等单元测试框架  
## selenium或者appium的环境配置
find_elements_by_name(‘xx’)
find_elements_by_id
find_elements_by_xpath
find_elements_by_link_text
find_elements_by_partial_link_text
find_elements_by_tag_name
find_elements_by_class_name
find_elements_by_css_selector
or
input_1 = browser.find_element(By.ID, 'q')  先导入from selenium.webdriver.common.by import By

## 显式等待
以下是可以在显式等待中使用的预期条件
以下两个条件类验证title，验证传入的参数title是否等于或包含于driver.title
title_is
title_contains

以下两个条件验证元素是否出现，传入的参数都是元组类型的locator，如(By.ID, ‘kw’)
顾名思义，一个只要一个符合条件的元素加载出来就通过；另一个必须所有符合条件的元素都加载出来才行
presence_of_element_located
presence_of_all_elements_located

以下三个条件验证元素是否可见，前两个传入参数是元组类型的locator，第三个传入WebElement
第一个和第三个其实质是一样的
visibility_of_element_located
invisibility_of_element_located
visibility_of

以下两个条件判断某段文本是否出现在某元素中，一个判断元素的text，一个判断元素的value
text_to_be_present_in_element
text_to_be_present_in_element_value

以下条件判断frame是否可切入，可传入locator元组或者直接传入定位方式：id、name、index或WebElement
frame_to_be_available_and_switch_to_it

以下条件判断是否有alert出现
alert_is_present

以下条件判断元素是否可点击，传入locator
element_to_be_clickable

以下四个条件判断元素是否被选中，第一个条件传入WebElement对象，第二个传入locator元组
第三个传入WebElement对象以及状态，相等返回True，否则返回False
第四个传入locator以及状态，相等返回True，否则返回False
element_to_be_selected
element_located_to_be_selected
element_selection_state_to_be
element_located_selection_state_to_be

最后一个条件判断一个元素是否仍在DOM中，传入WebElement对象，可以判断页面是否刷新了
staleness_of
![](UI%E8%87%AA%E5%8A%A8%E5%8C%96/7B9628CB-1720-49DB-8536-3E7BC8BE8418.png)
## xpath的高级定位等各种用法
1. 绝对路径定位
a = browser.find_element_by_xpath('/html/body/div/div[2]/div/div/div/from/span/input')
2. 标签+属性定位——xpath = "//标签名[@属性='属性值']"
例如  //*[@id="kw"]，其中*表示所有的标签名
当单一的属性无法确定到一个元素时，可以使用组合属性的方式
例如，百度首页的输入框可以表示为//*[@id="kw" and @name="wd"]
3. text()方法定位
例如，百度首页的新闻超链接的xpath可以表示为//*[text()='新闻']
4. contains()方法定位，也叫模糊定位
xpath = "//标签名[contains(@属性, '属性值')]"
例如，百度首页的新闻也可以写成//a[contains(@name,'news')]
5. starts-with ，ends-with方法定位
starts-with -- 匹配以xx开头的属性值；ends-with -- 匹配以xx结尾的属性值
//*[starts-with(@value,'百度一')]可以定位到百度一下按钮；
但是browser.find_element_by_xpath("//a[ends-with(@name,'_trnews')]")定位不到新闻，那是因为ends-with Xpath2.0的用法，但是浏览器一般通常只支持Xpath1.0
6. 如果一个元素无法通过自身的属性定位到，那么可以先定位到他的上一级或者上N级，然后再一级一级地找到他
例如，定位到百度首页的输入框，可以表示成//form[@id='form']/span[contains(@class,'s_ipt_wr')]/input

![](UI%E8%87%AA%E5%8A%A8%E5%8C%96/pastedGraphic.png)

> 缺点  
1. 性能差，因为使用这种方式进行定位，webdriver会将整个页面的所有元素进行扫描来找到我们所需的元素，所以当脚本中大量使用XPath方式定位，会大大降低脚本的执行速度。
2. Xpath会随着页面的布局的改变而改变，几乎不能维护
> 优点  
1. 可以做布尔逻辑判断，例如//*[@id="kw" and @name="wd"]
2. 可以进行模糊定位，contains(),start-with(),ends-with()等


::接下来的还要一个步骤就是去了解PO设计模式。::

#学习/测试