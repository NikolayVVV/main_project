

class Base():

    def __init__(self, driver):
        self.driver = driver


    """method get current url"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)