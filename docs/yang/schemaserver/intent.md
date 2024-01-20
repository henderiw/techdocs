# intent

cache:
- config datastore
- intent datastore


data-server:
- builds the candidates based on intent


intent operation/steps:
1. prune original data from the intent
    -> expand keys; if there is another intent that owns this, we prune the delete
    -> dataserver queries the cache(intent) checks if there is another intent owning this path

    => result is delete paths

2. add the new data from the intent to the candidate
    -> exapnd keys
    -> dataserver queries the cache(intent) to check if there is another intent with higher or equal priority.
    if so dont add this path to the candidate

3. transact the candidate, if success write the intent update to the cache

glitches would be resyned to the intent by subscription
e.g. cache becomes unreachable
