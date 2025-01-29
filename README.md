# md2cre-docker

Dockerized version of [md2cre](https://gist.github.com/mxswd/3158772)

### Usage

```bash
docker build -t md2cre .
docker run --rm -v $(pwd):/usr/src/app md2cre example.md > example.txt
``` 