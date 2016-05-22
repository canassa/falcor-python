

class ModelDataSourceAdapter:

    def __init__(self, model):
        self._model = model._materialize().boxValues().treatErrorsAsValues()

    def get(self, pathSets):
        return self._model.get(pathSets)._toJSONG()

    def set(self, jsongResponse):
        return self._model.set(jsongResponse)._toJSONG()

    def call(self, path, args, suffixes, paths):
        params = [path, args, suffixes].concat(paths)
        return self._model.call(self._model, params)._toJSONG()
