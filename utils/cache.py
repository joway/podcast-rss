_cache = {}


def cache_get(k, default):
    return _cache.get(k, default=default)


def cache_set(k, v):
    _cache[k] = v
    return _cache
