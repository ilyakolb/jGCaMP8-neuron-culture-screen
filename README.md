## jGCaMP8 neuronal culture screening results and plots
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ilyakolb/jGCaMP8-neuron-culture-screen/HEAD)

**The quickest way to reproduce the plots in the manuscript is using the Binder notebook link above**

The notebooks here can be used to generate the plots from the jGCaMP8 article.




Instructions for reproducing the plots are below.

To activate the relevant Anaconda environemt, execute `conda activate jgcamp8-culture`

**Figure 1B**

* Run `interactive-multiparameter-screening-plot.ipynb`
* Plot `Half-rise time (1 AP)` on x axis and `dprime (1AP)` on y axis

**Figure 1D**

* Run `AP_plots.ipynb` with the `plot_subset_for_paper` flag set to 1 to plot only the indicators in the figure; or set to 0 to plot all indicators (jGCaMP8f, jGCaMP8m, jGCaMP8s,jGCaMP8.712, GCaMP6s, GCaMP6f, jGCaMP7f, jGCaMP7s, jGCaMP7c, jGCaMP7b, XCaMP-Gf, XCaMP-G, XCaMP-Gf0)

**Figure 1E**

* Run `grand-avg-hits-plotting.ipynb` (1 AP data)

**Supp. Fig. 2**

* Run `screening_rounds_summary.ipynb`

**Supp. Fig. 3**

* Run `grand-avg-hits-plotting.ipynb` (3,10,160 AP data)

**Supp. Fig. 7**

* Run `linearity-assessment.ipynb`