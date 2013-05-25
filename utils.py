class Dotable(dict):
    __getattr__= dict.__getitem__
    def __init__(self, d=None):
        if isinstance(d, Dotable):
            return d
        if d is None:
            d = {}
        dict.update(self, **dict((k, self.parse(v)) for k, v in d.iteritems()))
    def parse(self, v):
        if isinstance(v, dict): return Dotable(v)
        elif isinstance(v, list): return [self.parse(i) for i in v]
        else: return v
    #def update(self, **d):
    #   d = Dotable(d)
    #   super(Dotable, self).update(**d)