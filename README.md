# Industry---Casualty-Challenge

## Overview
### Business Need
A common frustration in the industry, especially when it comes to getting business insights from tabular data, is that the most interesting questions (from their perspective) are often not answerable with observational data alone. These questions can be similar to:
“What will happen if I halve the price of my product?”
“Which clients will pay their debts only if I call them?”
Judea Pearl and his research group have developed in the last decades a solid theoretical framework to deal with that, but the first steps toward merging it with mainstream machine learning are just beginning. 

### causal graph
The causal graph is a central object in the framework mentioned above, but it is often unknown, subject to personal knowledge and bias, or loosely connected to the available data. The main objective of the task is to highlight the importance of the matter in a concrete way.

expected to attempt the following tasks:
	Perform a causal inference task using Pearl’s framework;
	Infer the causal graph from observational data and then validate the graph;
	Merge machine learning with causal inference;

### Data 
You can extract the data from <a href="https://www.kaggle.com/uciml/breast-cancer-wisconsin-data">kaggle</a> or from <a href="https://archive-beta.ics.uci.edu/ml/datasets?name=breast">UCI Machine Learning Repository</a>. In the latter you can find even more data that you may explore further. To understand more about the data, and how it is collected we highly recommend reading this paper: <a href="https://www.researchgate.net/publication/2302195_Breast_Cancer_Diagnosis_and_Prognosis_Via_Linear_Programming#pf1">(PDF)</a> <a href="https://www.researchgate.net/publication/2302195_Breast_Cancer_Diagnosis_and_Prognosis_Via_Linear_Programming#pf1">Breast Cancer Diagnosis and Prognosis Via Linear Programming (researchgate.net).</a> 



Features in the data are computed from a digitized image of a fine needle aspirate (FNA) of a breast mass.
Attribute Information:
	ID number
	Diagnosis (M = malignant, B = benign)
	The remaining (3-32)
	Ten real-valued features are computed for each cell nucleus:
	radius (mean of distances from center to points on the perimeter)
	texture (standard deviation of gray-scale values)
	Perimeter
	Area
	smoothness (local variation in radius lengths)
	compactness (perimeter^2 / area - 1.0)
	concavity (severity of concave portions of the contour)
	concave points (number of concave portions of the contour)
	Symmetry
	fractal dimension ("coastline approximation" - 1)
	The mean, standard error and "worst" or largest (mean of the three largest values) of these features were computed for each image, resulting in 30 features. For instance, field 3 is Mean Radius, field 13 is Radius SE, field 23 is Worst Radius. All feature values are recorded with four significant digits.
	Missing attribute values: none
Class distribution: 357 benign (not cancer), 212 malignant (cancer)

## TO DO:
	1: Data Exploration:

		Conduct an exploratory data analysis on the data & communicate useful insights.

		Ensure that you identify and treat all missing values and outliers in the dataset by using appropriate methods.


		Perform feature extraction and scaling 

	2: Causal learning:

		Split data into training and hold-out set 

		Create a causal graph using all training data and get the insights (this will be considered the ground truth)

		Create new causal graphs using increasing fractions of the data and compare with the ground truth graph
		The comparison can be done with a Jaccard Similarity Index, measuring the intersection and union of the graph edges

		After reaching a stable causal graph, select only variables that point directly to the target variable

		Train one model using all variables and another using only the variables selected by the graph

		Measure how much each of the models overfit the hold-out set created in step 1.

## Package structure:
