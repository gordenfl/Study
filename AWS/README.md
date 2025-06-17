# AWS

Amazon Web Service, include all the amazon cloud service platform. it provide all kinds of service include calculation, Storage, Database, Analysis, AI, about 200+ cloud service.

This Document only include the generate info of AWS. the detail info will distribute into different sub-folder or documents.


## Calculations

1. EC2 : virtual machine
2. ECS : Elastic Container Service (容器编排服务, 支持Docker)
3. EKS : Elastic Kubernetes Service (Kubernetes host)
4. Elastic_Beanstalk : Simple Application deploy management platform
5. Lambda : executable function without server
6. Batch : Batch job scheduling

## Storage

1. S3 : Object storage service
2. EBS: Elastic Block Storage (support EC2)
3. EFS: Elastic File System  (NFS, network file system)
4. FSx: support Windows and Lustre file system
5. Storage Gateway: Gateway of local storage and cloud storage

## Database

1. RDS: Relation database system (MySQL ,PostgreSQL, Oracle, etc.)
2. Aurora: High performance RDS, self-developed by Amazon. Compatible With MySQL and PostgreSQL.
3. DynamoDB: No-SQL database
4. ElasticCache: Memory database such like Redis/memcached
5. DocumentDB: MongoDB host
6. Neptune: Picture database
7. Time stream: database based on the time stream.
8. Keyspaces: Apache Cassandra Service host

## Network & CDN

1. VPC: Virtual Private Cloud, private network configuration
2. CloudFront: Content distribute globally. (CDN)
3. Route 53: DNS service
4. API Gateway: Construct API service and management all of that.
5. Direct Connect: local data center connect with AWS
6. Global Accelerator: network accelerator for the global network
7. ELB: Elastic Load Balance: load balance include ALB, NLB, CLB
8. App Mesh: microservice management as a grid

## Security and Authentication and Rule

1. IAM: Identity Add Access Management, include authentication and authorization.
2. Cognito: OAuth with user register and login and authorization
3. KMS: Key management service , mainly for the key pair management(generate, add, delete etc.)
4. Shield: protected for the DDoS
5. WAF: Web Application Firewall, protect the application
6. SecretsManager: manage sensitive info such like password

## DevOps Tools

1. CodeCommit: git repository service
2. CodeBuild: auto build service
3. CodeDeploy: auto deploy service
4. CodePipeline: integrate all 1,2,3 together and management all of them
5. CloudFormation: auto deploy service, this function can create Ec2, S3 etc. help to generate all the resource we need. but the code Deploy can only deploy the code to the Ec2 has already exist.
6. CloudWatch: watch and collect log from server.
7. X-Ray: Trace the path of user's request. to help you get the error, delay, bottleneck of network etc.
8. System Manager: Manage all the resource you use on the AWS platform. integrate all the function can manage different kinds of resource in AWS.