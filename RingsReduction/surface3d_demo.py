from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')
X = np.arange(233.4, 233.61, 0.02)
Y = np.arange(269.4, 269.61, 0.02)
X, Y = np.meshgrid(X, Y)

# Slice 5
Z5 = np.array([[1.2771,1.27673,1.27643,1.27624,1.27604,1.27604,1.27609,1.27619,1.27643,1.27665,1.27699],[1.27671,1.27635,1.27619,1.27592,1.27571,1.2757,1.27573,1.27594,1.27611,1.27636,1.27669],[1.27645,1.2761,1.2759,1.27564,1.27555,1.27543,1.2755,1.27564,1.27585,1.27607,1.27639],[1.27629,1.27597,1.27567,1.27548,1.27533,1.27527,1.27535,1.27544,1.27563,1.27593,1.27622],[1.27626,1.27589,1.27559,1.27533,1.27521,1.27515,1.27521,1.27531,1.27554,1.27578,1.27608],[1.27632,1.27593,1.27564,1.2754,1.27527,1.27522,1.27518,1.27526,1.2755,1.2758,1.27611],[1.27644,1.27602,1.27564,1.27545,1.27532,1.27526,1.27527,1.27532,1.2755,1.27584,1.27619],[1.27658,1.27616,1.27581,1.27557,1.27539,1.27544,1.2754,1.27549,1.27569,1.27603,1.27636],[1.27684,1.27644,1.27608,1.27585,1.27573,1.27567,1.27567,1.27577,1.27592,1.27628,1.27663],[1.27709,1.27674,1.27635,1.27617,1.27599,1.27593,1.27595,1.27603,1.27629,1.27656,1.27692],[1.27747,1.27709,1.27677,1.27658,1.27644,1.27633,1.27631,1.27643,1.27673,1.27695,1.27732]])


Z100 = np.array([[1.42041,1.41966,1.41918,1.41879,1.41862,1.41844,1.41838,1.41865,1.4191,1.41974,1.42052],[1.41976,1.41902,1.41845,1.41822,1.41805,1.4179,1.41789,1.41806,1.41858,1.4192,1.41997],[1.41914,1.41851,1.41797,1.41767,1.41761,1.4174,1.41742,1.41771,1.41805,1.41873,1.41946],[1.41901,1.41829,1.41779,1.41749,1.4173,1.41715,1.41724,1.41758,1.41789,1.4184,1.41912],[1.41904,1.41839,1.4178,1.41741,1.41723,1.41706,1.41714,1.41746,1.41788,1.41826,1.41901],[1.41908,1.41846,1.41794,1.41741,1.41719,1.41713,1.41727,1.41755,1.41795,1.41838,1.41911],[1.41924,1.41856,1.41813,1.41762,1.41739,1.41739,1.41734,1.41757,1.4181,1.41863,1.41924],[1.41951,1.41884,1.41839,1.41799,1.41773,1.41759,1.41762,1.41784,1.41835,1.41876,1.41951],[1.42011,1.41933,1.41879,1.41834,1.4181,1.41799,1.41808,1.41826,1.41873,1.41912,1.41977],[1.42063,1.4199,1.41932,1.41886,1.41854,1.41843,1.41844,1.41865,1.41908,1.41968,1.42048],[1.42125,1.42048,1.41995,1.41957,1.41921,1.41906,1.41927,1.41939,1.41978,1.4204,1.42107]])



Z350 = np.array([[1.20831,1.20744,1.20681,1.20616,1.20568,1.20551,1.20564,1.20602,1.20652,1.20741,1.20851],[1.20775,1.20675,1.2064,1.20542,1.20493,1.20506,1.20501,1.20527,1.20605,1.20684,1.20795],[1.20738,1.20633,1.20571,1.20502,1.20456,1.20468,1.20463,1.20471,1.20547,1.20638,1.20738],[1.20693,1.20599,1.20524,1.20467,1.20469,1.20444,1.20447,1.20451,1.2051,1.20596,1.20679],[1.20659,1.20595,1.20515,1.20466,1.2048,1.20438,1.20424,1.20444,1.2049,1.20572,1.20652],[1.20642,1.20583,1.20494,1.20475,1.20457,1.2044,1.2043,1.20403,1.20495,1.20601,1.20676],[1.20652,1.20598,1.20513,1.20475,1.20476,1.20472,1.2047,1.20468,1.20541,1.20628,1.20721],[1.20706,1.20638,1.20562,1.2051,1.20491,1.20516,1.20524,1.20526,1.2059,1.20691,1.20763],[1.20769,1.20701,1.20658,1.20604,1.20572,1.20591,1.20605,1.20609,1.20682,1.20738,1.20816],[1.20836,1.20777,1.2071,1.20664,1.2066,1.20654,1.20686,1.20702,1.2076,1.20819,1.20912],[1.20948,1.20877,1.20821,1.20765,1.20747,1.20747,1.20783,1.20805,1.20861,1.20916,1.21018]])



