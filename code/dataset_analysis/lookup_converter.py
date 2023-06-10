import pprint
import galois
from analysis import *

GF2 = galois.GF(2)

matrices_as_strings = {
# latex_marts_part1.txt
"mat:shark":'''
ce_x & 95_x & 57_x & 82_x & 8a_x & 19_x & b0_x & 01_x\\
e7_x & fe_x & 05_x & d2_x & 52_x & c1_x & 88_x & f1_x\\
b9_x & da_x & 4d_x & d1_x & 9e_x & 17_x & 83_x & 86_x\\
d0_x & 9d_x & 26_x & 2c_x & 5d_x & 9f_x & 6d_x & 75_x\\
52_x & a9_x & 07_x & 6c_x & b9_x & 8f_x & 70_x & 17_x\\
87_x & 28_x & 3a_x & 5a_x & f4_x & 33_x & 0b_x & 6c_x\\
74_x & 51_x & 15_x & cf_x & 09_x & a4_x & 62_x & 09_x\\
0b_x & 31_x & 7f_x & 86_x & be_x & 05_x & 83_x & 34_x
''',
"mat:shark-inv":'''
e7_x &30_x &90_x &85_x &d0_x &4b_x &91_x &41_x\\
53_x &95_x &9b_x &a5_x &96_x &bc_x &a1_x &68_x\\
02_x &45_x &f7_x &65_x &5c_x &1f_x &b6_x &52_x\\
a2_x &ca_x &22_x &94_x &44_x &63_x &2a_x &a2_x\\
fc_x &67_x &8e_x &10_x &29_x &75_x &85_x &71_x\\
24_x &45_x &a2_x &cf_x &2f_x &22_x &c1_x &0e_x\\
a1_x &f1_x &71_x &40_x &91_x &27_x &18_x &a5_x\\
56_x &f4_x &af_x &32_x &d2_x &a4_x &dc_x &71_x
''',
"mat:square":'''
02_x & 01_x & 01_x & 03_x\\
03_x & 02_x & 01_x & 01_x\\
01_x & 03_x & 02_x & 01_x\\
01_x & 01_x & 03_x & 02_x
''',
"mat:square-inv":'''
0e_x & 09_x & 0d_x & 0b_x\\
0b_x & 0e_x & 09_x & 0d_x\\
0d_x & 0b_x & 0e_x & 09_x\\
09_x & 0d_x & 0b_x & 0e_x
''',
"mat:tavares":'''
93_x & 13_x & 57_x & da_x & 58_x & 47_x & 0c_x & 1f_x\\
13_x & 93_x & da_x & 57_x & 47_x & 58_x & 1f_x & 0c_x\\
57_x & da_x & 93_x & 13_x & 0c_x & 1f_x & 58_x & 47_x\\
da_x & 57_x & 13_x & 93_x & 1f_x & 0c_x & 47_x & 58_x\\
58_x & 47_x & 0c_x & 1f_x & 93_x & 13_x & 57_x & da_x\\
47_x & 58_x & 1f_x & 0c_x & 13_x & 93_x & da_x & 57_x\\
0c_x & 1f_x & 58_x & 47_x & 57_x & da_x & 93_x & 13_x\\
1f_x & 0c_x & 47_x & 58_x & da_x & 57_x & 13_x & 93_x
''',
"mat:khazad":'''
01_x & 03_x & 04_x & 05_x & 06_x & 08_x & 0b_x & 07_x\\
03_x & 01_x & 05_x & 04_x & 08_x & 06_x & 07_x & 0b_x\\
04_x & 05_x & 01_x & 03_x & 0b_x & 07_x & 06_x & 08_x\\
05_x & 04_x & 03_x & 01_x & 07_x & 0b_x & 08_x & 06_x\\
06_x & 08_x & 0b_x & 07_x & 01_x & 03_x & 04_x & 05_x\\
08_x & 06_x & 07_x & 0b_x & 03_x & 01_x & 05_x & 04_x\\
0b_x & 07_x & 06_x & 08_x & 04_x & 05_x & 01_x & 03_x\\
07_x & 0b_x & 08_x & 06_x & 05_x & 04_x & 03_x & 01_x
''',
"mat:anubis":'''
01_x & 02_x & 04_x & 06_x\\
02_x & 01_x & 06_x & 04_x\\
04_x & 06_x & 01_x & 02_x\\
06_x & 04_x & 02_x & 01_x
''',
"mat:anubis-ke":'''
01_x & 01_x & 01_x & 01_x\\
01_x & 02_x & 04_x & 08_x\\
01_x & 06_x & 14_x & 78_x\\
01_x & 08_x & 40_x & 3a_x
''',
"mat:anubis-ke-inv":'''
71_x & 53_x & 7c_x & 5f_x\\
8c_x & 25_x & c3_x & 6a_x\\
a3_x & ad_x & 71_x & 7f_x\\
5f_x & db_x & ce_x & 4a_x
''',
"mat:rijndael":'''
02_x & 03_x & 01_x & 01_x\\
01_x & 02_x & 03_x & 01_x\\
01_x & 01_x & 02_x & 03_x\\
03_x & 01_x & 01_x & 02_x
''',
"mat:rijndael-inv":'''
0e_x & 0b_x & 0d_x & 09_x\\
09_x & 0e_x & 0b_x & 0d_x\\
0d_x & 09_x & 0e_x & 0b_x\\
0b_x & 0d_x & 09_x & 0e_x
''',
"mat:bksq":'''
03_x & 02_x & 02_x\\
02_x & 03_x & 02_x\\
02_x & 02_x & 03_x
''',
"mat:bksq-inv":'''
ac_x & ad_x & ad_x\\
ad_x & ac_x & ad_x\\
ad_x & ad_x & ac_x
''',
"mat:hierocrypt-3-lower":'''
c4_x & 65_x & c8_x & 8b_x\\
8b_x & c4_x & 65_x & c8_x\\
c8_x & 8b_x & c4_x & 65_x\\
65_x & c8_x & 8b_x & c4_x
''',
"mat:hierocrypt-3-lower-inv":'''
82_x & c4_x & 34_x & f6_x\\
f6_x & 82_x & c4_x & 34_x\\
34_x & f6_x & 82_x & c4_x\\
c4_x & 34_x & f6_x & 82_x
''',
"mat:hierocrypt-3-higher":'''
5_x & 5_x & a_x & e_x\\
e_x & 5_x & 5_x & a_x\\
a_x & e_x & 5_x & 5_x\\
5_x & a_x & e_x & 5_x
''',
"mat:hierocrypt-3-higher-inv":'''
b_x & e_x & e_x & 6_x\\
6_x & b_x & e_x & e_x\\
e_x & 6_x & b_x & e_x\\
e_x & e_x & 6_x & b_x
''',
"mat:hierocrypt-l1-higher":'''
5_x & 7_x\\
a_x & b_x
''',
"mat:hierocrypt-l1-higher-inv":'''
c_x & a_x\\
5_x & b_x
''',
"mat:fox-mu4":'''
01_x & 01_x & 01_x & 02_x\\
01_x & fd_x & 02_x & 01_x\\
fd_x & 02_x & 01_x & 01_x\\
02_x & 01_x & fd_x & 01_x
''',
"mat:fox-mu8":'''
01_x & 01_x & 01_x & 01_x & 01_x & 01_x & 01_x & 03_x\\
01_x & 03_x & 82_x & 02_x & 04_x & fc_x & 7e_x & 01_x\\
03_x & 82_x & 02_x & 04_x & fc_x & 7e_x & 01_x & 01_x\\
82_x & 02_x & 04_x & fc_x & 7e_x & 01_x & 03_x & 01_x\\
02_x & 04_x & fc_x & 7e_x & 01_x & 03_x & 82_x & 01_x\\
04_x & fc_x & 7e_x & 01_x & 03_x & 82_x & 02_x & 01_x\\
fc_x & 7e_x & 01_x & 03_x & 82_x & 02_x & 04_x & 01_x\\
7e_x & 01_x & 03_x & 82_x & 02_x & 04_x & fc_x & 01_x
''',
"mat:fox-mu4-inv":'''
7e_x & e1_x & ad_x & b0_x\\
7e_x & ad_x & b0_x & e1_x\\
7e_x & b0_x & e1_x & ad_x\\
c3_x & 7e_x & 7e_x & 7e_x
''',
"mat:fox-mu8-inv":'''
c6_x & fe_x & 3a_x & 73_x & 6d_x & 0c_x & d2_x & b7_x\\
c6_x & 3a_x & 73_x & 6d_x & 0c_x & d2_x & b7_x & fe_x\\
c6_x & 73_x & 6d_x & 0c_x & d2_x & b7_x & fe_x & 3a_x\\
c6_x & 6d_x & 0c_x & d2_x & b7_x & fe_x & 3a_x & 73_x\\
c6_x & 0c_x & d2_x & b7_x & fe_x & 3a_x & 73_x & 6d_x\\
c6_x & d2_x & b7_x & fe_x & 3a_x & 73_x & 6d_x & 0c_x\\
c6_x & b7_x & fe_x & 3a_x & 73_x & 6d_x & 0c_x & d2_x\\
ea_x & c6_x & c6_x & c6_x & c6_x & c6_x & c6_x & c6_x
''',
"mat:curupira":'''
03_x & 02_x & 02_x\\
04_x & 05_x & 04_x\\
06_x & 06_x & 07_x
''',
"mat:curupira-ke":'''
1d_x & 1c_x & 1c_x\\
1c_x & 1d_x & 1c_x\\
1c_x & 1c_x & 1d_x
''',
"mat:curupira-ke-inv":'''
1c_x & 1d_x & 1d_x\\
1d_x & 1c_x & 1d_x\\
1d_x & 1d_x & 1c_x
''',
"mat:grostl":'''
02_x & 02_x & 03_x & 04_x & 05_x & 03_x & 05_x & 07_x\\
07_x & 02_x & 02_x & 03_x & 04_x & 05_x & 03_x & 05_x\\
05_x & 07_x & 02_x & 02_x & 03_x & 04_x & 05_x & 03_x\\
03_x & 05_x & 07_x & 02_x & 02_x & 03_x & 04_x & 05_x\\
05_x & 03_x & 05_x & 07_x & 02_x & 02_x & 03_x & 04_x\\
04_x & 05_x & 03_x & 05_x & 07_x & 02_x & 02_x & 03_x\\
03_x & 04_x & 05_x & 03_x & 05_x & 07_x & 02_x & 02_x\\
02_x & 03_x & 04_x & 05_x & 03_x & 05_x & 07_x & 02_x
''',
"mat:grostl-inv":'''
13_x & 5a_x & 54_x & 72_x & 50_x & df_x & 45_x & 53_x\\
53_x & 13_x & 5a_x & 54_x & 72_x & 50_x & df_x & 45_x\\
45_x & 53_x & 13_x & 5a_x & 54_x & 72_x & 50_x & df_x\\
df_x & 45_x & 53_x & 13_x & 5a_x & 54_x & 72_x & 50_x\\
50_x & df_x & 45_x & 53_x & 13_x & 5a_x & 54_x & 72_x\\
72_x & 50_x & df_x & 45_x & 53_x & 13_x & 5a_x & 54_x\\
54_x & 72_x & 50_x & df_x & 45_x & 53_x & 13_x & 5a_x\\
5a_x & 54_x & 72_x & 50_x & df_x & 45_x & 53_x & 13_x
''',
"mat:led":'''
4_x & 1_x & 2_x & 2_x\\
8_x & 6_x & 5_x & 6_x\\
b_x & e_x & a_x & 9_x\\
2_x & 2_x & f_x & b_x
''',
"mat:led-inv":'''
c_x & c_x & d_x & 4_x\\
3_x & 8_x & 4_x & 5_x\\
7_x & 6_x & 2_x & e_x\\
d_x & 9_x & 9_x & d_x
''',
"mat:photon4x4":'''
01_x & 02_x & 01_x & 04_x\\
04_x & 09_x & 06_x & 11_x\\
11_x & 26_x & 18_x & 42_x\\
42_x & 95_x & 64_x & 0b_x
''',
"mat:photon4x4-inv":'''
14_x & 1a_x & 35_x & 0c_x\\
0c_x & 0c_x & 16_x & 05_x\\
05_x & 06_x & 09_x & 02_x\\
02_x & 01_x & 04_x & 01_x
''',
"mat:photon_a100":'''
1_x & 2_x & 9_x & 9_x & 2_x\\
2_x & 5_x & 3_x & 8_x & d_x\\
d_x & b_x & a_x & c_x & 1_x\\
1_x & f_x & 2_x & 3_x & e_x\\
e_x & e_x & 8_x & 5_x & c_x
''',
"mat:photon_a100-inv":'''
c_x & 5_x & 8_x & e_x & e_x\\
e_x & 3_x & 2_x & f_x & 1_x\\
1_x & c_x & a_x & b_x & d_x\\
d_x & 8_x & 3_x & 5_x & 2_x\\
2_x & 9_x & 9_x & 2_x & 1_x
''',
"mat:photon_a144":'''
1_x & 2_x & 8_x & 5_x & 8_x & 2_x\\
2_x & 5_x & 1_x & 2_x & 6_x & c_x\\
c_x & 9_x & f_x & 8_x & 8_x & d_x\\
d_x & 5_x & b_x & 3_x & a_x & 1_x\\
1_x & f_x & d_x & e_x & b_x & 8_x\\
8_x & 2_x & 3_x & 3_x & 2_x & 8_x
''',
"mat:photon_a144-inv":'''
8_x & 2_x & 3_x & 3_x & 2_x & 8_x\\
8_x & b_x & e_x & d_x & f_x & 1_x\\
1_x & a_x & 3_x & b_x & 5_x & d_x\\
d_x & 8_x & 8_x & f_x & 9_x & c_x\\
c_x & 6_x & 2_x & 1_x & 5_x & 2_x\\
2_x & 8_x & 5_x & 8_x & 2_x & 1_x
''',
"mat:photon_a196":'''
1_x & 4_x & 6_x & 1_x & 1_x & 6_x & 4_x\\
4_x & 2_x & f_x & 2_x & 5_x & a_x & 5_x\\
5_x & 3_x & f_x & a_x & 7_x & 8_x & d_x\\
d_x & 4_x & b_x & 2_x & 7_x & f_x & 9_x\\
9_x & f_x & 7_x & 2_x & b_x & 4_x & d_x\\
d_x & 8_x & 7_x & a_x & f_x & 3_x & 5_x\\
5_x & a_x & 5_x & 2_x & f_x & 2_x & 4_x
''',
"mat:photon_a196-inv":'''
4_x & 2_x & f_x & 2_x & 5_x & a_x & 5_x\\
5_x & 3_x & f_x & a_x & 7_x & 8_x & d_x\\
d_x & 4_x & b_x & 2_x & 7_x & f_x & 9_x\\
9_x & f_x & 7_x & 2_x & b_x & 4_x & d_x\\
d_x & 8_x & 7_x & a_x & f_x & 3_x & 5_x\\
5_x & a_x & 5_x & 2_x & f_x & 2_x & 4_x\\
4_x & 6_x & 1_x & 1_x & 6_x & 4_x & 1_x
''',
"mat:photon_a256":'''
2_x & 4_x & 2_x & b_x & 2_x & 8_x & 5_x & 6_x\\
c_x & 9_x & 8_x & d_x & 7_x & 7_x & 5_x & 2_x\\
4_x & 4_x & d_x & d_x & 9_x & 4_x & d_x & 9_x\\
1_x & 6_x & 5_x & 1_x & c_x & d_x & f_x & e_x\\
f_x & c_x & 9_x & d_x & e_x & 5_x & e_x & d_x\\
9_x & e_x & 5_x & f_x & 4_x & c_x & 9_x & 6_x\\
c_x & 2_x & 2_x & a_x & 3_x & 1_x & 1_x & e_x\\
f_x & 1_x & d_x & a_x & 5_x & a_x & 2_x & 3_x
''',
"mat:photon_a256-inv":'''
4_x & 7_x & 9_x & a_x & c_x & c_x & 3_x & f_x\\
d_x & d_x & a_x & a_x & 7_x & d_x & a_x & 7_x\\
e_x & 2_x & 3_x & e_x & 4_x & a_x & 5_x & b_x\\
5_x & 4_x & 7_x & a_x & b_x & 3_x & b_x & a_x\\
7_x & b_x & 3_x & 5_x & d_x & 4_x & 7_x & 2_x\\
4_x & f_x & f_x & 6_x & 1_x & e_x & e_x & b_x\\
5_x & e_x & a_x & 6_x & 3_x & 6_x & f_x & 1_x\\
2_x & 1_x & c_x & 1_x & 4_x & b_x & 3_x & 9_x
''',
"mat:photon_a288":'''
02_x & 03_x & 01_x & 02_x & 01_x & 04_x\\
08_x & 0e_x & 07_x & 09_x & 06_x & 11_x\\
22_x & 3b_x & 1f_x & 25_x & 18_x & 42_x\\
84_x & e4_x & 79_x & 9b_x & 67_x & 0b_x\\
16_x & 99_x & ef_x & 6f_x & 90_x & 4b_x\\
96_x & cb_x & d2_x & 79_x & 24_x & a7_x
''',
"mat:photon_a288-inv":'''
15_x & 50_x & eb_x & 62_x & 79_x & 99_x\\
29_x & a5_x & c9_x & c2_x & fb_x & 2b_x\\
56_x & 54_x & 8e_x & 9f_x & e9_x & 57_x\\
ae_x & af_x & 03_x & 20_x & c8_x & ae_x\\
47_x & 47_x & 01_x & 44_x & 8e_x & 46_x\\
8c_x & 8d_x & 01_x & 8d_x & 02_x & 8d_x
''',
"mat:joltik":'''
1_x & 4_x & 9_x & d_x\\
4_x & 1_x & d_x & 9_x\\
9_x & d_x & 1_x & 4_x\\
d_x & 9_x & 4_x & 1_x
''',
"mat:cui_jin":'''
01_x & 12_x & 04_x & 16_x\\
12_x & 01_x & 16_x & 04_x\\
04_x & 16_x & 01_x & 12_x\\
16_x & 04_x & 12_x & 01_x
''',
"mat:gupta_ray_0":'''
01_x & 02_x & 03_x & d0_x\\
02_x & 01_x & d0_x & 03_x\\
03_x & d0_x & 01_x & 02_x\\
d0_x & 03_x & 02_x & 01_x
''',
"mat:gupta_ray_0-inv":'''
98_x & 2b_x & b3_x & 7a_x\\
2b_x & 98_x & 7a_x & b3_x\\
b3_x & 7a_x & 98_x & 2b_x\\
7a_x & b3_x & 2b_x & 98_x
''',
"mat:gupta_ray_1":'''
7a_x & f4_x & 8e_x & 01_x\\
f4_x & 7a_x & 01_x & 8e_x\\
8e_x & 01_x & 7a_x & f4_x\\
01_x & 8e_x & f4_x & 7a_x
''',
"mat:gupta_ray_3x3":'''
7a_x & f4_x & 8e_x \\
f4_x & 7a_x & 01_x \\
8e_x & 01_x & 7a_x
''',
"mat:gupta_ray_3x3-inv":'''
aa_x & f7_x & 8c_x\\
f7_x & f3_x & 06_x\\
8c_x & 06_x & 89_x
''',
"mat:gupta_ray_2":'''
01_x & 02_x & fc_x & fe_x\\
02_x & 01_x & fe_x & fc_x\\
fc_x & fe_x & 01_x & 02_x\\
fe_x & fc_x & 02_x & 01_x
''',
"mat:gupta_ray_3":'''
01_x & 02_x & 06_x & 8c_x & 30_x & fb_x & 87_x & c4_x\\
02_x & 01_x & 8c_x & 06_x & fb_x & 30_x & c4_x & 87_x\\
06_x & 8c_x & 01_x & 02_x & 87_x & c4_x & 30_x & fb_x\\
8c_x & 06_x & 02_x & 01_x & c4_x & 87_x & fb_x & 30_x\\
30_x & fb_x & 87_x & c4_x & 01_x & 02_x & 06_x & 8c_x\\
fb_x & 30_x & c4_x & 87_x & 02_x & 01_x & 8c_x & 06_x\\
87_x & c4_x & 30_x & fb_x & 06_x & 8c_x & 01_x & 02_x\\
c4_x & 87_x & fb_x & 30_x & 8c_x & 06_x & 02_x & 01_x
''',
"mat:gupta_ray_4":'''
01_x & 03_x & 08_x & b2_x & 0d_x & 60_x & e8_x & 1c_x & 0f_x & 2c_x & a2_x & 8b_x & c9_x & 7a_x & ac_x & 35_x\\
03_x & 01_x & b2_x & 08_x & 60_x & 0d_x & 1c_x & e8_x & 2c_x & 0f_x & 8b_x & a2_x & 7a_x & c9_x & 35_x & ac_x\\
08_x & b2_x & 01_x & 03_x & e8_x & 1c_x & 0d_x & 60_x & a2_x & 8b_x & 0f_x & 2c_x & ac_x & 35_x & c9_x & 7a_x\\
b2_x & 08_x & 03_x & 01_x & 1c_x & e8_x & 60_x & 0d_x & 8b_x & a2_x & 2c_x & 0f_x & 35_x & ac_x & 7a_x & c9_x\\
0d_x & 60_x & e8_x & 1c_x & 01_x & 03_x & 08_x & b2_x & c9_x & 7a_x & ac_x & 35_x & 0f_x & 2c_x & a2_x & 8b_x\\
60_x & 0d_x & 1c_x & e8_x & 03_x & 01_x & b2_x & 08_x & 7a_x & c9_x & 35_x & ac_x & 2c_x & 0f_x & 8b_x & a2_x\\
e8_x & 1c_x & 0d_x & 60_x & 08_x & b2_x & 01_x & 03_x & ac_x & 35_x & c9_x & 7a_x & a2_x & 8b_x & 0f_x & 2c_x\\
1c_x & e8_x & 60_x & 0d_x & b2_x & 08_x & 03_x & 01_x & 35_x & ac_x & 7a_x & c9_x & 8b_x & a2_x & 2c_x & 0f_x\\
0f_x & 2c_x & a2_x & 8b_x & c9_x & 7a_x & ac_x & 35_x & 01_x & 03_x & 08_x & b2_x & 0d_x & 60_x & e8_x & 1c_x\\
2c_x & 0f_x & 8b_x & a2_x & 7a_x & c9_x & 35_x & ac_x & 03_x & 01_x & b2_x & 08_x & 60_x & 0d_x & 1c_x & e8_x\\
a2_x & 8b_x & 0f_x & 2c_x & ac_x & 35_x & c9_x & 7a_x & 08_x & b2_x & 01_x & 03_x & e8_x & 1c_x & 0d_x & 60_x\\
8b_x & a2_x & 2c_x & 0f_x & 35_x & ac_x & 7a_x & c9_x & b2_x & 08_x & 03_x & 01_x & 1c_x & e8_x & 60_x & 0d_x\\
c9_x & 7a_x & ac_x & 35_x & 0f_x & 2c_x & a2_x & 8b_x & 0d_x & 60_x & e8_x & 1c_x & 01_x & 03_x & 08_x & b2_x\\
7a_x & c9_x & 35_x & ac_x & 2c_x & 0f_x & 8b_x & a2_x & 60_x & 0d_x & 1c_x & e8_x & 03_x & 01_x & b2_x & 08_x\\
ac_x & 35_x & c9_x & 7a_x & a2_x & 8b_x & 0f_x & 2c_x & e8_x & 1c_x & 0d_x & 60_x & 08_x & b2_x & 01_x & 03_x\\
35_x & ac_x & 7a_x & c9_x & 8b_x & a2_x & 2c_x & 0f_x & 1c_x & e8_x & 60_x & 0d_x & b2_x & 08_x & 03_x & 01_x
''',

# latex_mats_part2.txt

"mat:khoo-7":'''
1_x & 2_x & 8_x & 9_x\\
2_x & 1_x & 9_x & 8_x\\
8_x & 9_x & 1_x & 2_x\\
9_x & 8_x & 2_x & 1_x
''',
"mat:khoo-7-inv":'''
d_x & 9_x & 2_x & f_x\\
9_x & d_x & f_x & 2_x\\
2_x & f_x & d_x & 9_x\\
f_x & 2_x & 9_x & d_x
''',
"mat:khoo-8":'''
01_x & 02_x & 04_x & 91_x\\
02_x & 01_x & 91_x & 04_x\\
04_x & 91_x & 01_x & 02_x\\
91_x & 04_x & 02_x & 01_x
''',
"mat:khoo-8-inv":'''
27_x & 4e_x & 9c_x & 79_x\\
4e_x & 27_x & 79_x & 9c_x\\
9c_x & 79_x & 27_x & 4e_x\\
79_x & 9c_x & 4e_x & 27_x
''',

# latex_mats_part2.txt Hadamard and Hadamard-Cauchy - use ff_hadamard_from_row to get full matrix

"mat:gupta_ray_5":'''
01_x & 02_x & 04_x & 69_x & 07_x & ec_x & cc_x & 72_x & 0b_x & 54_x & 29_x & be_x & 74_x & f9_x & c4_x & 87_x & 0e_x & 47_x & c2_x & c3_x & 39_x & 8e_x & 1c_x & 85_x & 55_x & 26_x & 1e_x & af_x & 68_x & b6_x & 59_x & 1f_x'''
,
"mat:khoo":'''
0f_x & 02_x & 0c_x & 05_x & 0a_x & 04_x & 03_x & 08_x'''
,
"mat:khoo-2":'''
01_x & 02_x & b0_x & b2_x'''
,
"mat:khoo-3":'''
01_x & 02_x & 03_x & 91_x & 04_x & 70_x & 05_x & e1_x'''
,
"mat:khoo-4":'''
2_x & 3_x & 4_x & c_x & 5_x & a_x & 8_x & f_x'''
,
"mat:khoo-5":'''
08_x & 16_x & 8a_x & 01_x & 70_x & 8d_x & 24_x & 76_x & a8_x & 91_x & ad_x & 48_x & 05_x & b5_x & af_x  & f8_x'''
,
"mat:khoo-6":'''
d2_x & 06_x & 05_x & 4d_x & 21_x & f8_x & 11_x & 62_x & 08_x & d8_x & e9_x & 28_x & 4b_x & a6_x & 10_x & 2c_x & a1_x & 49_x & 4c_x & d1_x & 59_x & b2_x & 13_x & a4_x & 03_x & c3_x & 42_x & 79_x & a0_x & 6f_x & ab_x & 41_x'''
,
"mat:khoo-9":'''
01_x & 02_x & 03_x & 08_x & 04_x & 91_x & e1_x & a9_x'''
,
"mat:khoo-9-inv":'''
1a_x & 34_x & 2e_x & d0_x & 68_x & e7_x & 0d_x & 92_x'''
,
"mat:khoo-10":'''
1_x & 2_x & 6_x & 8_x & 9_x & c_x & d_x & a_x'''
,
"mat:khoo-10-inv":'''
c_x & b_x & e_x & a_x & 6_x & f_x & 3_x & 1_x'''
,
"mat:khoo-11":'''
b1_x & 1c_x & 30_x & 09_x & 08_x & 91_x & 18_x & e4_x & 98_x & 12_x & 70_x & b5_x & 97_x & 90_x & a9_x & 5b_x'''
,
"mat:khoo-11-inv":'''
4c_x & 8b_x & bf_x & f6_x & 6a_x & 27_x & be_x & e7_x & d1_x & 2f_x & 69_x & 79_x & e9_x & bb_x & f2_x & 0f_x'''
,
"mat:khoo-12":'''
b9_x & 7c_x & 93_x & bc_x & bd_x & 26_x & fa_x & a9_x & 32_x & 31_x & 24_x & b5_x & bb_x & 06_x & a0_x & 44_x & 95_x & b3_x & 0c_x & 1c_x & 07_x & e5_x & a4_x & 2e_x & 56_x & 4c_x & 55_x & 02_x & 66_x & 39_x & 48_x & 08_x'''
,
"mat:khoo-12-inv":'''
a9_x & b7_x & 7f_x & b2_x & b5_x & f2_x & a3_x & d9_x & 9e_x & 97_x & fc_x & 8d_x & a7_x & 12_x & e6_x & 1f_x & 6d_x & 9f_x & 24_x & 54_x & 15_x & fe_x & fa_x & ca_x & 61_x & 27_x & 68_x & e &_x f1_x & af_x & 3b_x & 38_x'''
,
"mat:khoo-14":'''
1_x &2_x &6_x &4_x''',

# part 3

"mat:gupta-pandey-IDEA-inv":'''
01d6_x & e364_x & 02fb_x & 7901_x & fe00_x & 49e2_x & fd2e_x & 2c60_x\\
2c60_x & 01d6_x & e364_x & 02fb_x & 7901_x & fe00_x & 49e2_x & fd2e_x\\
fd2e_x & 2c60_x & 01d6_x & e364_x & 02fb_x & 7901_x & fe00_x & 49e2_x\\
49e2_x & fd2e_x & 2c60_x & 01d6_x & e364_x & 02fb_x & 7901_x & fe00_x\\
fe00_x & 49e2_x & fd2e_x & 2c60_x & 01d6_x & e364_x & 02fb_x & 7901_x\\
7901_x & fe00_x & 49e2_x & fd2e_x & 2c60_x & 01d6_x & e364_x & 02fb_x\\
02fb_x & 7901_x & fe00_x & 49e2_x & fd2e_x & 2c60_x & 01d6_x & e364_x\\
e364_x & 02fb_x & 7901_x & fe00_x & 49e2_x & fd2e_x & 2c60_x & 01d6_x
''',
"mat:gupta-pandey-24-2-inv":'''
01_x & cc_x & 22_x & ed_x & 02_x & 01_x\\
01_x & 01_x & cc_x & 22_x & ed_x & 02_x\\
02_x & 01_x & 01_x & cc_x & 22_x & ed_x\\
ed_x & 02_x & 01_x & 01_x & cc_x & 22_x\\
22_x & ed_x & 02_x & 01_x & 01_x & cc_x\\
cc_x & 22_x & ed_x & 02_x & 01_x & 01_x
''',
"mat:gupta-pandey-34-2-inv":'''
01_x & cc_x & 22_x & ed_x & 02_x & 01_x\\
01_x & 01_x & cc_x & 22_x & ed_x & 02_x\\
02_x & 01_x & 01_x & cc_x & 22_x & ed_x\\
ed_x & 02_x & 01_x & 01_x & cc_x & 22_x\\
22_x & ed_x & 02_x & 01_x & 01_x & cc_x\\
cc_x & 22_x & ed_x & 02_x & 01_x & 01_x
''',
"mat:duwal-1":'''
2 & 1 & 1 \\
1 & 2 & 1 \\
1 & 1 & 2
''',
"mat:duwal-2":'''
3 & 2 & 2 \\
2 & 3 & 2 \\
2 & 2 & 3
''',
"mat:duwal-3":'''
2 & 1 & 3 \\
1 & 1 & 1 \\
3 & 1 & 2
''',
"mat:duwal-3-inv":'''
3 & 1 & 2 \\
1 & 1 & 1 \\
2 & 1 & 3
''',
"mat:duwal-4":'''
3 & 1 & 3 \\
1 & 1 & 2 \\
2 & 1 & 1
''',
"mat:duwal-5":'''
2 & 1 & 1 \\
1 & 2 & 1 \\
1 & 1 & 2
''',
"mat:duwal-6":'''
2 & 2 & 3 & 1 \\
1 & 3 & 6 & 4 \\
3 & 1 & 4 & 4 \\
3 & 2 & 1 & 3
''',
"mat:duwal-8":'''
2 & 2 & 3 & 1 \\
1 & 3 & 6 & 4 \\
3 & 1 & 4 & 4 \\
3 & 2 & 1 & 3
''',
"mat:duwal-9":'''
5 & 7 & 1 & 3 \\
4 & 6 & 1 & 1 \\
1 & 3 & 5 & 7 \\
1 & 1 & 4 & 6
''',
"mat:duwal-10":'''
6 & 7 & 1 & 5 \\
2 & 3 & 1 & 1 \\
1 & 5 & 6 & 7 \\
1 & 1 & 2 & 3
''',
"mat:duwal-11":'''
3 & 2 & 1 & 3 \\
2 & 3 & 1 & 1 \\
4 & 3 & 6 & 4 \\
1 & 1 & 4 & 6
''',
"mat:duwal-13":'''
1 & 2 & 4 & 3 \\
2 & 3 & 2 & 3 \\
3 & 3 & 5 & 1 \\
3 & 1 & 1 & 3
''',
"mat:liu-sim-15-inv":'''
22_x & c4_x & 68_x & e7_x & e9_x & 38_x & 49_x & 54_x \\
c4_x & 68_x & e7_x & e9_x & 38_x & 49_x & 54_x & 22_x \\
68_x & e7_x & e9_x & 38_x & 49_x & 54_x & 22_x & c4_x \\
e7_x & e9_x & 38_x & 49_x & 54_x & 22_x & c4_x & 68_x \\
e9_x & 38_x & 49_x & 54_x & 22_x & c4_x & 68_x & e7_x \\
38_x & 49_x & 54_x & 22_x & c4_x & 68_x & e7_x & e9_x \\
49_x & 54_x & 22_x & c4_x & 68_x & e7_x & e9_x & 38_x \\
54_x & 22_x & c4_x & 68_x & e7_x & e9_x & 38_x & 49_x
''',
"mat:liu-sim-16-inv":'''
25_x & c6_x & c7_x & a9_x & fb_x & f2_x & b3_x & 9b_x \\
c6_x & c7_x & a9_x & fb_x & f2_x & b3_x & 9b_x & 25_x \\
c7_x & a9_x & fb_x & f2_x & b3_x & 9b_x & 25_x & c6_x \\
a9_x & fb_x & f2_x & b3_x & 9b_x & 25_x & c6_x & c7_x \\
fb_x & f2_x & b3_x & 9b_x & 25_x & c6_x & c7_x & a9_x \\
f2_x & b3_x & 9b_x & 25_x & c6_x & c7_x & a9_x & fb_x \\
b3_x & 9b_x & 25_x & c6_x & c7_x & a9_x & fb_x & f2_x \\
9b_x & 25_x & c6_x & c7_x & a9_x & fb_x & f2_x & b3_x
''',
"mat:liu-sim-13-inv":'''
4b_x & 43_x & 8c_x & 85_x & 65_x & 92_x & 04_x & 99_x \\
43_x & 8c_x & 85_x & 65_x & 92_x & 04_x & 99_x & 4b_x \\
8c_x & 85_x & 65_x & 92_x & 04_x & 99_x & 4b_x & 43_x \\
85_x & 65_x & 92_x & 04_x & 99_x & 4b_x & 43_x & 8c_x \\
65_x & 92_x & 04_x & 99_x & 4b_x & 43_x & 8c_x & 85_x \\
92_x & 04_x & 99_x & 4b_x & 43_x & 8c_x & 85_x & 65_x \\
04_x & 99_x & 4b_x & 43_x & 8c_x & 85_x & 65_x & 92_x \\
99_x & 4b_x & 43_x & 8c_x & 85_x & 65_x & 92_x & 04_x
''',
"mat:liu-sim-14-inv":'''
2a_x & 9d_x & 12_x & 27_x & ba_x & 0f_x & d2_x & a7_x \\
9d_x & 12_x & 27_x & ba_x & 0f_x & d2_x & a7_x & 2a_x \\
12_x & 27_x & ba_x & 0f_x & d2_x & a7_x & 2a_x & 9d_x \\
27_x & ba_x & 0f_x & d2_x & a7_x & 2a_x & 9d_x & 12_x \\
ba_x & 0f_x & d2_x & a7_x & 2a_x & 9d_x & 12_x & 27_x \\
0f_x & d2_x & a7_x & 2a_x & 9d_x & 12_x & 27_x & ba_x \\
d2_x & a7_x & 2a_x & 9d_x & 12_x & 27_x & ba_x & 0f_x \\
a7_x & 2a_x & 9d_x & 12_x & 27_x & ba_x & 0f_x & d2_x
''',
"mat:liu-sim-10-inv":'''
9_x & c_x & 2_x & 6_x & 7_x & e_x \\
c_x & 2_x & 6_x & 7_x & e_x & 9_x \\
2_x & 6_x & 7_x & e_x & 9_x & c_x \\
6_x & 7_x & e_x & 9_x & c_x & 2_x \\
7_x & e_x & 9_x & c_x & 2_x & 6_x \\
e_x & 9_x & c_x & 2_x & 6_x & 7_x
''',
"mat:liu-sim-11-inv":'''
d6_x & fa_x & ee_x & f7_x & f8_x & c7_x & f8_x & 21_x \\
fa_x & ee_x & f7_x & f8_x & c7_x & f8_x & 21_x & d6_x \\
ee_x & f7_x & f8_x & c7_x & f8_x & 21_x & d6_x & fa_x \\
f7_x & f8_x & c7_x & f8_x & 21_x & d6_x & fa_x & ee_x \\
f8_x & c7_x & f8_x & 21_x & d6_x & fa_x & ee_x & f7_x \\
c7_x & f8_x & 21_x & d6_x & fa_x & ee_x & f7_x & f8_x \\
f8_x & 21_x & d6_x & fa_x & ee_x & f7_x & f8_x & c7_x \\
21_x & d6_x & fa_x & ee_x & f7_x & f8_x & c7_x & f8_x
''',
"mat:liu-sim-12-inv":'''
8c_x & ec_x & 43_x & 0a_x & 98_x & 36_x & 79_x & 6d_x \\
ec_x & 43_x & 0a_x & 98_x & 36_x & 79_x & 6d_x & 8c_x \\
43_x & 0a_x & 98_x & 36_x & 79_x & 6d_x & 8c_x & ec_x \\
0a_x & 98_x & 36_x & 79_x & 6d_x & 8c_x & ec_x & 43_x \\
98_x & 36_x & 79_x & 6d_x & 8c_x & ec_x & 43_x & 0a_x \\
36_x & 79_x & 6d_x & 8c_x & ec_x & 43_x & 0a_x & 98_x \\
79_x & 6d_x & 8c_x & ec_x & 43_x & 0a_x & 98_x & 36_x \\
6d_x & 8c_x & ec_x & 43_x & 0a_x & 98_x & 36_x & 79_x
''',
"mat:liu-sim-7-inv":'''
7_x & 7_x & 9_x \\
7_x & 9_x & 7_x \\
9_x & 7_x & 7_x
''',
"mat:liu-sim-8-inv":'''
c_x & 8_x & 7_x & 7_x \\
8_x & 7_x & 7_x & c_x \\
7_x & 7_x & c_x & 8_x \\
7_x & c_x & 8_x & 7_x
''',
"mat:liu-sim-9-inv":'''
5_x & 5_x & 9_x & 1_x & 9_x \\
5_x & 9_x & 1_x & 9_x & 5_x \\
9_x & 1_x & 9_x & 5_x & 5_x \\
1_x & 9_x & 5_x & 5_x & 9_x \\
9_x & 5_x & 5_x & 9_x & 1_x
''',
"mat:liu-sim-4-inv":'''
11_x & 58_x & 90_x & 0f_x & 54_x & c0_x \\
58_x & 90_x & 0f_x & 54_x & c0_x & 11_x \\
90_x & 0f_x & 54_x & c0_x & 11_x & 58_x \\
0f_x & 54_x & c0_x & 11_x & 58_x & 90_x \\
54_x & c0_x & 11_x & 58_x & 90_x & 0f_x \\
c0_x & 11_x & 58_x & 90_x & 0f_x & 54_x
''',
"mat:liu-sim-5-inv":'''
e6_x & e6_x & 70_x & 0f_x & 91_x & 0f_x & 70_x \\
e6_x & 70_x & 0f_x & 91_x & 0f_x & 70_x & e6_x \\
70_x & 0f_x & 91_x & 0f_x & 70_x & e6_x & e6_x \\
0f_x & 91_x & 0f_x & 70_x & e6_x & e6_x & 70_x \\
91_x & 0f_x & 70_x & e6_x & e6_x & 70_x & 0f_x \\
0f_x & 70_x & e6_x & e6_x & 70_x & 0f_x & 91_x \\
70_x & e6_x & e6_x & 70_x & 0f_x & 91_x & 0f_x
''',
"mat:liu-sim-6-inv":'''
5d_x & c4_x & b8_x & 81_x & 5f_x & 5a_x & 22_x & 96_x \\
c4_x & b8_x & 81_x & 5f_x & 5a_x & 22_x & 96_x & 5d_x \\
b8_x & 81_x & 5f_x & 5a_x & 22_x & 96_x & 5d_x & c4_x \\
81_x & 5f_x & 5a_x & 22_x & 96_x & 5d_x & c4_x & b8_x \\
5f_x & 5a_x & 22_x & 96_x & 5d_x & c4_x & b8_x & 81_x \\
5a_x & 22_x & 96_x & 5d_x & c4_x & b8_x & 81_x & 5f_x \\
22_x & 96_x & 5d_x & c4_x & b8_x & 81_x & 5f_x & 5a_x \\
96_x & 5d_x & c4_x & b8_x & 81_x & 5f_x & 5a_x & 22_x
''',
"mat:liu-sim-1-inv":'''
5f_x & 5f_x & e1_x \\
5f_x & e1_x & 5f_x \\
e1_x & 5f_x & 5f_x
''',
"mat:liu-sim-2-inv":'''
55_x & 41_x & 71_x & 5a_x \\
41_x & 71_x & 5a_x & 55_x \\
71_x & 5a_x & 55_x & 41_x \\
5a_x & 55_x & 41_x & 71_x
''',
"mat:liu-sim-3-inv":'''
09_x & 09_x & c2_x & 04_x & c2_x \\
09_x & c2_x & 04_x & c2_x & 09_x \\
c2_x & 04_x & c2_x & 09_x & 09_x \\
04_x & c2_x & 09_x & 09_x & c2_x \\
c2_x & 09_x & 09_x & c2_x & 04_x
''',
"mat:gupta-pandey-34-1-inv":'''
02_x & 5e_x & 5d_x\\
5d_x & 02_x & 5e_x\\
5e_x & 5d_x & 02_x
''',
"mat:gupta-pandey-24-1-inv":'''
02_x & 5e_x & 5d_x\\
5d_x & 02_x & 5e_x\\
5e_x & 5d_x & 02_x
''',
"mat:gupta-pandey-23-inv":'''
2_x & 3_x\\
3_x & 2_x
''',
"mat:gupta-pandey-5-inv":'''
9_x & c_x & 5_x\\
7_x & 9_x & e_x\\
f_x & 4_x & a_x
''',
"mat:gupta-pandey-3-inv":'''
6_x & 4_x & 2_x & e_x\\
4_x & 6_x & e_x & 2_x\\
2_x & e_x & 6_x & 4_x\\
e_x & 2_x & 4_x & 6_x
''',
"mat:gupta-pandey-2-inv":'''
c_x & 6_x & 2_x\\
6_x & a_x & 3_x\\
2_x & 3_x & 7_x
''',
"mat:gupta-pandey-1-inv":'''
6_x & 1_x & d_x\\
c_x & d_x & c_x\\
4_x & 7_x & d_x
''',

# part4 - should circ

"mat:liu-sim-1":'''
01_x & 01_x & 02_x'''
,
"mat:liu-sim-2":'''
01_x & 01_x & 02_x & 91_x'''
,
"mat:liu-sim-3":'''
01_x & 01_x & 02_x & 91_x & 02_x'''
,
"mat:liu-sim-4":'''
01_x & 02_x & e1_x & 91_x & 01_x & 08_x'''
,
"mat:liu-sim-5":'''
01_x & 01_x & 91_x & 02_x & 04_x & 02_x & 91_x'''
,
"mat:liu-sim-6":'''
01_x & 01_x & 02_x & e1_x & 08_x & e0_x & 01_x & a9_x'''
,
"mat:liu-sim-7":'''
1_x & 1_x & 2_x'''
,
"mat:liu-sim-8":'''
1_x & 1_x & 9_x & 4_x'''
,
"mat:liu-sim-9":'''
2_x & 2_x & 9_x & 1_x & 9_x'''
,
"mat:liu-sim-10":'''
1_x & 1_x & 9_x & c_x & 9_x & 3_x'''
,
"mat:liu-sim-11":'''
01_x & 01_x & 91_x & 02_x & 04_x & 02_x & 12_x & 91_x'''
,
"mat:liu-sim-12":'''
01_x & 01_x & 04_x & 02_x & a9_x & 91_x & 02_x & 03_x'''
,
"mat:liu-sim-13":'''
01_x & 01_x & 02_x & e0_x & 06_x & e1_x & 91_x & 04_x'''
,
"mat:liu-sim-14":'''
01_x & 02_x & 91_x & 08_x & 04_x & 06_x & e1_x & 03_x'''
,
"mat:liu-sim-15":'''
01_x & 01_x & 02_x & 01_x & 74_x & 8d_x & 46_x & 04_x'''
,
"mat:liu-sim-16":'''
01_x & 01_x & 02_x & 8e_x & 47_x & 10_x & 01_x & 46_x'''
,
"mat:liu-sim-17":'''
5a_x & 0a_x & 51_x'''
,
"mat:liu-sim-18":'''
01_x & 02_x & b3_x & bb_x & 0a_x'''
,
"mat:liu-sim-19":'''
01_x & 01_x & b3_x & 2c_x & 04_x & 9a_x'''
,
"mat:liu-sim-20":'''
01_x & 02_x & 10_x & b2_x & 58_x & a4_x & 5c_x'''
,
"mat:liu-sim-21":'''
01_x & 01_x & 21_x & 08_x & 96_x & 26_x & 98_x'''
,
"mat:liu-sim-22":'''
2_x & f_x & c_x'''
,
"mat:liu-sim-23":'''
1_x & 2_x & 5_x & 4_x & 3_x''',

# Shirai's - should rcirc

"shirai-0":"01_x & 01_x & 02_x & 01_x & 05_x & 08_x & 09_x & 04_x",
"shirai-1":"01_x & 01_x & 02_x & 01_x & 06_x & 09_x & 08_x & 03_x",
"shirai-2":"01_x & 01_x & 02_x & 01_x & 08_x & 09_x & 04_x & 05_x",
"shirai-3":"01_x & 01_x & 02_x & 01_x & 09_x & 06_x & 04_x & 03_x",
"shirai-4":"01_x & 01_x & 02_x & 06_x & 05_x & 09_x & 01_x & 08_x",
"shirai-5":"01_x & 01_x & 03_x & 01_x & 04_x & 09_x & 05_x & 06_x",
"shirai-6":"01_x & 01_x & 03_x & 01_x & 08_x & 04_x & 09_x & 06_x",
"shirai-7":"01_x & 01_x & 04_x & 01_x & 08_x & 05_x & 02_x & 09_x",
"shirai-8":"01_x & 01_x & 04_x & 01_x & 09_x & 03_x & 02_x & 06_x",
"shirai-9":"01_x & 01_x & 04_x & 03_x & 06_x & 08_x & 01_x & 09_x",
"shirai-10":"01_x & 01_x & 05_x & 01_x & 04_x & 06_x & 03_x & 09_x",
"shirai-11":"01_x & 01_x & 05_x & 08_x & 02_x & 09_x & 01_x & 06_x",
"shirai-12":"01_x & 01_x & 08_x & 01_x & 06_x & 03_x & 02_x & 09_x",
"shirai-13":"01_x & 01_x & 08_x & 02_x & 04_x & 05_x & 01_x & 09_x",
"shirai-0-inv":"b5_x & 98_x & 23_x & fa_x & 23_x & a5_x & b6_x & 30_x",
"shirai-1-inv":"bb_x & de_x & a0_x & df_x & 4a_x & 55_x & 7a_x & c5_x",
"shirai-2-inv":"04_x & a4_x & cb_x & af_x & c2_x & 3e_x & 0e_x & c2_x",
"shirai-3-inv":"4f_x & aa_x & 2c_x & 0c_x & 84_x & 76_x & 14_x & bb_x",
"shirai-4-inv":"5b_x & e8_x & ed_x & e2_x & 33_x & 98_x & 82_x & 94_x",
"shirai-5-inv":"87_x & d4_x & 76_x & 80_x & 9d_x & e4_x & 24_x & c5_x",
"shirai-6-inv":"ad_x & ef_x & 44_x & 71_x & a8_x & e2_x & 42_x & 7e_x",
"shirai-7-inv":"04_x & af_x & 0e_x & a4_x & c2_x & c2_x & cb_x & 3e_x",
"shirai-8-inv":"4f_x & 0c_x & 14_x & aa_x & 84_x & bb_x & 2c_x & 76_x",
"shirai-9-inv":"e2_x & 44_x & 7e_x & a8_x & ef_x & 42_x & 71_x & ad_x",
"shirai-10-inv":"87_x & 80_x & 24_x & d4_x & 9d_x & c5_x & 76_x & e4_x",
"shirai-11-inv":"ed_x & 98_x & 5b_x & e2_x & 82_x & e8_x & 33_x & 94_x",
"shirai-12-inv":"bb_x & df_x & 7a_x & de_x & 4a_x & c5_x & a0_x & 55_x",
"shirai-13-inv":"a5_x & 23_x & 30_x & 23_x & 98_x & b6_x & fa_x & b5_x",
}

