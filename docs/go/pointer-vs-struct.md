# overview

- pointer
allows the function to modify the content

- struct
the go library provides a copy of the struct under the hood
- this is done to protect the content to be changed
if we dont want the fn to modify the content we can also
provide a copy ourselves and still provide a pointer
-> this gives more control to the code and does not rely on under the hood operations -> which can trigger the go garbage collector