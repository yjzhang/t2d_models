import tellurium as te

r = te.loadSBMLModel('MODEL1112110003_modified.xml')
print(r.getCurrentAntimony())
result = r.simulate(0, 10)
