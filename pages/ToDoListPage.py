from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from locators.locators import Locators
import time


class ToDoListPage:
    def __init__(self, driver):
        self.driver = driver

        self.todo_txtbox = Locators.todo_txtbox
        self.toggle_button = Locators.toggle_button
        self.edit_items = Locators.edit_items
        self.delete_items = Locators.delete_items
        self.all_button_filter = Locators.all_button_filter
        self.active_button_filter = Locators.active_button_filter
        self.completed_button_filter = Locators.completed_button_filter
        self.remaining_count = Locators.remaining_count
        self.checked_items_label = Locators.checked_items_label

    def enter_todolist(self, todolist):
        self.driver.find_element(By.XPATH, Locators.todo_txtbox).clear()
        self.driver.find_element(By.XPATH, Locators.todo_txtbox).send_keys(todolist)
        self.driver.find_element(By.XPATH, Locators.todo_txtbox).send_keys(Keys.ENTER)
        time.sleep(1)

    def click_toggle(self):
        toggle_items = self.driver.find_elements(By.XPATH, Locators.toggle_button)
        return toggle_items

    def click_edit(self):
        source = self.driver.find_element(By.XPATH, Locators.edit_items)
        action = ActionChains(self.driver)
        # double click operation and perform
        action.double_click(source).perform()

    def click_delete(self):
        action = ActionChains(self.driver)
        source = self.driver.find_element(By.XPATH, Locators.list_items_label)
        action.move_to_element(source).perform()
        self.driver.find_element(By.XPATH, Locators.delete_items).click()

    def click_all_filter(self):
        self.driver.find_element(By.XPATH, Locators.all_button_filter).click()

    def click_active_filter(self):
        self.driver.find_element(By.XPATH, Locators.active_button_filter).click()

    def click_completed_filter(self):
        self.driver.find_element(By.XPATH, Locators.completed_button_filter).click()

    def check_remaining_count(self):
        remaining = self.driver.find_element(By.XPATH, Locators.remaining_count).text
        return remaining

    def check_list_items_label(self):
        listitems = self.driver.find_elements(By.XPATH, Locators.list_items_label)
        return listitems

    def checked_items_label(self):
        checkeditems = self.driver.find_elements(By.XPATH, Locators.checked_items_label).text
        return checkeditems


