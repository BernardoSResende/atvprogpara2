import json


TYPE_QUESTION = "question"
TYPE_ANSWER = "answer"
TYPE_RESULT = "result"

FIELD_TYPE = "type"
FIELD_DATA = "data"


QUESTION_ID = "question_id"
QUESTION_TEXT = "question"
QUESTION_OPTIONS = "options"
QUESTION_CORRECT = "answer"

RESULT_SCORE = "score"
RESULT_TOTAL = "total"


class ProtocolMessage:
    def __init__(self, type_: str, data: dict):
        self.type = type_
        self.data = data

    def to_json(self):
        return json.dumps({
            FIELD_TYPE: self.type,
            FIELD_DATA: self.data
        }).encode()

    @staticmethod
    def from_json(raw: bytes):
        obj = json.loads(raw.decode())
        return ProtocolMessage(obj[FIELD_TYPE], obj[FIELD_DATA])


def send_message(sock, message: ProtocolMessage):
    sock.sendall(message.to_json())


def receive_message(sock) -> ProtocolMessage:
    data = sock.recv(1024)
    if not data:
        return None
    return ProtocolMessage.from_json(data)
