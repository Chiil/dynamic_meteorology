from ecmwfapi import ECMWFDataServer
server = ECMWFDataServer()
server.retrieve({
    "class": "ei",
    "dataset": "interim",
    "date": "20160101/20160201",
    "expver": "1",
    "grid": "0.75/0.75",
    "levelist": "1/2/3/5/7/10/20/30/50/70/100/125/150/175/200/225/250/300/350/400/450/500/550/600/650/700/750/775/800/825/850/875/900/925/950/975/1000",
    "levtype": "pl",
    "param": "131.128/132.128",
    "stream": "moda",
    "type": "an",
    'format': "netcdf",
    'target': "test.nc"
})
