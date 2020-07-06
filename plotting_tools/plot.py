import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import argparse, sys

def plotR2(coords):
    
    fig = plt.figure()
    ax = fig.gca()

    # todo: for each coordinate set, sort the coordinates in CCW order so that it plots the polygon correctly
    # since it will connect the vertices in the order given


    for idx, coordSet in enumerate(coords):
        ax.add_patch(patches.Polygon(coords[idx], fill = True))
    
    ax.set_ylim([-20, 20])
    ax.set_xlim([-20, 20])
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()
    plt.savefig("test.png")


def main():
    # Parse input file argument
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input')
    args = parser.parse_args()
    file = args.input

    
    coordinateSets = [] # List of arrays, each N by 2 array representing the 2D coordinates of a polygon's vertices

    # Read in lines for text file, create a list of tuples with no association (yet)
    raw_coordinates = [tuple(line.rstrip().replace(" ", "").split(",")) for line in open(file).readlines()]
    print(raw_coordinates)

    first_idx = 0; # Index indicating the first coordinate pair of a given set. Sets are delimeted by blank lines in the text file
    for idx, pair in enumerate(raw_coordinates):
        if pair == ('',): # When we hit a blank line, slice out the coordinates since the last encounter
            coordinateSets.append(np.array(raw_coordinates[first_idx:idx]))
            first_idx = idx + 1
    coordinateSets.append(np.array(raw_coordinates[first_idx:])) # Slice out the last set

    # Plot polygons
    plotR2(coordinateSets)
    


    

if __name__ == '__main__':
    main()