should_ff_had = [
"mat:gupta_ray_5",
"mat:khoo",
"mat:khoo-2",
"mat:khoo-3",
"mat:khoo-4",
"mat:khoo-5",
"mat:khoo-6",
"mat:khoo-9",
"mat:khoo-9-inv",
"mat:khoo-10",
"mat:khoo-10-inv",
"mat:khoo-11",
"mat:khoo-11-inv",
"mat:khoo-12",
"mat:khoo-12-inv",
"mat:khoo-14"
]

should_lcirc = [
"mat:liu-sim-1",
"mat:liu-sim-2",
"mat:liu-sim-3",
"mat:liu-sim-4",
"mat:liu-sim-5",
"mat:liu-sim-6",
"mat:liu-sim-7",
"mat:liu-sim-8",
"mat:liu-sim-9",
"mat:liu-sim-10",
"mat:liu-sim-11",
"mat:liu-sim-12",
"mat:liu-sim-13",
"mat:liu-sim-14",
"mat:liu-sim-15",
"mat:liu-sim-16",
"mat:liu-sim-17",
"mat:liu-sim-18",
"mat:liu-sim-19",
"mat:liu-sim-20",
"mat:liu-sim-21",
"mat:liu-sim-22",
"mat:liu-sim-23"
]

should_rcirc = [
"shirai-0",
"shirai-1",
"shirai-2",
"shirai-3",
"shirai-4",
"shirai-5",
"shirai-6",
"shirai-7",
"shirai-8",
"shirai-9",
"shirai-10",
"shirai-11",
"shirai-12",
"shirai-13",
"shirai-0-inv",
"shirai-1-inv",
"shirai-2-inv",
"shirai-3-inv",
"shirai-4-inv",
"shirai-5-inv",
"shirai-6-inv",
"shirai-7-inv",
"shirai-8-inv",
"shirai-9-inv",
"shirai-10-inv",
"shirai-11-inv",
"shirai-12-inv",
"shirai-13-inv",
]

