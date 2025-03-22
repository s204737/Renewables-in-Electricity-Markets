import numpy as np

# Time set
Time = np.arange(1, 25)  # 1 to 24 hours
T = len(Time)

# Technical data of generating units
Technical_Data = np.array([
    [1, 1, 152, 30.4, 40, 40, 120, 120, 8, 4],
    [2, 2, 152, 30.4, 40, 40, 120, 120, 8, 4],
    [3, 7, 350, 75, 70, 70, 350, 350, 8, 8],
    [4, 13, 591, 206.85, 180, 180, 240, 240, 12, 10],
    [5, 15, 60, 12, 60, 60, 60, 60, 4, 2],
    [6, 15, 155, 54.25, 30, 30, 155, 155, 8, 8],
    [7, 16, 155, 54.25, 30, 30, 155, 155, 8, 8],
    [8, 18, 400, 100, 0, 0, 280, 280, 1, 1],
    [9, 21, 400, 100, 0, 0, 280, 280, 1, 1],
    [10, 22, 300, 300, 0, 0, 300, 300, 0, 0],
    [11, 23, 310, 108.5, 60, 60, 180, 180, 8, 8],
    [12, 23, 350, 140, 40, 40, 240, 240, 8, 8]
])

Generator = Technical_Data[:, 0]
Gen = len(Generator)
Node_Generator = Technical_Data[:, 1]
P_max = Technical_Data[:, 2]  # Maximum power output of generating unit i.
P_min = Technical_Data[:, 3]  # Minimum power output of generating unit i.
RE_up = Technical_Data[:, 4]  # Maximum up reserve capacity of generating unit i.
RE_down = Technical_Data[:, 5]
R_U = Technical_Data[:, 6]
R_D = Technical_Data[:, 7]

# Costs and initial state of generating units
Cost_Generation = np.array([
    [1, 13.32, 15, 14, 15, 11, 1430.4, 76, 1, 22],
    [2, 13.32, 15, 14, 15, 11, 1430.4, 76, 1, 22],
    [3, 20.7, 10, 9, 24, 16, 1725, 0, 0, -2],
    [4, 20.93, 8, 7, 25, 17, 3056.7, 0, 0, -1],
    [5, 26.11, 7, 5, 28, 23, 437, 0, 0, -1],
    [6, 10.52, 16, 14, 16, 7, 312, 0, 0, -2],
    [7, 10.52, 16, 14, 16, 7, 312, 124, 1, 10],
    [8, 6.02, 0, 0, 0, 0, 0, 240, 1, 50],
    [9, 5.47, 0, 0, 0, 0, 0, 240, 1, 16],
    [10, 0, 0, 0, 0, 0, 0, 240, 1, 24],
    [11, 10.52, 17, 16, 14, 8, 624, 248, 1, 10],
    [12, 10.89, 16, 14, 16, 8, 2298, 280, 1, 50]
])

PC_DA = Cost_Generation[:, 1]
C_up = Cost_Generation[:, 2]
C_down = Cost_Generation[:, 3]
C_plus = Cost_Generation[:, 4]
C_min = Cost_Generation[:, 5]

# Wind farm data
Wind_Farms = np.arange(1, 7)  # Sets of wind farms
Wind = len(Wind_Farms)
Wind_Farm_Power = np.array([200, 200, 200, 200, 200, 200])  # Nominal power of wind farms
NodeWind_Farm = np.array([3, 5, 7, 16, 21, 23])  # Nodes to which the wind farm is connected

Wind_Profile = np.array([
    [0.384460432, 0.468188963, 0.354214143, 0.537425947, 0.46937358, 0.37111684],
    [0.334138265, 0.553788979, 0.406152998, 0.512694174, 0.531810887, 0.358509552],
    [0.392110218, 0.574218542, 0.406992692, 0.518133906, 0.597325971, 0.395214423],
    [0.320718433, 0.607521212, 0.459011055, 0.576877383, 0.676225062, 0.536898567],
    [0.511097833, 0.689705275, 0.454757025, 0.647928042, 0.658362503, 0.50624571],
    [0.670195009, 0.701065357, 0.420119392, 0.532133166, 0.654655133, 0.435896556],
    [0.732582857, 0.719544957, 0.427673241, 0.580717316, 0.641608209, 0.470324736],
    [0.715879043, 0.73209317, 0.436060125, 0.605752565, 0.63559409, 0.518071779],
    [0.81648375, 0.717602431, 0.438099048, 0.64194005, 0.630391444, 0.432091298],
    [0.863173498, 0.640840115, 0.426840611, 0.631495738, 0.625639584, 0.518978163],
    [0.834677138, 0.65899331, 0.399725141, 0.618482622, 0.591320238, 0.538114817],
    [0.809602492, 0.683786403, 0.404782357, 0.616228653, 0.598926838, 0.483479766],
    [0.779704416, 0.535433021, 0.355700598, 0.530936592, 0.576361222, 0.443034623],
    [0.737250633, 0.533898049, 0.353727465, 0.417897156, 0.563630686, 0.365624062],
    [0.720228322, 0.625764506, 0.34699596, 0.47679931, 0.616744905, 0.330565254],
    [0.745210235, 0.662574663, 0.385782509, 0.608361897, 0.624430342, 0.378272196],
    [0.682319242, 0.572373099, 0.404603876, 0.653535161, 0.686978816, 0.57009666],
    [0.656484829, 0.520871683, 0.398568812, 0.661271974, 0.716878781, 0.500574286],
    [0.73425636, 0.725853275, 0.432266577, 0.737453031, 0.778559187, 0.700494381],
    [0.724073595, 0.718833404, 0.419491943, 0.698456003, 0.726262276, 0.652552273],
    [0.736487841, 0.6614544, 0.412914541, 0.649226547, 0.731735824, 0.629955212],
    [0.631564115, 0.632218983, 0.401782442, 0.625401451, 0.734800193, 0.632758619],
    [0.624393969, 0.628146584, 0.393015089, 0.615593622, 0.709583251, 0.643573958],
    [0.689311008, 0.552697271, 0.324108229, 0.551886855, 0.70269395, 0.59442964]
])

