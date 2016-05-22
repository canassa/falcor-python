import copy

from falcor.model_data_source_adapter import ModelDataSourceAdapter


class Model:

    def __init__(self):
        self._materialized = False
        self._boxed = False
        self._progressive = False
        self._treatErrorsAsValues = False
        self._maxSize = 2 ** 53 - 1
        self._collectRatio = 0.75

    def asDataSource(self):
        return ModelDataSourceAdapter(self)

    def get(self):
        raise NotImplementedError

    def _getWithPaths(self):
        raise NotImplementedError

    def set(self):
        raise NotImplementedError

    def preload(self):
        raise NotImplementedError

    def call(self):
        raise NotImplementedError

    def invalidate(self):
        raise NotImplementedError

    def deref(self):
        raise NotImplementedError

    def _hasValidParentReference(self):
        raise NotImplementedError

    def getValue(self):
        raise NotImplementedError

    def setValue(self):
        raise NotImplementedError

    def _getValueSync(self):
        raise NotImplementedError

    def _setValueSync(self):
        raise NotImplementedError

    def _derefSync(self):
        raise NotImplementedError

    def setCache(self):
        raise NotImplementedError

    def getCache(self):
        raise NotImplementedError

    def getVersion(self):
        raise NotImplementedError

    def _syncCheck(self):
        raise NotImplementedError

    def _clone(self, **opts):
        clone = copy.deepcopy(self)
        for key, value in opts.items():
            if value == "delete":
                delattr(clone, key)
            else:
                setattr(clone, key, value)
        clone.setCache = None
        return clone

    def batch(self):
        raise NotImplementedError

    def unbatch(self):
        raise NotImplementedError

    def treatErrorsAsValues(self):
        """
        Returns a clone of the {@link Model} that treats errors as values.
        Errors will be reported in the same callback used to report data.
        Errors will appear as objects in responses, rather than being sent to
        the {@link Observable~onErrorCallback} callback of the {@link
        ModelResponse}.
        @return {Model}
        """
        return self._clone(_treatErrorsAsValues=True)

    def _materialize(self):
        return self._clone(_materialized=True)

    def _dematerialize(self):
        raise NotImplementedError

    def boxValues(self):
        """
        Returns a clone of the {@link Model} that boxes values returning the
        wrapper ({@link Atom}, {@link Reference}, or {@link Error}), rather
        than the value inside it. This allows any metadata attached to the
        wrapper to be inspected.
        @return {Model}
        """
        return self._clone(_boxed=True)

    def unboxValues(self):
        raise NotImplementedError

    def withoutDataSource(self):
        raise NotImplementedError

    def toJSON(self):
        raise NotImplementedError

    def getPath(self):
        raise NotImplementedError

    def _fromWhenceYouCame(self):
        raise NotImplementedError

    def _getBoundValue(self):
        raise NotImplementedError

    def _getVersion(self):
        raise NotImplementedError

    def _getPathValuesAsPathMap(self):
        raise NotImplementedError

    def _getPathValuesAsJSONG(self):
        raise NotImplementedError

    def _setPathValues(self):
        raise NotImplementedError

    def _setPathMaps(self):
        raise NotImplementedError

    def _setJSONGs(self):
        raise NotImplementedError

    def _setCache(self):
        raise NotImplementedError

    def _invalidatePathValues(self):
        raise NotImplementedError

    def _invalidatePathMaps(self):
        raise NotImplementedError
