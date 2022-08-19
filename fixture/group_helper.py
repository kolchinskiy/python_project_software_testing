class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create_group(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # create_new_group
        wd.find_element_by_name("new").click()
        self.complete_form(group)
        # save_group
        wd.find_element_by_name("submit").click()
        self.open_groups_page()

    def edit_first_group(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # select_first_group
        wd.find_element_by_name("selected[]").click()
        # click_button_Edit
        wd.find_element_by_name("edit").click()
        self.complete_form(group)
        # save_edited_group
        wd.find_element_by_name("update").click()
        self.open_groups_page()

    def complete_form(self, group):
        wd = self.app.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # delete selected group
        wd.find_element_by_name("delete").click()
        self.open_groups_page()

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
