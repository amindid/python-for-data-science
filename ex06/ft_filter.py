def ft_filter(function, iterable):
    """Return an iterator of items of iterable for which function is true."""
    return iter([item for item in iterable if function(item)])
