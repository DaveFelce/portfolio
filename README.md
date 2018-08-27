# portfolio
My recent Django demos

## Deploy
* 'make build_portfolio_webapp'
* 'make push_docker_portfolio_webapp'
* Make a tar of .env and docker-compose.yml (if they've changed)
* rsync it to digitalocean
* ssh to digitalocean
* docker-compose up
