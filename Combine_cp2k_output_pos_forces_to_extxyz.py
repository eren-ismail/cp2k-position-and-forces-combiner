# Author: Ismail Eren
# Description: This python script combines trajectory and its force files outputed from CP2K and turns them into simple extxyz fileformat
# similar to ASE which can be later be used as dataset in Allegro.
file1_path = input("Enter the path to the first file: ")
file2_path = input("Enter the path to the second file: ")
output_path = input("Enter the path for the combined output file: ")
periodicity_question=input("Do you want to use periodicity? (Y/N)")
if periodicity_question == "Y":
    lattice_info = input("Please enter the lattice constants (X1 X2 X3 Y1 Y2 Y3 Z1 Z2 Z3): ")
    pbc_info = input("Please enter PBC (ex T T T):")

with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2, open(output_path, 'w') as output_file:
    for line1, line2 in zip(file1, file2):
        columns1 = line1.strip().split()
        columns2 = line2.strip().split()
        if columns1 == columns2:
            # Lines are the same
            if len(columns1) == 1:
                # Single column, write as it is
                output_file.write(line1)
            else:
                # Multiple columns, extract the last column
                last_col = columns1[-1]
                if periodicity_question == "Y":
                    output_file.write(f"Lattice=\"{lattice_info}\" Properties=species:S:1:pos:R:3:forces:R:3 energy={last_col} pbc=\"{pbc_info}\"\n")
                else:
                    output_file.write(f"Properties=species:S:1:pos:R:3:forces:R:3 energy={last_col}\n")
        else:
            # Lines are different, combine lines from both files
            combined_line = '\t'.join([columns1[0]] + columns1[1:] + columns2[1:]) + '\n'
            output_file.write(combined_line)

