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