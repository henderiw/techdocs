## kpt example

```
gh auth login

gh repo create blueprint --public
gh repo create deployment --public

GITHUB_USER=henderiw
BLUEPRINT_REPO=git@github.com:${GITHUB_USER}/blueprint.git
DEPLOYMENT_REPO=git@github.com:${GITHUB_USER}/deployment.git

git clone $(BLUEPRINT_REPO)
git clone $(DEPLOYMENT_REPO)
```