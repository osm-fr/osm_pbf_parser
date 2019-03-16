OSM PBF Parser
==============

Python binding build upon libosmpbf and osmpbfreader.h from Canal TP:
- https://github.com/scrosby/OSM-binary
- https://github.com/CanalTP/libosmpbfreader

Build
-----

```
cd osm_pbf_parser; make; cd ..
# Then cheats about the binary compatibility
python setup.py bdist_wheel
mv dist/osm_pbf_parser-0.1.0-cp27-cp27mu-linux_x86_64.whl dist/osm_pbf_parser-0.1.0-cp27-cp27mu-manylinux1_x86_64.whl
```
