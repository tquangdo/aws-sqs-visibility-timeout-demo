# aws-sqs-visibility-timeout-demo 🐳

![Stars](https://img.shields.io/github/stars/tquangdo/aws-sqs-visibility-timeout-demo?color=f05340)
![Issues](https://img.shields.io/github/issues/tquangdo/aws-sqs-visibility-timeout-demo?color=f05340)
![Forks](https://img.shields.io/github/forks/tquangdo/aws-sqs-visibility-timeout-demo?color=f05340)
[![Report an issue](https://img.shields.io/badge/Support-Issues-green)](https://github.com/tquangdo/aws-sqs-visibility-timeout-demo/issues/new)

## reference
[haitrungnet](https://haitrung.net/hieu-dung-ve-khai-niem-visibility-timeout-delay-queue-trong-amazon-sqs/)

## IAM role
- create role name=`DTQRoleDemoSQS`
- with policy name=`SQSFullAccess`

## SQS
- create SQS name=`DTQSQSDemoSQS`
- Visibility timeout = 20''
- Delivery delay = 0
![sqs](screenshots/sqs.png)

## Lambda
- create lambda name=`DTQLambdaDemoSQS`
- with role name=`DTQRoleDemoSQS`
- run test -> check OK!
![lambda](screenshots/lambda.png)

## test SQS visibility timeout
### A) Visibility timeout = 20''
- SQS > click `Send and receive messages`
- Message body=`Visibility timeout = 20''`
- Lambda > click `Test` → just show MSG in 20'' & NOT show after 20''
- show
![20show](screenshots/20show.png)
---
- NOT show
![20NOTshow](screenshots/20NOTshow.png)
### B) Delivery delay=10''
- SQS > setting `Delivery delay=10''` > click `Send and receive messages`
- Message body=`Delivery delay is 10''`
- Lambda > click `Test` → opposite with Visibility, just show MSG after 10''
![10show](screenshots/10show.png)