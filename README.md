# Target set selection with snap.py

Implmentation of Target Set Selection with snap.py on blogcatalugue dataset.

**Description:** BlogCatalog is asocial blog directory. The dataset contains all links among users.

[Dataset](http://networkrepository.com/soc-BlogCatalog.php)

1. Create and activate a Python virtual environment

```sh
$ cd tssWithSnappy/
$ python -m venv ./venv
$ source venv/bin/activate
(venv) $
```

```sh
(venv) $ deactivate
```

2. Install the dependencies

```sh
(venv) $ python -m pip install -r requirements.txt
```

3. Run the application

```sh
(venv) $ python targetsetselection.py
```

## TODO-List

- [x] Treshold must be set as t(v) = min(treshold, degree(v))  
- [ ] Decide what metrics we will use
  - [ ] Threshold: constant (2, 4 e 6), proporzionale al grado (d(v)/2, d(v)/3, 2d(v)/3)
  - [ ] Edge: uniforme, neighborhood overlap biased, 1 - neighborhood overlap biased 
- [ ] Find and use other dataset


## Test
- Per ogni edge probability
  - Per ogni threshold function
    - Esegui algoritmo 10 volte e fai media dimensione target set

Salva il sottografo su disco, così quando lo devi ricaricare ad ogni iterazione è molto veloce