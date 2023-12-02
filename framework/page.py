class Page:
    """
    Dummy class for pages.
    Common page functionality can be added
    """
    def __init__(self, driver):
        self.driver = driver

    def go_back(self):
        self.driver.back()
