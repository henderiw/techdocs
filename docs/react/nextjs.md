# next.js

[example code](https://github.com/academind/react-complete-guide-code/tree/23-nextjs-introduction)

## what

- react framework for production (react is a library)
  - bigger than a library
  - clear rules and guidance
  - enhances react, making big react aps easier
  
## key features and benefits

- server side rendering (preparing the page to load)
  - search engine optimization
  - prefetching on the server -> not a flickering experience
  - with react this is complex
  - client side code and service side code is blended together
- file based routing (we give the illusion to have multiple pages)
  - no in code route definition -> uses files and folders
  - less code, less work, highly understandable, how we started
- fullstack capabilities (backend code -> file system, database)
  - store/get data
  - authentication

## creating a new project

```
npx create-next-app

npm run dev
```

## paths

- index.js
- dynamic pages -> [xxxx].js
- linking pages: 
    - <a href=""> -> send to a new page, this is not a single page app, we loose state
    - <Link href=""> -> this combines best of both worlds
      - search engines see the changes
- _app.js: root component
    - single Layout
- imperative navigation: meetupItem.js
  - useRouter
  - push
- useEffect: renders after the first component is loaded
  - page rendering
    - reuest -> /someroute => return pre-rendered page -> good for SEO
  - 2 forms of pre-rendering
    - static generation:
      - page component is pre-rendered when we build the side for production
      - if we know the data changes, we need to rerender
      - npm run build
      - export function getStaticProps() {}
        - prefetches the data
      - Con:
        - data can be outdated -> need to rebuild the site
          - // regenerates the page, 10 is 10 seconds
            // will be re-generated if there are request every 10 sec
            revalidate:10
     - Pro: CDN can serve the data
    - server-side rendering
      - regenerte the page for every incoming request
      -  getServerSideProps
         -  context: get access to incoming request and response
         -  props
      -  We need to wait for the page to be generated on every incoming request
- api routes
  - special routes which dont do html, but define api with put/get/etc
  - in pages folder add api folder (api name is hardcoded)
    - 
- metadata:
  - 

Server-side should be used when
- data changes a lot
- we need access to incoming req/resp e.g. authentication

## npm run build

404 is automatically done
empty dot we are not fetching data
filled dot we are fetching data

## deploy

hosting provider: 
- vercel

use github/gitlab/gitbucket