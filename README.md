# ghactivity-aws
End to End Pipeline using AWS Services such as s3, boto3, lambda, ECR, step functions, Dynamodb, Step Functions, etc.

Do you want to learn AWS Lambda Functions by building an **end-to-end data pipeline using Python and other key AWS Services such as Boto3, S3, Dynamodb, ECR, Cloudwatch, Glue Catalog, Athena**, etc? Here is one course using which you will learn AWS Lambda Functions by implementing an end-to-end pipeline by using all the services mentioned.

* Setup required tools on Windows to develop the code for ETL Data Pipelines using Python and AWS Services. You will take care of setting up **Ubuntu using wsl, Docker Desktop, Visual Studio Code along with Remote Development Extension Kit** so that you can develop Python-based applications using AWS Services.
* **Setup Project or Development Environment to develop applications using Python and AWS Services** on Windows and Mac.
* **Getting Started with AWS by creating an account in AWS and also configuring AWS CLI** as well as **Review Data Sets** used for the project
* **Develop Core Logic to Ingest Data from source to AWS s3 using Python boto3**. The application will be built using Boto3 to interact with AWS Services, Pandas for date arithmetic, and requests to get the files from the source via REST API.
* Getting Started with **AWS Lambda Functions using Python 3.9 Run-time Environment**
* **Refactor the application, and build a zip file to deploy as AWS Lambda Function**. The application logic includes capturing bookmark as well as Job Run Detail in Dynamodb. You will also get an overview of Dynamodb and how to interact with Dynamodb to manage Bookmark as well as Job Run details.
* Create **AWS Lambda Function using a Zip file**, deploy using AWS Console and Validate.
* Troubleshoot issues related to **AWS Lambda Functions using AWS Cloudwatch**
* Build a custom docker image for the application and push it to **AWS ECR (Elastic Container Registry)**
* **Create AWS Lambda Function** using the **custom docker image in AWS ECR (Elastic Container Registry)** and then validate.
* Get an understanding of **AWS s3 Event Notifications or s3-based triggers on Lambda Function**.
* Develop another Python application to transform the data and also write the data in the form of Parquet to s3. The application will be built using Pandas by converting 10,000 records at a time to Parquet.
* Build **orchestrated pipeline using AWS s3 Event Notifications between the two Lambda Functions**.
* **Schedule the first lambda function** using **AWS EventsBridge** and then validate.
* Finally, **create AWS Glue Catalog table** on the s3 location which has parquet files, and validate by running **SQL Queries using AWS Athena**.

Here are the key takeaways from this training:
* Develop Python Applications and Deploy as Lambda Functions by using a Zip-based bundle as well as a custom docker image.
* Monitor and troubleshoot the issues by going through Cloudwatch logs.
* The entire application code used for the demo along with the notebook used to come up with core logic.
* Ability to build solutions using multiple AWS Services such as Boto3, S3, Dynamodb, ECR, Cloudwatch, Glue Catalog, Athena, etc
