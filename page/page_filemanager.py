import os, sys
from time import sleep

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

sys.path.append(os.getcwd())
from base.base_action import BaseAction

menu_button = By.ID, "com.cyanogenmod.filemanager:id/ab_actions"
init_button = By.XPATH, "text,确定"
refresh_button = By.XPATH, "text,刷新"
ele = By.ID, "com.cyanogenmod.filemanager:id/navigation_view_item_name"


class PageFileManager(BaseAction):
    def __init__(self, driver):
        super().__init__(driver)
        self.init_click_and_tap()

    # 点击“确定”按钮，返回
    def init_click_and_tap(self):
        self.click(init_button)
        sleep(2)
        self.driver.press_keycode(4)
        sleep(2)

    # 然后记录一下页面的第一个元素的文本，从music滑动到data
    def file_swipe(self):
        self.ele1 = self.find_elements(ele)[0].text
        print(self.ele1)
        self.driver.swipe(372, 2058, 372, 1088, 3000)
        sleep(3)

    # 点击菜单按钮
    def click_menu(self):
        self.click(menu_button)

    # 点击刷新按钮，并获取当前页面第一个元素
    def click_refresh_button(self):
        self.click(refresh_button)
        sleep(2)
        self.ele2 = self.find_elements(ele)[0].text
        print(self.ele2)

    # 比较两个元素内容是否一致
    def is_refresh_successful(self):
        if self.ele1 == self.ele2:
            return True
        else:
            return False

