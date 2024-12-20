def puntuacion_tipica_mg(rango,pd):
    motricidad_gruesa=[
    [2,13,25,36,48,59,71,82,93,105,116,128,139,150,162,173,185,196,208,219,230,242,253,265,276,287,299,310,322,333,345,356,367,379,390,402,413],
    [None,0,11,21,31,41,51,61,72,82,92,102,112,122,132,143,153,163,173,183,193,204,214,224,234,244,254,265,275,285,295,305,315,325,336,346,356],
    [None,None,None,None,8,16,25,33,42,50,58,67,75,84,92,100,109,117,126,134,142,151,159,168,176,185,193,201,210,218,227,235,243,252,260,269,277],
    [None,None,None,None,None,0,8,15,22,29,37,44,51,58,66,73,80,88,95,102,109,117,124,131,138,146,153,160,167,175,182,189,197,204,211,218,226],
    [None,None,None,None,None,None,None,2,9,15,22,28,35,41,47,54,60,67,73,80,86,93,99,106,112,119,125,132,138,144,151,157,164,170,177,183,190],
    [None,None,None,None,None,None,None,None,None,1,6,12,17,23,29,34,40,46,51,57,63,68,74,80,85,91,97,102,108,114,119,125,131,136,142,148,153],
    [None,None,None,None,None,None,None,None,None,None,None,None,3,8,13,18,23,28,33,38,43,48,53,58,63,68,73,78,83,88,93,98,103,108,113,118,123],
    [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,3,7,12,16,21,25,30,34,39,43,48,52,57,61,66,70,75,79,84,88,93,97],
    [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,2,6,11,15,19,24,28,33,37,41,46,50,54,59,63,68,72,76,81],
    [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,2,7,11,16,20,25,30,34,39,43,48,53,57,62,66,71,76],
    [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,4,10,17,23,30,36,43,49,56,62,69],
    [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,11,24,37,51]
    ]
    return motricidad_gruesa[rango-1][pd]



def puntuacion_tipica_mf(rango,pd):
    motricidad_fina=[
    [0,12,32,52,72,92,112,132,152,172,192,212,232,252,272,292,312,332,352,372,392,412,432,452,472,492,512,532,552,572,592,612,632,652,672,692,712],
    [4,11,19,26,33,40,47,55,62,69,76,83,91,98,105,112,119,127,134,141,148,155,163,170,177,184,191,199,206,213,220,227,235,242,249,256,263],
    [None,5,11,17,23,29,34,40,46,52,58,64,70,76,82,88,94,100,106,112,118,124,130,136,142,148,154,160,166,172,178,184,190,196,202,208,214],
    [None,None,None,2,8,15,21,27,33,39,46,52,58,64,70,77,83,89,95,101,108,114,120,126,132,139,145,151,157,163,170,176,182,188,194,201,207],
    [None,None,None,None,None,0,7,13,20,26,32,39,45,52,58,65,71,77,84,90,97,103,110,116,122,129,135,142,148,155,161,168,174,180,187,193,200],
    [None,None,None,None,None,None,None,None,5,11,17,23,29,34,40,46,52,58,64,70,76,82,88,94,100,106,112,118,124,130,136,142,148,154,160,166,172],
    [None,None,None,None,None,None,None,None,None,None,None,None,None,7,14,21,28,35,42,50,57,64,71,78,85,93,100,107,114,121,129,136,143,150,157,164,172],
    [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,4,10,16,23,29,35,41,47,53,59,65,71,77,83,89,96,102,108,114,120,126],
    [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,1,6,11,17,22,28,33,39,44,49,55,60,66,71,77,82,88,93],
    [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,4,11,17,23,30,36,43,49,55,62,68,75,81,87],
    [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,5,11,17,23,29,35,41,47,53,59,65,71],
    [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,0,9,18,28,37,46,55,64,73,82]
    ]
    return motricidad_fina[rango-1][pd]



