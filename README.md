## Task
Finding minimal absolute difference between two elements of two sorted arrays

### How to use
```shell script
python find_difference.py
```
then

```shell script
enter array A:5 4 3 0  
enter array B:1000, 2000
Min difference: 995
```

Requirements needed for tests
```shell script
poetry export -f requirements.txt --without-hashes --dev | pip install -r /dev/stdin
```
or just
```shell script
pip install -r requirements.txt
```

### Time measure
for all three approaches, using automatically generated lists
```shell script
python measure_time.py
```
