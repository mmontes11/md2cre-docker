# md2cre-docker

Markdown to Creole converter in a Docker container.

### Usage

```bash
docker build -t md2cre .
docker run --rm -v $(pwd):/usr/src/app md2cre docs/API_REFERENCE.md > result.txt
``` 