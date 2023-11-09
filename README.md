# shibboleth-over-nginx-okadai

## description

1. first, run `make certs` to generate the certs for the encrypt, signing keys
```bash
make certs
```


2. then, run `mkcert [FQDN]` to generate the certs for the domain
```
mkcert devshibd.okayama-u.ac.jp
```


3. then, run `make up` to build and run the docker containers
```bash
make up
```

4. access the service at [`https://devshibd.okayama-u.ac.jp`](https://devshibd.okayama-u.ac.jp). you may need to add the following to your `/etc/hosts` file
```bash
127.0.0.1 devshibd.okayama-u.ac.jp
```

5. get Metadata from [`https://devshibd.okayama-u.ac.jp/Shibboleth.sso/Metadata`](https://devshibd.okayama-u.ac.jp/Shibboleth.sso/Metadata)
6. upload Metadata to Shibboleth IdP
7. access the service at [`https://devshibd.okayama-u.ac.jp`](https://devshibd.okayama-u.ac.jp) again

## license
Copyright (c) 2023 R74


## references
- https://shibboleth.atlassian.net/wiki/spaces/SP3/pages/2065335537/Installation
- https://github.com/pennlabs/docker-shibboleth-sp-nginx [MIT License] Penn Labs