build_portfolio_webapp:
	docker build -t davefelce/portfolio_webapp:latest -f ./Dockerfile .
push_docker_portfolio_webapp:
	docker push davefelce/portfolio_webapp:latest
