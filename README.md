# my-first-app
in class practice of creating own repository

## Setup

Create and activate a virtual environment:

```sh
conda create -n my-first-env python=3.10

conda activate my-first-env
```

# Run the script
python app/my_script.py


# run the unemployment report
``` sh
python app/unemployment.py
```



# install packages
```sh
pip install -r requirements.txt
```


Obtain an [API Key from Alphavantage](https://www.alphavantage.co/support/#api-key) or from the prof (`ALPHAVANTAGE_API_KEY`).

Create a ".env" file and paste in the following contents:

```sh
# this is the ".env" file...

ALPHAVANTAGE_API_KEY="_________"
```

Obtain an API KEY from sendgrid. To create an account, veryify your accoutn,setup a single sender, and obtain an API Key



```sh

SENDGRID_API_KEY="_______"
SENDER_ADDRESS="TODO"

```




SEND AN EXAMPLE EMAIL:

```sh
python app/email_service.py

```