.PHONY: run_db

run_db:
	docker run --name=product-db -e POSTGRES_DB='product-db' -e POSTGRES_USER=root -e POSTGRES_PASSWORD='qwerty' -p 5432:5432 -d --rm postgres

start_app:
	python3 main.py

run_test_db:
	docker run --name=product-test-db -e POSTGRES_DB='product-test-db' -e POSTGRES_USER=root -e POSTGRES_PASSWORD='qwerty' -p 5433:5432 -d --rm postgres

run_tests:
	pytest