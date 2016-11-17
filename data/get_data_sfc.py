from ecmwfapi import ECMWFDataServer

server = ECMWFDataServer()

server.retrieve({
    'stream'    : "oper",
    'levtype'   : "sfc",
    'param'     : "142/143/151",
    'dataset'   : "interim",
    'step'      : "3",
    'grid'      : "0.75/0.75",
    'time'      : "00",
    'date'      : "2016-01-01/to/2016-01-01",
    'type'      : "fc",
    'class'     : "ei",
    'format'    : "netcdf",
    'target'    : "era_data_sfc.nc"
})
