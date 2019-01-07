import os, sys

import allure

sys.path.append(os.getcwd())

from base.base_driver import init_driver
from page.page_filemanager import PageFileManager


class TestFileManager:

    def setup(self):
        self.driver = init_driver()
        self.page_filemanager = PageFileManager(self.driver)

    @allure.step(title="刷新功能测试")
    def test_refresh(self):
        # self.page_filemanager.init_click_and_tap()
        allure.attach('滑动屏幕','')
        self.page_filemanager.file_swipe()
        allure.attach('点击菜单按钮', '')
        self.page_filemanager.click_menu()
        allure.attach('记录下页面当前元素并刷新', '')
        self.page_filemanager.click_refresh_button()
        allure.attach('判断是否刷新成功', '')
        assert self.page_filemanager.is_refresh_successful()
