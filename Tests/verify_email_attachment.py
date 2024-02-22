from mailosaur.models import SearchCriteria
from resources.config import *

my_config = get_config()
# Available in the API tab of a server
mailosaur = get_mailosaur_client(my_config['QA']['api_key'])

criteria = SearchCriteria()
criteria.sent_to = my_config['QA']['email_id']
criteria.subject = 'Sample Email with Attachment'

email = mailosaur.messages.get(my_config['QA']['server_id'], criteria)

first_attachment = email.attachments[0]

print(first_attachment.file_name)
print(first_attachment.content_type)