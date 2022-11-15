from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

class ViewTimeCounter(object):
    def setupUi(self, ViewTimeCounter):
        if not ViewTimeCounter.objectName():
            ViewTimeCounter.setObjectName(u"ViewTimeCounter")
        ViewTimeCounter.resize(500, 300)
        ViewTimeCounter.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label = QLabel(ViewTimeCounter)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 10, 251, 91))
        self.label.setPixmap(QPixmap(u"assets\Screenshot_1.jpg"))
        self.label.setScaledContents(True)
        self.counts_label = QLabel(ViewTimeCounter)
        self.counts_label.setObjectName(u"counts_label")
        self.counts_label.setGeometry(QRect(0, 120, 501, 61))
        self.counts_label.setStyleSheet(u"")
        self.counts_label.setAlignment(Qt.AlignCenter)
        self.counts_label.setStyleSheet(u"font-size:36pt")
        self.hs_label = QLabel(ViewTimeCounter)
        self.hs_label.setObjectName(u"hs_label")
        self.hs_label.setGeometry(QRect(100, 180, 300, 20))
        self.hs_label.setText("Dias___Horas___Minutos___Segundos")
        self.hs_label.setStyleSheet(u"font-size:10pt")
        self.hs_label.setAlignment(Qt.AlignCenter)
        

        self.retranslateUi(ViewTimeCounter)

        QMetaObject.connectSlotsByName(ViewTimeCounter)
    

    def retranslateUi(self, ViewTimeCounter):
        ViewTimeCounter.setWindowTitle(QCoreApplication.translate("ViewTimeCounter", u"Cuenta Regresiva Qatar 2022", None))
        self.counts_label.setText('#Time')
        self.counts_label.setText(QCoreApplication.translate("ViewTimeCounter", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:700;\">#Time</span></p></body></html>", None))
       
 

