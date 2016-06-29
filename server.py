import tornado.ioloop
import tornado.web
from app.dictionary.stardict import IfoFileReader, IdxFileReader, DictFileReader
from app.handler.bot import BotHandler


def make_app():
    ifo_reader = IfoFileReader('./data/en_vi.ifo')
    idx_reader = IdxFileReader('./data/en_vi.idx')
    dict_reader = DictFileReader('./data/en_vi.dict.dz', ifo_reader, idx_reader, True)

    return tornado.web.Application([
        (r"/slash", BotHandler, dict(dictdb=dict_reader)),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

