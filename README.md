# md2cre-docker

Markdown to [Creole](https://mariadb.com/kb/en/meta/creole-formatting/) converter in a Docker container.

### Usage

```bash
docker build -t md2cre .
docker run --rm -v $(pwd):/usr/src/app md2cre docs/API_REFERENCE.md > result.txt
``` 