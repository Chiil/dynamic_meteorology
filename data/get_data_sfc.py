from ecmwfapi import ECMWFDataServer

server = ECMWFDataServer()

server.retrieve({
    'stream'    : "oper",
    'levtype'   : "sfc",
    'param'     : "142.128/143.128/228.128",
    'dataset'   : "interim",
    'step'      : "3",
    'grid'      : "0.75/0.75",
    'time'      : "00",
    'date'      : "2007-01-20/to/2007-01-20",
    'type'      : "fc",
    'class'     : "ei",
    'format'    : "netcdf",
    'target'    : "test_sfc.nc"
})
