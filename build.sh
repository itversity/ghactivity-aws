rm -f ghactivity-aws.zip
mkdir -p dependencies
pip install -r requirements.txt -t dependencies
cd dependencies; zip -r ghactivity-aws.zip .
mv -f ghactivity-aws.zip ..
cd ..
rm -rf dependencies
zip -r ghactivity-aws.zip app