from google_auth_oauthlib.flow import InstalledAppFlow

# This is the scope for sending email with Gmail API
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def main():
    flow = InstalledAppFlow.from_client_secrets_file(
        'client_secret.json', SCOPES)

    creds = flow.run_local_server(port=0)

    print("\n✅ COPY THESE VALUES INTO YOUR .env FILE:")
    print("GMAIL_CLIENT_ID =", creds.client_id)
    print("GMAIL_CLIENT_SECRET =", creds.client_secret)
    print("GMAIL_REFRESH_TOKEN =", creds.refresh_token)

if __name__ == '__main__':
    main()
