import pprint

matrices_as_strings = {"mat:shark":'''
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
'''}

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
        integer_mat = convert(g(id))
        matrices_as_ints[id] = integer_mat
    return matrices_as_ints

pprint.pprint(integer_dict())