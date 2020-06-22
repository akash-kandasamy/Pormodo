import sys
import time

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtWidgets import QApplication as App
from PyQt5.QtWidgets import QDial as Dial
from PyQt5.QtWidgets import QHBoxLayout as HoriArr
from PyQt5.QtWidgets import QLabel as Label
from PyQt5.QtWidgets import QPushButton as Pbutton
from PyQt5.QtWidgets import QSlider as Slider
from PyQt5.QtWidgets import QVBoxLayout as VertArr
from PyQt5.QtWidgets import QWidget as Widg

Primaryfont = QtGui.QFont('Jetbrains Mono',12,QtGui.QFont.Bold)
Secondaryfont = QtGui.QFont('Jetbrains Mono',10,QtGui.QFont.Medium)
SliderFont = QtGui.QFont('Jetbrains Mono',90,QtGui.QFont.Bold)
