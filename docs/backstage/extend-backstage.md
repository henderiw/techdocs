# backstage

## portgres

```
brew install PostgreSQL
```

login

```
psql postgres
```

```
\du
```

```
ALTER USER postgres PASSWORD 'secret';
```

[postgres info on mac](https://www.codementor.io/@engineerapart/getting-started-with-postgresql-on-mac-osx-are8jcopb)

## add postgres to the 

```
yarn add --cwd packages/backend pg
```

edit app-config.yaml

```
backend:
  database:
-    client: better-sqlite3
-    connection: ':memory:'
+    # config options: https://node-postgres.com/api/client
+    client: pg
+    connection:
+      host: ${POSTGRES_HOST}
+      port: ${POSTGRES_PORT}
+      user: ${POSTGRES_USER}
+      password: ${POSTGRES_PASSWORD}
+      # https://node-postgres.com/features/ssl
+      #ssl: require # see https://www.postgresql.org/docs/current/libpq-ssl.html Table 33.1. SSL Mode Descriptions (e.g. require)
+        #ca: # if you have a CA file and want to verify it you can uncomment this section
+        #$file: <file-path>/ca/server.crt
```

```
export POSTGRES_HOST=127.0.0.1
export POSTGRES_PORT=5432
export POSTGRES_USER=henderiw
export POSTGRES_PASSWORD=
```

## github

```
export GITHUB_CLIENT_ID=
export GITHUB_CLIENT_SECRET=

```

```
export GITHUB_PA_TOKEN=
```