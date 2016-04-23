"""
Downloads the OSM data for the Yucatan Peninsula. 
"""
import argparse
import os
import sys
import requests
import tqdm
import random

filename = 'data.xml'
overpass_url = "http://overpass-api.de/api/interpreter"
lat = [18.521, 23.403]
lon = [-92.670, -86.440]
small_reduction_scale=10

def download_overpass_file(lats, lon):
    payload={"data": "(node(" + str(lats[0]) + "," + str(lon[0]) + "," + str(lats[1]) + "," + str(lon[1]) + ");<;);out meta;"}
    r = requests.get(overpass_url, data=payload, stream=True)
    with open(filename, 'wb') as f:
        for chunk in tqdm.tqdm(r.iter_content(chunk_size=1024)): 
            if chunk:
                f.write(chunk)
    return filename

def get_reduced_range(coords):
    coords_range = coords[1] - coords[0]
    coords_size = coords_range / small_reduction_scale
    coords_max_start = coords_range - coords_size
    coords_rand_start = random.uniform(0, coords_max_start)
    coords_start = coords_rand_start + coords[0]
    coords_end = coords_start + coords_size
    return [coords_start, coords_end]

def download_osm_file(small):
    if(small==True):
        print("Downloading small map.")
        sm_lat = get_reduced_range(lat)
        sm_lon = get_reduced_range(lon)
        download_overpass_file(sm_lat, sm_lon)
    else:
        print("Downloading full map.")
        download_overpass_file(lat, lon)
    print("Finished downloading " + filename)
    filesize = os.stat(filename).st_size * 1E-6
    print("size:  %.1f MB" % filesize)
    return

def main():
    parser = argparse.ArgumentParser(description='Downloads Yucatan OSM data for P3.')
    parser.add_argument('--small', action='store_true',
                                        help='Only download a small portion of the full OSM data.')
    parser.add_argument('--force', action='store_true',
                                        help='Automatically download even if a file with the expected name already exists.')
    args = parser.parse_args()

    if(args.force == True):
        download_osm_file(args.small)
    elif(os.path.isfile(filename)):
        print("Expected file (" + filename + ") already exists.")

        valid_answer = False
        while not valid_answer:
            answer = input("Continue and overwrite it? (y/n):")
            if(answer == "y"):
                valid_answer = True
                download_osm_file(args.small)
            elif(answer == "n"):
                valid_answer = True
    else:
        download_osm_file(args.small)

    sys.exit(0)

if __name__ == "__main__":
    main()
