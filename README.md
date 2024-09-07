# MS Teams Automation with Selenium & LLaMA3 API Integration
## Project Overview
This project automates the login process for Microsoft Teams using Selenium and handles unread chats by navigating through the web page's HTML content. Additionally, it integrates with an API that utilizes the LLaMA3 model for generating responses to user input.

## Features
Automates login to MS Teams using username and password.
Retrieves unread chat messages by parsing the HTML content.
Sends messages to the LLaMA3 model via an API to generate responses.
## Technologies Used
### Python: Main programming language.
### Selenium: For web automation and interaction with Microsoft Teams.
### WebDriverManager: Automatically manages the Chrome WebDriver.
### Requests: To send API requests to the LLaMA3 model.
### JSON: To handle API payloads and responses.
## Installation
### Clone the repository:
```
bash
git clone https://github.com/yourusername/your-repo-name.git
```
### Install the required Python packages:

```
bash
pip install -r requirements.txt
```
### Set your MS Teams credentials:

Replace YOUR_TEAMS_USER_NAME/EMAIL and your_password in the code with your Microsoft Teams login credentials.
### Configure the LLaMA3 API:

Replace the API URL and any other required parameters.
Usage
Run the script to automate MS Teams login and retrieve unread chat messages:

```
bash
python ms_teams_automation.py
```

## The program will:

Open Chrome and log into MS Teams.
Parse the HTML to identify unread chats.
Interact with the LLaMA3 API to generate and display a response.
## License
This project is licensed under the MIT License.
