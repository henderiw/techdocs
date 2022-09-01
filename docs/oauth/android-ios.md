Q:

What is the use of the redirect uri for a mobile application needing a token? The mobile is not reachable by URL.



A:

The redirect URI for mobile apps typically has a custom protocol.

An example of a redirect URI for mobile apps: myapp:///events/3/

This URL is sent back in the location header to the web browser on the mobile including the HTTP status code 301 for redirect. The browser on the mobile now interprets the location header and resolves the address. MyApp needs to have a custom protocol handler installed on the device, so the browser redirects the request directly to the App on the same mobile device.



If you want to get into detail on how to install custom protocol handlers on iOS or Android, read the following:





-----------

Android

-----------



For Android, refer to Intent Filter to Launch My Activity when custom URI is clicked.



You use an intent-filter:



<intent-filter>

  <action android:name="android.intent.action.VIEW" /> 

  <category android:name="android.intent.category.DEFAULT" /> 

  <category android:name="android.intent.category.BROWSABLE" /> 

  <data android:scheme="myapp" /> 

</intent-filter>



This is attached to the Activity that you want launched. For example:



<activity android:name="com.MyCompany.MyApp.MainActivity" android:label="@string/app_name">

  <intent-filter>

      <action android:name="android.intent.action.MAIN" />

      <category android:name="android.intent.category.LAUNCHER" />

  </intent-filter>

  <intent-filter>

      <action android:name="android.intent.action.VIEW" />

      <category android:name="android.intent.category.DEFAULT" />

      <category android:name="android.intent.category.BROWSABLE" /> 

      <data android:scheme="myapp" android:host="com.MyCompany.MyApp" />

  </intent-filter>

</activity>



Then, in your activity, if not running, the activity will be launched with the URI passed in the Intent.



Intent intent = getIntent();

Uri openUri = intent.getData();



If already running, onNewIntent() will be called in your activity, again with the URI in the intent.



Lastly, if you instead want to handle the custom protocol in UIWebView's hosted within your native app, you can use:



myWebView.setWebViewClient(new WebViewClient()

{

 public Boolean shouldOverrideUrlLoading(WebView view, String url)

 {

  // inspect the url for your protocol

 }

});







-----------

iOS

-----------





For iOS, define your URL scheme via Info.plist keys similar to:



<key>CFBundleURLTypes</key>

    <array>

        <dict>

            <key>CFBundleURLName</key>

            <string>com.yourcompany.myapp</string>

        </dict>

        <dict>

            <key>CFBundleURLSchemes</key>

            <array>

                <string>myapp</string>

            </array>

        </dict>

    </array>

Then define a handler function to get called in your app delegate



- (BOOL)application:(UIApplication *)application openURL:(NSURL *)url sourceApplication:(NSString *)sourceApplication annotation:(id)annotation

{

 // parse and validate the URL

}



If you want to handle the custom protocol in UIWebViews hosted within your native app, you can use the UIWebViewDelegate method:



- (BOOL)webView:(UIWebView *)webView shouldStartLoadWithRequest:(NSURLRequest *)request navigationType:(UIWebViewNavigationType)navigationType

{

 NSURL *urlPath = [request URL];

 if (navigationType == UIWebViewNavigationTypeLinkClicked)

 {

    // inspect the [URL scheme], validate

    if ([[urlPath scheme] hasPrefix:@"myapp"]) 

    {

      ...

    }

  }

}

}



For WKWebView (iOS8+), you can instead use a WKNavigationDelegate and this method:



- (void)webView:(WKWebView *)webView decidePolicyForNavigationAction:(WKNavigationAction *)navigationAction decisionHandler:(void (^)(WKNavigationActionPolicy))decisionHandler

{

 NSURL *urlPath = navigationAction.request.URL;  

 if (navigationAction.navigationType == WKNavigationTypeLinkActivated)

 {

   // inspect the [URL scheme], validate

   if ([[urlPath scheme] hasPrefix:@"myapp"])

   {

    // ... handle the request

    decisionHandler(WKNavigationActionPolicyCancel);

    return;

   }

 }



 //Pass back to the decision handler

 decisionHandler(WKNavigationActionPolicyAllow);

}