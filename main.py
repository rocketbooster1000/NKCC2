from proccess import process_and_plot as pplot

design_identity = "E"
# folders = ["temp0.2", "temp0.3"]
folders = ["temp0.2", "temp0.3", "temp0.4"]
# folders = ["temp0.2"]

# pplot("E", ["temp0.3"], split_pdb="first", source="E F")
# pplot("F", ["temp0.3"], split_pdb="second", source="E F")

# pplot("D", ["temp0.3", "temp0.2"])
pplot(design_identity, folders)
