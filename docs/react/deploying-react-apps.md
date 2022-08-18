# react app deployments

section 21

## steps

- test
- optimize
  - react.Memo
  - Lazy loading: load chunks of the code only when it is needed
    - only when it needed
- build app for production
- upload to production code
- configure server

## lazy loading

see example section 20 (react-router)
used in conjunction with react router

import React, Suspense

## building the code code for production

package.json

```
npm run build
```

move to the build folder

## deploy on a server

upload to a production server
- a react SPA is a Static Website: only html, css, js (client side brower based)

NO node.js/PHP/etc

firebase login
firebase init

-> use build
-> configure as a single page app -> rewite to index.html

firebase deploy

firebase hosting:disable

## client-side routing or server side routing

