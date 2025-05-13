import socket
import argparse
import threading
from pathlib import Path
import json
from protocol import (
    ProtocolMessage, send_message, receive_message,
    TYPE_QUESTION, TYPE_RESULT, TYPE_ANSWER,
    QUESTION_ID, QUESTION_TEXT, QUESTION_OPTIONS, QUESTION_CORRECT,
    RESULT_SCORE, RESULT_TOTAL
)

class QuizServer:
    def __init__(self, host='localhost', port=5000, topic='technology'):
        self.host = host
        self.port = port
        self.topic = topic
        self.questions = self.load_questions()
        self.scores = {}

    def load_questions(self):
        path = Path(__file__).parent / 'questions' / f'{self.topic}.json'
        with open(path) as f:
            return json.load(f)

    def handle_client(self, conn, addr):
        print(f"[LOG] Cliente conectado: {addr}")
        score = 0
        try:
            for q in self.questions:
                question_msg = ProtocolMessage(
                    type_=TYPE_QUESTION,
                    data={
                        QUESTION_ID: q['id'],
                        QUESTION_TEXT: q['question'],
                        QUESTION_OPTIONS: q['options']
                    }
                )
                send_message(conn, question_msg)
                
                answer_msg = receive_message(conn)
                if answer_msg and answer_msg.data[QUESTION_CORRECT] == q[QUESTION_CORRECT]:
                    score += 1
            
            result_msg = ProtocolMessage(
                type_=TYPE_RESULT,
                data={
                    RESULT_SCORE: score,
                    RESULT_TOTAL: len(self.questions)
                }
            )
            send_message(conn, result_msg)
        
        finally:
            conn.close()

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            print(f"Servidor {self.topic} ouvindo em {self.host}:{self.port}")
            
            while True:
                conn, addr = s.accept()
                threading.Thread(target=self.handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Iniciar servidor de quiz')
    parser.add_argument('--topic', type=str, required=True, help='Tópico do quiz (ex: technology, movies)')
    parser.add_argument('--port', type=int, default=5000, help='Porta para escutar conexões')
    
    args = parser.parse_args()
    
    server = QuizServer(port=args.port, topic=args.topic)
    server.start()
