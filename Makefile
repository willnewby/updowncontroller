DATETIME := $(shell date "+%Y-%m-%d_%H-%M-%S")

default: build push

all: build push deploy logs

build:
	docker build . -t 275271710846.dkr.ecr.us-west-2.amazonaws.com/updowncontroller:$(DATETIME)

push:
	`AWS_PROFILE='zentainer' aws ecr get-login --no-include-email` && docker push 275271710846.dkr.ecr.us-west-2.amazonaws.com/updowncontroller:$(DATETIME)

deploy:
	kubectl apply -f kube/

logs:
	stern --since=60s updowncontroller
