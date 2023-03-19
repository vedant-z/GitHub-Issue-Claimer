from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

# Set the URL of the issue page you want to monitor
url = 'https://github.com/lone-wolf45/Webpage-Maker/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc'

# Set the path of your Chrome driver executable
path='C:\\Users\vedant\OneDrive\Desktop'

# Set the labels you want to monitor
# labels = ["up-for-grabs", "good first issue"]

# Set the path of the file where you want to store the issue information
file_path = 'C:\\Users\\vedant\OneDrive\Desktop\issues.txt'

# Define a function to write the issue information to the file
def write_to_file(issue_info):
    with open(file_path, 'a') as f:
        f.write(issue_info + '\n\n')

# Define a function to claim the issue by adding a comment
def claim_issue(driver):
    comment_box = wait.until(EC.element_to_be_clickable((By.ID, "new_comment_field")))
    comment_box.send_keys("Claiming this issue", Keys.CONTROL, Keys.RETURN)

# Define a function to check if that issue is already been visited
def search_issue(issue_link):
    with open(file_path, 'r') as file:
        # read all content of a file
        content = file.read()
        # check if string present in a file
        if issue_link in content:
            return False
        else:
            return True

#####################################################################################################################

# Start the browser and open the issue page
driver = webdriver.Chrome(path)

driver.get(url)

# Set up the wait object
wait = WebDriverWait(driver, 20)

#####################################################################################################################

# c=1

while True:

    # Find all the issues with the required labels
    issues_label_xpath = "//a[contains(@class,'IssueLabel')]"
    issues_label = wait.until(EC.presence_of_all_elements_located((By.XPATH, issues_label_xpath)))

    for issue_label in issues_label:

        # Check if the issue has the required label
        label = issue_label.text

        # if label in labels:
        if label=="good first issue":

            # Get the URL of the issue and open it
            issue_parent_element = issue_label.find_element(By.XPATH, "..")
            issue_grandparent_element = issue_parent_element.find_element(By.XPATH, "..")
            issue_link_element = issue_grandparent_element.find_element(By.CLASS_NAME, "Link--primary")
            issue_link = issue_link_element.get_attribute('href')

            if(search_issue(issue_link)):
                driver.get(issue_link)

                # Write the issue information to the file
                issue_title = driver.find_element(By.XPATH, "//bdi[contains(@class, 'js-issue-title')]")
                issue_info = f"{issue_title.text}\n{issue_link}\n\n"
                write_to_file(issue_info)

                # if(c):
                #     c=0
                #     signin_link = driver.find_element(By.XPATH, "//a[text()='Sign in']").get_attribute('href')
                #     driver.get(signin_link)
                #     username_box = wait.until(EC.element_to_be_clickable((By.XPATH, '// input[ @ id = "login_field"]')))
                #     username_box.send_keys("vedant-z")
                #     password_box = wait.until(EC.element_to_be_clickable((By.XPATH, '// input[ @ id = "password"]')))
                #     password_box.send_keys("nightfury45@D")
                #     driver.find_element(By.XPATH, '//input[@value="Sign in"]').click()

                # Claim the issue by adding a comment
                claim_issue(driver)
                # break
            else:
                break
            # break

    driver.get(url)
    time.sleep(600)
    # driver.refresh()

driver.quit()
