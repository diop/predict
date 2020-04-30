![Predict](images/cover.png)

# Twilio Hackathon 2020 - Predict
![Screenshot](images/screenshot.png)

## About
Predict allows you to simply text a person's first name to a Twilio number and get back their gender i.e Male or Female

## Example
+ Web --> [https://twilio-predict.herokuapp.com/predict/michelle](https://twilio-predict.herokuapp.com/predict/michelle)
+ SMS --> [https://twilio-predict.herokuapp.com/hook](https://twilio-predict.herokuapp.com/hook)

### Software Requirement
+ Python 3.7 or later
+ [FastAPI](https://fastapi.tiangolo.com/)
+ [scikit-learn](https://scikit-learn.org/stable/)
+ [Jupyter Notebook](https://jupyter.org/)
+ A Twilio account - [sign up](https://www.twilio.com/try-twilio)

### API Documentation
+ [FastAPI](https://twilio-predict.herokuapp.com/redoc)
+ [Swagger](https://twilio-predict.herokuapp.com/docs)


### Setup Python Env
```
pip install virtualenv
virtualenv venv
source venv/bin/activate
```

### Install Packages
```
pip install -r requirements.txt
```

### Credentials config
```
cp .env.template .env
code .env
```

### Twilio Account Settings
Before we begin, we need to collect
all the config values we need to run the application:

| Config&nbsp;Value | Description                                                                                                                                                  |
| :---------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Account&nbsp;Sid  | Your primary Twilio account identifier - find this [in the Console](https://www.twilio.com/console).                                                         |
| Auth&nbsp;Token   | Used to authenticate - [just like the above, you'll find this here](https://www.twilio.com/console).                                                         |
| Phone&nbsp;number | A Twilio phone number in [E.164 format](https://en.wikipedia.org/wiki/E.164) - you can [get one here](https://www.twilio.com/console/phone-numbers/incoming) |

### Local development
See [Twilio Account Settings](#twilio-account-settings) to locate the necessary environment variables.

1. Run the application

```bash
uvicorn app:app --reload
```

2. Navigate to [http://localhost:8000](http://localhost:8000)

That's it!

### Tests

You can run the tests locally by typing:

```bash
cd genclf
py.test
```

### Cloud deployment

Additionally to trying out this application locally, you can deploy it to a variety of host services. Here is a small selection of them.

Please be aware that some of these might charge you for the usage or might make the source code for this application visible to the public. When in doubt research the respective hosting service first.

| Service                           |                                                                                                                                                                                                                           |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Heroku](https://www.heroku.com/) | [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)                                                                                                                                       |
| [Glitch](https://glitch.com)      | [![Remix on Glitch](https://cdn.glitch.com/2703baf2-b643-4da7-ab91-7ee2a2d00b5b%2Fremix-button.svg)](https://glitch.com/edit/#!/remix/clone-from-repo?REPO_URL=https://github.com/twilio-labs/sample-template-nodejs.git) |
| [Zeit](https://zeit.co/)          | [![Deploy with ZEIT Now](https://zeit.co/button)](https://zeit.co/new/project?template=https://github.com/twilio-labs/sample-template-nodejs/tree/master)                                                                 |

### Resources

- [GitHub's repository template](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-from-a-template) functionality

### Contributing

This template is open source and welcomes contributions. All contributions are subject to our [Code of Conduct](https://github.com/twilio-labs/.github/blob/master/CODE_OF_CONDUCT.md).

[Visit the project on GitHub](https://github.com/twilio-labs/sample-template-nodejs)

### License

[MIT](http://www.opensource.org/licenses/mit-license.html)

### Disclaimer

No warranty expressed or implied. Software is as is.

© Copyright 2020 Fodé Diop