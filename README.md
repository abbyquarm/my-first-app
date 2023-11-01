# my-first-app
in class practice of creating own repository

## Setup

Create and activate a virtual environment:

```sh
conda create -n my-first-env python=3.10

conda activate my-first-env
```

# install packages
# packages listed in the requirement text file
```sh
pip install -r requirements.txt
```

# Run the my script
python app/my_script.py

# run the unemployment report (usage comand)
``` sh
python -m app.unemployment
```


# Run the email service code

# Setup instructions
Obtain an [API Key from Alphavantage](https://www.alphavantage.co/support/#api-key) or from the prof (`ALPHAVANTAGE_API_KEY`).
Obtain an API KEY from sendgrid. To create an account, veryify your accoutn,setup a single sender, and obtain an API Key

# Create a ".env" file and paste in the following contents:
# These are my api KEYS

```sh
# this is the ".env" file...

ALPHAVANTAGE_API_KEY="_________"
```

```sh

SENDGRID_API_KEY="_______"
SENDER_ADDRESS="TODO"

```

SEND AN EXAMPLE EMAIL:

```sh
python app/email_service.py

```