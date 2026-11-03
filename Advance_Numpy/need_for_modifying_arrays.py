"""Why Do We Need to Modify Arrays in Data Science & Data Analytics?

1. Matching Machine Learning Model Requirements
- Machine learning algorithms (like Scikit-Learn) strictly require data in a specific shape—usually a 2D table where rows are samples and columns are features: (samples, features).
- If your data is a 1D list or has mismatched dimensions, the model will crash. You must use reshape() to fit the algorithm's expectations.

2. Preparing Images for Deep Learning (Flattening)
- Images are stored as 3D arrays (Height x Width x Color Channels, like 28x28x3).
- Traditional neural network layers cannot read 3D grids directly. We use flatten() or ravel() to convert that 3D image into a single 1D line of pixel values before passing it to the network.

3. Mathematical and Statistical Operations
- Data science relies heavily on linear algebra (matrix multiplication, dot products, etc.). 
- To multiply two matrices, their shapes must align perfectly. Reshaping arrays allows you to align dimensions so mathematical formulas can run correctly.

4. Saving Memory and Boosting Performance
- Real-world datasets often contain millions of rows. 
- Using efficient array modifications (like ravel() instead of flatten()) creates a "view" in memory rather than duplicating heavy data. This saves RAM and makes code run significantly faster."""

