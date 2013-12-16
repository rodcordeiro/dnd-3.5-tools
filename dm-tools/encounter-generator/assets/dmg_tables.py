weird_mix_cr = {
  '1/6' : ['1/8', '1/8'],
  '1/4' : ['1/6', '1/8'],
  '1/3' : ['1/4', '1/6'],
  '1/2' : ['1/3', '1/4'],
  1 : ['1/3', '1/2'],
  2 : ['1/2', 1],
  3 : [1, 2],
}

weird_same_cr = {
  1 : ['1/2', '1/3', '1/4', '1/6', '1/8', '1/8'],
  2 : [1, ['1/2', 1], '1/2', '1/3', '1/4', '1/8'],
  3 : [[1, 2], 1, ['1/2', 1], '1/2', '1/3', '1/4'],
  4 : [2, [1, 2], 1, ['1/2', 1], '1/2', '1/3'],
  5 : [3, 2, [1, 2], 1, '1/2', '1/2'],
  6 : [4, 3, 2, [1,2], 1, '1/2'],
}

xp_table = [[],
[1,300,600,900,1350,1800,2700,3600,5400,7200,10800],
[2,300,600,900,1350,1800,2700,3600,5400,7200,10800],
[3,300,600,900,1350,1800,2700,3600,5400,7200,10800],
[4,300,600,800,1200,1600,2400,3200,4800,6400,9600,12800],
[5,300,500,750,1000,1500,2250,3000,4500,6000,9000,12000,18000],
[6,300,450,600,900,1200,1800,2700,3600,5400,7200,10800,14400,21600],
[7,263,350,525,700,1050,1400,2100,3150,4200,6300,8400,12600,16800,25200],
[8,200,300,400,600,800,1200,1600,2400,3600,4800,7200,9600,14400,19200,28800],
[9,0,225,338,450,675,900,1350,1800,2700,4050,5400,8100,10800,16200,21600,32400],
[10,0,0,250,375,500,750,1000,1500,2000,3000,4500,6000,9000,12000,1800,24000,36000],
[11,0,0,0,275,413,550,825,1100,1650,2200,3300,4950,6600,9900,13200,19800,26400,39600],
[12,0,0,0,0,300,450,600,900,1200,1800,2400,3600,5400,7200,10800,14400,21600,28800,43200],
[13,0,0,0,0,0,325,488,650,975,1300,1950,2600,3900,5850,7800,11700,15600,23400,31200,46800],
[14,0,0,0,0,0,0,350,525,700,1050,1400,2100,2800,4200,6300,8400,12600,16800,25200,33600],
[15,0,0,0,0,0,0,0,375,563,750,1125,1500,2250,3000,4500,6750,9000,13500,18000,27000],
[16,0,0,0,0,0,0,0,0,400,600,800,1200,1600,2400,3200,4800,7200,9600,14400,19200],
[17,0,0,0,0,0,0,0,0,0,425,638,850,1275,1700,2550,3400,5100,7650,10200,15300],
[18,0,0,0,0,0,0,0,0,0,0,450,675,900,1350,1800,2700,3600,5400,8100,10800],
[19,0,0,0,0,0,0,0,0,0,0,0,475,713,950,1425,1900,2850,3800,5700,8550],
[20,0,0,0,0,0,0,0,0,0,0,0,0,500,750,1000,1500,2000,3000,4000,6000]]
