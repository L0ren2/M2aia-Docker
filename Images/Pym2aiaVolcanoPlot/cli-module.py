import m2aia as m2
from m2aia.utils import volcano
from m2aia.utils import binning
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sea
import seaborn_image as seai
import SimpleITK as sitk
import wget
import zipfile
import pathlib
import sys

input_file = "/data1/" + str(sys.argv[1])

image = m2.ImzMLReader(input_file)
image.Execute()


mask = image.GetMaskArray()
# bin peaks for pixels in a region
bin_ass, bin_xs, bin_counts = binning.bin_peaks(image, mask)
bin_counts = [len(x) for x in bin_counts]
print("Binned peaks found", len(bin_xs))

# FILTER PEAKS
# peaks mus occur in more than p*100 of the spectra
p = 0.1
xs = bin_xs[bin_counts > (p*np.sum(mask>0))]
print("Filtered peaks found", len(xs))
     

# generate a mask by thresholds
mask = image.GetArray(700,2)
# mask containse labels (0: background, 1: HT (healthy tissue), 2: CT (cancerous tissue))
mask = (mask > 300).astype(np.int16) + (mask > 100).astype(np.int16)

p_fc_sig = volcano.volcano_plot_data(image, mask, xs)

# Plot
plt.figure()
sea.scatterplot(x=p_fc_sig[:,1], y=-np.log10(p_fc_sig[:,0]),hue=p_fc_sig[:,2])
plt.xlabel("log2FC")
plt.ylabel("-log10(p)")
f = open("/output1/out.txt")
s1 = ("x=", p_fc_sig[:,1])
s2 = ("y=", -np.log10(p_fc_sig[:,0]))
s3 = ("hue=", p_fc_sig[:,2])
f.write(str(s1) + str(s2) + str(s3))
f.close()
print("s1", s1)
print("s2", s2)
print("s3", s3)
plt.savefig("/output1/out.png")
