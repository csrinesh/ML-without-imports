def R2(y, yhat):
    sst = sum([i**2 for i in y])
    ssr = sum([(i-yhat[ind])**2 for ind, i in enumerate(y)])

    return float('{:.3f}'.format(1 - (ssr/sst))) 