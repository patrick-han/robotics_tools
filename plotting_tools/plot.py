import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import argparse, sys

# Inputs: Take in a list of 2D coordinate sets, each represented by an Nx2 numpy array
# Effects: Plot polygons on a 2D plane
def plotR2(coords):
    
    fig = plt.figure()
    ax = fig.gca()

    # todo maybe: concave hull for funsies so the coordinates don't have to be put in "order"

    # Plot a patch for each coordinate set, creating each polygon
    for idx, coordSet in enumerate(coords):
        ax.add_patch(patches.Polygon(coords[idx], fill = True))
    
    ax.set_ylim([-20, 20])
    ax.set_xlim([-20, 20])
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()
    plt.savefig("test.png")

# Inputs: Properly formatted text file containing the coordinates of polygon objects
# Effects: Send extracted coordinates to the plotter function plotR2()
def main():
    # Parse input file argument
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input')
    args = parser.parse_args()
    file = args.input


    # Read in lines and do a bit of clean up. But user should follow the relatively easy format specified.
    raw_coordinates = [line.rstrip().replace(" ", "") for line in open(file).readlines()]

    # Create coordinate pairs
    raw_coordinates = list(map(lambda x: tuple(x.split(",")), raw_coordinates))

    print(raw_coordinates)

    # Sets of coords are delimited by single blank lines in the text file which become --> ('',)
    coordinateSets = [] # List of np arrays, each N by 2 array representing the 2D coordinates of a polygon's vertices

    first_idx = 0; # Indicates the start of the slice from raw_coordinates containing a set of coordinates

    # Slice out each coordinate set based on the delimiter, cast to np.float arrays
    for idx, coord_pair in enumerate(raw_coordinates):
        if coord_pair == ('',):
            coordinateSets.append(np.array(raw_coordinates[first_idx:idx]).astype(np.float))
            first_idx = idx + 1
    coordinateSets.append(np.array(raw_coordinates[first_idx:]).astype(np.float)) # Slice out the last set

    # Plot polygons
    plotR2(coordinateSets)
    
    

if __name__ == '__main__':
    main()