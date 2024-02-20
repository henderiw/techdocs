# git

- git stores the new file
    - delta based systems -> challenge: start with the original file + add all changes (clunky, takes time)
    - full file approach:
        - revision/commit:
            - snapshot of all files at that moment
            - if no change git stores a link to previous identical file

## logical layout in git

- repository: your local git repository
- working directory: single checkout of one revision of your files
- staging area: (index) files to get ready for your next commit (so you can share with others)

commands:
- git checkout (repo -> working dir)
    - takes care of not loosing your work
- git add (woring dir -> staging area)
- git commit (staging area -> repository)

## physical layout

- /project
    - file1
    - file2
    - file3
    - /.git
        - index
        - /objects


sha1/ message digest 40 digit or 20 byte
- used to identify if 2 files are identical
- used to refer to a previous file
- used as filename we store


file has sha1 hash
dir has a sha1 hash
commit has a sha1 hash -> reference the files that changed
head master


Blob Object -> file -> file contents
Tree Object -> dir  -> Reference other blobs or trees
Commit Object -> link tree with history
Head

## branch

used parallel line of development
- defect repair
- new feature
- release candidate

create a feature branch

```s
git branch feature
```

-> simpler name than a commit
-> superlight in git

working directory changed to content of the new branch
- git is very careful on not loosing changes

```s
git checkout feature
```



## merging

we restore to the main branch

```s
git checkout main
```

merge to where the main branch converged

```s
git merge -m 'merge in feature' feature
```