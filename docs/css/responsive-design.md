# responive design

which tools do we have?
- viewport metatag (html)
  - adjust the site to the device viewport
  - actual pixels will not work on mobile devices -> we need to add the device width and the pixel ratio is required (## HW vs SW/CSS pixels)
    - [mydevice.io](https://mydevice.io)
  - No design changes
- media queries (css)
  - change design depending on size (like width)


## viewport metatag

```
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
```

- name attribute -> viewport
- content attribute -> use the width of the device -> apply the pixel ratio of the device
- initial scale -> defines the zoom level
  - 1.0: no zoom
  - 1.5: zoom
- user-scalable = yes/no => allows zooming
- maximum-scale = 2.0 -> max scale level
- minimum-cale = 1.2 -> restricts zoomin out

## media queries

condition to change properties of your choice

- media query is like an if statement
- mobile first -> all the code is mobile design based -> in media query is for large devices
  - mobile first: @media (min-width: 40rem)
  - desktop first: @media (max-width: 40rem)
- multiple media queries -. order is important so make sure the selctor is not overriding eachother
- add the media queries at the end of the css code

How do we know the breaking points?
- mydevice.io

- landscape mode

and operation

```
@media (min-width: 40rem) and (orientation: landscape) {}
```

or operation

```
@media (min-width: 40rem), (orientation: landscape) {}
```

info:

[lengths](https://www.w3.org/TR/css-values-3/#absolute-lengths)
[pixel ratio](https://bjango.com/articles/min-device-pixel-ratio/)
[media query](https://developer.mozilla.org/en-US/docs/Web/CSS/Media_Queries)
[apply media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Media_Queries/Using_media_queries)