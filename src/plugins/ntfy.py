from subprocess import call

class ntfy:
    def __init__(self, server, topic):
        self.server = server
        self.topic = topic
    def send_message(self, server, topic, message):
        call(f"curl -d '{self.message}' {self.server}/{self.topic}", shell=True)