Wind_Hours = np.zeros((Wind, T))
for wind in range(Wind):
    for t in range(T):
        Wind_Hours[wind, t] = Wind_Profile[t, wind] * Wind_Farm_Power[wind]

# Load and demand data
Load_Profile = np.array([
    [1, 1775.835],
    [2, 1669.815],
    [3, 1590.3],
    [4, 1563.795],
    [5, 1563.795],
    [6, 1590.3],
    [7, 1961.37],
    [8, 2279.43],
    [9, 2517.975],
    [10, 2544.48],
    [11, 2544.48],
    [12, 2517.975],
    [13, 2517.975],
    [14, 2517.975],
    [15, 2464.965],
    [16, 2464.965],
    [17, 2623.995],
    [18, 2650.5],
    [19, 2650.5],
    [20, 2544.48],
    [21, 2411.955],
    [22, 2199.915],
    [23, 1934.865],
    [24, 1669.815]
])

Load_Demand = Load_Profile[:, 1]

Load_Node_Profile = np.array([
    [1, 1, 3.8],
    [2, 2, 3.4],
    [3, 3, 6.3],
    [4, 4, 2.6],
    [5, 5, 2.5],
    [6, 6, 4.8],
    [7, 7, 4.4],
    [8, 8, 6],
    [9, 9, 6.1],
    [10, 10, 6.8],
    [11, 13, 9.3],
    [12, 14, 6.8],
    [13, 15, 11.1],
    [14, 16, 3.5],
    [15, 18, 11.7],
    [16, 19, 6.4],
    [17, 20, 4.5]
])

# Number of nodes
N = 24      
# Sets of nodes from 1 to 24
Nodes = np.arange(1, N + 1)  
# Load data for each node
Load = Load_Node_Profile[:, 0]  # First column
# Nodes where demand is located
Node_Demand = Load_Node_Profile[:, 1]  # Second column
# Number of nodes where demand is present
Dem = len(Node_Demand)  
# Percentage of the load according to the global demand
Load_Percent = Load_Node_Profile[:, 2]  # Third column
# Number of loads
L = len(Load)  


Load_Percent = Load_Node_Profile[:, 2]
L = len(Load_Node_Profile)
L_D_Hours = np.zeros((L, T))

for l in range(L):
    for t in range(T):
        L_D_Hours[l, t] = round(Load_Percent[l] / 100 * Load_Demand[t], 1)

# Transmission line data
Transmission_Lines = np.array([
    [1, 2, 0.0146, 175],
    [1, 3, 0.2253, 175],
    [1, 5, 0.0907, 350],
    [2, 4, 0.1356, 175],
    [2, 6, 0.205, 175],
    [3, 9, 0.1271, 175],
    [3, 24, 0.084, 400],
    [4, 9, 0.111, 175],
    [5, 10, 0.094, 350],
    [6, 10, 0.0642, 175],
    [7, 8, 0.0652, 350],
    [8, 9, 0.1762, 175],
    [8, 10, 0.1762, 175],
    [9, 11, 0.084, 400],
    [9, 12, 0.084, 400],
    [10, 11, 0.084, 400],
    [10, 12, 0.084, 400],
    [11, 13, 0.0488, 500],
    [11, 14, 0.0426, 500],
    [12, 13, 0.0488, 500],
    [12, 23, 0.0985, 500],
    [13, 23, 0.0884, 500],
    [14, 16, 0.0594, 500],
    [15, 16, 0.0172, 500],
    [15, 21, 0.0249, 1000],
    [15, 24, 0.0529, 500],
    [16, 17, 0.0263, 500],
    [16, 19, 0.0234, 500],
    [17, 18, 0.0143, 500],
    [17, 22, 0.1069, 500],
    [18, 21, 0.0132, 1000],
    [19, 20, 0.0203, 1000],
    [20, 23, 0.0112, 1000],
    [21, 22, 0.0692, 500]
])