def puntuacion_tipica_al(rango,pd):
    audicion_lenguaje=[
    [None,None,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320,330,340,350],
    [None,None,3,12,22,31,40,49,58,67,77,86,95,104,113,123,132,141,150,159,168,178,187,196,205,214,224,233,242,251,260,270,279,288,297,306,315],
    [None,None,None,1,9,17,25,33,41,49,56,64,72,80,88,96,104,112,120,128,136,144,152,160,168,176,184,192,200,208,216,224,232,240,248,256,264],
    [None,None,None,None,None,6,13,20,27,34,42,49,56,63,70,77,84,91,98,105,113,120,127,134,141,148,155,162,169,176,184,191,198,205,212,219,226],
    [None,None,None,None,None,None,4,11,17,23,30,36,43,49,56,62,69,75,82,88,94,101,107,114,120,127,133,140,146,153,159,166,172,178,185,191,198],
    [None,None,None,None,None,None,None,None,5,11,16,22,28,34,39,45,51,57,63,68,74,80,86,91,97,103,109,114,120,126,132,137,143,149,155,161,166],
    [None,None,None,None,None,None,None,None,None,None,3,8,13,18,23,28,34,39,44,49,54,59,65,70,75,80,85,90,96,101,106,111,116,121,127,132,137],
    [None,None,None,None,None,None,None,None,None,None,None,None,None,1,5,10,15,19,24,29,33,38,43,47,52,57,61,66,71,75,80,85,89,94,99,104,108],
    [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,4,8,13,17,22,26,31,35,40,44,49,53,58,62,67,71,76,80,85],
    [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,2,6,11,15,20,25,29,34,38,43,48,52,57,62,66,71,75],
    [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,1,7,12,18,24,29,35,41,46,52,58,63],
    [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,6,14,22,31,39,47,55,64]
    ]
    return audicion_lenguaje[rango-1][pd]

def puntuacion_tipica_ps(rango,pd):
    personal_social=[
    [0,8,17,25,34,42,50,59,67,76,84,92,101,109,118,126,134,143,151,160,168,176,185,193,202,210,218,227,235,244,252,260,269,277,286,294,302],
    [None,3,11,18,26,34,41,49,57,64,72,79,87,95,102,110,118,125,133,141,148,156,163,171,179,186,194,202,209,217,225,232,240,248,255,263,270],
    [None,None,1,8,14,21,27,34,40,47,53,60,67,73,80,86,93,99,106,112,119,125,132,138,145,152,158,165,171,178,184,191,197,204,210,217,223],
    [None,None,None,None,6,11,17,23,29,34,40,46,52,58,63,69,75,81,86,92,98,104,110,115,121,127,133,138,144,150,156,162,167,173,179,185,190],
    [None,None,None,None,None,4,9,14,20,25,30,35,41,46,51,56,61,67,72,77,82,88,93,98,103,109,114,119,124,130,135,140,145,150,156,161,166],
    [None,None,None,None,None,None,None,4,9,14,18,23,28,32,37,42,46,51,56,60,65,70,74,79,84,88,93,98,102,107,112,116,121,126,130,135,140],
    [None,None,None,None,None,None,None,None,None,2,6,10,15,19,23,27,31,36,40,44,48,52,57,61,65,69,74,78,82,86,90,95,99,103,107,111,116],
    [None,None,None,None,None,None,None,None,None,None,None,None,None,3,7,11,15,19,22,26,30,34,38,42,46,50,54,57,61,65,69,73,77,81,85,89,92],
    [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,3,7,11,15,19,23,27,31,35,39,43,47,50,54,58,62,66,70,74],
    [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,3,7,12,16,20,24,29,33,37,41,46,50,54,58,62,67],
    [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,6,12,19,26,33,39,46,53,59],
    [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,18,39,61,82]
    ]
    return personal_social[rango-1][pd]