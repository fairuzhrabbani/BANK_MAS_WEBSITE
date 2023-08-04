class Locators:

    # Todos objects
    todo_txtbox = '//input[@class="new-todo"]'
    list_items = '//ul[@class="todo-list"]//li'
    list_items_label = '//ul[@class="todo-list"]//li//div//label'
    checked_items_label = '//li[@class="completed"]//div//label'
    edit_items = '//ul[@class="todo-list"]//li//input[@class="edit"]'
    delete_items = '//button[@class="destroy"]'
    toggle_button = '//ul[@class="todo-list"]//li//div//input[@class="toggle"]'
    all_button_filter = '//a[@href="#/all"]'
    # active_button_filter = '//*[text()[contains(., "Active")]]'
    active_button_filter = '//a[@href="#/active"]'
    completed_button_filter = '//a[@href="#/completed"]'
    remaining_count = '//strong[@data-bind="text: remainingCount"]'