# jagramont_python

Hej
This is my Git for my python course 2023 

# Course project in progress:

The script: is the file named ppk_biofilm-quant.ipynb (jupyter notebook)

To runn the Jupyter notebook is necesary to use the conda environment provided in the current respository called 'environment_jorge.yml' (python_test).

The script is designed to read a .csv file that contains Absorvance values. The values are measurements of biofilm production in a system of 96 well plates.

Biofilm production was quantified along five days.

Each culture treatment (all possible combinations of each member of PPK: 8 possible combinations) has at least 8 technical replicates.

The script can read the data of the .csv file and make a line plot to explore the biofilm production of each culture treatment along five days.

The script can analyze the biofilm production at any timepoint of the assay. The analysis consist on checking the distribution of the data, determine the most adecuated statistical tool to use: one-way anova for normally distributed data and Kruskal-Wallis test for non-normally distributed data.

After using one of the previus tests, the script can perform a pos hoc analysis: Tukey test if the data was analysed using one-way anova or Dunn test if the data was analyzed by Kruskal-Wallis test.

After the statistical analysis it is possible to generate heatmaps for the comparation matrixes of the post hoc analysis to help you visualize the statistically significant differences among the treatments.

The script will generate a box plot showing the mean and SD for each treatment per day. 