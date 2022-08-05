# ui-cli 

## link cluster

- git url
- branch
- directory
- personal access token

## add blueprint

```
kpt pkg init basens
```

## add resource

```
kpt pkg tree
kpt fn eval
kpt fn render
```

## publish

```
git push origin main
git tag <tag> && git push origin <tag>
```

## link blueprint repo to deployment repo

```
kpt pkg get <repo> backend --for-deployment
```

## commit the change in the deployment repo

```
git add backend && git commit -m ""
git push origin main
git tag <tag> && git push origin <tag>
```

## sync

```
kpt live init backend
kpt live apply backend
```