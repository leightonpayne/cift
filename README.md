# cift

#### extract_chain.py

Filter an mmCIF file for a particular chain of a particular model (by name):

```bash
extract_chain.py <input> <output> <model> <chain>
# $ python extract_chain.py 1fnt.cif 1fnt_1_g.cif 1 g
```

Filter a list of files using `sbatch` and `parallel`: 

```bash
cat list.txt
# > 1fnt 1 g
# > 1914 1 A
# > 1a04 1 B
# > ...
```

```bash
sbatch -c 54 --time "00:30:00" --mem "32G" parallel -j 54 --colsep ' ' "source activate <gemmi-env>; python extract_chain.py {1}.cif {1}.cif {2} {3}" :::: list.txt
```
