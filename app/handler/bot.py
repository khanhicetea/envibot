import tornado
import re


class BotHandler(tornado.web.RequestHandler):
    def initialize(self, dictdb):
        self.dictdb = dictdb

    def format_meaning(self, text):
        lines = text.split("\n")
        lines[0] = "`" + lines[0] + "`"
        result = []
        for line in lines:
            if line[0] == "*":
                line += "*"
            result.append(line)
        return "\n".join(result)

    def post(self):
        word = self.get_argument('text')
	result = self.dictdb.get_dict_by_word(word)
        res_text = "Not found this word :("
	if result:
            meaning = result[0]['m']
            res_text = self.format_meaning(meaning)

        self.write(tornado.escape.json_encode({
            'text': res_text,
            'response_type': 'ephemeral'
        }))
        self.set_header("Content-Type", "application/json")