gupta_pandey_1 = [
            ["1", "x^3 + x^2 + x + 1", "x^2 + x + 1"],
            ["x^3 + 1", "x^2 + 1", "x^3 + x + 1"],
            ["x^3 + x^2 + 1", "x^2", "x^3 + x^2 + x"]
         ]

gupta_pandey_2 = [
            ["1", "x^2 + x", "x^2 + 1"],
            ["x^2 + x", "1", "x^2"],
            ["x^2 + 1", "x^2", "1"]
         ]

gupta_pandey_3 = [
    ["x^3+x^2+1" , "x^2+x+1"   , "x^3+x"      , "x+1"],
    ["x^2+x+1"   , "x^3+x^2+1" , "x+1"        , "x^3+x"],
    ["x^3+x"     , "x+1"       , "x^3+x^2+1"  , "x^2+x+1"],
    ["x+1"       , "x^3+x"     , "x^2+x+1"    , "x^3+x^2+1"],
]

gupta_pandey_3_made_involutory = [[10, 12, 6, 1], [12, 10, 1, 6], [6, 1, 10, 12], [1, 6, 12, 10]]

gupta_pandey_5 = [
    ["x^3 + x^2", "x^2 + 1", "1"],
    ["x^2 + 1", "x^3 + x + 1  ", "1"],
    ["x^3", "x^3 + x^2 + x + 1", "1"],
]

