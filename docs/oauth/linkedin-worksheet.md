How to call a LinkedIn API

and get a Linkedin OAuth Access Token

---



Prerequisites:

LinkedIn Account

curl



---

Client Registration



go to:

https://www.linkedin.com/developers/apps



click on "create new" or use this direct link:

https://www.linkedin.com/developers/apps/new



What you need:



redirectURI =

URLENCODE(redirectURI) =

clientId =

clientSecret =





---

Authorization Endpoint (Browser)



What you need:

scope = r_liteprofile



https://www.linkedin.com/oauth/v2/authorization?response_type=code&state=987654321&scope=scope&client_id=clientId&redirect_uri=URLENCODE(redirectURI)





What you need from the response:

code =



---

Token Endpoint:



curl -ik -X POST https://www.linkedin.com/oauth/v2/accessToken \

-d grant_type=authorization_code \

-d code=code \

-d redirect_uri=URLENCODE(redirectURI) \

-d client_id=clientId \

-d client_secret=clientSecret



What you need from the response:

access_token =



---

Resource Access:



curl https://api.linkedin.com/v2/me -H "Authorization: Bearer access_token"



What you need from the response:

firstname =



---------



Documentation



https://docs.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow

We are on API v2

Upgrade notice from v1 to v2: https://developer.linkedin.com/blog/posts/2018/redirecting-oauth-uas

