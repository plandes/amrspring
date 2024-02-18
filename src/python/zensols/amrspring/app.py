"""A client and server that generates AMR graphs from natural language
sentences.

"""
__author__ = 'Paul Landes'

from typing import Iterable, Dict, Any
from dataclasses import dataclass, field
import logging
import requests
from requests.models import Response
from zensols.util import APIError

logger = logging.getLogger(__name__)


class AmrServiceError(APIError):
    pass


class AmrServiceRequestError(AmrServiceError):
    def __init__(self, request: Dict[str, Any], res: Response):
        super().__init__(f'Error ({res.status_code}): {res.reason}')
        self.response = res


@dataclass
class AmrParseClient(object):
    host: str = field()
    port: int = field()

    def _invoke(self, data: Dict[str, Any]):
        endpoint: str = f'http://{self.host}:{self.port}/parse'
        res: Response = requests.post(endpoint, json=data)
        if res.status_code != 200:
            raise AmrServiceRequestError(data, res)
        serv_res: Dict[str, Any] = res.json()
        if 'error' in serv_res:
            raise AmrServiceError(serv_res['error'])
        return serv_res

    def parse(self, sents: Iterable[str]):
        res: Dict[str, Any] = self._invoke({'sents': sents})
        if 'amrs' not in res:
            raise AmrServiceError(f'Unknown data: {res}')
        return res['amrs']


@dataclass
class Application(object):
    """A client and server that generates AMR graphs from natural language
    sentences.

    """
    client: AmrParseClient = field()

    def parse(self, text: str):
        """Parse ``text`` and generate AMRs.

        :param text: the sentence to parse

        """
        graph_str: str
        for graph_str in self.client.parse([text]):
            print(graph_str)
