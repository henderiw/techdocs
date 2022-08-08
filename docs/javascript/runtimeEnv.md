# javascript runtime environment

- browser
- node

## browser example

frontend access to:
- browser

```
<!-- my_website.html -->
<html>
  <body>
    <h1> My Website </h1>
    <script> window.alert('Hello World'); </script>
  </body>
</html>
```

## node example

backend access to:
- file system
- databases
- networks attached to the server.
- etc

file my-app.js
```
console.log(process.env.PWD);
```

```
node my-app.js
```

result

```
/path/to/working/directory
```