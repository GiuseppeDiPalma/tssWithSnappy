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
(venv) $ python targetsetselection.py -d dataset.txt
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
|Blog_catalog|88.784|2.093.195|32|   	|   	|   	|0.3533|   	|
|Blog_catalog_3|10.312|333.983|4839|   	|   	|   	|0.4631|   	|
|CA-AstroPh|18.772|198.110|7299|14|17.903|1.351.441|0.6309|   	|
|CA-CondMat|23.133|93.497|15756|14|21.363|173.361|0.6339|   	|
|CA-GrQc|5.242|14.496|4234|17|4158|48.260|0.5304|   	|
|CA-HepPh|10.008|118.521|9647|13|11.204|3.358.499|0.6118|   	|
|CA-HepTh|9.877|25.998|223|17|8638|28.399|0.4718|   	|
|LiveMocha|104.438|2.196.188|106|6|104.103|336.651|0.0544|   	|
|Delicious|103.144|1.419.519|3216|-|536.108|487.972|   	|   	|
|Douban|154.907|654.188|885|9|154.908|40.612|0.0160|   	|
|Youtube2|1.138.499|2.990.443|28.754|-|1.134.890|3.056.537|   	|   	|
