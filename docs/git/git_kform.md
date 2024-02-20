# git kform

a package is a branch and the name of the package = packagePath in the directory of the repo

e.g. 
infra/pkg1 -> packageName == packagePath == branch
tag: infra/pkg1/v1, infra/pkg1/v2

```s
# create branch -> create local workspace/scratchpath
git checkout -b infra/pkg1

# local commit
git commit -m "branch: infra/pkg1 initial commit"

# push branch remote
git push --set-upstream origin infra/pkg1

# tag a branch
git tag -a infra/pkg1/v1 -m "initial revisions" infra/pkg1

git push origin --tags