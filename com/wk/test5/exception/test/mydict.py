# 单元测试
class mydict(dict) :
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % item)
    def __setattr__(self, key, value):
        self[key] = value