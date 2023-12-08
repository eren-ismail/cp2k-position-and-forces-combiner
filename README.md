# cp2k-position-and-forces-combiner
Create simple extxyz file by combining output trajectory and corresponding forces from Cp2k results into one file.

# How to use
 You have to follow specific order.
 First give the destination to your trajectory xyz files that has the positions.
 Then script prompts for the second file, then choose your force file.

 In this way, you have positions for first three columns (after species), then next three columns are the forces.

 XYZ file generally does not contain information for lattice parameters and periodicity.
 You can also add these.

 Input "Y" if you wish so (only upper case Y works.)
 Then enter lattice parameters in the X1 X2 X3 Y1 Y2 Y3 Z1 Z2 Z3 order,
 and enter "T T T" for pbc.

# What can you do with this?
 You can use the final file as a dataset for training with Nequip + Allegro to create 
 machine learning interatomic potential.

 # Disclaimer
 I didn't test that ase can read or not.

 # Legal notice:
 I have no rights for CP2K, ASE, Nequip and Allegro. This is just a basic script that
 combining and converting files.

 Have a nice day!
 Ismail Eren