.DEFAULT_GOAL := release

BUILD_DIR=build
FUNCTION_NAME=gpt_alexa
ZIP_NAME=$(shell pwd)/$(BUILD_DIR)/jee-pee-tee.zip

release: clean
	mkdir $(BUILD_DIR)
	zip -r $(BUILD_DIR)/jee-pee-tee.zip lambda -x lambda/\config.example.json -x lambda/\.venv/\* -x .git -x .env

deploy: clean
	mkdir $(BUILD_DIR)
	#pip install --target lambda/site-packages -r lambda/requirements.txt
	zip $(BUILD_DIR)/jee-pee-tee.zip -j lambda/*.py -j lambda/.env -j lambda/requirements.txt
	cd lambda; zip $(ZIP_NAME) -r site-packages/*
	# Update to S3 s3://nachouve-alexa-dev/jee-pee-tee.zip
	##aws lambda update-function-code --function-name $(FUNCTION_NAME) --zip-file fileb://$(ZIP_NAME)

clean:
	rm -rf $(BUILD_DIR) 2> /dev/null
