# Locust

[Locust](https://docs.locust.io/) is a load testing framework.

## Quick Setup

Setup the endpoints you want to test on the [locustfile.py](locustfile.py).

You will need `docker` and `docker-compose` installed in your system, in order to run this infrastructure. 

Type:

```
docker compose up
```

Or, if you want to run it in the background

```
docker compose up -d
```

Access the UI at [http://localhost:8089/](http://localhost:8089/) and run your tests.

Some result tests can be found [here](./report_1725036621.259672.html). You can preview it [here](https://doublebyte1.github.io/locust/report_1725036621.259672.html).

## License

This project is released under an [MIT License](./LICENSE)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)