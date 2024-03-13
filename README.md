# Automated Path Planning for Micro and Nano Fibers on Non-Planar Surfaces

## introduction

This Python program is a key part of Zhu Jingjing's graduation thesis. It's designed to automate the path planning process for laying down micro and nano fibers on non-flat surfaces, specifically on parts of a cylinder to mimic human bones. The goal is to fabricate scaffolds with high degrees of control.

## Features

- **Cylinder Mimicking Human Bones**: Focuses on a cylindrical part, simulating the structure of human bones.
- **Highly Controllable Scaffolds**: Enables the creation of scaffolds with precise control over the fiber layout.
- **Automated Path Planning**: Automates the computation of paths for fiber deposition on the specified non-planar surface.

## Requirements

- Python 3.12
- NumPy

## Installation

1. Ensure that Python 3.12 is installed on your system.
2. Install NumPy using pip:
   
   ``` pip install numpy ```

## Usage

1. Modify the parameters in the script as needed, such as the radius of the cylinder, the length, the cutting height, and the interval between paths.
2. Run the script:
   
   ```python main.py```
3. The program will generate a text file (`cylinder.txt`) with the planned paths for laying down the fibers.

## Parameters

- `F`: Speed of the path planning.
- `r`: Radius of the cylinder.
- `Z`: Initial Z height.
- `h`: Cutting height of the cylinder.
- `L`: Length of the cylinder.
- `xianc`: Chord length.
- `interval`: Interval between each path.
- `layers`: Number of layers to be planned.
- `Z_up`: Initial Z offset for each layer.

## Contributing

Feel free to fork the project and submit pull requests with any enhancements or fixes.


## Acknowledgments

This project is part of Zhu Jingjing's graduation thesis aimed at advancing the field of scaffold fabrication using automated path planning.

