up: 
	docker-compose up -d

down:
	docker-compose down

runserver:
	uvicorn main:app --reload

logs:
	docker logs -f airtel-mock