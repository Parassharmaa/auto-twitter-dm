# auto-twitter-dm

Script to automate direct message for new followers using schedular

## Usage
1. Fork the repo
2. Update the config file with your custom message and twitter username.
3. Also, create a MongoDB instance on [mlab](https://mlab.com)
4. Click on **Deploy on Heroku**.
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
5. After heroku is done with set up, go to setting of the app and set the following environment variables on heroku:
	+ TW_CTOKEN (twitter consumer token)
	+ TW_CSECRET (twitter consumer secret)
	+ TW_ATOKEN (twitter access token)
	+ TW_ASECRET (twitter access secret)
	+ DB_AUTOMATE (MongoDB db url => mongodb://<dbuser>:<dbpassword>@dsrandom.mlab.com:51242/random

**Congrats, The script is live**



