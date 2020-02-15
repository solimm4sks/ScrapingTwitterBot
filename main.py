from selenium import webdriver
import data
from time import sleep


def concStrToNum(x):
    num = 0.0
    atDeci = False
    deciCnt = 0.1
    for i in x:
        if i == ',':
            continue
        if i == 'K':
            num *= 1000
            continue
        if i == 'M':
            num *= 1000000
            continue
        if atDeci:
            num += deciCnt * int(i)
            deciCnt /= 10
        else:
            if i == '.':
                atDeci = True
            else:
                num *= 10
                num += int(i)
    return int(num)

class TwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def closePopup(self):
        try:
            closeButton = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div[1]/div/div/div/div/div[2]/div[2]/div[2]/div/svg/g/path')
            closeButton.click()
            # print("Popup closed!")
        except Exception:
            # print("No popup needs to be closed")
            pass

    def loginTwitter(self, ind):
        self.driver.get('https://twitter.com')
        sleep(2)

        loginButton = self.driver.find_element_by_xpath('//*[text() = "Log in"]')
        loginButton.click()

        sleep(1)
        username = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/main/div/div/form/div/div[1]/label/div[2]/div/input')
        username.send_keys(data.username[ind])

        password = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/main/div/div/form/div/div[2]/label/div[2]/div/input')
        password.send_keys(data.password[ind])

        login = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/main/div/div/form/div/div[3]/div/div')
        login.click()

        sleep(3)

        self.closePopup()

    def openProfile(self, profileName):
        self.driver.get('https://twitter.com/' + profileName)
        sleep(2)

    def scrollToBottom(self, timeBetweenScrools = 2, functionWhileScrolling = lambda : None):
        SCROLL_PAUSE_TIME = timeBetweenScrools
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        results = set([])

        while True:
            tmp = functionWhileScrolling()
            for i in tmp:
                results.add(i)

            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # print('Going down')
            sleep(SCROLL_PAUSE_TIME)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        return  results

    def getProfileFollowerList(self, pfName, tbs):
        def scrape():
            userAts = []
            userText = [str(x.text).split('\n') for x in self.driver.find_elements_by_xpath('//div[@data-testid = "UserCell"]')]
            for i in userText:
                for j in i:
                    if j[0] == '@':
                        userAts.append(j)
                        break
            return  userAts

        self.openProfile(pfName)

        followersButton = self.driver.find_element_by_xpath('//span[text()="Followers"]')
        followersButton.click()

        return self.scrollToBottom(2, scrape)

    def getProfileInfo(self, name):
        self.openProfile(name)
        sleep(1)
        #fullName = self.driver.find_element_by_xpath('//main[@role = "main"]/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div[1]/div/span[1]/span').text

        numFollowing = 0
        numFollowers = 0

        tmparr = self.driver.find_elements_by_xpath('//*[@title]')
        ind = 0
        for i in tmparr:
            if not ('9' >= i.get_attribute('title')[0] >= '1'):
                ind += 1
            else:
                break

        numFollowing = concStrToNum(tmparr[ind].get_attribute('title'))
        numFollowers = concStrToNum(tmparr[ind + 1].get_attribute('title'))
        """
        try:
            tmparr = self.driver.find_elements_by_xpath('//a[@title]')
            ind = 0
            for i in tmparr:
                if not ('9' >= i.get_attribute('title')[0] >= '1'):
                    ind += 1
                else:
                    break

            numFollowing = concStrToNum(tmparr[ind].get_attribute('title'))
            numFollowers = concStrToNum(tmparr[ind + 1].get_attribute('title'))
        except Exception:
            tmparr = self.driver.find_elements_by_xpath('//[@title]')
            ind = 0
            for i in tmparr:
                if not ('9' >= i.get_attribute('title')[0] >= '1'):
                    ind += 1
                else:
                    break

            numFollowing = concStrToNum(tmparr[ind].get_attribute('title'))
            numFollowers = concStrToNum(tmparr[ind + 1].get_attribute('title'))
        """
        return [numFollowing, numFollowers]


# tw = TwitterBot()
# tw.loginTwitter(0)
# tw.writeTextBox('test')