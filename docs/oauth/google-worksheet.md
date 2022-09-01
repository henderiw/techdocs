Documentation:

https://developers.google.com/accounts/docs/OAuth2

https://developers.google.com/oauthplayground/



Prerequisites:

Google Account
curl




Registration:

https://console.developers.google.com

What you need from registration:

redirectURI =
URLENCODE(redirectURI) =
clientId =
clientSecret =




Authorization Endpoint (Browser):

https://accounts.google.com/o/oauth2/auth?redirect...URLENCODE(redirectURI)&response_type=code&client_id=clientId&scope=https%3A%2F%2Fmail.google.com%2F&approval_prompt=force

What you need:

code =




Token Endpoint:

curl -X POST -H "content-type: application/x-www-form-urlencoded" -d "grant_type=authorization_code&code=code&redirect_uri=URLENCODE(redirectURI)&client_id=clientId&client_secret=clientSecret" "https://accounts.google.com/o/oauth2/token"

What you need:

access_token =




Resource Access:

curl -H "Authorization: Bearer access_token" "https://www.googleapis.com/gmail/v1/users/eMailAddress/messages"