Z400 = np.array([[1.49207,1.49106,1.49023,1.48954,1.48933,1.48939,1.4894,1.48967,1.49012,1.49053,1.49143],[1.49125,1.49042,1.4897,1.48904,1.48876,1.48873,1.48873,1.48905,1.48954,1.49,1.49096],[1.49093,1.49007,1.48935,1.48852,1.48833,1.4883,1.4882,1.48857,1.48899,1.48949,1.49048],[1.49065,1.48982,1.48925,1.48842,1.48815,1.48823,1.48821,1.48842,1.48868,1.48942,1.49023],[1.49046,1.4896,1.489,1.4884,1.48796,1.48802,1.48813,1.48829,1.4886,1.48944,1.49032],[1.49054,1.48956,1.48901,1.48835,1.48797,1.48807,1.48808,1.48812,1.4887,1.48947,1.49027],[1.49089,1.49003,1.4894,1.48884,1.48856,1.4886,1.48842,1.48865,1.48902,1.48978,1.49081],[1.49146,1.49055,1.4899,1.48929,1.48898,1.48889,1.48899,1.48935,1.48977,1.49031,1.4913],[1.49218,1.4914,1.49058,1.49002,1.48948,1.48952,1.48968,1.4901,1.49043,1.49083,1.4918],[1.49288,1.49219,1.49145,1.49105,1.4905,1.49046,1.49062,1.491,1.49144,1.49191,1.49277],[1.49398,1.49328,1.49273,1.49197,1.49162,1.49158,1.49179,1.49205,1.49264,1.49304,1.49382]])



Z450 = np.array([[1.48683,1.48611,1.48559,1.48528,1.48505,1.48497,1.48496,1.48508,1.48538,1.48578,1.48626],[1.48654,1.48584,1.48527,1.48495,1.48471,1.48459,1.48467,1.48487,1.48509,1.48553,1.48593],[1.48634,1.48562,1.48502,1.48476,1.48454,1.4845,1.48457,1.48469,1.48491,1.48519,1.48574],[1.48615,1.48548,1.48494,1.48463,1.48446,1.48446,1.48453,1.4846,1.4848,1.48514,1.48568],[1.4862,1.4856,1.485,1.48474,1.48449,1.48449,1.48453,1.48474,1.48487,1.48524,1.48572],[1.48633,1.48568,1.48525,1.48482,1.48469,1.48466,1.4848,1.48487,1.48513,1.48542,1.48589],[1.48661,1.48589,1.48549,1.48519,1.48489,1.48498,1.48502,1.48516,1.48549,1.48584,1.48638],[1.48696,1.48628,1.48574,1.48556,1.48542,1.48537,1.48536,1.48551,1.48584,1.48624,1.48672],[1.4875,1.48687,1.48634,1.48599,1.48595,1.48589,1.48585,1.48589,1.48614,1.48661,1.48716],[1.48824,1.48753,1.48707,1.48671,1.48659,1.4865,1.48655,1.48666,1.48688,1.48727,1.48788],[1.48905,1.48828,1.48781,1.48744,1.48734,1.48723,1.48722,1.48741,1.48763,1.48799,1.4887]])


Z600 = np.array([[0.947064,0.946591,0.946219,0.945946,0.945702,0.945599,0.945587,0.945695,0.946051,0.94653,0.947005],[0.94653,0.946084,0.945762,0.945518,0.945215,0.945128,0.945186,0.945296,0.945623,0.946139,0.946666],[0.946206,0.945756,0.945376,0.94506,0.944945,0.944791,0.944894,0.94502,0.945283,0.945759,0.946321],[0.945979,0.94556,0.945159,0.944978,0.944738,0.944639,0.944721,0.94491,0.94514,0.945504,0.945999],[0.945786,0.945334,0.944962,0.944832,0.944627,0.944525,0.944628,0.944786,0.945005,0.945409,0.945911],[0.945819,0.945376,0.944994,0.944785,0.944565,0.944528,0.944643,0.944837,0.945076,0.945455,0.945867],[0.945853,0.945458,0.945124,0.944852,0.944583,0.944616,0.944741,0.944919,0.945138,0.945578,0.945997],[0.946098,0.945702,0.945333,0.944998,0.944823,0.944857,0.945028,0.945193,0.945408,0.945785,0.946211],[0.946454,0.946002,0.945725,0.945437,0.94522,0.94521,0.945365,0.945486,0.945791,0.946116,0.946478],[0.946884,0.946535,0.946172,0.945891,0.945723,0.945673,0.945843,0.945976,0.946238,0.946628,0.947056],[0.947378,0.947005,0.946628,0.946405,0.94626,0.946184,0.946279,0.946469,0.946795,0.947141,0.94764]])


# Slice 800
Z800 = np.array([[0.314264,0.314129,0.314016,0.313937,0.31387,0.313871,0.313863,0.313892,0.313937,0.314018,0.314136],[0.314133,0.314016,0.313895,0.313818,0.313755,0.313754,0.313762,0.313791,0.313836,0.313888,0.313991],[0.314053,0.313909,0.313804,0.313723,0.313693,0.313668,0.313667,0.31369,0.313743,0.313815,0.313914],[0.314012,0.313871,0.313747,0.313669,0.313615,0.313594,0.3136,0.313636,0.313658,0.313736,0.313862],[0.313977,0.313848,0.313728,0.313649,0.313601,0.313539,0.313572,0.313598,0.313624,0.313714,0.313819],[0.313976,0.313821,0.313719,0.313647,0.313578,0.313528,0.313553,0.313588,0.313629,0.31369,0.313843],[0.313987,0.313853,0.313737,0.31365,0.313588,0.313572,0.313584,0.313619,0.313658,0.313758,0.313869],[0.31406,0.31392,0.313806,0.313717,0.313641,0.313625,0.313616,0.313639,0.31372,0.313795,0.313922],[0.314124,0.313966,0.313885,0.313789,0.313721,0.313711,0.313693,0.313726,0.3138,0.313888,0.313983],[0.314208,0.314066,0.31396,0.313886,0.313834,0.313809,0.313794,0.313826,0.313883,0.313953,0.314078],[0.314317,0.314203,0.31409,0.313976,0.313939,0.313946,0.313929,0.313981,0.314022,0.314103,0.314212]])


surf = ax.plot_surface(X, Y, Z350, rstride=1, cstride=1, cmap=cm.coolwarm,
        linewidth=0, antialiased=False)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()

