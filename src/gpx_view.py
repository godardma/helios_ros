#!/usr/bin/env python3
import gpxpy.gpx

def main():
	gpx = gpxpy.gpx.GPX()

	gpx_track = gpxpy.gpx.GPXTrack()
	gpx.tracks.append(gpx_track)

	gpx_segment = gpxpy.gpx.GPXTrackSegment()
	gpx_track.segments.append(gpx_segment)

	lon_list = []
	lat_list = []
	lon_data = open("lon150.txt")
	lat_data = open("lat150.txt")
	for i in lon_data.readlines():
		if i[0] == 'd':
			lon_list.append(float(i[6:]))

	for j in lat_data.readlines():
		if j[0] == 'd':
			lat_list.append(float(j[6:]))
	
	for i in range(len(lon_list)):
		gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(lat_list[i], lon_list[i]))
	
	fp = open("tst_150.gpx","w")
	fp.write(gpx.to_xml())
	fp.write("\n")
	fp.close()

if __name__ == "__main__":
	main()	
