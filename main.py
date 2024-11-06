from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

USERNAME = "killbusyness2@gmail.com"
PASSWORD ="randomguy1234"
NUMBER = "8291147114"
clicked_on_cross = False

def exp_input_py():
    python_exp_input = driver.find_element(by=By.CSS_SELECTOR, value='.artdeco-text-input--input')
    print(python_exp_input)
    python_exp_input.send_keys("1")

def exp_input_ts():
    typescript_exp_input = driver.find_element(by=By.XPATH ,value='//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3800368576-109125003-numeric"]')
    print(typescript_exp_input)
    typescript_exp_input.send_keys("1")

def radio_button():
    yes_radio_button = driver.find_element(by=By.XPATH, value='//*[@id="radio-button-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3800368576-109124995-multipleChoice"]/div[1]/label')
    print(yes_radio_button)
    yes_radio_button.click()

def click_cross_discard():
    global clicked_on_cross
    clicked_on_cross = True
    cross_xpath = "/html/body/div[3]/div/div/button"
    cross_button = driver.find_element(by=By.XPATH, value=cross_xpath)
    print(cross_button)
    cross_button.click()

    discard_xpath = '/html/body/div[3]/div[2]/div/div[3]/button[1]'
    discard_button = driver.find_element(by=By.XPATH, value=discard_xpath)
    print(discard_button)
    discard_button.click()

def apply_for_job():
    try:
        easy_apply_xpath = '/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[4]/div/div/div/button'
        easy_apply_button = driver.find_element(by=By.XPATH, value=easy_apply_xpath)
        easy_apply_button.click()#button

        # number_input = driver.find_element(by=By.XPATH, value=f'/html/body/div[3]/div/div/div[2]/div/div[2]/form/div/div/div[4]/div/div/div[1]/div/input')
        # if number_input=="":
        #     number_input.send_keys(NUMBER)

        # next_button1_xpath = "//*[contains(@class, 'artdeco-button') and contains(@class, 'artdeco-button--primary') and contains(@class, 'ember-view')]"
        # next_button1 = driver.find_element(by=By.XPATH, value=next_button1_xpath)
        # next_button1.click()

        # next_button2_xpath ="//*[contains(@class,'artdeco-button') and contains(@class,'artdeco-button--2') and contains(@class,'artdeco-button--primary') and contains(@class,'ember-view')]"
        next_button2 = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        next_button2.click() #button

        check_list = [exp_input_py,exp_input_ts,radio_button]

        for function in check_list:
            try:
                function()
            except NoSuchElementException:
                click_cross_discard()
                pass
                break
        if clicked_on_cross is False:
            xpath_review_button = "/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]"
            review_button = driver.find_element(by=By.XPATH, value=xpath_review_button)
            review_button.click()

            xpath_submit_button = "/html/body/div[3]/div/div/div[2]/div/div[2]/div/footer/div[3]/button[2]"
            submit_button = driver.find_element(by=By.XPATH, value=xpath_submit_button)

            submit_button.click()#button
    except NoSuchElementException:
        print("this is being executed")
        pass

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.linkedin.com/login')
time.sleep(5)

username_input = driver.find_element(by=By.CSS_SELECTOR, value="#username")
username_input.send_keys(USERNAME)
password_input = driver.find_element(by=By.CSS_SELECTOR, value="#password")
password_input.send_keys(PASSWORD)

signin_button = driver.find_element(By.CSS_SELECTOR, '.btn__primary--large.from__button--floating')
signin_button.click()

search_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'input[aria-label="Search"]'))
)

# Enter the search term "Python jobs" in the input field
search_input.send_keys("Python jobs")

# Submit the search by simulating the 'Enter' key
search_input.send_keys(Keys.ENTER)
search_input.send_keys(Keys.ENTER)
# all_listings = driver.find_element(by=By.CSS_SELECTOR, value="app-aware-link.global-nav__primary-link--active.global-nav__primary-link")
# network_button = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[aria-label="My Network"]'))
# )
# network_button.click()
# print(network_button)

# job_address = ".scaffold-layout__list-container .jobs-search-results__list-item .job-card-container .job-card-list__entity-lockup .flex-grow-1 .full-width .disabled"
# jobs_link_element = driver.find_elements(by=By.CSS_SELECTOR , value=job_address)
# job_links = [link for link in jobs_link_element]
# print(len(job_links))

# for job in job_links:
#     job.click()
#     apply_for_job()



























