# tiledb-sandbox
A quick look at using TileDB for geospatial data

## Install

Create the environment with:

```shell
conda env create -f environment.yml
```

Then setup TileDB using some sample Sentinel 2 data by running the script:

```shell
./init-tiledb.sh
```

You should now have a functional TileDB Embedded with a few Sentinel 2 images present. There are some example notebooks provided that show how to interact with TileDB and performing efficient slicing of the data.