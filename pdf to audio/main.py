import boto3
from pypdf import PdfReader

# Open pdf file and read
with open('yourfile.pdf', 'rb') as file:
    reader = PdfReader(file)
    # Loops file of how many pages to be converted/Extract text to strings
    number_of_pages = len(reader.pages)
    text = ""
    for i in range(number_of_pages):
        page = reader.pages[i]
        string = page.extract_text()
        text += string
    print(text)

# Create your own account on AWS and get access_key_id and secret_access_key(create IAM user)
polly_client = boto3.Session(
    aws_access_key_id='your access_key_id',
    aws_secret_access_key='your secret_access_key',
    region_name='us-west-2',).client('polly')


response = polly_client.synthesize_speech(
    Text=text, OutputFormat='mp3',
    VoiceId='Joanna'
)

# Creating Audio Output File
with open('outputname.mp3', 'wb') as f:
    f.write(response['AudioStream'].read())
