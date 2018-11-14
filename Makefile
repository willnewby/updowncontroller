DATETIME := $(shell date "+%Y-%m-%d_%H-%M-%S")

default: build push

all: build push deploy logs

build:
	docker build . -t willnewby/updowncontroller:$(DATETIME)

push:
	docker push willnewby/updowncontroller:$(DATETIME)

deploy:
	kubectl apply -f kube/

logs:
	stern --since=60s updowncontroller