gupta_pandey_6 = [
    ["x^3", "x^3+1", "x^3+1"],
    ["x^3+x^2+x", "x^3+x^2+x+1", "x^3+x^2+x"],
    ["x^2+x+1", "x^2+x+1", "x^2+x"],
]

gupta_pandey_idea = [
    ["1", "1", "x^2", "1", "x^3", "1+x^2", "x", "1+x^3"],
    ["1+x^3", "1", "1", "x^2", "1", "x^3", "1+x^2", "x"],
    ["x", "1+x^3", "1", "1", "x^2", "1", "x^3", "1+x^2"],
    ["1+x^2", "x", "1+x^3", "1", "1", "x^2", "1", "x^3"],
    ["x^3", "1+x^2", "x", "1+x^3", "1", "1", "x^2", "1"],
    ["1", "x^3", "1+x^2", "x", "1+x^3", "1", "1", "x^2"],
    ["x^2", "1", "x^3", "1+x^2", "x", "1+x^3", "1", "1"],
    ["1", "x^2", "1", "x^3", "1+x^2", "x", "1+x^3", "1"],
]

gupta_pandey_23 = [
    ["x", "x+1"],
    ["x+1", "x"]
]

gupta_pandey_24_1 = [
    ["x", "1+x^2+x^3+x^4+x^6", "x+x^2+x^3+x^4+x^6"],
    ["x+x^2+x^3+x^4+x^6", "x", "1+x^2+x^3+x^4+x^6"],
    ["1+x^2+x^3+x^4+x^6", "x+x^2+x^3+x^4+x^6", "x"],
]

