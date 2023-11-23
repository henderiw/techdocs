# github actions

- ci solution: trigegrs workflows based on pushes/pull requests and other events
- a managed service
- community actions

## terminology 

- worflows: 
    - collection of jobs that run based on a trigger
    - a ci pipeline
    - defined in YAML
- runners:
    - a compute machine where worflows are executed
    - github managed or custom runners
- job:
    - a set of steps that execute in a single runner workspace
    (build, test, deploy)
- step
    - lowest level, can be a command, a script, a javascript file a dockerfile or a community action

workflows <- 1:N -> job/runner <- 1: N -> step 


workflow example

```yaml
name: build application code

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest       # runner
    steps:
    - name: check out code       # name of the step
      uses: actions/checkout@v2  # community action
    - name: install libraries
      run: pip install -r requirements.txt -t .
  test:
    runs-on: ubuntu-latest
    needs: build                 # dependency
    steps:
```

## community actions

prepackaged steps for GHA

[actions marketplace](https://github.com/marketplace?category=&query=&type=actions&verification=)


3 types of custom actions:
- javascript:  supported on all OS
- composite: supported on all OS -> allows to run native go with caveats
- docker: only supported on linux

## runners

a vm where jobs defined in a workfloe are run
- linux, windows, mac

custom runner: runs in your environments
- used when running your own github instance
- security
- cost mgmt

setting up a custom runner (VM)
- create a private repo [custom runner repo](https://github.com/henderiw/custom-runner)
- settings/actions/

### download

```bash
# Create a folder
mkdir actions-runner && cd actions-runner
# Download the latest runner package
curl -o actions-runner-linux-x64-2.311.0.tar.gz -L https://github.com/actions/runner/releases/download/v2.311.0/actions-runner-linux-x64-2.311.0.tar.gz
# Optional: Validate the hash
echo "29fc8cf2dab4c195bb147384e7e2c94cfd4d4022c793b346a6175435265aa278  actions-runner-linux-x64-2.311.0.tar.gz" | shasum -a 256 -c
# Extract the installer
tar xzf ./actions-runner-linux-x64-2.311.0.tar.gz
```

### configure

```bash
# Create the runner and start the configuration experience
./config.sh --url https://github.com/henderiw/custom-runner --token ACMXXVC3JOU5FKPFMWID7J3FLEHES
# Last step, run it!
./run.sh
```

### create a workflow

```yaml
name: runs on custom runner

on: push

jobs:
  init:
    runs-on: self-hosted
    steps:
    - run: echo 'hello cloud gurus'
    - run: echo $HOSTNAME
```

### remove runner

settings/action/runner delete

./config.sh remove --token ACMXXVDLCVDRFWI6ZAHG5Q3FLEI62

## github a ations/security

- avoid untrusted inputs
- community actions: verify
- custom runners with public repos is not usefull
- github org: 

## trigger worflows

- push or pull request
- schedule
- ...

environment variables
- repository information
    - name
    - url
- event information
    - initiating event
    - initiating user
- commit information
    - commit SHA
    - git branch
    - git head
- job information
    - job id
    - run id
    - action id
- server informarion
    - github server url
    - api api
    - graphQL url
- runner info
    - os
    - temp dir
    - tool cache


build workflow
```yaml
name: Deploy my Lambda Function

# trigger on all push events to main branch
on: 
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Check out code
        uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.8
      - name: Install libraries
        run: |
            cd function
            python -m pip install --upgrade pip
            if [ -f requirements.txt ]; then pip install -r requirements.txt -t .; fi
      - name: Create zip bundle
        run: |
            cd function
            zip -r ../${{ github.sha }}.zip .
      - name: Archive artifact
        uses: actions/upload-artifact@v2
        with:
          name: zipped-bundle
          path: ${{ github.sha }}.zip
```

store artifacts -> github packages

github packages support
- container registry
- rugby gems
- node modules
- maven registry
- gradle registry
- nuGet


```yaml
env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  build-and-push-image:
  - name: checkout code
    uses: actions/checkout@v2
  - name: login to the container registry
    uses: docker/login-action
    with:
      registry: ${{ env.REGISTRY }}
      username: ${{ github.actor }}
      password: ${{ secrets.GOTHUB.TOKEN }}
  - name: build and push docker image
    uses: docker/build-push-action
    with:
      context: .
      push: true
```

```yaml
name: Deploy Lambda Function
on: [push]

jobs:

  lint:
    runs-on: ubuntu-latest
    steps: 
      - name: Check out code
        uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.8
      - name: Install libraries
        run: pip install flake8
      - name: Lint with flake8
        run: |
            cd function
            flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
            flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

  build:
    runs-on: ubuntu-latest
    needs: lint
    steps:
      - name: Check out code
        uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.8
      - name: Install libraries
        run: |
            cd function
            python -m pip install --upgrade pip
            if [ -f requirements.txt ]; then pip install -r requirements.txt -t .; fi 
      - name: Zip bundle
        run: |
            cd function
            zip -r ../${{ github.sha }}.zip .
      - name: Archive artifact
        uses: actions/upload-artifact@v2
        with:
          name: zipped-bundle
          path: ${{ github.sha }}.zip

  publish:
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Create release
        id: create_release
        uses: actions/create-release@v1
        env:
          GITHUB_TOKEN: ${{ secrets.github_token }} # This token is provided by Actions, you do not need to create your own token
        with:
          tag_name: ${{ github.run_number }}
          release_name: Release ${{ github.run_number }}
          body: New release for ${{ github.sha }}. Release notes can be found in the docs.
          draft: false
          prerelease: false
      - name: Download artifact
        uses: actions/download-artifact@v2
        with:
          name: zipped-bundle
      - name: Upload release asset
        uses: actions/upload-release-asset@v1
        env:
          GITHUB_TOKEN: ${{ secrets.github_token }}
        with:
          upload_url: ${{ steps.create_release.outputs.upload_url }} 
          asset_path: ./${{ github.sha }}.zip
          asset_name: source_code_with_libraries.zip
          asset_content_type: application/zip
```


```yaml
- name: download aws cli
  run: curl "https://awscli.amazonaws.cli/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
- name: unzip aws cli
  run: unzip awscliv1.zip
- name: install aws cli
  run: suo ./aws/install
- name: configure aws cli
  run: |
    export AWS_ACCESS_KEY_ID=${{ secrets.AWS_ACCESS_KEY_ID }}
    export AWS_SECRET_ACCESS_KEY=${{ secrets.AWS_SECRET_ACCESS_KEY }}
    export AWS_DEFAULT_REGION=${{ secrets.AWS_DEFAULT_REGION }}
```

```yaml
name: Deploy my Lambda Function

# trigger on all push events to main branch
on: 
  push:
    branches:
      - main

jobs:

  build:
    runs-on: ubuntu-latest
    steps:
      - name: Check out code
        uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.8
      - name: Install libraries
        run: |
            cd function
            python -m pip install --upgrade pip
            if [ -f requirements.txt ]; then pip install -r requirements.txt -t .; fi
      - name: Create zip bundle
        run: |
            cd function
            zip -r ../${{ github.sha }}.zip .
      - name: Archive artifact
        uses: actions/upload-artifact@v2
        with:
          name: zipped-bundle
          path: ${{ github.sha }}.zip
  
  upload:
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Download artifact
        uses: actions/download-artifact@v2
        with:
          name: zipped-bundle
      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v1
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: us-east-1
      - name: Upload to S3
        run: aws s3 cp ${{ github.sha }}.zip s3://<YOUR BUCKET NAME HERE>/${{ github.repository }}/${{ github.sha }}.zip

  deploy:
    runs-on: ubuntu-latest
    needs: upload
    steps:
      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v1
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: us-east-1
      - name: Update function code
        run: |
            aws lambda update-function-code \
              --function-name <YOUR FUNCTION NAME HERE> \
              --s3-bucket <YOUR BUCKET NAME HERE> \
              --s3-key ${{ github.repository }}/${{ github.sha }}.zip \
              --publish
```

```yaml
name: Deploy my Lambda Function

# trigger on all push events to main branch
on: 
  push:
    branches:
      - main

jobs:

  lint:
    runs-on: ubuntu-latest
    steps: 
      - name: Check out code
        uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.8
      - name: Install linting libraries
        run: |
            cd function
            pip install flake8
      - name: Lint with flake8
        run: |
            # Select identifies which errors should cause the job to fail
            flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
            # The exit zero flag will show errors as warnings and not fail the run
            flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

  build:
    runs-on: ubuntu-latest
    needs: lint
    steps:
      - name: Check out code
        uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.8
      - name: Install libraries
        run: |
            cd function
            python -m pip install --upgrade pip
            if [ -f requirements.txt ]; then pip install -r requirements.txt -t .; fi
      - name: Create zip bundle
        run: |
            cd function
            zip -r ../${{ github.sha }}.zip .
      - name: Archive artifact
        uses: actions/upload-artifact@v2
        with:
          name: zipped-bundle
          path: ${{ github.sha }}.zip
  
  upload:
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Download artifact
        uses: actions/download-artifact@v2
        with:
          name: zipped-bundle
      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v1
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: us-east-1
      - name: Upload to S3
        run: aws s3 cp ${{ github.sha }}.zip s3://<YOUR BUCKET NAME HERE>/${{ github.repository }}/${{ github.sha }}.zip

  nonprod:
    runs-on: ubuntu-latest
    needs: upload
    strategy:
      matrix:
        input: ["Hello", "Hi"]
    steps:
      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v1
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: us-east-1
      - name: Create test function
        run: |
            aws lambda create-function --function-name test-function-${{ matrix.input }} \
              --code S3Bucket=<YOUR BUCKET NAME HERE>,S3Key=${{ github.repository }}/${{ github.sha }}.zip \
              --handler lambda_function.lambda_handler --runtime python3.8 \
              --role arn:aws:iam::${{ secrets.AWS_ACCOUNT_ID }}:role/<YOUR ROLE NAME HERE>
      - name: Invoke test function 
        run: |
            aws lambda invoke --function-name test-function-${{ matrix.input }} \
              --payload $(echo "{\"input\": \"${{ matrix.input }}\"}" | base64) \
              --output json out 
            if grep -q "Error" out; then
              exit1
            fi
      - name: Destroy test function
        if: ${{ always() }}
        run: |
            aws lambda delete-function --function-name test-function-${{ matrix.input }}

  deploy:
    runs-on: ubuntu-latest
    needs: upload
    steps:
      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v1
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: us-east-1
      - name: Update function code
        run: |
            aws lambda update-function-code \
              --function-name <YOUR FUNCTION NAME HERE> \
              --s3-bucket <YOUR BUCKET NAME HERE> \
              --s3-key ${{ github.repository }}/${{ github.sha }}.zip \
              --publish
```

lint

```yaml
name: Deploy my Lambda Function

# trigger on all push events to main branch
on: 
  push:
    branches:
      - main

jobs:

  lint:
    runs-on: ubuntu-latest
    steps: 
      - name: Check out code
        uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.8
      - name: Install linting libraries
        run: |
            cd function
            pip install flake8
      - name: Lint with flake8
        run: |
            # Select identifies which errors should cause the job to fail
            flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
            # The exit zero flag will show errors as warnings and not fail the run
            flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

  build:
    runs-on: ubuntu-latest
    needs: lint
    steps:
      - name: Check out code
        uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.8
      - name: Install libraries
        run: |
            cd function
            python -m pip install --upgrade pip
            if [ -f requirements.txt ]; then pip install -r requirements.txt -t .; fi
      - name: Create zip bundle
        run: |
            cd function
            zip -r ../${{ github.sha }}.zip .
      - name: Archive artifact
        uses: actions/upload-artifact@v2
        with:
          name: zipped-bundle
          path: ${{ github.sha }}.zip
  
  upload:
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Download artifact
        uses: actions/download-artifact@v2
        with:
          name: zipped-bundle
      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v1
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: us-east-1
      - name: Upload to S3
        run: aws s3 cp ${{ github.sha }}.zip s3://<YOUR BUCKET NAME HERE>/${{ github.repository }}/${{ github.sha }}.zip

  deploy:
    runs-on: ubuntu-latest
    needs: upload
    steps:
      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v1
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: us-east-1
      - name: Update function code
        run: |
            aws lambda update-function-code \
              --function-name <YOUR FUNCTION NAME HERE> \
              --s3-bucket <YOUR BUCKET NAME HERE> \
              --s3-key ${{ github.repository }}/${{ github.sha }}.zip \
              --publish

```

## setup test environment

- configure aws cli
- create non prod lambda
- insert function
- destroy

```yaml
name: Deploy my Lambda Function

# trigger on all push events to main branch
on: 
  push:
    branches:
      - main

jobs:

  lint:
    runs-on: ubuntu-latest
    steps: 
      - name: Check out code
        uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.8
      - name: Install linting libraries
        run: |
            cd function
            pip install flake8
      - name: Lint with flake8
        run: |
            # Select identifies which errors should cause the job to fail
            flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
            # The exit zero flag will show errors as warnings and not fail the run
            flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

  build:
    runs-on: ubuntu-latest
    needs: lint
    steps:
      - name: Check out code
        uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.8
      - name: Install libraries
        run: |
            cd function
            python -m pip install --upgrade pip
            if [ -f requirements.txt ]; then pip install -r requirements.txt -t .; fi
      - name: Create zip bundle
        run: |
            cd function
            zip -r ../${{ github.sha }}.zip .
      - name: Archive artifact
        uses: actions/upload-artifact@v2
        with:
          name: zipped-bundle
          path: ${{ github.sha }}.zip
  
  upload:
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Download artifact
        uses: actions/download-artifact@v2
        with:
          name: zipped-bundle
      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v1
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: us-east-1
      - name: Upload to S3
        run: aws s3 cp ${{ github.sha }}.zip s3://<YOUR BUCKET NAME HERE>/${{ github.repository }}/${{ github.sha }}.zip

  nonprod:
    runs-on: ubuntu-latest
    needs: upload
    strategy:
      matrix:
        input: ["Hello", "Hi"]
    steps:
      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v1
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: us-east-1
      - name: Create test function
        run: |
            aws lambda create-function --function-name test-function-${{ matrix.input }} \
              --code S3Bucket=<YOUR BUCKET NAME HERE>,S3Key=${{ github.repository }}/${{ github.sha }}.zip \
              --handler lambda_function.lambda_handler --runtime python3.8 \
              --role arn:aws:iam::${{ secrets.AWS_ACCOUNT_ID }}:role/<YOUR ROLE NAME HERE>
      - name: Invoke test function 
        run: |
            aws lambda invoke --function-name test-function-${{ matrix.input }} \
              --payload $(echo "{\"input\": \"${{ matrix.input }}\"}" | base64) \
              --output json out 
            if grep -q "Error" out; then
              exit1
            fi
      - name: Destroy test function
        if: ${{ always() }}
        run: |
            aws lambda delete-function --function-name test-function-${{ matrix.input }}

  deploy:
    runs-on: ubuntu-latest
    needs: upload
    steps:
      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v1
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: us-east-1
      - name: Update function code
        run: |
            aws lambda update-function-code \
              --function-name <YOUR FUNCTION NAME HERE> \
              --s3-bucket <YOUR BUCKET NAME HERE> \
              --s3-key ${{ github.repository }}/${{ github.sha }}.zip \
              --publish
```

## deploy static site to S3 with github actions

AWS
    2 buckets:
    - S3 non prod
    - S3 prod

    user: github-actions-user
    -> programatic access
    -> full managed policy


Github
    Settings/Secrets
    Name: AWS_ACCESS_KEY_ID -> paste key
    Name: AWS_SECRET_ACCESS_KEY => paste key

non-roduction.yaml
```yaml
name: non prod

on:
  push:
    branches:
    - feature*

jobs:
  build:
    runs-on: ubuntu-latest
    env:
      BUCKET_NAME: xxx ## this should be the non production bucket
    steps:
    - name: checkout code
      uses: actions/checkout@v2
    - name: configure aws cli
      uses: aws-actions/configure-aws-credentials@v1
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: us-east-1
    - name: setup node js
      uses: actions/setup-node@v2
      with:
        node-versopn: 14
    - name: build site
      run: |
        npm cli
        npm run build
    - name: deploy files to bucket
      run: aws s3 cp public s3://${{ env.BUCKET_NAME }} --recursive --acl public-read   
```

production.yaml workflow

```yaml
name: prod

on:
  push:
    branches:
    - main # protect main so people cannot push to main

jobs:
  build:
    runs-on: ubuntu-latest
    env:
      BUCKET_NAME: xxx ## this should be the production bucket
    steps:
    - name: checkout code
      uses: actions/checkout@v2
    - name: configure aws cli
      uses: aws-actions/configure-aws-credentials@v1
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: us-east-1
    - name: setup node js
      uses: actions/setup-node@v2
      with:
        node-versopn: 14
    - name: build site
      run: |
        npm cli
        npm run build
    - name: deploy files to bucket
      run: aws s3 cp public s3://${{ env.BUCKET_NAME }} --recursive --acl public-read  
```

## gh pages

```yaml
  docs:
    runs-on: ubuntu-latest
    needs: deploy
    steps:
      - name: Check out code
        uses: actions/checkout@v2
      - name: Deploy docs
        uses: mhausenblas/mkdocs-deploy-gh-pages@master
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          CONFIG_FILE: mkdocs.yaml
```

```yaml
name: Deploy Lambda Function
on: 
  push:
    paths:
      - userguide.md

jobs:

  lint:
    runs-on: ubuntu-latest
    steps: 
      - name: Check out code
        uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.8
      - name: Install libraries
        run: pip install flake8
      - name: Lint with flake8
        run: |
            cd function
            flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
            flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

  build:
    runs-on: ubuntu-latest
    needs: lint
    steps:
      - name: Check out code
        uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.8
      - name: Install libraries
        run: |
            cd function
            python -m pip install --upgrade pip
            if [ -f requirements.txt ]; then pip install -r requirements.txt -t .; fi 
      - name: Zip bundle
        run: |
            cd function
            zip -r ../${{ github.sha }}.zip .
      - name: Archive artifact
        uses: actions/upload-artifact@v2
        with:
          name: zipped-bundle
          path: ${{ github.sha }}.zip
          
  documentation:
    runs-on: ubuntu-latest
    needs: lint
    steps:
      - name: Checkout code code
        uses: actions/checkout@v2
      - name: Create pages directory
        run: mkdir docs
      - name: Convert markdown to HTML 
        uses: docker://pandoc/core:2.9
        with:
          args: userguide.md -t html -o docs/index.html
      - name: Deploy Pages site
        uses: JamesIves/github-pages-deploy-action@4.1.4
        with:
          branch: gh-pages
          folder: docs
```