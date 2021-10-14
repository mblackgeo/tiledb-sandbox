import os
import json
import subprocess

import requests


def main():
    # Setup the output directory
    out_dir = os.path.join(os.path.dirname(__file__), 'data')
    os.makedirs(out_dir, exist_ok=True)

    # Download 3 Sentinel 2 images
    payload = {
        'collections': ['sentinel-s2-l2a-cogs'],
        'datetime': '2019-06-09T00:00:00Z/2020-06-28T23:59:59Z',
        'intersects': {'type': 'Point', 'coordinates': [-121.461647, 39.558225]},
        'limit': 3,
    }

    response = requests\
        .post("https://earth-search.aws.element84.com/v0/search", data=json.dumps(payload))\
        .json()

    # Download the red band from each image
    for idx, feature in enumerate(response['features']):
        href = feature['assets']['B04']['href']
        out_fname = os.path.join(out_dir, f'{idx + 1}.tif')

        if not os.path.exists(out_fname):
            subprocess.check_output(["wget", href, f"--output-document={out_fname}"])


if __name__ == "__main__":
    main()
