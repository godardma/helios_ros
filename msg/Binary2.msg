std_msgs/Header header


uint32 maskSatsTracked # SATS Tracked, bit mapped 0..31
uint32 maskSatsUsed    # SATS Used, bit mapped 0..31
uint16 gpsUtcDiff      # GPS/UTC time difference (GPS minus UTC)
uint16 hdopTimes10     # HDOP (0.1 units)
uint16 vdopTimes10     # VDOP (0.1 units)
uint16 waasMask        # Bits 0-1: tracked sats, Bits 2-3:
                       # used sats, Bits 5-9 WAAS PRN 1 minus
                       # 120, Bits 10-14 WAAS PRN 1 minus 120
