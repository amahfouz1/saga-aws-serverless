# Saga Pattern Implementation using Serverless Framework, Python, DynamoDB, and AWS Step Functions

## Project structure
- `serverless.yaml` this yaml file is the core file for our implementation, it contains all the declaration and configurations needed for the Severless framework to be able to create all the AWS resources we need to implement the Saga design pattern (Lambda functions, DynamoDB table creation, IAM roles, State machine model, and other configurations).

- `functions` this folder has all the Python lambda functions:  
  - create_order
  - process_payment
  - process_shipment
  - delete_order
  - refund_payment
  - cancel_shipment

> If you prefer using Docker then you can skip the Install steps and pull the docker image:  

```
docker run -it -v `pwd`:/saga-aws-serverless amahfouz/serverless /bin/bash
```
and start [Configure](#Configure)

## Install
You need first to install the Serverless framework and all its prereqs:

- NodeJS

  - MacOS (using brew)
      ```
      brew install node
      ```
  - Linux (Ubuntu)
      ```
      apt install nodejs
      apt install npm
      ```
  - Windows:
      Download and install from this link [https://nodejs.org/en/download/](https://nodejs.org/en/download/)


- Severless framework  

  Follow the instructions here [https://www.serverless.com/framework/docs/getting-started/](https://www.serverless.com/framework/docs/getting-started/)

## Configure

After installing the Serverless framework you need to start setting it up. Run `serverless` command and you will be asked several questions as follow:

```
Serverless: No project detected. Do you want to create a new one?
```
You won't get this question if you already running it from an existing serverless project.  

If you answered Yes to create a new project you will be asked some other questions:

```
Serverless: What do you want to make? AWS Python
Serverless: What do you want to call this project? saga-aws-serverless

Project successfully created in 'saga-aws-serverless' folder.
```

I chose AWS Python for the programming language the serverless functions will be using, and then I gave the project name to be saga-aws-serverless.

```
You can monitor, troubleshoot, and test your new service with a free Serverless account.

Serverless: Would you like to enable this? No
You can run the “serverless” command again if you change your mind later.
```
For the above two questions, it's all up to you.

If you already have your AWS credentials setup on your machine you should be fine, otherwise, you will get the below prompt to configure your AWS
credentials:

```
No AWS credentials were found on your computer, you need these to host your application.

Serverless: Do you want to set them up now? Yes
Serverless: Do you have an AWS account? Yes

If your browser does not open automatically, please open the URL: https://console.aws.amazon.com/iam/home?region=us-east-1#/users$new?step=final&accessKey&userNames=serverless&permissionType=policies&policies=arn:aws:iam::aws:policy%2FAdministratorAccess

Serverless: Press Enter to continue after creating an AWS user with access keys
Serverless: AWS Access Key Id: ####
Serverless: AWS Secret Access Key: ####

AWS credentials saved on your machine at ~/.aws/credentials. Go there to change them at any time.

Serverless: Would you like the Framework to update automatically? Yes

Auto updates were succesfully turned on.
You may turn off at any time with "serverless config --no-autoupdate"
```

The auto-complete if you don't have this already setup on your linux/Mac machine it will be nice to have it setup:

```
Serverless: Would you like to setup a command line <tab> completion? Yes
Serverless: Which Shell do you use ? bash
Serverless: We will install completion to ~/.bashrc, is it ok ? Yes

Command line <tab> completion was successfully setup. Make sure to reload your SHELL.
You may uninstall it by running: serverless config tabcompletion uninstall
```

Congrats now you have Serverless framework installed and configured on your machine.


## Deploy

To deploy first you need to install the project dependencies:
```
npm install
```
Now you are all set to deploy all the lambda functions and create the AWS Step state machine model:
```
sls deploy
```
(sls is short for serverless)

If you would like to invoke any function all you need to do:
```
sls invoke -f create_order -d {"order_id":"1", "total":100}
```

## Remove
Finally to remove all the AWS resources you created all you need to do is:
```
sls remove
```

## Testing

- To test the state machine model, go to AWS console, Services and search for Step Functions.
- Select State machines from the left menu.
- Select the state machine model created with OrderFulfilment in its name.
- Click on Start Execution

### Successful Input:
```
{
  "order_id": "1",
  "total": 100,
  "card_no": "123-1234",
  "address": "123 st"
}
```
![Successful Order](/screenshots/successful_order.PNG "Successful Order")

### Failure Input:

#### Failed Order
Missing total
```
{
  "order_id": "2"
}
```
![Failed Order](/screenshots/failed_order.PNG "Failed Order")

#### Failed Payment
Missing card_no
```
{
  "order_id": "3",
  "total": 100
}
```
![Failed Payment](/screenshots/failed_payment.PNG "Failed Payment")

#### Failed Shipment
Missing address
```
{
  "order_id": "5",
  "total": 100,
  "card_no": "123-1234"
}
```
![Failed Shipment](/screenshots/failed_shipment.PNG "Failed Shipment")

## Addition information
- [Serverless Framework](https://www.serverless.com/framework/docs/guides/)
- [Python AWS Lambda handlers](https://docs.aws.amazon.com/lambda/latest/dg/python-handler.html)

- [Python Lambda and DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.html)

- [Serverless step functions plugin](https://www.serverless.com/plugins/serverless-step-functions)
