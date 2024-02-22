from mailosaur import MailosaurClient
from mailosaur.models import SearchCriteria
from resources.config import *
from bs4 import BeautifulSoup
import requests

my_config = get_config()
# Available in the API tab of a server
mailosaur = get_mailosaur_client(my_config['QA']['api_key'])

criteria = SearchCriteria()
criteria.sent_to = my_config['QA']['email_id']
criteria.subject = my_config['QA']['sent_email_subject']

email = mailosaur.messages.get(my_config['QA']['server_id'], criteria)


# Function to verify links
def verify_links_in_email(my_email):
    html_content = email.html.body

    # Extract links from HTML content
    links = extract_links(html_content)

    # Verify each link
    for link in links:
        print(f'Pinging {link}')
        response = requests.head(link)
        assert response.status_code == 200, f'Link {link} is invalid with status code {response.status_code}'


# Function to extract links from HTML content
def extract_links(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    links = [a['href'] for a in soup.find_all('a', href=True)]
    return links


verify_links_in_email(email)
