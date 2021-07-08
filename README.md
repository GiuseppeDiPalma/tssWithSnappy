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
- [x] Decide what metrics we will use
  - [x] Threshold: constant (2, 4 e 6), proporzionale al grado (d(v)/2, d(v)/3, 2d(v)/3)
  - [x] Edge: uniforme, neighborhood overlap biased, 1 - neighborhood overlap biased 
- [x] Find and use other dataset
- [ ] Make all benchmarks for all datasets
- [ ] Write report


## Test
- Per ogni edge probability
  - Per ogni threshold function
    - Esegui algoritmo 10 volte e fai media dimensione target set

## Datasets

|Name|#nodes|#edges|Max Deg|Diam|LCC Size|#Triangles|Clust Coeff|Modul|
|---|---|---|---|---|---|---|---|---|
|Blog_catalog|88.784|2.093.195||   	|   	|   	|   	|   	|
|Blog_catalog_3|10.312|333.983||   	|   	|   	|   	|   	|
|CA-AstroPh|18.772|198.110||14|17.903|1.351.441|   	|   	|
|CA-CondMat|23.133|93.497||14|21.363|173.361|   	|   	|
|CA-GrQc|5.242|14.496||17|4158|48.260|   	|   	|
|CA-HepPh|10.008|118.521||13|11.204|3.358.499|   	|   	|
|CA-HepTh|9.877|25.998||17|8638|28.399|   	|   	|
|LiveMocha|104.438|2.196.188||6|104.103|336.651|   	|   	|
|Delicious|103.144|1.419.519||-|536.108|487.972|   	|   	|
|Douban|154.907|654.188||9|154.908|40.612|   	|   	|
|Youtube2|1.138.499|2.990.443||-|1.134.890|3.056.537|   	|   	|
