# A Spring AMR service and client

[![PyPI][pypi-badge]][pypi-link]
[![Python 3.10][python3100-badge]][python3100-link]
[![Python 3.11][python311-badge]][python311-link]
[![Build Status][build-badge]][build-link]

A client and server that generates AMR graphs from natural language sentences.
This repository has a Docker that compiles the [AMR SPRING parser] using the
original settings of the authors.

The Docker image was created because this parser has a very specific set of
Python dependencies that do not compile under some platforms.  Specifically
`tokenizers==0.7.0` fails to compile from source on a `pip` install because of
a Rust compiler misconfiguration.

The Docker image provides a very simple service written in [Flask] that
uses the SPRING model for inferencing and returns the parsed AMRs.

Features:

* Parse natural language sentence (batched) into AMRs.
* Results cached either in memory or an SQLite database.
* Both a command line and Pythonic object oriented client API.


## Documentation

See the [full documentation](https://plandes.github.io/amrspring/index.html).
The [API reference](https://plandes.github.io/amrspring/api.html) is also
available.


## Installing

First install the client:
```bash
pip3 install zensols.amrspring
```

To build the Docker image:
1. Download the model(s) from the [AMR SPRING parser] repository.
1. Build the image: `cd docker ; make build`
1. Check for errors.
1. Start the image: `make up`

Of course, the server code can be run without docker by cloning the [AMR SPRING
parser] repository and adding the [server code](docker/src).  See the
[Dockerfile](docker/Dockerfile) for more information on how to do that.


## Usage

The package can be used from the command line or directly via a Python API.

Command line:
```bash
$ amrspring --level warn parse 'Obama was the president.'
sent: Obama was the president.
graph:
    # ::snt Obama was the president.
    (z0 / person
        :ARG0-of (z1 / have-org-role-91
                     :ARG2 (z2 / president))
        :domain (z3 / person
                    :name (z4 / name
                              :op1 "Obama")))
```

Python API:
```python
>>> from zensols.amrspring import AmrPrediction, ApplicationFactory
>>> client = ApplicationFactory.get_client()
>>> pred = tuple(client.parse(['Obama was the president.']))[0]
2024-02-19 19:41:03,659 parsed 1 sentences in 3ms
>>> print(pred.graph)
# ::snt Obama was the president.
(z0 / person
    :ARG0-of (z1 / have-org-role-91
                 :ARG2 (z2 / president))
    :domain (z3 / person
                :name (z4 / name
                          :op1 "Obama")))
```


## Changelog

An extensive changelog is available [here](CHANGELOG.md).


## Community

Please star this repository and let me know how and where you use this API.
Contributions as pull requests, feedback and any input is welcome.


## License

[MIT License](LICENSE.md)

Copyright (c) 2024 Paul Landes


<!-- links -->
[pypi]: https://pypi.org/project/zensols.amrspring/
[pypi-link]: https://pypi.python.org/pypi/zensols.amrspring
[pypi-badge]: https://img.shields.io/pypi/v/zensols.amrspring.svg
[python3100-badge]: https://img.shields.io/badge/python-3.10-blue.svg
[python3100-link]: https://www.python.org/downloads/release/python-3100
[python311-badge]: https://img.shields.io/badge/python-3.11-blue.svg
[python311-link]: https://www.python.org/downloads/release/python-3110
[build-badge]: https://github.com/plandes/amrspring/workflows/CI/badge.svg
[build-link]: https://github.com/plandes/amrspring/actions

[AMR SPRING parser]: git clone https://github.com/SapienzaNLP/spring
