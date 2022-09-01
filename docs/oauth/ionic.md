Redirect URL on Ionic
Q:

What is the OAuth 2.0 redirect URL for the Ionic app to integrate LinkedIn and Google using the REST API?



A:

Short answer:



You define the redirect URI yourself, as a custom deeplink URL for your own app. It can have a customer scheme or it can be a specific URL. An example of a redirect URI for mobile apps: myapp:///events/3/



Longer answer:



How does the redirect work?

This URL is sent back in the location header to the web browser on the mobile including the HTTP status code 301 for redirect. The browser on the mobile now interprets the location header and resolves the address. MyApp needs to have a custom protocol handler installed on the device, so the browser redirects the request directly to the App on the same mobile device.



How do I define a custom deeplink URL in Ionic?

Deeplinking as a concept has evolved heavily over the last few years, with mobile devices going from supporting custom URL schemes (like instagram://) to now opening native apps in response to navigation to URLs (like amazon.com). Additionally, OS’s now support powerful ways to index and search data inside of native apps.

To help Ionic developers deeplink more easily, we are excited to announce a new, official way to deeplink into both Ionic 1 and Ionic 2 apps (and non-ionic Cordova apps): the Ionic Deeplinks Plugin along with Ionic Native1.3.0. Let’s take a look at how it works:



Choosing a Deeplink



The first thing we need to do is figure out what kind of deeplink we want our app to respond to. Let’s say we run a Hat Shop and we have a website version of our store where we display our many fancy Hats. A URL to one of those Hats might look like https://myapp.com/events.

We can actually launch our app when someone navigates to this URL on Android or iOS and display the app version of the Hat product page. Additionally, let’s say we want to enable a custom URL scheme of the form myapp://events.

Now that we have our URL scheme, website, and deeplinking path decided, let’s install the Deeplinks Plugin.



Installing Ionic Deeplinks



The Ionic Deeplinks plugin requires some variables in order to get set up properly:

cordova plugin add ionic-plugin-deeplinks --variable URL_SCHEME=myapp --variable DEEPLINK_SCHEME=https --variable DEEPLINK_HOST=myapp.com

In the install command, we provide the custom URL scheme we want to handle (myapp), the host domain we will respond to (myapp.com) and the host protocol we will listen for, which 99% of the time will be httpsas it’s required on iOS and Android.

We’re almost ready to handle deeplinks, we just need to configure Universal Links on iOS and App Links on Android 6.0 so our app can open when navigating to ionic-hats.com.



Configuring Universal Links (iOS) and App Links (Android)



To configure iOS and Android, we need to enable Universal Links for iOS, and App Links for Android (6.0+). This process is primarily done on the server side of your website. You’ll publish a specific json file for iOS and one for Android, ensure your site is using HTTPS, and then configure your app to open in response to links to that domain.



For Android, it pretty much just works from the plugin install above.



However, for iOS, you’ll then enable the domain in the Associated Domains section of your entitlements, with the form applinks:yourdomain.com.