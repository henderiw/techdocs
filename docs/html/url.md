# url

URI: Uniform resource indicator -> used to identify anything

URN: 
- Uniform resource name -> provide only a unique name, without a means of locating or retrieving the resource or information about it
- anologoues to a name
- example: book: ISBN 0-486-27557-4  -> urn:isbn:0-486-27557-4 -> no info where to fins it

URL: Uniform resource locators 
- provide a means of locating and retrieving information resources on a network (file system or internet)
- analogous to a street
- example: http://example.org/wiki/Main_Page
    - resource identifier: /wiki.Main_Page
    - representation is obtainable via http
    - network host: example.org

[url rfc](https://www.rfc-editor.org/rfc/rfc3986.html)

[scheme:][//[userinfo@]host][/]path[?query][#fragment]


components:
- scheme (mandatory): http/https/mailto/file/...
    - [iana scheme registry](https://www.iana.org/assignments/uri-schemes/uri-schemes.xhtml)
- authority (optional):
    - authority = [userinfo "@"] host [":" port]
    - userinfo (optional)-> username:password
    - host (mandatory): e.g. google.com
    - port (optional)
- path (mandatory):
    - path Sections: how many "/ are in a path -> /a/b/c -> 3
    - path Segments: a,b,c /a/b/c
    - sequence of path segments separated by a slash (/)
    - path segment can have only 1 : or * -> wildcard
    - in http/https:
        - last part of the path is pathinfo (optional)
- query (optional):
    - proceeded by ?
    - delimiter can be: ; or &
    e.g. 
        - key1=value1&key2=value2
        - key1=value1;key2=value2
- fragment (optional):
    - proceeded by #
    - fragment identifier providing direction to a secondary resource (e.g. section heading)
    - 


-> url decoding
rawPath is there to indicate an escape with a / so there is a distinction between a path with / or one using an escape path

url.Path: /dog/cat?key=value
url.RawPath: /dog%2Fcat%3Fkey=value

if there is no escape char for the / the url.RawPath is not set


## Query parameter example

https://example.com/search?q=keyword&page=1

In this URL, the "q" parameter is set to the value "keyword", indicating a search query. The "page" parameter is set to "1", indicating the first page of results.

## Path parameters:

https://example.com/users/1234

In this URL, the "1234" parameter is a path parameter that identifies a specific user's profile.

https://example.com/products/category1/subcategory2/item3

## fragment parameters

https://example.com/page#section2

In this URL, the "section2" parameter is a fragment parameter that points to a specific section of the page.

## matrix parameters

https://example.com/files;type=image/png;size=100x100/foo.png

In this URL, the "type" parameter is set to "image/png" and the "size" parameter is set to "100x100". These are matrix parameters that describe the file "foo.png".

Note that there are many different ways to structure URLs and include parameters, and different frameworks and systems may use different conventions. These are just a few examples to give you an idea of the different types of parameters that can be included in a URL.