UpDownController
=====
-
A Kubernetes-based controller for managing updown.io checks.

Using
===
The updowncontroller runs as a Deployment + Service in Kubernetes and needs only an API key to interact with the updown.io API.

```bash
git clone git@github.com:willnewby/updowncontroller.git
cd updowncontroller
make deploy
```



Developing
===
