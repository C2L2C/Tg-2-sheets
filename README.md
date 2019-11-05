# Tg-2-sheets
This simple python script fetches target groups (from elbv2 AWS API) and dumps it to google spreadsheets. You only need to provide the spreadsheet URL as input and you are good to go!

NOTE: I have built this using python v3.6. In case you are using an older version of python and run into issues, do let me know!

How to use:

1. Clone the repo.
    `git clone https://github.com/C2L2C/Tg-2-sheets.git`
2. Create a new google project, enable sheets API and generate credentials (credentials.json) as follows:

    ![Sheets API creds](https://s3.amazonaws.com/com.twilio.prod.twilio-docs/original_images/google-developer-console.gif)
    
    source: [Google Spreadsheets and Python- Twilio
](https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html)

3. Create a new google spreadsheet and share it with the email mentioned in the `client_email` field in `credentials.json`  
   generated from step 2.

3. Run the script as follows:
      ```
      python refreshTG.py
      ```
4. Provide the spreadsheets URL, would look something like this:
                `https://docs.google.com/spreadsheets/d/<spreadsheet_ID>/edit#gid=xxxxxxxx`

5. Provide the spreadsheet name.

6. And you are done!

Thanks.
