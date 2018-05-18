# -*- coding: utf-8 -*-

###
### This file is generated automatically by SALOME v7.8.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
theStudy = salome.myStudy

import salome_notebook
notebook = salome_notebook.NoteBook(theStudy)
sys.path.insert( 0, r'/home/jukka/Documents')

###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS


geompy = geomBuilder.New(theStudy)

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
Face_1 = geompy.MakeFaceHW(200, 200, 1)
Disk_1 = geompy.MakeDiskR(50, 1)
geompy.TranslateDXDYDZ(Disk_1, 0, 50, 0)
[Wire_1] = geompy.ExtractShapes(Disk_1, geompy.ShapeType["WIRE"], True)
geompy.TranslateDXDYDZ(Face_1, 0, -100, 0)
[Wire_2] = geompy.ExtractShapes(Face_1, geompy.ShapeType["WIRE"], True)
Vertex_1 = geompy.MakeVertex(-20, 10, 0)
Vertex_2 = geompy.MakeVertex(-10, 10, 0)
Vertex_3 = geompy.MakeVertex(10, 10, 0)
Vertex_4 = geompy.MakeVertex(20, 10, 0)
Vertex_5 = geompy.MakeVertex(-20, -10, 0)
Vertex_6 = geompy.MakeVertex(-10, -10, 0)
Vertex_7 = geompy.MakeVertex(10, -10, 0)
Vertex_8 = geompy.MakeVertex(20, -10, 0)
Line_1 = geompy.MakeLineTwoPnt(Vertex_1, Vertex_5)
Line_2 = geompy.MakeLineTwoPnt(Vertex_2, Vertex_6)
Line_3 = geompy.MakeLineTwoPnt(Vertex_3, Vertex_7)
Line_4 = geompy.MakeLineTwoPnt(Vertex_4, Vertex_8)
Partition_1 = geompy.MakePartition([Wire_1], [Line_1, Line_2, Line_3, Line_4], [], [], geompy.ShapeType["WIRE"], 0, [], 0)
Partition_2 = geompy.MakePartition([Wire_2], [Line_1, Line_2, Line_3, Line_4], [], [], geompy.ShapeType["WIRE"], 0, [], 0)
CYLINDER = geompy.MakeFaceWires([Partition_1], 1)
BLOCK = geompy.MakeFaceWires([Partition_2], 1)
Vertex_9 = geompy.MakeVertex(0, 80, 0)
Vertex_10 = geompy.MakeVertex(0, 120, 0)
Vertex_11 = geompy.MakeVertex(0, -180, 0)
Vertex_12 = geompy.MakeVertex(0, -220, 0)
Line_5 = geompy.MakeLineTwoPnt(Vertex_9, Vertex_10)
Line_6 = geompy.MakeLineTwoPnt(Vertex_11, Vertex_12)
CYLINDER_1 = geompy.MakePartition([CYLINDER], [Line_5], [], [], geompy.ShapeType["FACE"], 0, [], 0)
listSubShapeIDs = geompy.SubShapeAllIDs(CYLINDER_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(CYLINDER_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(CYLINDER_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(CYLINDER_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(CYLINDER_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(CYLINDER_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(CYLINDER_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(CYLINDER_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(CYLINDER_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(CYLINDER_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(CYLINDER_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(CYLINDER_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(CYLINDER_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(CYLINDER_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(CYLINDER_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(CYLINDER_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(CYLINDER_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(CYLINDER_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(CYLINDER_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(CYLINDER_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(CYLINDER_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(CYLINDER_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(CYLINDER_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(CYLINDER_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(CYLINDER_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(CYLINDER_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(CYLINDER_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(CYLINDER_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(CYLINDER_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(CYLINDER_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(CYLINDER_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(CYLINDER_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(CYLINDER_1, geompy.ShapeType["EDGE"])
BLOCK_1 = geompy.MakePartition([BLOCK], [Line_6], [], [], geompy.ShapeType["FACE"], 0, [], 0)
listSubShapeIDs = geompy.SubShapeAllIDs(BLOCK_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(BLOCK_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(BLOCK_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(BLOCK_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(BLOCK_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(BLOCK_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(BLOCK_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(BLOCK_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(BLOCK_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(BLOCK_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(BLOCK_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(BLOCK_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(BLOCK_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(BLOCK_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(BLOCK_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(BLOCK_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(BLOCK_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(BLOCK_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(BLOCK_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(BLOCK_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(BLOCK_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(BLOCK_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(BLOCK_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(BLOCK_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(BLOCK_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(BLOCK_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(BLOCK_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(BLOCK_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(BLOCK_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(BLOCK_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(BLOCK_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(BLOCK_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(BLOCK_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(BLOCK_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(BLOCK_1, geompy.ShapeType["EDGE"])
listSubShapeIDs = geompy.SubShapeAllIDs(BLOCK_1, geompy.ShapeType["EDGE"])
BLOCK_BOTTOM = geompy.CreateGroup(BLOCK_1, geompy.ShapeType["EDGE"])
geompy.UnionIDs(BLOCK_BOTTOM, [6])
BLOCK_SYMMETRY = geompy.CreateGroup(BLOCK_1, geompy.ShapeType["EDGE"])
geompy.UnionIDs(BLOCK_SYMMETRY, [20])
BLOCK_TO_CYLINDER = geompy.CreateGroup(BLOCK_1, geompy.ShapeType["EDGE"])
geompy.UnionIDs(BLOCK_TO_CYLINDER, [16])
CYLINDER_TO_BLOCK = geompy.CreateGroup(CYLINDER_1, geompy.ShapeType["EDGE"])
geompy.UnionIDs(CYLINDER_TO_BLOCK, [12])
CYLINDER_SYMMETRY = geompy.CreateGroup(CYLINDER_1, geompy.ShapeType["EDGE"])
geompy.UnionIDs(CYLINDER_SYMMETRY, [14])
geompy.DifferenceIDs(CYLINDER_TO_BLOCK, [12])
geompy.UnionIDs(CYLINDER_TO_BLOCK, [14])
geompy.DifferenceIDs(CYLINDER_SYMMETRY, [14])
geompy.UnionIDs(CYLINDER_SYMMETRY, [16])
geompy.DifferenceIDs(BLOCK_BOTTOM, [6])
geompy.UnionIDs(BLOCK_BOTTOM, [6, 10])
geompy.DifferenceIDs(BLOCK_BOTTOM, [6, 10])
geompy.UnionIDs(BLOCK_BOTTOM, [6, 10])
geompy.DifferenceIDs(BLOCK_BOTTOM, [6, 10])
geompy.UnionIDs(BLOCK_BOTTOM, [6, 10])
geompy.DifferenceIDs(BLOCK_SYMMETRY, [20])
geompy.UnionIDs(BLOCK_SYMMETRY, [22])
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Face_1, 'Face_1' )
geompy.addToStudy( Disk_1, 'Disk_1' )
geompy.addToStudyInFather( Disk_1, Wire_1, 'Wire_1' )
geompy.addToStudyInFather( Face_1, Wire_2, 'Wire_2' )
geompy.addToStudy( Vertex_1, 'Vertex_1' )
geompy.addToStudy( Vertex_2, 'Vertex_2' )
geompy.addToStudy( Vertex_3, 'Vertex_3' )
geompy.addToStudy( Vertex_4, 'Vertex_4' )
geompy.addToStudy( Vertex_5, 'Vertex_5' )
geompy.addToStudy( Vertex_6, 'Vertex_6' )
geompy.addToStudy( Vertex_7, 'Vertex_7' )
geompy.addToStudy( Vertex_8, 'Vertex_8' )
geompy.addToStudy( Line_1, 'Line_1' )
geompy.addToStudy( Line_2, 'Line_2' )
geompy.addToStudy( Line_3, 'Line_3' )
geompy.addToStudy( Line_4, 'Line_4' )
geompy.addToStudy( Partition_1, 'Partition_1' )
geompy.addToStudy( Partition_2, 'Partition_2' )
geompy.addToStudy( CYLINDER, 'CYLINDER' )
geompy.addToStudy( BLOCK, 'BLOCK' )
geompy.addToStudy( Vertex_9, 'Vertex_9' )
geompy.addToStudy( Vertex_10, 'Vertex_10' )
geompy.addToStudy( Vertex_11, 'Vertex_11' )
geompy.addToStudy( Vertex_12, 'Vertex_12' )
geompy.addToStudy( Line_5, 'Line_5' )
geompy.addToStudy( Line_6, 'Line_6' )
geompy.addToStudy( CYLINDER_1, 'CYLINDER' )
geompy.addToStudy( BLOCK_1, 'BLOCK' )
geompy.addToStudyInFather( BLOCK_1, BLOCK_BOTTOM, 'BLOCK_BOTTOM' )
geompy.addToStudyInFather( BLOCK_1, BLOCK_SYMMETRY, 'BLOCK_SYMMETRY' )
geompy.addToStudyInFather( BLOCK_1, BLOCK_TO_CYLINDER, 'BLOCK_TO_CYLINDER' )
geompy.addToStudyInFather( CYLINDER_1, CYLINDER_TO_BLOCK, 'CYLINDER_TO_BLOCK' )
geompy.addToStudyInFather( CYLINDER_1, CYLINDER_SYMMETRY, 'CYLINDER_SYMMETRY' )

###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New(theStudy)
NETGEN_2D = smesh.CreateHypothesis('NETGEN_2D', 'libNETGENEngine.so')
block_1mm = smesh.CreateHypothesis('NETGEN_Parameters_2D', 'libNETGENEngine.so')
block_1mm.SetMaxSize( 20 )
block_1mm.SetSecondOrder( 0 )
block_1mm.SetOptimize( 1 )
block_1mm.SetFineness( 3 )
block_1mm.SetMinSize( 5 )
block_1mm.SetUseSurfaceCurvature( 1 )
block_1mm.SetFuseEdges( 1 )
block_1mm.SetQuadAllowed( 0 )
block_1mm.SetLocalSizeOnShape(BLOCK_TO_CYLINDER, 1)
cylinder_1mm = smesh.CreateHypothesis('NETGEN_Parameters_2D', 'libNETGENEngine.so')
cylinder_1mm.SetMaxSize( 20 )
cylinder_1mm.SetSecondOrder( 0 )
cylinder_1mm.SetOptimize( 1 )
cylinder_1mm.SetFineness( 3 )
cylinder_1mm.SetMinSize( 5 )
cylinder_1mm.SetUseSurfaceCurvature( 1 )
cylinder_1mm.SetFuseEdges( 1 )
cylinder_1mm.SetQuadAllowed( 0 )
cylinder_1mm.SetLocalSizeOnShape(CYLINDER_TO_BLOCK, 1)
CYLINDER_2 = smesh.Mesh(CYLINDER_1)
status = CYLINDER_2.AddHypothesis(cylinder_1mm)
status = CYLINDER_2.AddHypothesis(NETGEN_2D)
isDone = CYLINDER_2.Compute()
BLOCK_2 = smesh.Mesh(BLOCK_1)
status = BLOCK_2.AddHypothesis(block_1mm)
status = BLOCK_2.AddHypothesis(NETGEN_2D)
isDone = BLOCK_2.Compute()
CYLINDER_3 = CYLINDER_2.GroupOnGeom(CYLINDER_1,'CYLINDER',SMESH.FACE)
CYLINDER_TO_BLOCK_1 = CYLINDER_2.GroupOnGeom(CYLINDER_TO_BLOCK,'CYLINDER_TO_BLOCK',SMESH.EDGE)
CYLINDER_SYMMETRY_1 = CYLINDER_2.GroupOnGeom(CYLINDER_SYMMETRY,'CYLINDER_SYMMETRY',SMESH.EDGE)
BLOCK_3 = BLOCK_2.GroupOnGeom(BLOCK_1,'BLOCK',SMESH.FACE)
BLOCK_BOTTOM_1 = BLOCK_2.GroupOnGeom(BLOCK_BOTTOM,'BLOCK_BOTTOM',SMESH.EDGE)
BLOCK_SYMMETRY_1 = BLOCK_2.GroupOnGeom(BLOCK_SYMMETRY,'BLOCK_SYMMETRY',SMESH.EDGE)
BLOCK_TO_CYLINDER_1 = BLOCK_2.GroupOnGeom(BLOCK_TO_CYLINDER,'BLOCK_TO_CYLINDER',SMESH.EDGE)
MESH1 = smesh.Concatenate([CYLINDER_2.GetMesh(), BLOCK_2.GetMesh()], 1, 0, 1e-05)
[ CYLINDER_4, CYLINDER_TO_BLOCK_2, CYLINDER_SYMMETRY_2, BLOCK_4, BLOCK_BOTTOM_2, BLOCK_SYMMETRY_2, BLOCK_TO_CYLINDER_2 ] = MESH1.GetGroups()
MESH1.SetAutoColor( 1 )
[ CYLINDER_4, CYLINDER_TO_BLOCK_2, CYLINDER_SYMMETRY_2, BLOCK_4, BLOCK_BOTTOM_2, BLOCK_SYMMETRY_2, BLOCK_TO_CYLINDER_2 ] = MESH1.GetGroups()
CYLINDER_4.SetColor( SALOMEDS.Color( 0.396078, 0.8, 0.396078 ))
CYLINDER_TO_BLOCK_2.SetColor( SALOMEDS.Color( 0.396078, 0.8, 0.8 ))
CYLINDER_SYMMETRY_2.SetColor( SALOMEDS.Color( 0.396078, 0.396078, 0.8 ))
BLOCK_4.SetColor( SALOMEDS.Color( 0.8, 0.396078, 0.8 ))
BLOCK_BOTTOM_2.SetColor( SALOMEDS.Color( 0.6, 0.298039, 0.298039 ))
BLOCK_SYMMETRY_2.SetColor( SALOMEDS.Color( 0.6, 0.6, 0.298039 ))
BLOCK_TO_CYLINDER_2.SetColor( SALOMEDS.Color( 0.298039, 0.6, 0.298039 ))
smesh.SetName(MESH1, 'MESH1')
try:
  MESH1.ExportMED( r'/home/jukka/Documents/2d_hertz_mesh.med', 0, SMESH.MED_V2_2, 1, None ,1)
except:
  print 'ExportToMEDX() failed. Invalid file name?'
cylinder_3mm = smesh.CreateHypothesis('NETGEN_Parameters_2D', 'NETGENEngine')
cylinder_3mm.SetMaxSize( 20 )
cylinder_3mm.SetSecondOrder( 0 )
cylinder_3mm.SetOptimize( 1 )
cylinder_3mm.SetFineness( 3 )
cylinder_3mm.SetMinSize( 5 )
cylinder_3mm.SetUseSurfaceCurvature( 1 )
cylinder_3mm.SetFuseEdges( 1 )
cylinder_3mm.SetQuadAllowed( 0 )
cylinder_3mm.SetLocalSizeOnShape(CYLINDER_TO_BLOCK, 3)
status = CYLINDER_2.RemoveHypothesis(cylinder_1mm)
status = CYLINDER_2.AddHypothesis(cylinder_3mm)
isDone = CYLINDER_2.Compute()
[ CYLINDER_3, CYLINDER_TO_BLOCK_1, CYLINDER_SYMMETRY_1 ] = CYLINDER_2.GetGroups()
block_4mm = smesh.CreateHypothesis('NETGEN_Parameters_2D', 'NETGENEngine')
block_4mm.SetMaxSize( 20 )
block_4mm.SetSecondOrder( 0 )
block_4mm.SetOptimize( 1 )
block_4mm.SetMinSize( 5 )
block_4mm.SetUseSurfaceCurvature( 1 )
block_4mm.SetFuseEdges( 1 )
block_4mm.SetQuadAllowed( 0 )
block_4mm.SetLocalSizeOnShape(BLOCK_TO_CYLINDER, 4)
block_4mm.SetFineness( 3 )
status = BLOCK_2.RemoveHypothesis(block_1mm)
status = BLOCK_2.AddHypothesis(block_4mm)
isDone = BLOCK_2.Compute()
[ BLOCK_3, BLOCK_BOTTOM_1, BLOCK_SYMMETRY_1, BLOCK_TO_CYLINDER_1 ] = BLOCK_2.GetGroups()
MESH2 = smesh.Concatenate([CYLINDER_2.GetMesh(), BLOCK_2.GetMesh()], 1, 0, 1e-05)
[ CYLINDER_5, CYLINDER_TO_BLOCK_3, CYLINDER_SYMMETRY_3, BLOCK_5, BLOCK_BOTTOM_3, BLOCK_SYMMETRY_3, BLOCK_TO_CYLINDER_3 ] = MESH2.GetGroups()
smesh.SetName(MESH2, 'MESH2')
try:
  MESH2.ExportMED( r'/home/jukka/Documents/2d_hertz_mesh.med', 0, SMESH.MED_V2_2, 0, None ,1)
except:
  print 'ExportToMEDX() failed. Invalid file name?'


## Set names of Mesh objects
smesh.SetName(NETGEN_2D, 'NETGEN_2D')
smesh.SetName(cylinder_1mm, 'cylinder_1mm')
smesh.SetName(cylinder_3mm, 'cylinder 3mm')
smesh.SetName(block_1mm, 'block_1mm')
smesh.SetName(block_4mm, 'block_4mm')
smesh.SetName(MESH2.GetMesh(), 'MESH2')
smesh.SetName(CYLINDER_2.GetMesh(), 'CYLINDER')
smesh.SetName(BLOCK_TO_CYLINDER_2, 'BLOCK_TO_CYLINDER')
smesh.SetName(BLOCK_SYMMETRY_2, 'BLOCK_SYMMETRY')
smesh.SetName(MESH1.GetMesh(), 'MESH1')
smesh.SetName(BLOCK_2.GetMesh(), 'BLOCK')
smesh.SetName(CYLINDER_TO_BLOCK_2, 'CYLINDER_TO_BLOCK')
smesh.SetName(BLOCK_BOTTOM_2, 'BLOCK_BOTTOM')
smesh.SetName(CYLINDER_SYMMETRY_2, 'CYLINDER_SYMMETRY')
smesh.SetName(CYLINDER_SYMMETRY_1, 'CYLINDER_SYMMETRY')
smesh.SetName(CYLINDER_TO_BLOCK_1, 'CYLINDER_TO_BLOCK')
smesh.SetName(BLOCK_5, 'BLOCK')
smesh.SetName(CYLINDER_5, 'CYLINDER')
smesh.SetName(CYLINDER_4, 'CYLINDER')
smesh.SetName(BLOCK_4, 'BLOCK')
smesh.SetName(CYLINDER_SYMMETRY_3, 'CYLINDER_SYMMETRY')
smesh.SetName(BLOCK_BOTTOM_3, 'BLOCK_BOTTOM')
smesh.SetName(CYLINDER_TO_BLOCK_3, 'CYLINDER_TO_BLOCK')
smesh.SetName(BLOCK_3, 'BLOCK')
smesh.SetName(CYLINDER_3, 'CYLINDER')
smesh.SetName(BLOCK_SYMMETRY_3, 'BLOCK_SYMMETRY')
smesh.SetName(BLOCK_TO_CYLINDER_3, 'BLOCK_TO_CYLINDER')
smesh.SetName(BLOCK_BOTTOM_1, 'BLOCK_BOTTOM')
smesh.SetName(BLOCK_SYMMETRY_1, 'BLOCK_SYMMETRY')
smesh.SetName(BLOCK_TO_CYLINDER_1, 'BLOCK_TO_CYLINDER')


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(1)