gupta_pandey_24_2 = [
    ["1", "1", "x", "1+x^2+x^3+x^5+x^6+x^7", "x+x^5", "x^2+x^3+x^6+x^7"],
    ["x^2+x^3+x^6+x^7", "1", "1", "x", "1+x^2+x^3+x^5+x^6+x^7", "x+x^5"],
    ["x+x^5", "x^2+x^3+x^6+x^7", "1", "1", "x", "1+x^2+x^3+x^5+x^6+x^7"],
    ["1+x^2+x^3+x^5+x^6+x^7", "x+x^5", "x^2+x^3+x^6+x^7", "1", "1", "x"],
    ["x", "1+x^2+x^3+x^5+x^6+x^7", "x+x^5", "x^2+x^3+x^6+x^7", "1", "1"],
    ["1", "x", "1+x^2+x^3+x^5+x^6+x^7", "x+x^5", "x^2+x^3+x^6+x^7", "1"],
]

gupta_x = [
     ("mat:gupta-pandey-1", gupta_pandey_1),
     ("mat:gupta-pandey-2", gupta_pandey_2),
     ("mat:gupta-pandey-3", gupta_pandey_3),
     ("mat:gupta-pandey-5", gupta_pandey_5),
     ("mat:gupta-pandey-6", gupta_pandey_6),
     ("mat:gupta-pandey-IDEA", gupta_pandey_idea),
     ("mat:gupta-pandey-23", gupta_pandey_23),
     ("mat:gupta-pandey-24-1", gupta_pandey_24_1),
     ("mat:gupta-pandey-24-2", gupta_pandey_24_2)
]

