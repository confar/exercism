def largest_product(series, size):
    if not series:
        raise ValueError('String must not be empty')
    if size < 0:
        raise ValueError('Size must be positive')
    elif series.isalnum():
        raise ValueError('String must contain of digits only')
    else:
        for i in series.split():
            pass

