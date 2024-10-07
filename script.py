import time
from playwright.sync_api import sync_playwright


def login(page, username, password):
    page.wait_for_selector('#userName')
    page.fill('#userName', username)

    page.fill('#userPwd', password)

    page.click('#userLogin')

    page.wait_for_url(
        "https://portal.svkm.ac.in/MPSTME-NM-M/viewFeedbackDetails")

    print("Login successful.")


def click_toggle_and_feedback_link(page):
    # Wait for the toggle link and click it
    page.wait_for_selector('a[href="#feeback_acoording1"]')
    page.click('a[href="#feeback_acoording1"]')
    print("Toggle clicked.")

    # Wait for the "Provide Feedback" button and click it
    page.wait_for_selector(
        'a[href="/MPSTME-NM-M/giveStudentFeedback?feedbackId=2277"]')
    page.click('a[href="/MPSTME-NM-M/giveStudentFeedback?feedbackId=2277"]')
    print("Provide Feedback button clicked.")

    # Wait for the next page to load
    page.wait_for_url(
        "https://portal.svkm.ac.in/MPSTME-NM-M/giveStudentFeedback?feedbackId=2277")
    print("Feedback form page loaded.")


def fill_form(page):
    dropdowns = page.query_selector_all('select[id^="answer"]')

    for dropdown in dropdowns:
        if dropdown:
            dropdown.select_option('5')
            print(f"Selected '5' for {dropdown.get_attribute('id')}")

    page.click('#btn1')

    print("Form filled and submitted for the current page.")

    time.sleep(3)


with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)  # Launch the browser
    page = browser.new_page()

    page.goto('https://portal.svkm.ac.in/usermgmt/login')

    username = "your_sap_id"  # Replace with actual username
    password = "your_password"  # Replace with actual password

    login(page, username, password)

    click_toggle_and_feedback_link(page)

    for i in range(1, 5):
        fill_form(page)

    browser.close()
