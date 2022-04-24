setup-db:
	docker-compose down --volumes && docker-compose up -d
	
format:
	black lambda_func tests
	flake8 lambda_func tests

test:
	python3 -m pytest tests --no-header -v
	docker-compose down --volumes

