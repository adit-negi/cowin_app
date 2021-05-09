# cowin-alerts-app
Register using your email and pincode get real time alerts on your email once a slot opens.
http://ec2-54-159-10-134.compute-1.amazonaws.com/

## set up
    1. git clone ................
    2. set up virtualevn
    3. pip install -r requirements.txt
    4. Setup local SETTINGS.py (prerequisite is have mysql installed)
    5. python manage.py migrate
    6. start contributing

## ToDo
    1. Currently the bot is a task, add it the production ec2 cron tab.
    2. Improve styling on the home page.
    3. Auto generate neighboring pincodes for better search results.
    4. Add other covid resources.
    6. Validate pincodes at time of input/ Add select2 to pincodes
