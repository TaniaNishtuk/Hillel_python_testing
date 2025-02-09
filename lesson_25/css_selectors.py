#xpath locators:
class InitialWebPageCSSSelectors:
    """
    Class containing css selectors for web page - https://qauto2.forstudy.space
    """
    # мені це не нравиця, але в ДОМі цієї пейджі - це унікальний селектор
    SIGN_UP_BUTTON_SELECTOR = "button.hero-descriptor_btn.btn"
    SIGN_IN_BUTTON_SELECTOR = "button.header_signin"
    GUEST_LOG_IN_BUTTON_SELECTOR = "button.-guest"
    # тут знайде конкретне відео на головній сторінці
    VIDEO_SELECTOR = 'iframe[src="https://www.youtube.com/embed/znjjC0Iw8Wc?showinfo=0&controls=0"]'
    # пошук усіх соц мереж
    SOCIAL_LINKS = "a.socials_link"
    HILLEL_WEB_LINK = 'a[href="https://ithillel.ua"]'
    HILLEL_SUPPORT_LINK = 'a[href="mailto:developer@ithillel.ua"]'

class LogInPageCSSSelectors:
    """
    Class containing css selectors for web page - https://qauto2.forstudy.space/panel/garage after 'Sign in' click
    """
    EMAIL_FIELD = 'input#signinEmail.form-control[name="email"]'
    PASSWORD_FIELD = 'input#signinPassword.form-control[name="password"]'
    REMEMBER_ME_CHECKBOX = 'input[name="remember"]'
    FORGOT_PASSWORD = "//button[text() = 'Forgot password']"
    REGISTRATION = 'button.btn.btn-link[type="button"]'# це мені не нравиця
    LOGIN_BUTTON = 'button.btn.btn-primary[type="button"]'# це мені не нравиця
    # думаю, цей локатор дасть змогу закрити будь - яке вікно
    DISMISS_WINDOW_BUTTON = 'span[aria-hidden="true"]'

class GarageCSSSelectors:
    """
    Class containing css selectors for web page - https://qauto2.forstudy.space/panel/garage
    Appears on the screen after clik on:
    GUEST_LOG_IN_BUTTON_SELECTOR = "button.-guest"
    """
    GARAGE_BUTTON = 'a[routerlink="garage"]'
    FUEL_EXPENSES_BUTTON = 'a[routerlink="expenses"]'
    INSTRUCTIONS_BUTTON = "//a[@routerlink='instructions']"
    LOG_OUT_BUTTON = 'a[routerlink="instructions"]'
    ADD_CAR_BUTTON = 'button.btn.btn-primary' # це мені не нравиця, але цсс безпощадний якийсь

    # тицьни на 'add car' кнопку

    CAR_BRAND_POP_UP = 'select[id="addCarBrand"]'
    CAR_MODEL_POP_UP = 'select[id="addCarModel"]'
    CAR_MILEAGE_TEXT_FIELD = 'input[id="addCarMileage"]'
    # тут знайде дві кнопки на попапі, треба буде вже якось пайтоном танцювати від цього далі
    FOOTER_BUTTONS = 'button[_ngcontent-wlg-c67].btn'

    # https://qauto2.forstudy.space/panel/instructions - тепер ми тут

    BRAND_SELECTION_DROPDOWN = 'button[id="brandSelectDropdown"]'
    MODEL_SELECTION_DROPDOWN = 'button[id="modelSelectDropdown"]'
    SEARCH_BUTTON = 'button.instructions-search-controls_search'


