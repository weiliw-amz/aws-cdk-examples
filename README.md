# AWS CDK code examples

This AWS CDK code example deploys stacks containing AWS constructs to your AWS account's CloudFormation.

The development and deployment are performed on your AWS account's **EC2 instances with necessary permission**, please double-check your EC2 instance role policies if any permission issues occur.

## Prerequisites

Install npm:
```
# Download nvm script
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash

export NVM_DIR="$HOME/.nvm"                                                                              
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

# Install latest CDK-supported Node.js and npm
# NOTE: latest node version is not always supported by CDK, double-check before installation
nvm install 17.3.0

# Check installation
node -v
npm -v
```

Install AWS CDK:
```
npm install -g aws-cdk

# Check installation
cdk --version
```

Bootstrapping:
```
# Replace contents in <> with your AWS account number and region
cdk bootstrap aws://<ACCOUNT_NUMBER>/<REGION>
```

## Usage

Clone code:
```
git clone https://github.com/weiliw-amz/aws-cdk-examples.git
cd aws-cdk-examples
```

Create Python virtual environment and install dependencies:
```
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

CDK synthesize:
```
cdk synth
```

CDK deploy all stacks:
```
cdk deploy --all
```

CDK diff after code change:
```
cdk diff
```

CDK destroy all stacks:
```
cdk destroy --all
```

## References

* Developer Guide: https://docs.aws.amazon.com/cdk/v2/guide/home.html
* Python API Reference: https://docs.aws.amazon.com/cdk/api/v2/python/index.html
