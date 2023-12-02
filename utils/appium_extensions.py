class AnyExpectedConditions:
    """
    Written alike many methods in `selenium expected_conditions`
    to be used with `WebDriverWait().until()` and `WebDriverWait().until_not()`;
    is true when any one of conditions is true.

    Use examples:
    `WebDriverWait(driver, timeout).until(AnyExpectedConditions(condition1, condition2, ...))`
    what is equivalent to the next logic:
    WebDriverWait(driver, timeout).until(condition1 or condition2 or ...)
    """

    def __init__(self, *args):
        """
        :param args: one or more seleniums' expected_conditions or alike functions
        """
        self.expected_conditions = args

    def __call__(self, driver):
        """
        :param driver: webdriver; typically passed
        by selenium's WebDriverWait().until() and WebDriverWait().until_not()
        :return: result of first expected_condition to be true if any
        """
        for c in self.expected_conditions:
            try:
                res = c(driver)
                if res:
                    return res
            except:
                pass


class AnyExpectedConditionsWithOrder:
    """
    Written alike many methods in `selenium expected_conditions`
    to be used with `WebDriverWait().until()` and `WebDriverWait().until_not()`;
    is true when any one of conditions is true.

    Use examples:
    `WebDriverWait(driver, timeout).until(AnyExpectedConditions(condition1, condition2, ...))`
    what is equivalent to the next logic:
    WebDriverWait(driver, timeout).until(condition1 or condition2 or ...)
    """

    def __init__(self, *args):
        """
        :param args: one or more seleniums' expected_conditions or alike functions
        """
        self.expected_conditions = args

    def __call__(self, driver):
        """
        :param driver: webdriver; typically passed
        by selenium's WebDriverWait().until() and WebDriverWait().until_not()
        :return: result of first expected_condition to be true if any and its order
        """
        for i, c in enumerate(self.expected_conditions):
            try:
                res = c(driver)
                if res:
                    return i, res
            except:
                pass
