import time
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium import webdriver

from msedge.selenium_tools import Edge, EdgeOptions
import os
# load the desired webpage
edge_options = EdgeOptions()
edge_options.use_chromium = True
edge_options.binary_location = r"C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
edge_options.add_experimental_option("prefs", {
  "download.default_directory": r"C:\Users\Juan\Desktop\Internship\Week 1\OroratechDownloads"})

#Enter MTC date that you want to start downloading data from
EDGEDRIVER = "./msedgedriver.exe"
#Enter name of the selected fire that you want to start downloading data from 
#Convert it to UTC

YEAR = "2022"

driver = Edge(EDGEDRIVER, options=edge_options)

#Begin selecting the date


print(os.listdir("./OroratechDownloads"))

#Get past starting screen

#Go to the monitor path

class OroraScraper:
    def __init__(self, loginLink, driver):
        self.driver = driver
        self.fromSelected = False
        self.toSelected = False
        self.loginLink = loginLink
        self.metaDataSelected = False
        self.prevToDay = None
        self.prevFromDay = None

    def login(self, username, password):
        
        print(type(username), type(password))
        #Log in
        self.driver.get(self.loginLink)
        self.driver.maximize_window()

        usernameBar = self.driver.find_element(By.NAME, value="username")
        passwordBar = self.driver.find_element(By.NAME, value = "password")
        usernameBar.send_keys(username)
        passwordBar.send_keys(password)
        usernameBar.send_keys(Keys.ENTER)

        #Get past intro screem
        self.driver.find_element(By.CSS_SELECTOR, "button[class='button is-primary is-fullwidth']").click()
        self.driver.find_element(By.CSS_SELECTOR, "button[class='button is-normal is-fullwidth']").click()
        self.driver.find_element(By.CSS_SELECTOR, "button[class='button is-normal is-fullwidth']").click()
    def goToMonitoredAreas(self):
        driver.find_element(By.XPATH, "//*[@class='navbar-item']//span[.='Monitor']/parent::node()").click()


        driver.find_element(By.XPATH, "//*[@id='export-label']").click()


    def selectFromDate(self, year, month, day, hour, minute, ampm):
        """Year: String
        Month: String - Eg, february, january...
        day: String
        ampm: am or pm

        """
        if ampm.lower() == "am":
            ampm = "a.m."
            hourSelectCond = '0'
        elif ampm.lower() =="pm":
            ampm = "p.m." 
            hourSelectCond = '13'
        month = month.capitalize()
        #Click left drop down menu

        if not self.fromSelected:
            print("WENT HERE")
            self.driver.find_element(By.XPATH, "//section[@class ='tab-content']//*[@class='field']//label[.='From']//parent::node()//div[@class='dropdown dropdown-menu-animation is-bottom-right is-mobile-modal']").click()
            self.fromSelected = True
            self.toSelected = False

        #Find drop down menu and select year

        leftDropdownYear = self.driver.find_element(By.XPATH,"//div[@class='control datepicker']//span[@class='select']//option[@value='2000']//parent::node()")
        leftYearSelect = Select(leftDropdownYear)

        #Select month
        leftDropdownMonth = self.driver.find_element(By.XPATH," //div[@class='control datepicker']//span[@class='select']//option[@value='0']//parent::node()") 
        leftMonthSelect = Select(leftDropdownMonth) 
        leftYearSelect.select_by_visible_text(year)


        leftMonthSelect.select_by_visible_text(month)
        #Select day


        if self.prevFromDay != day:
            self.driver.find_element(By.XPATH, "//div[@class='datepicker-body']//a[@class='datepicker-cell is-selectable']//span[.={0}]".format(day)).click()
        
        self.prevFromDay = day


        #Select hour, minute, am or pm
        leftAMPM = self.driver.find_element(By.XPATH, "//div[@class='timepicker control']//span[@class='select']//option[@value='a.m.']//parent::node()")
        leftAMPMSelection = Select(leftAMPM)
        leftAMPMSelection.select_by_visible_text(ampm)

        leftHour = self.driver.find_element(By.XPATH, "//div[@class='timepicker control']//span[@class='select']//option[@value='{0}']//parent::node()".format(hourSelectCond))
        leftHourSelection = Select(leftHour)
        leftHourSelection.select_by_visible_text(hour)

        leftMinute = self.driver.find_element(By.XPATH, "//div[@class='timepicker control']//span[@class='select']//option[@value='59']//parent::node()")
        leftMinuteSelection = Select(leftMinute)

        leftMinuteSelection.select_by_visible_text(minute)






    def selectToDate(self, year, month, day, hour, minute, ampm, debug = False):
        if ampm.lower() == "am":
            ampm = "a.m."
            hourSelectCond = '0'
        elif ampm.lower() =="pm":
            ampm = "p.m." 
            hourSelectCond = '13'
        month = month.capitalize()

        #Click left drop down menu
        if not self.toSelected:
            self.driver.find_element(By.XPATH, "//section[@class ='tab-content']//*[@class='field']//label[.='To']//parent::node()//div[@class='dropdown dropdown-menu-animation is-bottom-left is-mobile-modal']").click()
            self.toSelected = True
            self.fromSelected = False
        
        #Find drop down menu and select year
        

        rightDropdownYear = self.driver.find_element(By.XPATH,"//div[@class='control datepicker']//div[@tabindex='0']//span[@class='select']//option[@value='2023']//parent::node()")
        rightYearSelect = Select(rightDropdownYear)
        #Select month
        rightDropdownMonth = self.driver.find_element(By.XPATH," //div[@class='control datepicker']//div[@tabindex='0']//span[@class='select']//option[@value='0']//parent::node()") 
        rightMonthSelect = Select(rightDropdownMonth) 
        rightYearSelect.select_by_visible_text(year)


        rightMonthSelect.select_by_visible_text(month)

        if self.prevToDay != day:
            self.driver.find_element(By.XPATH, "//div[@class='control datepicker']//div[@class='datepicker-body']//a[@class='datepicker-cell is-selectable']//span[.={0}]".format(day)).click()
        
        self.prevToDay = day
        
        rightAMPM = self.driver.find_element(By.XPATH, "//div[@class='control datepicker']//div[@class='timepicker control']//span[@class='select']//option[@value='a.m.']//parent::node()")

        rightAMPMSelection = Select(rightAMPM)
        #Do not move this line or it wll cause a bug
        rightAMPMSelection.select_by_visible_text(ampm)

        rightHour = self.driver.find_element(By.XPATH, "//div[@class='control datepicker']//div[@class='timepicker control']//span[@class='select']//option[@value='{0}']//parent::node()".format(hourSelectCond))
        rightHourSelection = Select(rightHour)
        rightHourSelection.select_by_visible_text(hour)

        rightMinute = self.driver.find_element(By.XPATH, "//div[@class='control datepicker']//div[@class='timepicker control']//span[@class='select']//option[@value='59']//parent::node()")
        rightMinuteSelection = Select(rightMinute)
        rightMinuteSelection.select_by_visible_text(minute)
    def downloadKML(self):
        self.driver.find_element(By.XPATH, "//*[text()[contains(.,'KML')]]").click()
    def selectMetaData(self, options = None):
        if not self.metaDataSelected:
            option = 'Select all Metadata'
            self.metaDataSelected = True
        else:
            option = 'Deselect all Metadata'
            self.metaDataSelected = False
        self.driver.find_element(By.XPATH, "//div[.='{0}']//parent::node()//div[@class='b-tooltip is-primary is-top is-medium']".format(option)).click()







