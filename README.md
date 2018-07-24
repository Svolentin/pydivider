# pydivider

Doing same as [godivider](https://github.com/webislife/godivider)

Uses `japronto` and `uvloop`

- threadless
- lockless
- asynchronous

### install environment and requirements:
`virtualenv --python=python3.6 --download env && source env/bin/activate && pip install -r requirements.txt`

### Run:
`source env/bin/activate && python pydivider.py` 

### Output:
```
Accepting connections on http://0.0.0.0:9099
```
__(Press CTRL+C to quit)__

### Test it:
`watch -n .1 'curl -s http://localhost:9099/?a=$RANDOM\&b=$RANDOM'`

### Benchmark
`wrk -t24 -c500 -d30s http://127.0.0.1:9099/?a=$RANDOM\&b=$RANDOM`
```
Running 30s test @ http://127.0.0.1:9099/?a=15296&b=29370
  24 threads and 500 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    15.51ms    5.76ms  38.48ms   59.97%
    Req/Sec     1.22k   263.99     8.37k    91.09%
  875014 requests in 30.08s, 81.78MB read
  Socket errors: connect 0, read 533, write 0, timeout 0
Requests/sec:  29088.45
Transfer/sec:      2.72MB
```

### Deactivate env:
`deactivate`