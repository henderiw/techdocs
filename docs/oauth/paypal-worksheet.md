Documentation:

https://developer.paypal.com/docs/integration/direct/paypal-oauth2/

https://developer.paypal.com/docs/integration/direct/make-your-first-call/

also: playground: https://devtools-paypal.com/guide/pay_paypal



Prerequisites:

Paypal Account
curl



Client Registration:

https://developer.paypal.com/developer/applications/create

What you need from registration:

clientId =
clientSecret =



Token Endpoint:

paypal uses client credentials

curl -ik https://api.sandbox.paypal.com/v1/oauth2/token \

-H "Accept: application/json" \

-H "Accept-Language: en_US" \

-u “clientId:clientSecret" \

-d "grant_type=client_credentials"



What you need:

access_token =




Resource Access:

curl -v https://api.sandbox.paypal.com/v1/payments/payment \

-H 'Content-Type: application/json' \

-H 'Authorization: Bearer access_token' \

-d '{
"intent":"sale",

"redirect_urls":{

"return_url":"http://example.com/your_redirect_url.html",

"cancel_url":"http://example.com/your_cancel_url.html"

},

"payer":{

"payment_method":"paypal"

},

"transactions":[

{

"amount":{

"total":"7.47",

"currency":"USD"

}

}

]