def rcirc_from_row(first_row):
    dim = len(first_row)
    
    rows = []
    prev_row = []

    for i in range(dim):
        if i == 0:
            rows.append(first_row)
            prev_row = first_row
        else:
            new_first = prev_row[-1]
            new_row = [new_first]
            new_row += prev_row[0:-1]
            rows.append(new_row)
            prev_row = new_row
    return rows

def ff_hadamard_from_row(first_row):
    n = len(first_row)
    ff_had = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            ff_had[i][j] = first_row[i ^ j]
    return ff_had

def lcirc_from_row(first_row):
	dim = len(first_row)
	rows = []
	prev_row = []

	for i in range(dim):
		if i == 0:
			rows.append(first_row)
			prev_row = first_row
		else:
			new_row = prev_row[1:]
			new_last = prev_row[0]
			new_row += [new_last]
			rows.append(new_row)
			prev_row = new_row
	return rows

def poly_string_to_integer(poly_string_mat):
    rows = len(poly_string_mat)
    cols = len(poly_string_mat[0])

    output_mat = [[0 for j in range(cols)] for i in range(rows)]

    for i in range(rows):
        for j in range(cols):
            poly_string = poly_string_mat[i][j]
            poly = galois.Poly.Str(poly_string, field=GF2)
            integer = poly._integer
            output_mat[i][j] = integer
    
    return output_mat

