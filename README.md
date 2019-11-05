# Tg-2-sheets
This simple python script fetches target groups (from elbv2 AWS API) and dumps it to google spreadsheets. You only need to provide the spreadsheet URL as input and you are good to go!

NOTE: I have built this using python v3.6. In case you are using an older version of python and run into issues, do let me know!

How to use:

1. Clone the repo.
    git clone 
2. Create a new google project, enable sheets API and generate credentials (it will be a json file) as follows:

    ![Sheets API creds](https://s3.amazonaws.com/com.twilio.prod.twilio-docs/original_images/google-developer-console.gif)
3. Run the script as follows:
      ```
      python refreshTG.py
      ```
4. Provide the spreadsheets URL, would look something like this:
                `https://docs.google.com/spreadsheets/d/<spreadsheet_ID>/edit#gid=xxxxxxxx`
                
5. And you are done!

Thanks.
