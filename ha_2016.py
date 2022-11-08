import tellurium as te

r = te.loada("""
species $G; species $I; species $beta; species $sigma; species $M; species $ISR;

//rates
G' = R0 - (EG0 + SI*I)*G; // glucose concentration in blood (mg/dL)
I' = beta*ISR/V - k*I; // insulin concentration in blood
beta' = ((P - A)*beta)/tau_beta; // beta cell mass - based on workload hypothesis
// functional compensation - persistent high glucose shifts the glucose response curve to the left
// gamma is glucose response curve shift by beta cells?
gam' = (gam_inf - gam)/tau_gam;
// persistent high glucose increases maximal insulin concentration
sigma' = (sigma_inf - sigma)/tau_sigma; //sigma is beta cell function
SI' = (S0 - SI)/tau_SI; // insulin sensitivity

// auxiliary functions
M := G^kM/(alpha_M^kM + G^kM); // beta cell metabolism
ISR := sigma*(M + gam)^kISR/(alpha_ISR^kISR + (M + gam)^kISR); // insulin secretion rate

P := P_max*(ISR^kP/(alpha_P^kP + ISR^kP)); // beta cell proliferation
A := A_max*(M^kA/(alpha_A^kA + M^kA)) + A_b; // beta cell apoptosis

gam_inf := gam_max/(1 + exp(-(G - gam_s)/gam_n)) - gam_0;

// sigma calculation
sigma_inf := sigma_ISRinf*sigma_Minf + sigma_b;
M_sigma := M_max*(G-G_sigmas)^kM/(alpha_M^kM + (G-G_sigmas)^kM); #M_Gsh
ISR_sigma := sigma*(M_sigma + gam)^kISR/(alpha_ISR^kISR + (M_sigma + gam)^kISR); #ISR_Gsh

// positive feedback from ISR
sigma_ISRinf := sigma_ISRmax/(1 + sigma_ISRk*exp(-(ISR_sigma - sigma_ISRs)/sigma_ISRn)); #sigma_ISRI

# negative feedback from M
sigma_Minf := 1 - sigma_Mmax/(1 + sigma_Mk*exp(-(M_sigma - sigma_Ms)/sigma_Mn)); #sigma_MI

// parameters
S0 = 0.8;
EG0 = 1.44;
R0 = 864;
V = 0.01;
k = 700;

// time scales (in days)
tau_gam = 2.14;
tau_sigma = 10.71;
tau_beta = 42.85;
tau_SI = 16.2;

// auxilliary function parameters (based on zdf rats)
M_max = 1;
kM = 2;
alpha_M = 150;

kISR = 2;
alpha_ISR = 1.2;

P_max = 4.55;
kP = 4;
alpha_P = 41.77;

A_max = 3.11;
kA = 6;
alpha_A = 0.44;
A_b = 0.8;

gam_max = 0.2; #G_bar
gam_s = 99.9; #Gs
gam_n = 1; #Gn
gam_0 = 0.1; #Gshft

sigma_ISRmax = 867.6; #ISRI_bar
sigma_ISRs = 0.1; #ISRI_s
sigma_ISRn = 0.1; #ISRI_n
sigma_ISRk = 1; #ISRI_k
sigma_b = 3;

sigma_Mmax = 1; #MI_bar
sigma_Ms = 0.2; #MI_s
sigma_Mn = 0.02; #MI_n
sigma_Mk = 0.2; #MI_k

// this value isn't provided in the paper, but it is in the code (as sigma_Gsh).
G_sigmas := 75; #sigma_Gsh

//initial values
G = 99.7664
I = 9.025 
beta = 2.00069  
gam = -0.006666 
sigma = 536.7163 
SI = 0.8

// Events

// variables
G is "plasma glucose concentration (mg/dL)";
I is "plasma insulin concentration (microU/mL)";
beta is "beta cell mass (mg)";
gam is "dose response curve shift";
sigma is "beta cell function (microU/(microg*d))";
SI is "insulin sensitivity (mL/(microU*d))";

// functions
M is "metabolic rate";
ISR is "insulin secretion rate";
P is "beta cell proliferation rate";
A is "beta cell apoptosis rate";

// parameters
R0 is "average daily glucose production rate";
EG0 is "insulin-independent glucose disposal rate";
S0 is "initial insulin sensitivity";
V is "volume of distribution";
k is "insulin clearance rate";
""")

result = r.simulate(0, 80)
print(result)