def toep(sequence, n):
    n = len(sequence) // 2
    first_column = sequence[n:]
    first_row = sequence[:n]
    matrix = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if j >= i:
                matrix[i][j] = first_row[j-i]
            else:
                matrix[i][j] = first_column[i-j]
    return matrix

def hank(values, n):
    A = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            hank_index = i+j
            A[i][j] = values[hank_index]
    return A

gupta_pandey_31_1_first_row = ["1", "x", "x^7+x^5+x^4+x+1", "x^7+x^5+x^4+x^3+x+1", "x^3+x"]
gupta_pandey_31_1_strings = lcirc_from_row(gupta_pandey_31_1_first_row)
gupta_pandey_31_1_mat = poly_string_to_integer(gupta_pandey_31_1_strings)

gupta_pandey_31_2_first_row = ["1", "1", "x^7+x^5+x^4+x+1", "x^5+x^3+x^2", "x^2", "x^7+x^4+x^3+x"]
gupta_pandey_31_2_strings = lcirc_from_row(gupta_pandey_31_2_first_row)
gupta_pandey_31_2_mat = poly_string_to_integer(gupta_pandey_31_2_strings)

gp_34_1_vals = ["x", "1+x^2+x^3+x^4+x^6", "x+x^2+x^3+x^4+x^6", "x+x^2+x^3+x^4+x^6", "1+x^2+x^3+x^4+x^6"]
gp_34_1_str = toep(gp_34_1_vals, 3)
gp_34_1_mat = poly_string_to_integer(gp_34_1_str)

