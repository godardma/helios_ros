std_msgs/Header header

uint8   ageOfDiff     # age of differential, seconds (255 max)
uint8   numOfSats     # number of satellites used (12 max)
uint16  gpsWeek       # GPS week
float64 gpsTimeOfWeek # GPS tow
float64 latitude      # Latitude degrees, -90..90
float64 longitude     # Longitude degrees, -180..180
float32 height        # (m), Altitude ellipsoid
float32 vNorth        # Velocity north m/s
float32 vEast         # Velocity east m/s
float32 vUp           # Velocity up m/s
float32 stdDevResid   # (m), Standard Deviation of Residuals
uint16  navMode
uint16  ageOfDiffLong # age of diff using 16 bits (WHY?)

