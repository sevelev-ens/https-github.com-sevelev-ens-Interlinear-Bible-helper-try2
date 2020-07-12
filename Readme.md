Useful data derived from [https://github.com/openscriptures/morphhb](https://github.com/openscriptures/morphhb).


The `yaml` files were obtained from the `xml` sources in `../bigxml` using

```
for i in ../bigxml/*.xml; do python xml2yaml.py $i $( basename "$i" .xml ).yaml  ; done
```

The python script needs [`xmlplain`](https://pypi.org/project/xmlplain/) to be installed.

The interesting data in WLC https://hb.openscriptures.org/ xml files: for the 5 poetic books, there are poetic line divisions.
