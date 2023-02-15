std_msgs/Header header

float64 gpsTimeOfWeek  # GPS tow [8 bytes]
uint16  gpsWeek        # GPS week [2 bytes]
uint16  numSatsTracked # SATS Tracked [2 bytes]
uint16  numSatsUsed    # SATS Used [2 bytes]
uint8   navMode        # Nav Mode (same as message 1) [1 byte ]
uint8   spare00        # Spare [1 byte ]
float64 latitude       # Latitude degrees, -90..90 [8 bytes]
float64 longitude      # Longitude degrees, -180..180 [8 bytes]
float32 height         # (m), Altitude ellipsoid [4 bytes]
float32 speed          # Horizontal Speed m/s [4 bytes]
float32 vUp            # Vertical Velocity +up m/s [4 bytes]
float32 cog            # Course over Ground, degrees [4 bytes]
float32 heading        # Heading (degrees), Zero unless vector[4 bytes]
float32 pitch          # Pitch (degrees), Zero unless vector [4 bytes]
float32 spare01        # Spare [4 bytes]
uint16  ageOfDiff      # age of differential, seconds [2 bytes]
# uint16  attitudeStatus # Attitude Status, Zero unless vector [2 bytes]
#                        # attitudeStatus: bit {0-3} = sStatus.eYaw
#                        # bit {4-7} = sStatus.ePitch
#                        # bit {8-11} = sStatus.eRoll
#                        # where sStatus can be 0 = INVALID, 1 = GNSS, 2 = Inertial, 3= Magnetic
uint8   yawStatus
uint8   pitchStatus
uint8   rollStatus
uint8   spare02
float32 stdevHeading   # Yaw stdev, degrees, 0 unless vector [4 bytes]
float32 stdevPitch     # Pitch stdev, degrees, 0 unless vector[4 bytes]
float32 hRMS           # Horizontal RMS [4 bytes]
float32 vRMS           # Vertical RMS [4 bytes]
float32 hdop           # Horizontal DOP [4 bytes]
float32 vdop           # Vertical DOP [4 bytes]
float32 tdop           # Time DOP [4 bytes]
float32 covNN          # Covaraince North-North [4 bytes]
float32 covNE          # Covaraince North-East [4 bytes]
float32 covNU          # Covaraince North-Up [4 bytes]
float32 covEE          # Covaraince East-East [4 bytes]
float32 covEU          # Covaraince East-Up [4 bytes]
float32 covUU          # Covaraince Up-Up [4 bytes]