loginLink = "https://app.ororatech.com/login?backTo=https%3A%2F%2Fapp.ororatech.com%2F#/"


def test():
    theScraper.selectFromDate("2022", "february", "19", "2", "31","pm")
    for ampm in ["am", "pm"]:
        for hour in range(1, 13):
            for minute in range(1, 60):
                theScraper.selectFromDate("2022", "february", "19", str(hour), '{0:02d}'.format(minute), ampm)

                theScraper.selectToDate("2022", "february", "23", str(hour), '{0:02d}'.format(minute), ampm)


theScraper = OroraScraper(loginLink= loginLink, driver = driver)

USERNAME = "jbb@ualberta.ca"
PASSWORD = "firesarecool2022"
print(type(USERNAME), type(PASSWORD))
theScraper.login(USERNAME, PASSWORD)
theScraper.goToMonitoredAreas()



prevfileNames = os.listdir('./OroratechDownloads')

theScraper.selectMetaData()

theScraper.selectFromDate("2023", "january", "2", "2", "31","pm")

theScraper.selectToDate("2023", "january", "14", "2", "31","pm")
theScraper.downloadKML()

wfs = False
while len(os.listdir('./OroratechDownloads')) == len(prevfileNames):
    
      print(len(os.listdir('./OroratechDownloads')), len(prevfileNames))

      time.sleep(0.1)
i = 0
print(len(os.listdir('./OroratechDownloads')), len(prevfileNames))

for filename in os.listdir("./OroratechDownloads"):
    print("Filename ", filename)
    if "wfs-area-export" in filename:
        print("here")
        os.rename("./OroratechDownloads/"+filename, "./OroratechDownloads/test{0}.kml".format(i))
    i+=1
#theScraper.selectFromDate("2023", "january", "9", "2", "31","pm")



"""

leftMonthSelect.select_by_visible_text("February")
#Select day
driver.find_element(By.XPATH, "//div[@class='datepicker-body']//a[@class='datepicker-cell is-selectable']//span[.=3]").click()


#Select hour, minute, am or pm

leftHour = driver.find_element(By.XPATH, "//div[@class='timepicker control']//span[@class='select']//option[@value='13']//parent::node()")
leftHourSelection = Select(leftHour)

leftMinute = driver.find_element(By.XPATH, "//div[@class='timepicker control']//span[@class='select']//option[@value='59']//parent::node()")
leftMinuteSelection = Select(leftMinute)

leftAMPM = driver.find_element(By.XPATH, "//div[@class='timepicker control']//span[@class='select']//option[@value='a.m.']//parent::node()")


leftAMPMSelection = Select(leftAMPM)
leftHourSelection.select_by_visible_text("4")
leftMinuteSelection.select_by_visible_text("47")
leftAMPMSelection.select_by_visible_text("p.m.")

"""
#Select hour
time.sleep(5)



#Then be able to pick day



#Make sure the day is selectable,

#One the day has been chosen click on the day
#driver.find_element(By.XPATH,"//div[@class='control datepicker']//span[@class='select']//option[@value='2022']").click()
#Go onto the website using selenium
#Log in
time.sleep(5)
#Go to the terminal where you have your saved files

#As a programmer I want to be able to use a download function



#The function will have as parameters, name of monitored fire, date-time start, date-time end


def getFirePolygon(monitoredName, startDate, endDate):
    pass
    #Start