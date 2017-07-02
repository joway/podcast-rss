_cache = {}


def cache_get(k, default):
    return _cache.get(k) if _cache.get(k) else default


def cache_set(k, v):
    _cache[k] = v
    return _cache
