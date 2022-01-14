Termy : Your Terminal Assistant
=========
A lightweight terminal assistant to give a natural language interface to your terminal commands. It allows you to authenticate and connect to a google sheet that has all the frequently used commands and their natural language queries. This way all the members of the organisation can connect to this central repository and easily manage the configured commands. Termy also has a interface with [GPT-3](https://openai.com/blog/openai-api/) from OpenAI.



How to install
============
Thanks to pip! its as simple as :

```
pip install --upgrade pip
pip install termy
```


How to Use Termy
=============

### Step 1: Configure Termy
```termy --configure```

You will be asked to give the link of the google sheet containing the commands and queries. After that it will authenticate with your google account to access the sheet in case it is a protected file. [This](https://docs.google.com/spreadsheets/d/1-wtkODsgt0EJzARAo7BBNOXwkd1W3vDiPH1HZoyskXI/edit?usp=sharing) is a sample sheet for reference, follow the same format while you create your google sheet.

>Note: If your google sheet already has the sharing settings set to allow view access for anyone on the internet, termy would not ask for google authentication since it is not required. 

### Step 2: Search commands using Termy
```temry <search query>```

For eg: \
`termy check the logs of service x` \
`termy is service abc up?` \
`termy shutdown in 5 mins` \
`termy sort files by their sizes`


### Step 3: Update data from google sheet
```termy --update``` \
This will sync the contents of the google sheet in your local system. Execute this when you make changes to your google sheet.


Termy GPT-3 Integration
=============

Termy has a feature to connect with GPT-3 API. Using GPT-3, you can convert any natural language query into a terminal command. For this feature, you would need to sign up for the GPT-3 API KEY. Sign up [here](https://beta.openai.com/signup) for getting a free API Key.  

Usage: 
```termy --gpt3 <query>```

For eg: 
`termy --gpt3 find files which are bigger than 50MB in my home folder`

would trigger the command. 
`find ~/ -size +50M`


Contribute and Make it better
=============

Any form of contribution is welcome. From finding and reporting bugs to giving feedback to suggesting cool features to building out cool features. Check out [CONTRIBUTING.md](https://github.com/dingusagar/termy/blob/master/CONTRIBUTING.md) for more details. 
