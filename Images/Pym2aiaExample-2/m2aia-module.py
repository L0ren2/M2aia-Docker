import m2aia as m2
import numpy as np
import matplotlib as plt
import seaborn as sns
import SimpleITK as sitk

import sys

file_names = ["/data1/" + sys.argv[1], "/output1/" + sys.argv[2]]

mzVal = 150 # default
tol   = 0.25
for i in range(0, len(sys.argv) - 1):
    if sys.argv[i] == "--mz" or sys.argv[i] == "-mz":
        mzVal = float(sys.argv[i + 1])
    if sys.argv[i] == "--tol":
        tol = float(sys.argv[i + 1])

sns.set_theme(style="darkgrid")
sns.set(rc={'figure.figsize':(19,6)})

def showimg(image, cmap=None, title=None):
    sns.set_theme(style="ticks")
    fig = plt.figure(figsize = (10,10)) # create a 5 x 5 figure 
    ax = fig.add_subplot(111)
    ax.tick_params(
        which='both',
        bottom=False,
        left=False,
        labelleft=False,
        labelbottom=False)
    x = [10,60]
    y = [10,10]

    spacing = I.GetSpacing()
    ax.plot(x, y, color="white", linewidth=3)
    ax.text(x[0], y[0]+7, f"{int(spacing[0]*(x[1]-x[0])* 1000)} μm", color="white",size=14)
    if title:
        ax.text(x[0], y[0]-3, title, color="white", size=14)
    ax.imshow(image, interpolation='none', cmap=cmap)

    return fig, ax 

# Set the parameters
I = m2.ImzMLReader(str(file_names[0]))
#I.SetNormalization(m2.m2NormalizationTIC)
I.SetSmoothing(m2.m2SmoothingGaussian,12)
I.SetBaselineCorrection(m2.m2BaselineCorrectionTopHat)
I.Execute()

# 1) GetArray(mz, tol) will generate a numpy array, loosing all real world information like the origin, spacing or direction of the image.
# 2) GetImage(mz, tol) will generate a itkImage, that holds those real world information. 
#
# If ion images are produced for further analysis pipelines, it is recommended to use the GetImage method and save the images as .nrrd files [1], using SimpleITK [2].
# E.g.: sitk.WriteImage(I.GetImage(mz,tol), path/to/file.nrrd)
#
# [1] http://teem.sourceforge.net/nrrd/format.html
# [2] https://simpleitk.org/

I.SetPooling(m2.m2PoolingMean)

#MUSC = I.GetImage(1088.868, 0.25)
#CONT = I.GetImage(177.919, 0.25)
TUMOR = I.GetImage(mzVal, tol)
FileWriter = sitk.ImageFileWriter()
FileWriter.SetFileName(str(file_names[1]))
FileWriter.Execute(TUMOR)

#showimg(np.squeeze(MUSC), cmap='gray', title='musculature (m/z 1088.868±0.249 Da)')
#showimg(np.squeeze(CONT), cmap='gray', title='gut content (m/z 177.919±0.2 Da)')
#showimg(np.squeeze(NEMA), cmap='gray', title='nematode cysts (m/z 262.177±0.2 Da)')
