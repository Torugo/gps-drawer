import sys
import array
import yaml
import math
import os
import gmplot


class DrawMapGoogle(object):
    def __init__(self):
        self.file_path = ''
        self.datum = []
        self.virtual_fence_limits = []
        self.obstaclesPoints = []
        self.parse_yaml_data()

    def parse_yaml_data(self):
        with open(self.file_path + 'points2.yml', 'r') as f:
            doc = yaml.load(f)

        self.datum = tuple(doc['DATUM'])
        self.virtual_fence_limits = ([tuple(x) for x in doc['Fence']])
        number_of_obstacles = doc['Obstacles'].keys()
        obstacles_points = []

        for keys in number_of_obstacles:
            obstacles_points.append([tuple(d) for d in doc['Obstacles'][keys]])
        self.obstaclesPoints = obstacles_points

    def drawPath(self):
        lats =[]
        longs = []
        gmap = gmplot.GoogleMapPlotter(self.datum[0], self.datum[1], self.datum[2])
        for i in range(self.virtual_fence_limits.__len__()):
            lats.append(self.virtual_fence_limits[i][0])
            longs.append(self.virtual_fence_limits[i][1])
        gmap.plot(lats, longs, 'cornflowerblue', edge_width=10)
        gmap.draw("mymap2.html")

    def drawMarkers(self):
        lats = []
        longs = []
        gmap = gmplot.GoogleMapPlotter(self.datum[0], self.datum[1], self.datum[2])
        for i in range(self.virtual_fence_limits.__len__()):
            lats.append(self.virtual_fence_limits[i][0])
            longs.append(self.virtual_fence_limits[i][1])
       # gmap.scatter(lats, longs, '#FFFFFF', marker=True)
        gmap.heatmap(lats,longs, radius=5)
       # gmap.marker(lats[0], longs[0], "yellow")
        gmap.draw("mymap2-marker.html")

draw = DrawMapGoogle()
draw.drawPath()
draw.drawMarkers()
