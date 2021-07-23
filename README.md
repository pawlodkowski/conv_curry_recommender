# Convultional Curry Recommender

## Introduction

Lorem Ipsem

## How to Install / Run

### OPTION A:

```bash
git clone github.com:pawlodkowski/conv_curry_recommender.git
cd conv_curry_recommender/
pip install .

#eventually: pip install conv_curry_recommender
```

alternatively:

```bash
pip install github.com:pawlodkowski/conv_curry_recommender.git

#I think this works out of the box; but need to verify
```

Maybe also create a new virtual environment with Anaconda.

### OPTION B:

Good for more complicated programs, e.g. servers / databases, etc.

```bash
docker build -t cc_rec .
docker run cc_rec
```

## Examples

```python
import conv_curry_recommender
stuff = ['hello', 'hi', 'bonjour', 'sup']
rec = Recommender(stuff)

print(rec.simple_recommend())

```

### Acknowledgements / Credits

it's free yo.
