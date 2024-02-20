# github labels

[info](https://dev.to/optnc/manage-github-milestones-from-cli-2hkh)

OWNER=iptecharch 
REPO=config-server

gh repo label create --repo $OWNER/$REPO --name bug --color F29513

gh issue create -R $OWNER/$REPO -m MS5 -t "Milestone5" -b "Milestone5"

## list milestone

gh api \
  -H "Accept: application/vnd.github.v3+json" \
  /repos/sdcio/config-server/milestones

## create milestone

gh api \
  --method POST \
  -H "Accept: application/vnd.github.v3+json" \
  /repos/$OWNER/$REPO/milestones \
  -f title='MS7' \
  -f state='open' \
  -f description='Milestone7' \
  -f due_on='2024-02-25T08:00:00Z'

gh api \
  --method DELETE \
  -H "Accept: application/vnd.github.v3+json" \
  /repos/$OWNER/$REPO/milestones/7


repos="schema-server data-server cache docs sdctl integration-tests"
for repo in $repos
do
  echo $repo
  gh api \
      --method POST \
      -H "Accept: application/vnd.github+json" \
      -H "X-GitHub-Api-Version: 2022-11-28" \
      /repos/iptecharch/$repo/milestones \
      -f title='MS5' \
      -f state='open' \
      -f due_on='2024-02-11T08:00:00Z'
done

repos=("schema-server" "data-server" "cache" "docs" "sdctl" "integration-tests" "config-server" "sdc-protos" "yang-parser")
for repo in "${repos[@]}"
do
  echo $repo
  gh api \
      --method POST \
      -H "Accept: application/vnd.github+json" \
      -H "X-GitHub-Api-Version: 2022-11-28" \
      /repos/sdcio/$repo/milestones \
      -f title='MS5' \
      -f state='open' \
      -f due_on='2024-02-25T08:00:00Z'
done