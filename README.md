1.Scatter plot:
 In the file "multiple_plot_figure.png", I use the scatter plot
to study correlations between few columns e.g.
A1. GRE Score vs Chances of Admission
B1. TOEFL Score vs Chances of Admission
C1. GRE Score vs CGPA
D1. TOEFL Score vs CGPA

Interpretation:

From A and B it seems that the chances of
admission are directly(positively) correlated to the GRE and
TOEFL Score. While C and D indicate that the CGPA
is also correlated(positively) to the GRE score! That means chances
of admission are also positively correlated to the CGPA/

2. Multiple axes plot:
Next, we try to add the third column by using the multiple-axes plots, see e.g.
the file "multiple_axes_plot.png".
A2. GRE Score vs CGPA with Chances of Admission represented
by the size of the circles.
B2. TOEFL Score vs CGPA with Chances of Admission represented
by the size of the circles.
C2. SOP vs LOR with University rating by the size of the circles.
D2. GRE Score vs TOEFL with Chances of Admission represented
by the size of the circles.

Interpretation:
Looking at A2, we can see that likewise C1 it gives us the correlation of
GRE score vs CGPA, but besides on the third axis represented by the size
of the circles, it also correlates the chances of admission to these two variables.
That means the single plot A2  supersedes C1 and A1!. In the same sense, B2
supersedes B1 and D1.

Next, in C2 the university rating in which a candidate can be admitted
is projected on the SOP and LOR score. Higher scores in two parameters mean he or she can be admitted to a university with a higher rating.

Finally, D2 tells that the chances of admission enhance with the higher
GRE and TOEFL scores.

3. Multiple Columns: Since the SOP and LOR score both vary in the range 0-5, both
can be projected on the same axes, e.g. see file "SOP_LOR_Chances_of_Admit_scatter.png"
in which SOP and LOR are plotted on the x-axis and chances of admission on the y-axis.

Interpretation:
Interestingly, for a higher SOP score, the chances of admission can go up to
a very high-value e..g 1, but with the same SOP score the chances of
admission can also below, that means SOP score and chances of admission are
not linearly correlated.
The LOR score shows a similar pattern with slight differences in the
the higher side of LOR score where minimum chances of admission are only
higher with a higher LOR score.


4. Heat map: In file "GRE_admission_Seaborn_heatmap.png", the correlation
of the matrix of all columns is shown and also the heat color indicate the
size of correlation, the highest correlation is yellowest in color.

Interpretation:
For instance, the correlation between GRE Score and the CGPA is 0.83 which was
also shown in C1 and A2. Additionally, the correlation GRE vs chances of admission
shown in A2 can also be found in the heat map, which is 0.8. Therefore, these plots
supersede even Multiple column plots as in single plots it contains all the
correlations, so we can say this as the master plot.











