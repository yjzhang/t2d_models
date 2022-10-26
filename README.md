Tools:

- **tellurium**
- MATLAB
- Octave
- PySB
- COPASI

Parameter inference:
???

Models implemented:
- De Gaetano 2008 - https://pubmed.ncbi.nlm.nih.gov/18780774/, https://www.ebi.ac.uk/biomodels/MODEL1112110003 - I could not get this to work (yet)
- Topp 2000 - https://www.sciencedirect.com/science/article/pii/S0022519300921507, https://www.ebi.ac.uk/biomodels/BIOMD0000000341 (I didn't use this; I just implemented it myself, with the same results I believe.)
- Ha 2016 - https://academic.oup.com/endo/article/157/2/624/2422698 - I believe the description in the paper is missing at least one parameter value.
- Dalla Man 2007 - http://www.ncbi.nlm.nih.gov/pubmed/17926672, https://www.ebi.ac.uk/biomodels/BIOMD0000000379
- De Gaetano 2019 - https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0222833#pone.0222833.e034 - this is a very complicated model...

References: ...
- MODEL1112110003_url.xml: Gaetano 2008 (model for diabetes progression) - this does not work as-is. I tried to modify it to make it work; now it compiles, but I think the description of the model in the paper might not be enough to implement it.
- BIOMD0000000379_url.xml: Dalla Man 2007 (model for meal insulin/glucose dynamics) 
