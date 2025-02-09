#xpath locators:
class InitialWebPageXpathSelectors:
    """
    Class containing xpath selectors for web page - https://qauto2.forstudy.space
    """
    SIGN_UP_BUTTON_SELECTOR = "//button[text() = 'Sign up']"
    SIGN_IN_BUTTON_SELECTOR = "//div//button[contains(text(), 'Sign In')]"
    GUEST_LOG_IN_BUTTON_SELECTOR = "//div//button[contains(@class, 'header-link -guest')]"
    # тут можна буде знайти усі ютубні відео і далі вже працювати з потрібним через пайтон
    VIDEO_SELECTOR = "//iframe[contains(@src, 'https://www.youtube.com')]"
    # пошук усіх соц мереж
    SOCIAL_LINKS = "//a[contains(@class, 'socials_link')]"
    HILLEL_WEB_LINK = "//a[@href='https://ithillel.ua']"
    HILLEL_SUPPORT_LINK = "//a[@href='mailto:developer@ithillel.ua']"

class LogInPageXpathSelectors:
    """
    Class containing xpath selectors for web page - https://qauto2.forstudy.space/panel/garage after 'Sign in' click
    """
    EMAIL_FIELD = "//*[@id='signinEmail']"
    PASSWORD_FIELD = "//*[@id='signinPassword']"
    REMEMBER_ME_CHECKBOX = "//*[@name='remember']"
    FORGOT_PASSWORD = "//button[text() = 'Forgot password']"
    REGISTRATION = "//button[text() = 'Registration']"
    LOGIN_BUTTON = "//button[text() = 'Login']"
    # думаю, цей локатор дасть змогу закрити будь - яке вікно
    DISMISS_WINDOW_BUTTON = "//span[@aria-hidden='true']"

class GarageXpathSelectors:
    """
    Class containing xpath selectors for web page - https://qauto2.forstudy.space/panel/garage
    Appears on the screen after clik on:
    GUEST_LOG_IN_BUTTON_SELECTOR = "//div//button[contains(@class, 'header-link -guest')]"
    """
    GARAGE_BUTTON = "//a[@routerlink='garage']"
    FUEL_EXPENSES_BUTTON = "//a[@routerlink='expenses']"
    INSTRUCTIONS_BUTTON = "//a[@routerlink='instructions']"
    LOG_OUT_BUTTON = "//span[contains(@class, 'icon icon-logout')]"
    ADD_CAR_BUTTON = "//button[text()='Add car']"

    # тицьни на 'add car' кнопку

    CAR_BRAND_POP_UP = "//*[@id='addCarBrand']"
    CAR_MODEL_POP_UP = "//*[@id='addCarModel']"
    CAR_MILEAGE_TEXT_FIELD = "//*[@id='addCarMileage']"
    CANCEL_BUTTON = "//button[text()='Cancel']"
    ADD_BUTTON = "//button[text()='Add']" # active only of car/model/mileage fields are selected and filled in

    # https://qauto2.forstudy.space/panel/instructions - тепер ми тут

    BRAND_SELECTION_DROPDOWN = "//*[@id='brandSelectDropdown']"
    MODEL_SELECTION_DROPDOWN = "//*[@id='modelSelectDropdown']"
    SEARCH_BUTTON = "//button[text()='Search']"


