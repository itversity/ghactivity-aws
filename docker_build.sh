docker rmi 269066542444.dkr.ecr.us-east-1.amazonaws.com/ghactivity-aws:latest
docker rmi ghactivity-aws

docker build -t ghactivity-aws .

export AWS_PROFILE=ghactivity

aws ecr get-login-password \
    --region us-east-1 | \
    docker login \
        --username AWS \
        --password-stdin 269066542444.dkr.ecr.us-east-1.amazonaws.com

docker tag ghactivity-aws:latest \
    269066542444.dkr.ecr.us-east-1.amazonaws.com/ghactivity-aws:latest

docker push 269066542444.dkr.ecr.us-east-1.amazonaws.com/ghactivity-aws:latest

aws lambda update-function-code \
    --function-name ghactivity-ingestor \
    --image-uri 269066542444.dkr.ecr.us-east-1.amazonaws.com/ghactivity-aws:latest