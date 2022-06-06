# Build custom docker image using lambda as base image
docker build -t ghactivity-aws .

# Start docker container with custom image
docker run \
  --name ghactivity-aws \
  -v /Users/itversity/.aws:/root/.aws \
  -p 9000:8080 \
  -e BUCKET_NAME=itversitydata \
  -e TARGET_FOLDER=raw \
  -d \
  ghactivity-aws

# Validate docker image for lambda function locally
curl -XPOST \
  "http://localhost:9000/2015-03-31/functions/function/invocations" \
  -d '{"file_name": "s3://itversitydata/ghactivity/2022-06-02-3.json.gz"}'

# Login to docker
aws ecr get-login-password \
  --region us-east-1 | \
  docker login \
  --username AWS \
  --password-stdin \
  582845781536.dkr.ecr.us-east-1.amazonaws.com

# Tag docker image to make it ready to push to AWS ECR
docker tag ghactivity-aws:latest \
  582845781536.dkr.ecr.us-east-1.amazonaws.com/ghactivity-aws:latest

# Push custom docker image to AWS ECR
docker push 582845781536.dkr.ecr.us-east-1.amazonaws.com/ghactivity-aws:latest
