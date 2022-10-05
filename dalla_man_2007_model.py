import tellurium as te

r = te.loadSBMLModel('BIOMD0000000379_url.xml')
print(r.getCurrentAntimony())
result = r.simulate(0, 10)