gp_34_2_vals = ["1","1","x","1+x^2+x^3+x^5+x^6+x^7", "x+x^5", "x^2+x^3+x^6+x^7", "x^2+x^3+x^6+x^7", "x+x^5", "1+x^2+x^3+x^5+x^6+x^7", "x","1"]
gp_34_2_str = toep(gp_34_2_vals, 6)
gp_34_2_mat = poly_string_to_integer(gp_34_2_str)

gp_36_1_vals = ["1", "x", "x^7+x^5+x^4+x+1", "x^7+x^5+x^4+x^3+x+1","x^3+x", "1","x","x^7+x^5+x^4+x+1", "x^7+x^5+x^4+x^3+x+1"]
gp_36_1_str = hank(gp_36_1_vals, 5)
gp_36_1_mat = poly_string_to_integer(gp_36_1_str)

gp_36_2_vals = ["1","1","x^7+x^5+x^4+x+1","x^5+x^3+x^2","x^2","x^7+x^4+x^3+x","1","1","x^7+x^5+x^4+x+1","x^5+x^3+x^2","x^2"]
gp_36_2_str = hank(gp_36_2_vals, 6)
gp_36_2_mat = poly_string_to_integer(gp_36_2_str)

gupta_alpha = [
     ("mat:gupta-pandey-31-1", gupta_pandey_31_1_mat),
     ("mat:gupta-pandey-31-2", gupta_pandey_31_2_mat),
     ("mat:gupta-pandey-34-1", gp_34_1_mat),
     ("mat:gupta-pandey-34-2", gp_34_2_mat),
     ("mat:gupta-pandey-36-1", gp_36_1_mat),
     ("mat:gupta-pandey-36-2", gp_36_2_mat),
]

sarkar1 = [[2, 1, 3, 1, 6, 9, 11, 5], [8, 2, 1, 3, 1, 6, 9, 11], [12, 8, 2, 1, 3, 1, 6, 9], [9, 12, 8, 2, 1, 3, 1, 6], [9, 9, 12, 8, 2, 1, 3, 1], [5, 9, 9, 12, 8, 2, 1, 3], [12, 5, 9, 9, 12, 8, 2, 1], [8, 12, 5, 9, 9, 12, 8, 2]]
sarkar2 = [[1, 1, 2, 145, 1, 145, 169, 3], [6, 1, 1, 2, 145, 1, 145, 169], [145, 6, 1, 1, 2, 145, 1, 145], [225, 145, 6, 1, 1, 2, 145, 1], [2, 225, 145, 6, 1, 1, 2, 145], [225, 2, 225, 145, 6, 1, 1, 2], [4, 225, 2, 225, 145, 6, 1, 1], [2, 4, 225, 2, 225, 145, 6, 1]]

sarkar1inv = [[ 6,  9, 14,  3, 11,  4,  9,  1],
 [ 1,  5,  3, 11,  8,  3, 15,  9],
 [ 6,  5,  8,  6, 14,  6,  3,  4],
 [ 1, 14,  2,  4, 11, 14,  8, 11],
 [ 4,  3,  4, 13,  4,  6, 11,  3],
 [14, 10, 13,  4,  2,  8,  3, 14],
 [ 7, 10, 10,  3, 14,  5,  5,  9],
 [ 3,  7, 14,  4,  1,  6,  1,  6]]

sarkar2inv = [[240,  99,  21,   8, 119,  12, 187, 181],
 [169, 240,  99,  21,   8, 119,  12, 187],
 [181, 169, 240,  99,  21,   8, 119,  12],
 [ 24, 181, 169, 240,  99,  21,   8, 119],
 [238,  24, 181, 169, 240,  99,  21,   8],
 [ 16, 238,  24, 181, 169, 240,  99,  21],
 [ 42,  16, 238,  24, 181, 169, 240,  99],
 [198,  42,  16, 238,  24, 181, 169, 240]]

def convert(mat_str):
    integer_matrix = []
    rows = mat_str.split("\\\n")
    for r in rows:
        r_elements = r.split("&")
        r_elements = [int(elem.strip().replace("_x", ""),16) for elem in r_elements]
        integer_matrix.append(r_elements)

    return integer_matrix

def g(id):
    return matrices_as_strings[id]

def integer_dict():
    matrices_as_ints = {}
    for id in matrices_as_strings:
        #print(id)
        integer_mat = convert(g(id))

        if id in should_ff_had:
            integer_mat = ff_hadamard_from_row(integer_mat[0])
        
        if id in should_lcirc:
            integer_mat = lcirc_from_row(integer_mat[0])

        if id in should_rcirc:
            integer_mat = rcirc_from_row(integer_mat[0])

        matrices_as_ints[id] = integer_mat
    
    for gupta_poly_string_tuple in gupta_x:
        integer_mat = poly_string_to_integer(gupta_poly_string_tuple[1])
        matrices_as_ints[gupta_poly_string_tuple[0]] = integer_mat
    
    for gupta_id in gupta_alpha:
        matrices_as_ints[gupta_id[0]] = gupta_id[1]
    
    matrices_as_ints["mat:gupta-pandey-3-made-involutory"] = gupta_pandey_3_made_involutory
    matrices_as_ints["mat:sarkar-1"] = sarkar1
    matrices_as_ints["mat:sarkar-2"] = sarkar2
    matrices_as_ints["mat:sarkar-1-inv"] = sarkar1inv
    matrices_as_ints["mat:sarkar-2-inv"] = sarkar2inv
    return matrices_as_ints

def equals(mat1, mat2):
    if len(mat1) != len(mat2):
        return False
    
    rows = len(mat1)
    cols = len(mat1[0])

    for i in range(rows):
        for j in range(cols):
            if mat1[i][j] != mat2[i][j]:
                return False
    
    return True


def exists(dic, mat):
    for id in dic:
        if equals(dic[id], mat):
            return True
    return False


def test_lookup():
    cui_jin = [[1, 18, 4, 22],
                 [18, 1, 22, 4],
                 [4, 22, 1, 18],
                 [22, 4, 18, 1]]
    other = [[1, 0, 4, 22],
            [18, 1, 22, 4],
            [4, 22, 1, 18],
            [22, 4, 18, 1]]
    ms = integer_dict()
    print(exists(ms, cui_jin))
    print(exists(ms, other))

def check_that_i_have_all_matrices_on_my_lookup():
    lookup_d = integer_dict()
    pprint.pprint(lookup_d)
    print(len(lookup_d))

    objs, dicts = get_datapoint_list_from_csv()
    for datapoint in objs:
        id = datapoint.mat_id
        inv_id = datapoint.mat_inv_id
        if id not in lookup_d:
            print("id", id, "is missing")
        if inv_id not in lookup_d:
            print("inv_id", inv_id, "is missing (id: ", id, "), involutory: ", datapoint.involutory)

#check_that_i_have_all_matrices_on_my_lookup()

def export_lookup():
    lookup_d = integer_dict()
    #pprint.pprint(lookup_d)
    #print(len(lookup_d))
    print(lookup_d)
    return lookup_d

export_lookup()

