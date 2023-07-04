from classes.school import SchoolOperations
from classes.driver import DriverOperations

if __name__ == "__main__":
    driver_chrome = DriverOperations()
    driver_chrome.start_driver()

    school = SchoolOperations(driver_chrome.driver)
    school.search_school()