#!/usr/bin/env bash

# Use STAC to download some Sentinel 2 images for populating the TileDB instance
echo "Downloading images"
python3 download.py
echo "Finished downloading images"

# Use GDAL to convert the images to TileDB
dir="$(dirname "$(realpath $0)")/data"
for i in {1..3}
do
    echo "image $i converting to tiledb"
    gdal_translate -OF TileDB "$dir/$i.tif" "$dir/tiledb-array-$i"
    echo "image $i done"
done