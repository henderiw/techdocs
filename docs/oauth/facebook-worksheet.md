https://developers.facebook.com/docs/facebook-login/manually-build-a-login-flow/



Prerequisites:

Facebook Account

curl



---

Client Registration:



https://developers.facebook.com/



create an app and add the Facebook Login product, set valid OAuth redirect URIs in the settings of the product,

needs to be an exact match, watch out for trailing slashes etc. (e.g.: https://api-university.com/ != https://api-university.com)



your redirect URI needs to have a slash in the end, otherwise Facebook adds one!



What you need:

appId = clientId =

appSecret = clientSecret =

redirectURI =

URLENCODE(redirectURI) =







---

Authorization Endpoint (Browser):



https://www.facebook.com/v6.0/dialog/oauth?client_id=clientId&redirect_uri=URLENCODE(redirectURI)&state=987654321



What you need to extract from the response:

code =



---

Token Endpoint:



non-standard: it is a GET instead of a POST



curl -ik "https://graph.facebook.com/v6.0/oauth/access_token?redirect_uri=URLENCODE(redirectURI)&client_id=clientId&client_secret=clientSecret&code=code"



What you need from the response:

access_token =



---

Resource Access:



curl -H "Accept: application/json" -H "Authorization: Bearer access_token" "https://graph.facebook.com/me"



What you need from the response:

name =