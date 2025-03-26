import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Authenticate and create a client to interact with Google Sheets
def authenticate_google_sheets():
    # Set up the scope and credentials
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    client = gspread.authorize(creds)
    return client

# List all spreadsheets in your Google Drive
def list_spreadsheets():
    client = authenticate_google_sheets()
    spreadsheets = client.openall()  # Fetch all the spreadsheets

    # Print the titles of all spreadsheets
    if spreadsheets:
        print("List of all spreadsheets:")
        for sheet in spreadsheets:
            print(sheet.title)
    else:
        print("No spreadsheets found.")

if __name__ == '__main__':
    list_spreadsheets()
