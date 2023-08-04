import time
import unittest
from conftest import *
from pages.ToDoListPage import ToDoListPage
# from locators.locators import Locators
import allure
import pytest
# from allure_commons._allure import severity
from allure_commons.types import AttachmentType

@pytest.mark.usefixtures("browser_setup")
class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver.get(BaseUrl)
        self.todo_page = ToDoListPage(self.driver)
        # self.get_url = self.driver.current_url

    # @pytest.mark.postive
    @allure.severity(allure.severity_level.MINOR)
    @allure.title("TC 01 - Check Title URL")
    def test_01_check_url_title(self):
        """ Descrtion : TC 01 - Check Title URL """
        expected_title = 'Knockout.js • TodoMVC'
        # Verify
        self.assertEqual(self.driver.title, expected_title, 'Title is not match')
        # Screenshoot
        allure.attach(self.driver.get_screenshot_as_png(), name="test_01_check_url_title",
                      attachment_type=AttachmentType.PNG)

    # @pytest.mark.postive
    @allure.severity(allure.severity_level.MINOR)
    @allure.title("TC 02 - Menambahkan ToDo List Items")
    def test_02_menambahkan_to_do_items(self):
        self.todo_page.enter_todolist("Meeting")
        self.todo_page.enter_todolist("Plan for a training activity")
        self.todo_page.enter_todolist("Write monthly reports")
        self.todo_page.enter_todolist("Check the stock market")
        time.sleep(2)
        all_field = self.todo_page.check_list_items_label()
        expected_list = ["Meeting", "Plan for a training activity",
                    "Write monthly reports", "Check the stock market"]
        actual_list = []
        for option in all_field:
            # print("\nTo Do List Number", all_field.index(option) + 1, "is", option.text)
            actual_list.append(option.text)

        # Verify
        assert actual_list == expected_list, "To Do List isn't match"
        assert len(all_field) == 4, "Items left isn't match"
        # Screenshoot
        allure.attach(self.driver.get_screenshot_as_png(), name="test_02_menambahkan_to_do_items",
                      attachment_type=AttachmentType.PNG)

    # @pytest.mark.postive
    @allure.severity(allure.severity_level.MINOR)
    @allure.title("TC 03 - Menyelesaikan ToDo List Items")
    def test_03_menyelesaikan_to_do_items(self):
        self.todo_page.enter_todolist("Meeting")
        self.todo_page.enter_todolist("Plan for a training activity")
        self.todo_page.enter_todolist("Write monthly reports")
        self.todo_page.enter_todolist("Afternoon tea")
        self.todo_page.enter_todolist("Check the stock market")
        time.sleep(2)
        all_field = self.todo_page.click_toggle()

        # actual = []
        actual_selected = []
        for option in all_field:
            self.converted_num = "% s" % all_field.index(option)
            if self.converted_num == '0':
                option.click()
                time.sleep(2)
                actual_selected.append(self.converted_num)
                continue
                # print(option.is_selected())
            if self.converted_num == '2':
                option.click()
                time.sleep(2)
                actual_selected.append(self.converted_num)
                break
                # print(option.is_selected())
            # actual.append(option.is_selected())

        # Verify
        expected_selected_index = ['0', '2']
        assert actual_selected == expected_selected_index, "Selected Index isn't match"
        # Screenshoot
        allure.attach(self.driver.get_screenshot_as_png(), name="test_03_menyelesaikan_to_do_items",
                      attachment_type=AttachmentType.PNG)

    # @pytest.mark.postive
    @allure.severity(allure.severity_level.MINOR)
    @allure.title("TC 04 - Filter ALL ToDo List Items")
    def test_04_filter_ALL_to_do_items(self):
        self.todo_page.enter_todolist("Meeting")
        self.todo_page.enter_todolist("Plan for a training activity")
        self.todo_page.enter_todolist("Write monthly reports")
        self.todo_page.enter_todolist("Afternoon tea")
        self.todo_page.enter_todolist("Check the stock market")
        self.todo_page.click_all_filter()
        expected_all = '5'
        expected_all_url = 'https://todomvc.com/examples/knockoutjs/#/all'
        self.get_url = self.driver.current_url

        # Verify
        assert self.todo_page.check_remaining_count() == expected_all, "Items left isn't match"
        assert self.get_url == expected_all_url, 'URL is not match'
        # Screenshoot
        allure.attach(self.driver.get_screenshot_as_png(), name="test_04_filter_ALL_to_do_items",
                      attachment_type=AttachmentType.PNG)

    # @pytest.mark.postive
    @allure.severity(allure.severity_level.MINOR)
    @allure.title("TC 05 - Filter ACTIVE ToDo List Items")
    def test_05_filter_ACTIVE_to_do_items(self):
        self.todo_page.enter_todolist("Meeting")
        self.todo_page.enter_todolist("Plan for a training activity")
        self.todo_page.enter_todolist("Write monthly reports")
        self.todo_page.enter_todolist("Afternoon tea")
        self.todo_page.enter_todolist("Check the stock market")
        self.todo_page.click_active_filter()
        expected_active = '5'
        expected_active_url = 'https://todomvc.com/examples/knockoutjs/#/active'
        self.get_url = self.driver.current_url

        # Verify
        assert self.todo_page.check_remaining_count() == expected_active, "Items left isn't match"
        assert self.get_url == expected_active_url, 'URL is not match'
        # Screenshoot
        allure.attach(self.driver.get_screenshot_as_png(), name="test_05_filter_ACTIVE_to_do_items",
                      attachment_type=AttachmentType.PNG)

    # @pytest.mark.postive
    @allure.severity(allure.severity_level.MINOR)
    @allure.title("TC 06 - Filter COMPLETED ToDo List Items")
    def test_06_filter_COMPLETED_to_do_items(self):
        self.todo_page.enter_todolist("Meeting")
        self.todo_page.enter_todolist("Plan for a training activity")
        self.todo_page.enter_todolist("Write monthly reports")
        self.todo_page.enter_todolist("Afternoon tea")
        self.todo_page.enter_todolist("Check the stock market")
        self.todo_page.click_completed_filter()
        expected_completed = '5'
        expected_completed_url = 'https://todomvc.com/examples/knockoutjs/#/completed'
        self.get_url = self.driver.current_url

        # Verify
        assert self.todo_page.check_remaining_count() == expected_completed, "Items left isn't match"
        assert self.get_url == expected_completed_url, 'URL is not match'
        # Screenshoot
        allure.attach(self.driver.get_screenshot_as_png(), name="test_06_filter_COMPLETED_to_do_items",
                      attachment_type=AttachmentType.PNG)

    # @pytest.mark.postive
    @allure.severity(allure.severity_level.MINOR)
    @allure.title("TC 07 - Hapus ToDo List Items")
    def test_07_hapus_to_do_items(self):
        self.todo_page.enter_todolist("Meeting")
        self.todo_page.enter_todolist("Plan for a training activity")
        self.todo_page.enter_todolist("Write monthly reports")
        self.todo_page.enter_todolist("Afternoon tea")
        self.todo_page.enter_todolist("Check the stock market")
        self.todo_page.click_delete()
        expected_delete = '4'

        # Verify
        assert self.todo_page.check_remaining_count() == expected_delete, "Items left isn't match"
        # Screenshoot
        allure.attach(self.driver.get_screenshot_as_png(), name="test_07_hapus_to_do_items",
                      attachment_type=AttachmentType.PNG)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()