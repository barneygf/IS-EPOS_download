''' The program download .seed signals form IS-EPOS platform. You have to input your registered e-mail and password.
You have to prepare folders using IS-EPOS platform GUI amicably attached .jpg and introduce appriopriate folders
numbers. Downloaded signal will be saved in default browser folder for downloaded files (most probably Downloads
in user folder - in the case of Windows). .seed files have log and difficult name, so text file with signals numbers
and data with appropriate .seed files names will be created and saved in the same folder as this script.
Dowloading signals takes a long time - saving 100 signals is almost two hours.
And now I have a little problem - Google Chrome suspends after 172 signals, so if you have more, you
have to modificate last for loop in this script. Do not hesitate to contact me.
Maciej Barnaś, e-mail: maciej.michal.barnas(at)gmail.com
Last edited: 2017-08-31 '''

import selenium.webdriver as webdriver
import time
from math import ceil

print('*** Download signals from IS-EPOS platform ***')
username = input('Type your e-mail on IS-EPOS platform: ')
password = input('Type your password on IS-EPOS platform: ')  # getpass.getpass() doesn't work in PyCharm

nr_f = [1, 2]  # Number of folder in 'My Workspace' at TCS Portal, starting from zero (first folder=0, second folder=1 etc.)
sd_name = 'Signal download aa'  # Name of 'Signal download' folder
dt = 1  # Sleeping time

# Standard input
events_per_page = 20

# App
nr_f_corr = []
for i in range(len(nr_f)):
    nr_f_corr.append(sum(nr_f[:i+1]))
print(nr_f_corr)
driver = webdriver.Chrome()  # Open browser
url = 'https://tcs.ah-epos.eu/login.html'
driver.get(url)  # Open webpage
time.sleep(dt)
driver.find_element_by_link_text('LOGIN').click()  # Click LOGIN
time.sleep(dt)

# Input username
username_field = driver.find_element_by_id('AuthenticationUI.username')
username_field.clear()
username_field.send_keys(username)

# Input password
password_field = driver.find_element_by_id('WebPasswordRetrieval.password')
password_field.clear()
password_field.send_keys(password)

driver.find_element_by_id('AuthenticationUI.authnenticateButton').click()  # Click "Authenticate"
time.sleep(5*dt)
driver.find_element_by_link_text("MY WORKSPACE").click()  # Click MY WORKSPACE
time.sleep(4*dt)

# Expand on catalogue tree
for i in range(len(nr_f)):
    driver.find_elements_by_xpath('//i[@class="fa fa-caret-right container-icon"]')[nr_f_corr[i]].click()
    time.sleep(dt)

driver.find_element_by_link_text(sd_name).click()  # Open your "Signal download" folder
time.sleep(3*dt)

# Get number of all events
events_number = driver.find_element_by_class_name('pageDetails').text
events_number = events_number.split('of ')[1]
events_number = int(events_number)

pages_number = ceil(events_number/events_per_page)  # Calculate number of pages in "Signal download" folder

nowdate = time.strftime('%Y-%m-%d %H%M%S')  # Now date with seconds
filename = nowdate + '.txt'  # Name of file with events and their signals

# Expand header for this file
header = driver.find_element_by_xpath('//tr[@__gwt_header_row="0"]').text
header = header.split()
header.extend(['First_file', 'Second_file'])
print('header:', header)

# Save header to file
with open(filename, 'w') as file_output:
    for item in header:
        file_output.write('%s\t' % item)
    file_output.write('\n')

def downloading(row, event_number, number_of_page):
    driver.find_element_by_link_text(sd_name).click()  # Open your "Signal download" folder
    time.sleep(3*dt)

    # Open appriopriate page in "Signal download" folder
    for i in range(number_of_page - 1):
        driver.find_element_by_xpath('//img[@aria-label="Next page"]').click()
        time.sleep(dt)

    clicked_row = driver.find_elements_by_class_name(row)[event_number]  # Click on specific event
    temp_text = clicked_row.text  # Scrap text from clicked row
    temp_text = temp_text.split('\n')  # Divide this text to list
    print('temp text: ', temp_text)
    clicked_row.click()  # Click on this row
    time.sleep(2*dt)
    driver.find_element_by_xpath('//button[@class="gwt-Button btn btn-primary"]').click()  # Click on RUN button
    time.sleep(10*dt)  # Long wait - generating signal

    # Get name of generated files
    signal_name = driver.find_element_by_class_name('result-panel').text  # Get names of generated signals
    signal_name = signal_name.split('\n')
    print('signal name: ', signal_name)
    temp_text.extend(signal_name)

    def click_download(file):
        driver.find_element_by_link_text(signal_name[file]).click()  # Open generated signal
        time.sleep(5*dt)
        driver.find_element_by_xpath('//i[@class="fa fa-cogs"]').click()  # Click ACTIONS button
        time.sleep(dt)
        driver.find_element_by_xpath('//i[@class="fa fa-download"]').click()  # Click DOWNLOAD option

    click_download(0)  # Download first generated file
    click_download(1)  # Download second generated

    print(temp_text)

    # Save data of signal to text file
    with open(filename, 'a') as file_output:
        for item in temp_text:
            file_output.write('%s\t' % item)
        file_output.write('\n')

for i in range(pages_number + 1):
    for j in range(int(events_per_page/2)):
        downloading('cellTableEvenRow', j, i)
        downloading('cellTableOddRow', j, i)