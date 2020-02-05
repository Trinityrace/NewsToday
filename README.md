# NEWS TODAY
[![codebeat badge](https://codebeat.co/badges/985570b0-3819-426f-a080-fe95135784ca)](https://codebeat.co/projects/github-com-trinityrace-newstoday-master)


## Author
[TRINITY](https://github.com/Trinityrace/newstoday)

## Versioning
NewsToday version 1.0, Future releases should have the following features:

- Ability to search news.
- Ability to star favorite specific articles.
- be responsive

### Description
- This is a simple application which lists and previews news articles from various sources using the News API, made by python web framework, Flask.

### Features
Here are the features in summary:
```
- A minimalistic landing page showing trending world news and a variety of news sources
- Clickable news sources which direct the user to a page with article highlights from the particular source.
```
### Behaviour Driven Development (BDD)
- Behaviour
```
* Page loads, user arrives in the landing page, is greeted to a list of all available news sources.
- input
* The user can click on any particular list group item to be directed to a separate page containing news highlights curated by the same publisher.
- output
* On clicking the "read more" button, the user is redirected to the main article to read the full article.
```

### Requirements
- This program requires python3.+ (and pip) installed.
- Use package manager [pip](https://pip.pypa.io/en/stable/)
- Once python is installed, install the folowing external libraries provided in the requirements.txt file using pip
Example:
```
- pip install flask
```

### Installation and Set-up
To view the app, open the live site link provided below on the README. Here is a run through of how to set up the application:
```
Step 1 : Clone this repository using git clone https://github.com/Trinityrace/NewsToday.git, or downloading a ZIP file of the code.
Step 2 : The repository, if downloaded as a .zip file will need to be extracted to your preferred location and opened
Step 3 : Go to the project root directory and install the virtualenv library using pip an afterwards create a virtual environment. 
```
Run the following commands respectively:
```
- pip install virtualenv
- virtualenv venv
- source venv/bin/activate
```
Note that you can exit the virtual environment by running the command deactivate
```
Step 4 : Download the all dependencies in the requirements.txt using pip install <name>
Step 5 : Go to the news API WEBSITE, sign up for a free account and generate an API key.
Create a file in your root directory called start.sh and store the API key like so export API_KEY="<your-key>"
On the same file write down the command python3 manage.py server
Step 6 : On your terminal, run the following command, chmod a+x start.sh
```
You can now launch the application locally by running the command ./start.sh
Open your preferred browser and view the app by opening the link http://127.0.0.1:5000/.

### Known Bugs
cannot redirect to the sources links to the specific links

### Technologies Used
- Python 3.7.4
-HTML
-CSS

#### Support and contact details
You can contact me for feedback or raise any issues/ bugs through the following email:

[trinityrtime@gmail.com]

## License
### MIT License

#### Copyright (c) [2020] [TRINITY]
[MIT](https://choosealicense.com/licenses/mit/)