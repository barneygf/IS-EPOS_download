# IS-EPOS_download

Downloading raw .seed signals from geophysical IS-EPOS platform (https://tcs.ah-epos.eu/) is time-consuming 
and labor intensive. If you have, e.g. hundred of chosen events, it could takes hours and it is not amplyfying
at all. This script downloads raw signals without your action.

## Getting started

You have to get an account on IS-EPOS platform (contact with organisers and validate your e-mail).

### Preparing using IS-EPOS platform

1. Prepare appriopriate folder using "Signal download" tool. Name of this folder must be unique in your all
MY WORKSPACE! E.g. if you have "Signal download" folder change it to "Signal download aa", 
"Signal download 170831" or another. Type this name in variable "sd_name" as a Python string (name in single
or double quotes).
2. Open attached Folders.png file. In this case, if you would like to use "bb" folder, you have to type 
to the variable "nr_f" Python list: [1, 2, 2] (always in square brackets, only integrers, separated by commas, 
counting starts from 0, not 1) and "bb" to the variable "sd_name". If you have to use "Signal download aa" folder, 
you have to type [1, 2] to variable nr_f, and "Signal download aa" to the variable "sd_name".
Find your Signal download folder in your MY WORKSPACE and type appriopriate "nr_f" and "sd_name".
3. You can change variable "dt". Default is 1, so browser waiting time in different steps fluctuates between 
1 and 10 seconds. Bigger dt -> longer downloading. With dt = 1 downloading time for 100 signals takes almost two
hours. And with dt = 2 it will take two times more. But if you have slow computer or slow internet connection,
increasing dt may be necessary.

Please remember - if you do not know Python and Selenium, change only variables beetwen rows full of hashes!

### Prerequisites

Software uses Python 3 with module Selenium adn Google Chrome browser. It is necessary to have the newest
chromedriver.exe file in the same folder as a script. If you would like to use e.g. Mozilla Firefox, 
appriopriate driver and changing the driver vairiable in the code are necessary.
Firefox, you have to 

## Running

After run program ask you about e-mail at the IS-EPOS platform. Type it and click Enter. Next type your password
and click Enter. Chrome will be opened and downloading will start.

### Note about visible password

While you type your password, it is visible in the command line, so pay attention - somebody can peek it!
There is a Python module, named getpass, which allow hide password, but today it does not work with
PyCharm, which I use. So I decided to use simple input.

### Output

Downloaded .seed signals will be saved in the dafeault browser folder for downloaded files (most probably Downloads
in user folder - in the case of Windows). Some events at the IS-EPOS platform have two .seed signals, some one. In
the second case, you will get many .json files, which does not contain signal, but downloading it, it is necessary
for correct program operation. You can delete they later.
.seed files have log and difficult name, so text file with signals numbers
and data with appropriate .seed files names will be created and saved in the same folder as this script.

### Errors
I have a little problem - Google Chrome suspends after 172 signals, so if you have more, you have to modificate last 
for loop in this script. Do not hesitate to contact me.
