# pydivider

Doing same as [godivider]('https://github.com/webislife/godivider')

Uses `aiohttp` as webserver

- threadless
- lockless
- asynchronous

### install environment and requirements:
`virtualenv --python=python3.7 --download env && source env/bin/activate && pip install -r requirements.txt`

### Run:
`source env/bin/activate && python pydivider.py` 

### Output:
```
======== Running on http://0.0.0.0:9099 ========
(Press CTRL+C to quit)
```

### Test it:
`watch -n .1 'curl -s http://localhost:9099/?a=$RANDOM\&b=$RANDOM'`

### Bencmark
`wrk -t12 -c100 -d30s http://127.0.0.1:9099/?a=$RANDOM\&b=$RANDOM`
```
Running 30s test @ http://127.0.0.1:9099/?a=19515&b=18458
  12 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    24.35ms  730.52us  38.41ms   95.86%
    Req/Sec   329.81     21.17   435.00     82.89%
  118430 requests in 30.09s, 19.09MB read
Requests/sec:   3936.10
Transfer/sec:    649.62KB
```
