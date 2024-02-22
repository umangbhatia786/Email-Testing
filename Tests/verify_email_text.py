from mailosaur.models import SearchCriteria
from resources.config import *

my_config = get_config()
# Available in the API tab of a server
mailosaur = get_mailosaur_client(my_config['QA']['api_key'])

criteria = SearchCriteria()
criteria.sent_to = my_config['QA']['email_id']
criteria.subject = my_config['QA']['sent_email_subject']

email = mailosaur.messages.get(my_config['QA']['server_id'], criteria)

text_to_test = 'XYZ'
contains_text = text_to_test in email.text.body

assert contains_text == True, f'{text_to_test} keyword is missing from the email'
