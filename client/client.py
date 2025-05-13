import socket
import argparse
from protocol import (
    ProtocolMessage, send_message, receive_message,
    TYPE_QUESTION, TYPE_ANSWER, TYPE_RESULT,
    QUESTION_ID, QUESTION_TEXT, QUESTION_OPTIONS,
    RESULT_SCORE, RESULT_TOTAL, QUESTION_CORRECT
)

class QuizClient:
    def __init__(self, host='localhost', port=5000):
        self.host = host
        self.port = port
    
    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            print("Conectado ao servidor!")
            
            while True:
                message = receive_message(s)
                if not message:
                    break
                
                if message.type == TYPE_QUESTION:
                    self.handle_question(s, message.data)
                elif message.type == TYPE_RESULT:
                    self.handle_result(message.data)
                    break
    
    def handle_question(self, sock, question):
        print(f"\nPergunta {question[QUESTION_ID]}: {question[QUESTION_TEXT]}")
        for i, option in enumerate(question[QUESTION_OPTIONS], 1):
            print(f"{i}. {option}")
        
        answer = input("Sua resposta (número): ")
        response = ProtocolMessage(
            type_=TYPE_ANSWER,
            data={
                QUESTION_ID: question[QUESTION_ID],
                QUESTION_CORRECT: question[QUESTION_OPTIONS][int(answer)-1]
            }
        )
        send_message(sock, response)
    
    def handle_result(self, result):
        print(f"\nPontuação final: {result[RESULT_SCORE]}/{result[RESULT_TOTAL]}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Cliente do Quiz')
    parser.add_argument('--host', type=str, default='localhost', help='Endereço do servidor')
    parser.add_argument('--port', type=int, required=True, help='Porta do servidor')
    
    args = parser.parse_args()
    
    client = QuizClient(host=args.host, port=args.port)
    client.start()
