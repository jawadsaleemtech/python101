import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Authenticate and create a client to interact with the Google Sheets API
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)

# Create a new spreadsheet
spreadsheet = client.create("Python Learning Path v3")
# Create the spreadsheet and print its URL
spreadsheet = client.create("Python Learning Path")
print(f"Spreadsheet created with ID: {spreadsheet.id}")
print(f"View the spreadsheet at: https://docs.google.com/spreadsheets/d/{spreadsheet.id}")

# Open the first sheet (default sheet when creating a new spreadsheet)
worksheet = spreadsheet.get_worksheet(0)

# Now update the cell A1 with the value 'Phase'
worksheet.update('A1', [['Phase']])  # Correct format

print("Update successful!")
spreadsheet.share('jawadsalim12@gmail.com', perm_type='user', role='writer')