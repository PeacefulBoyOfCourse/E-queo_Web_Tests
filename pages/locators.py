from selenium.webdriver.common.by import By


class BasePageLocators:
    PROFILE_HEAD_INFO = (By.CLASS_NAME, "app-profile-head-info__title")


class LoginPageLocators:
    LOG_IN_BY_CREDITS_BUTTON = (By.XPATH, "//div[@class='app-auth-form-card__title']")
    LOG_IN_BUTTON = (By.XPATH, "//button[@type='submit']")
    LOGIN_FIELD = (By.XPATH, "//input[@type='text']")
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")
