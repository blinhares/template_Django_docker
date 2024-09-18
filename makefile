all:
	@sudo docker compose up
ch_permi:
	@ls | xargs sudo chown -R bruno:bruno
build:
	@sudo docker compose up --build --force-recreate
apagar_dockers:
	@sudo docker rm -vf $(sudo docker ps -aq) ; sleep 1; sudo docker rmi -f $(sudo docker images -aq)