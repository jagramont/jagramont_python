# jagramont_python

Hej
This is my Git for my python course 2023 

# Course project in progress:

The script, named "ppk_biofilm-quant.ipynb," is a Jupyter notebook that requires a specific conda environment provided in the repository, named 'environment_jorge.yml' (python_test), to run successfully.

This script is designed for analyzing data from a .csv file containing absorbance values. These values represent measurements of biofilm production in a system of 96-well plates. The biofilm production data spans across five days.

For the experiment, each culture treatment, which encompasses all possible combinations of PPK members (8 possible combinations), has at least 8 technical replicates.

The script's capabilities include reading the data from the .csv file and creating line plots to explore the biofilm production of each culture treatment over the course of five days.

Additionally, the script allows you to perform data analysis at any timepoint of the assay. The analysis involves checking the data distribution and selecting the most suitable statistical test: one-way ANOVA for normally distributed data or the Kruskal-Wallis test for non-normally distributed data.

Following the initial statistical test, the script offers post hoc analysis options: Tukey test if the data was analyzed using one-way ANOVA or Dunn test if the data was analyzed by the Kruskal-Wallis test.

After conducting the statistical analysis, the script can generate heatmaps for the comparison matrices derived from the post hoc analysis. These heatmaps provide a visual representation of statistically significant differences among the treatments.

Finally, the script produces box plots that display the mean and standard deviation for each treatment per day.

In summary, this versatile script allows you to explore, analyze, and visualize biofilm production data, making it a valuable tool for experimental data analysis.

After the statistical analysis it is possible to generate heatmaps for the comparation matrixes of the post hoc analysis to help you visualize the statistically significant differences among the treatments.

The script will generate a box plot showing the mean and SD for each treatment per day. 