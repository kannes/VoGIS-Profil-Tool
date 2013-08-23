# -*- coding: utf-8 -*-

from os.path import basename
from PyQt4.QtCore import QVariant
from PyQt4.QtGui import QMessageBox
from qgis.core import QgsMessageLog
from qgis.core import QGis
from qgis.core import QgsVectorFileWriter
from qgis.core import QgsField
from qgis.core import QgsPoint
#from qgis.core import QgsGeometry
#from qgis.core import QgsFeature
from u import Util
from ..bo.settings import enumModeLine


class ExportShape:

    def __init__(self, iface, hekto, attribs, delimiter, decimalDelimiter, fileName, settings, profiles):
        self.iface = iface
        self.hekto = hekto
        self.attribs = attribs
        self.delimiter = delimiter
        self.decimalDelimiter = decimalDelimiter
        self.fileName = fileName
        self.settings = settings
        self.profiles = profiles

    def exportPoint(self):

        if self.__deleteShape(self.fileName) is False:
            return

        flds = {}
        #standardfeler
        flds[0] = QgsField('Profillaenge', QVariant.Double)
        flds[1] = QgsField('Segmentlaenge', QVariant.Double)
        flds[2] = QgsField('Rechtswert', QVariant.Double)
        flds[3] = QgsField('Hochwert', QVariant.Double)

        fldCnt = len(flds)

        #raster
        for r in self.settings.mapData.rasters.rasters():
            if r.selected is True:
                flds[fldCnt] = QgsField(r.name, QVariant.Double)
                fldCnt += 1

        #Punkttypen
        pntAttribs = ['ProfilNr', 'SegNr', 'PktNr']
        for pntAttr in pntAttribs:
            flds[fldCnt] = QgsField(pntAttr, QVariant.Int)
            fldCnt += 1

        #PktKlasse
        flds[fldCnt] = QgsField('PktKlasse', QVariant.String)
        fldCnt += 1

        if self.hekto is True:
            flds[fldCnt] = QgsField('Hekto', QVariant.String)
            fldCnt += 1

        if self.attribs is True:
            QgsMessageLog.logMessage('EXPORT POINT attribs TRUE', 'VoGis')
            if self.settings.modeLine == enumModeLine.line:
                provider = self.settings.mapData.selectedLineLyr.line.dataProvider()
                for(idx, fld) in provider.fields().iteritems():
                    flds[fldCnt] = fld
                    fldCnt += 1
        else:
            QgsMessageLog.logMessage('attribs FALSE', 'VoGis')

        QgsMessageLog.logMessage('flds: {0}'.format(flds), 'VoGis')

        shpWriter = QgsVectorFileWriter(self.fileName,
                                        "CP1250",
                                        flds,
                                        QGis.WKBPoint,
                                        self.settings.mapData.selectedLineLyr.line.crs()
                                        )
        if shpWriter.hasError() != QgsVectorFileWriter.NoError:
            QMessageBox.warning(self.iface.mainWindow(),
                                "VoGIS-Profiltool",
                                'Konnte Shapefile nicht erstellen: {0}'.format(self.fileName)
                                )
            return

        ut = Util(self.iface)
        segOld = None

        for p in self.profiles:
            for s in p.segments:
                if segOld is not None:
                    v = segOld.vertices[len(segOld.vertices) - 1]
                    feat = ut.createQgPointFeature(v)
                    feat = self.__addValues(feat, v, s.id)
                    shpWriter.addFeature(feat)
                for v in s.vertices:
                    feat = ut.createQgPointFeature(v)
                    feat = self.__addValues(feat, v, None)
                    shpWriter.addFeature(feat)
                segOld = s
            segOld = None

        del shpWriter
        self.__loadShp(self.fileName)

    def __addValues(self, feat, v, sId):
        feat.addAttribute(0, v.distanceProfile)
        if sId is None:
            feat.addAttribute(1, v.distanceSegment)
        else:
            feat.addAttribute(1, 0)
        feat.addAttribute(2, v.x)
        feat.addAttribute(3, v.y)
        fldCnt = 4
        if len(v.zvals) > 0:
            for z in v.zvals:
                zVal = -9999
                if z is not None:
                    zVal = z
                feat.addAttribute(fldCnt, zVal)
                fldCnt += 1
        feat.addAttribute(fldCnt, v.profileId)
        fldCnt += 1
        if sId is None:
            feat.addAttribute(fldCnt, v.segmentId)
        else:
            feat.addAttribute(fldCnt, sId)
        fldCnt += 1
        feat.addAttribute(fldCnt, v.vertexId)
        fldCnt += 1
        feat.addAttribute(fldCnt, v.getType())
        fldCnt += 1
        if self.hekto is True:
            feat.addAttribute(fldCnt, v.getHekto(self.decimalDelimiter))
            fldCnt += 1
        if self.attribs is True:
            QgsMessageLog.logMessage('modeLine:{0}'.format(self.settings.modeLine), 'VoGis')
            if self.settings.modeLine == enumModeLine.line:
                for a in v.attributes:
                    feat.addAttribute(fldCnt, a)
                    fldCnt += 1
        return feat

    def exportLine(self):

        if self.__deleteShape(self.fileName) is False:
            return

        flds = {}
        flds[0] = QgsField('Profillaenge', QVariant.Double)
        fldCnt = len(flds)

        if self.attribs is True:
            if self.settings.modeLine == enumModeLine.line:
                provider = self.settings.mapData.selectedLineLyr.line.dataProvider()
                for(idx, fld) in provider.fields().iteritems():
                    flds[fldCnt] = fld
                    fldCnt += 1

        shpWriter = QgsVectorFileWriter(self.fileName,
                                        "CP1250",
                                        flds,
                                        QGis.WKBLineString,
                                        self.settings.mapData.selectedLineLyr.line.crs()
                                        )
        if shpWriter.hasError() != QgsVectorFileWriter.NoError:
            QMessageBox.warning(self.iface.mainWindow(),
                                "VoGIS-Profiltool",
                                'Konnte Shapefile nicht erstellen: {0}'.format(self.fileName)
                                )
            return

        ut = Util(self.iface)

        for p in self.profiles:
            vertices = []
            lastV = None
            profileLength = 0
            for s in p.segments:
                for v in s.vertices:
                    lastV = v
                    profileLength = v.distanceProfile
                    vertices.append(QgsPoint(v.x, v.y))
            feat = ut.createQgLineFeature(vertices)
            feat.addAttribute(0, profileLength)
            fldCnt = 1
            if self.attribs is True:
                if self.settings.modeLine == enumModeLine.line:
                    lastV
                    for a in lastV.attributes:
                        feat.addAttribute(fldCnt, a)
                        fldCnt += 1
            shpWriter.addFeature(feat)

        del shpWriter
        self.__loadShp(self.fileName)

    def __loadShp(self, fileName):
        reply = QMessageBox.question(self.iface.mainWindow(),
                                     "VoGIS-Profiltool",
                                     'Shapefile gespeichert.\r\n\r\n\r\nLaden?',
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.Yes
                                     )
        if reply == QMessageBox.Yes:
            self.iface.addVectorLayer(fileName,
                                      basename(str(fileName)),
                                      'ogr'
                                      )

    def __deleteShape(self, fileName):

        if QgsVectorFileWriter.deleteShapeFile(fileName) is False:
            QMessageBox.warning(self.iface.mainWindow(),
                                "VoGIS-Profiltool",
                                'Konnte vorhandenes Shapefile nicht löschen: {0}'.format(fileName)
                                )
            return False
        else:
            return True