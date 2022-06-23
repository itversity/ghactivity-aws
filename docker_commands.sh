docker build -t ghactivity-aws .

docker run \
  --name ghactivity-aws \
  -d \
  ghactivity-aws

docker exec -it ghactivity-aws bash

docker run \
  --name ghactivity-aws \
  -v /Users/itversity/.aws:/root/.aws \
  -e AWS_PROFILE=ghactivity \
  -e BUCKET_NAME=aigithub \
  -e FOLDER=landing/ghactivity \
  -d \
  ghactivity-aws

python -c "import app;app.lambda_ingest(None, None)"

aws s3 ls s3://aigithub/landing/ghactivity --recursive 

docker run \
  --name ghactivity-aws \
  -p 9080:8080 \
  -v /Users/itversity/.aws:/root/.aws \
  -e AWS_PROFILE=ghactivity \
  -e BUCKET_NAME=aigithub \
  -e FOLDER=landing/ghactivity \
  -d \
  ghactivity-aws

export AWS_PROFILE=ghactivity

aws ecr get-login-password \
    --region us-east-1 | \
    docker login \
        --username AWS \
        --password-stdin 269066542444.dkr.ecr.us-east-1.amazonaws.com

docker tag ghactivity-aws:latest \
    269066542444.dkr.ecr.us-east-1.amazonaws.com/ghactivity-aws:latest

docker push 269066542444.dkr.ecr.us-east-1.amazonaws.com/ghactivity-aws:latest

aws ecr list-images \
    --repository-name ghactivity-aws
    
aws lambda get-function \
    --function-name ghactivity-ingestor

aws lambda get-function-configuration \
    --function-name ghactivity-ingestor

docker run \
  --name ghactivity-aws \
  -p 9080:8080 \
  -v /Users/itversity/.aws:/root/.aws \
  -e AWS_PROFILE=ghactivity \
  -e BUCKET_NAME=aigithub \
  -e FOLDER=landing/ghactivity \
  -e TARGET_FOLDER=raw/ghactivity \
  -d \
  ghactivity-aws

curl -XPOST \
  "http://localhost:9080/2015-03-31/functions/function/invocations" \
  -d '{"jobRunDetails": {"last_run_file_name": "2022-06-05-2.json.gz"}}'