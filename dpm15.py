# source: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0222833

model_antimony = """

// parameters

t0 = 0;
tend = 1080;
Bmax = 4000;
B0 = 1000;
vBG = 2;
GB50 = 9;
n0 = 0.04;
kxnG0 = 0.02;
knendprop = 0.4;
kGG = 0.4;
Gf0 = 4.2;
kXA = 0.4;
A0 = 5;
VG = 0.19;
VI = 0.19;
W = 70;
kXIstart = 0.05;
kXIend = 0.45;
kXGI0max = 0.08;
kXGI00 = 0.0001;
fkXGImin = 0.05;
tkXGIstart = 216;
vkXGI = 3;
tkXGI50 = 800;
lamGI0 = 0.015;
flamGImin = 0.05;
tlamGIstart = 216;
kIB0max = 0.5;
fkIBmin = 0.25;
tkIBstart = 216;
vkIB = 2.5;
tkIB50 = 950;
kJS0 = 0.023;
aLyKxgi = 0.1;
bLyKxgi = 0.009;
LyKxgiCurr = 0;
aLyLamgi = 0.3;
bLyLamgi = 0.01;
LyLamgiCurr = 0;
aLyKjs = 0.05;
bLyKjs = 0.002;
LyKJS = 0;
tau0 = 360;
tauend = 1800;
tau1 = 420;
M1gluc = 417;
tau2 = 720;
M2gluc = 280;
tau3 = 1080;
M3gluc = 280;
kXgbroxmax = 0.0059;
Gbrox50 = 0.5;
kGJ = 0.025;
fGJ = 0.9;
kXG = 0.001;
kGImax = 0.75;
LG50 = 0.05;
L0 = 15;
kXL = 0.04;
fLGmin = 0.15;
lamLG = 0.55;
fIJ = 1.15;
JG50 = 200;
vIG = 3;
GI50 = 14.4;
ClInulin = 0.0018;
Furine = 0.00002;
Du = 0;
kGUmax = 0.027;
CGU50 = 19;
lamVZ = 8;
lamQZ = 7;
If0 = 19.8;
IKXGI50 = 333;
kGLmax = 0.0685;
kLGmax = 2.56;
knstart = 0.00085;
kBBmin = -0.0104;
kAG = 0.395;

// Variables
B = B0;
kBB;
n = n0;
kXnG;
kn;
Gf = Gf0;

// display names
B is "beta-cell population size";
kBB is "beta-cell net replication rate in fraction per month";
mu is "rate constant for additional beta-cell mortality";
n is "beta-cell replication reserve";
kXnG is "glucotoxicity (glucose-dependent pancreatic replication reserve decay)";
kn is "spontaneous recovery rate of the pancreas";
Gf is "fasting glycemia";
A is "glycosylated haemoglobin (percent)";
If is "fasting serum insulin concentration";
kXI is "apparent first-order elimination rate constant for insulin";
kXGImax is "maximal insulin-depndent tissue glucose uptake rate as modified by therapy";
lamGI is "hepatic insulin sensitivity (natural value of insulin- and glucose-dependent HGO suppression) as modified by therapy";
kIBmax is "maximal insulin secretion per million beta-cells as modified by therapy";
kJS is "apparent first-order stomach emptying as modified by therapy";
Gn is "weighted glycemia toxicity determining n suppresion, as fraction of normal";
GB is "weighted glycemia average stimulating beta-cell replication";
HomaIR is "homeostasis model assessment index of insulin resistance";
HomaB is "homeostasis model assessment index of beta-cell function";
Igenicx is "insulinogenic index";
ClampM1 is "Clamp M value first step";
ClampM2 is "Clamp M value second step";
S is "glucose content in the stomach";
J is "glucose content in the absorptive bowel";
ra is "rate of glucose appearance in the systemic circulation (from the gut)";
G is "plasma glucose concentration (in fast time)";
L is "serum  glucagon concentration (in fast time)";
I is "serum insulin concentration (in fast time)";
q is "density of glucose amount in tubule with respect to normalized tubule length";
v is "density of tubular water volume";
C is "concentration of glucose in pre-urine";
ur is "rate of urinary glucose loss";

"""
