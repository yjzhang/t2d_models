# implementation of bergman's minimal model in tellurium
# https://journals.physiology.org/doi/pdf/10.1152/ajpendo.1979.236.6.e667
# https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7917251/

# https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2769581/ - more recent paper

# 
# this is the one we are using.


import tellurium as te

# I, X, G represent plasma insulin, remote insulin, and plasma glucose.
# Ib is the initial concentration of plasma insulin
# u1(t) is exogenous insulin
# u2(t) is intravenous glucose
# each time point is 1 minute

mm0 = te.loada('''
        model minimal
          G -> ; p1*G + X*G
          -> G; p1*Gb + u2/Vol

          I -> ; n*I
          -> I ; p4*u1

          X -> ; p2*X
          -> X ; p3*(I - Ib)

          p1 = 0.035
          p2 = 0.05
          p3 = 0.000028
          p4 = 0.098
          n = 0.142
          Vol = 117.0
          Gb = 80

          Ib = p4/n
          X = 0
          G = Gb
          I = Ib

          u1 = 0
          u2 = 0
        end
        ''')
