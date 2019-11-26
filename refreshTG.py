#!/usr/bin/env python
import json
import gspread
import boto3
import validators
import csv
import re
from googleapiclient.discovery import build
from oauth2client.client import SignedJwtAssertionCredentials

spreadsheet_url = input("Enter the google spreadsheet ID (you can get it from the sheet URL or paste the URL here, we will extract it out): ") 

#Validate the spreadsheet URL
url_validation_result=validators.url(spreadsheet_url)
url_string=str(spreadsheet_url)

if (url_validation_result):
     spreadsheet_id= re.findall(r"/spreadsheets/d/([a-zA-Z0-9-_]+)", url_string)[0]
     print(spreadsheet_id)
else:
    print('Please enter a valid URL! It should be of the following format: https://docs.google.com/spreadsheets/d/<id>/edit#gid=0 ')
    quit()

spreadsheet_name = input("Enter the spreadsheet name:")

#Initialize the elbv2 method
elbv2 = boto3.client('elbv2')

#Fetch target group info from AWS
response = elbv2.describe_target_groups(
    TargetGroupArns=[]
    )

json_key = json.load(open('credentials.json')) 
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

# get email and key from creds
credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope) 

# authenticate with Google
file = gspread.authorize(credentials) 

#Initialize the list
TGList=[]        

for TG in response["TargetGroups"]: 
       TGList.append([TG['TargetGroupName'],TG['Port']])

TGList.sort(key=lambda elem:elem[1])

service = build('sheets', 'v4', credentials=credentials)

#Clear all the previous values from the sheet
rangeRemoval = '{0}!A2:Z'.format(spreadsheet_name)
body = {}
resultClear = service.spreadsheets( ).values( ).clear( spreadsheetId=spreadsheet_id, range=rangeRemoval,
                                                        body=body ).execute( )

# #Add the updated values
rangeAddition = "A1:B1"
resource = {
   "majorDimension": "ROWS",
   "values": TGList
}

service.spreadsheets().values().append(
   spreadsheetId=spreadsheet_id,
   range=rangeAddition,
   body=resource,
   valueInputOption="USER_ENTERED"
).execute()