Trans_L = Transmission_Lines.shape[0]
From = Transmission_Lines[:, 0].astype(int)
To = Transmission_Lines[:, 1].astype(int)
Reac = Transmission_Lines[:, 2]
Cap = Transmission_Lines[:, 3]

# Initialize matrices
N = 24  # Number of nodes
Capacity = np.zeros((N, N))
Reactance = np.zeros((N, N))
Line = np.zeros((N, N))

# Populate matrices
for k in range(Trans_L):
    i, j = From[k] - 1, To[k] - 1 
    Capacity[i, j] = Capacity[j, i] = Cap[k]
    Reactance[i, j] = Reactance[j, i] = Reac[k]
    Line[i, j] = 1

# Compute susceptance matrix
B = np.zeros((N, N))
for i in range(N):
    for j in range(N):
        if Reactance[i, j] != 0:
            B[i, j] = 1 / Reactance[i, j]
            B[j, i] = 1 / Reactance[j, i]

# Transmission line data (sensitivity analysis)
Transmission_Lines_sen = np.array([
    [1, 2, 0.0146, 175],
    [1, 3, 0.2253, 175],
    [1, 5, 0.0907, 350],
    [2, 4, 0.1356, 175],
    [2, 6, 0.205, 175],
    [3, 9, 0.1271, 175],
    [3, 24, 0.084, 400],
    [4, 9, 0.111, 175],
    [5, 10, 0.094, 350],
    [6, 10, 0.0642, 175],
    [7, 8, 0.0652, 350],
    [8, 9, 0.1762, 175],
    [8, 10, 0.1762, 175],
    [9, 11, 0.084, 400],
    [9, 12, 0.084, 400],
    [10, 11, 0.084, 400],
    [10, 12, 0.084, 400],
    [11, 13, 0.0488, 500],
    [11, 14, 0.0426, 500],
    [12, 13, 0.0488, 500],
    [12, 23, 0.0985, 500],
    [13, 23, 0.0884, 250], # changed
    [14, 16, 0.0594, 250], # changed
    [15, 16, 0.0172, 500],
    [15, 21, 0.0249, 400], # changed
    [15, 24, 0.0529, 500],
    [16, 17, 0.0263, 500],
    [16, 19, 0.0234, 500],
    [17, 18, 0.0143, 500],
    [17, 22, 0.1069, 500],
    [18, 21, 0.0132, 1000],
    [19, 20, 0.0203, 1000],
    [20, 23, 0.0112, 1000],
    [21, 22, 0.0692, 500]
])

Trans_L_sen = Transmission_Lines_sen.shape[0]
From_sen = Transmission_Lines_sen[:, 0].astype(int)
To_sen = Transmission_Lines_sen[:, 1].astype(int)
Reac_sen = Transmission_Lines_sen[:, 2]
Cap_sen = Transmission_Lines_sen[:, 3]

# Initialize matrices
N_sen = 24  # Number of nodes
Capacity_sen = np.zeros((N_sen, N_sen))
Reactance_sen = np.zeros((N_sen, N_sen))
Line_sen = np.zeros((N_sen, N_sen))

# Populate matrices
for k in range(Trans_L_sen):
    i, j = From[k] - 1, To[k] - 1 
    Capacity_sen[i, j] = Capacity_sen[j, i] = Cap_sen[k]
    Reactance_sen[i, j] = Reactance_sen[j, i] = Reac_sen[k]
    Line_sen[i, j] = 1

# Compute susceptance matrix
B_sen = np.zeros((N_sen, N_sen))
for i in range(N_sen):
    for j in range(N_sen):
        if Reactance_sen[i, j] != 0:
            B_sen[i, j] = 1 / Reactance_sen[i, j]
            B_sen[j, i] = 1 / Reactance_sen[j, i]

# Zonal system
Node_Zone = [
    [11, 14, 15, 16, 17, 18, 19, 21, 24],
    [12, 23, 20, 22, 23],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
]
Z = len(Node_Zone)
N = max(max(zone) for zone in Node_Zone)  
Zone = np.zeros((N, Z))

# The zonal network (Building)
for n in range(N):
    for z in range(Z):
        if n+1 in Node_Zone[z]:  
            Zone[n, z] = 1

# The transfer capacities
Capacity_Zone = np.zeros((Z, Z))  # store the transfer capacities between different zones.

for z1 in range(Z):
    for z2 in range(Z):
        if z2 > z1:
            for i in range(N):
                for j in range(N):
                    if (i+1) in Node_Zone[z1] and (j+1) in Node_Zone[z2] and (Line[i, j] + Line[j, i]) == 1:
                        Capacity_Zone[z1, z2] += Capacity[i, j] 
                        Capacity_Zone[z2, z1] += Capacity[j, i] 

