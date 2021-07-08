# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preferences_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(463, 450)
        icon = QIcon()
        iconThemeName = u"preferences-system"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u"", QSize(), QIcon.Normal, QIcon.Off)
        
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(True)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_General = QWidget()
        self.tab_General.setObjectName(u"tab_General")
        self.layoutGeneral = QVBoxLayout(self.tab_General)
        self.layoutGeneral.setObjectName(u"layoutGeneral")
        self.checkBox_newTab = QCheckBox(self.tab_General)
        self.checkBox_newTab.setObjectName(u"checkBox_newTab")

        self.layoutGeneral.addWidget(self.checkBox_newTab)

        self.checkBox_lineNumbers = QCheckBox(self.tab_General)
        self.checkBox_lineNumbers.setObjectName(u"checkBox_lineNumbers")

        self.layoutGeneral.addWidget(self.checkBox_lineNumbers)

        self.checkBox_showAllMessages = QCheckBox(self.tab_General)
        self.checkBox_showAllMessages.setObjectName(u"checkBox_showAllMessages")

        self.layoutGeneral.addWidget(self.checkBox_showAllMessages)

        self.label_showAllMessages = QLabel(self.tab_General)
        self.label_showAllMessages.setObjectName(u"label_showAllMessages")

        self.layoutGeneral.addWidget(self.label_showAllMessages)

        self.checkBox_showHiddenFiles = QCheckBox(self.tab_General)
        self.checkBox_showHiddenFiles.setObjectName(u"checkBox_showHiddenFiles")

        self.layoutGeneral.addWidget(self.checkBox_showHiddenFiles)

        self.useSpacesLayout = QHBoxLayout()
        self.useSpacesLayout.setObjectName(u"useSpacesLayout")
        self.useSpacesCheckBox = QCheckBox(self.tab_General)
        self.useSpacesCheckBox.setObjectName(u"useSpacesCheckBox")

        self.useSpacesLayout.addWidget(self.useSpacesCheckBox)

        self.useSpacesLabel = QLabel(self.tab_General)
        self.useSpacesLabel.setObjectName(u"useSpacesLabel")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.useSpacesLabel.sizePolicy().hasHeightForWidth())
        self.useSpacesLabel.setSizePolicy(sizePolicy)
        self.useSpacesLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.useSpacesLayout.addWidget(self.useSpacesLabel)

        self.useSpacesSpinBox = QSpinBox(self.tab_General)
        self.useSpacesSpinBox.setObjectName(u"useSpacesSpinBox")
        self.useSpacesSpinBox.setMinimum(1)
        self.useSpacesSpinBox.setMaximum(96)
        self.useSpacesSpinBox.setValue(4)

        self.useSpacesLayout.addWidget(self.useSpacesSpinBox)


        self.layoutGeneral.addLayout(self.useSpacesLayout)

        self.checkBox_autoIndent = QCheckBox(self.tab_General)
        self.checkBox_autoIndent.setObjectName(u"checkBox_autoIndent")

        self.layoutGeneral.addWidget(self.checkBox_autoIndent)

        self.themeWidget = QCheckBox(self.tab_General)
        self.themeWidget.setObjectName(u"themeWidget")

        self.layoutGeneral.addWidget(self.themeWidget)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.labelTextEditor = QLabel(self.tab_General)
        self.labelTextEditor.setObjectName(u"labelTextEditor")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelTextEditor)

        self.lineEditTextEditor = QLineEdit(self.tab_General)
        self.lineEditTextEditor.setObjectName(u"lineEditTextEditor")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEditTextEditor)

        self.labelDiffTool = QLabel(self.tab_General)
        self.labelDiffTool.setObjectName(u"labelDiffTool")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelDiffTool)

        self.lineEditDiffTool = QLineEdit(self.tab_General)
        self.lineEditDiffTool.setObjectName(u"lineEditDiffTool")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEditDiffTool)


        self.layoutGeneral.addLayout(self.formLayout)

        self.fontLayout = QHBoxLayout()
        self.fontLayout.setObjectName(u"fontLayout")
        self.labelFont = QLabel(self.tab_General)
        self.labelFont.setObjectName(u"labelFont")

        self.fontLayout.addWidget(self.labelFont)

        self.buttonFont = QPushButton(self.tab_General)
        self.buttonFont.setObjectName(u"buttonFont")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.buttonFont.sizePolicy().hasHeightForWidth())
        self.buttonFont.setSizePolicy(sizePolicy1)
        icon1 = QIcon()
        iconThemeName = u"preferences-desktop-font"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u"", QSize(), QIcon.Normal, QIcon.Off)
        
        self.buttonFont.setIcon(icon1)

        self.fontLayout.addWidget(self.buttonFont)


        self.layoutGeneral.addLayout(self.fontLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.layoutGeneral.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.tab_General, "")
        self.tab_Programs = QWidget()
        self.tab_Programs.setObjectName(u"tab_Programs")
        self.layoutPrograms = QGridLayout(self.tab_Programs)
        self.layoutPrograms.setObjectName(u"layoutPrograms")
        self.scrollArea = QScrollArea(self.tab_Programs)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidget = QWidget()
        self.scrollAreaWidget.setObjectName(u"scrollAreaWidget")
        self.scrollAreaWidget.setGeometry(QRect(0, 0, 421, 187))
        self.scrollAreaLayout = QGridLayout(self.scrollAreaWidget)
        self.scrollAreaLayout.setObjectName(u"scrollAreaLayout")
        self.buttonNewProg = QPushButton(self.scrollAreaWidget)
        self.buttonNewProg.setObjectName(u"buttonNewProg")
        sizePolicy1.setHeightForWidth(self.buttonNewProg.sizePolicy().hasHeightForWidth())
        self.buttonNewProg.setSizePolicy(sizePolicy1)
        icon2 = QIcon()
        iconThemeName = u"list-add"
        if QIcon.hasThemeIcon(iconThemeName):
            icon2 = QIcon.fromTheme(iconThemeName)
        else:
            icon2.addFile(u"", QSize(), QIcon.Normal, QIcon.Off)
        
        self.buttonNewProg.setIcon(icon2)

        self.scrollAreaLayout.addWidget(self.buttonNewProg, 2, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.scrollAreaLayout.addItem(self.verticalSpacer_2, 3, 0, 1, 1)

        self.progWidget = QWidget(self.scrollAreaWidget)
        self.progWidget.setObjectName(u"progWidget")

        self.scrollAreaLayout.addWidget(self.progWidget, 0, 0, 1, 1)

        self.extWidget = QWidget(self.scrollAreaWidget)
        self.extWidget.setObjectName(u"extWidget")

        self.scrollAreaLayout.addWidget(self.extWidget, 0, 1, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidget)

        self.layoutPrograms.addWidget(self.scrollArea, 9, 0, 1, 2)

        self.labelExtExample = QLabel(self.tab_Programs)
        self.labelExtExample.setObjectName(u"labelExtExample")

        self.layoutPrograms.addWidget(self.labelExtExample, 8, 1, 1, 1)

        self.labelProgExample = QLabel(self.tab_Programs)
        self.labelProgExample.setObjectName(u"labelProgExample")

        self.layoutPrograms.addWidget(self.labelProgExample, 8, 0, 1, 1)

        self.labelExt = QLabel(self.tab_Programs)
        self.labelExt.setObjectName(u"labelExt")
        self.labelExt.setStyleSheet(u"font-weight:bold;")

        self.layoutPrograms.addWidget(self.labelExt, 7, 1, 1, 1)

        self.labelProg = QLabel(self.tab_Programs)
        self.labelProg.setObjectName(u"labelProg")
        self.labelProg.setStyleSheet(u"font-weight:bold;")

        self.layoutPrograms.addWidget(self.labelProg, 7, 0, 1, 1)

        self.lineEdit = QLineEdit(self.tab_Programs)
        self.lineEdit.setObjectName(u"lineEdit")

        self.layoutPrograms.addWidget(self.lineEdit, 1, 0, 1, 2)

        self.label_3 = QLabel(self.tab_Programs)
        self.label_3.setObjectName(u"label_3")

        self.layoutPrograms.addWidget(self.label_3, 0, 0, 1, 2)

        self.line = QFrame(self.tab_Programs)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.layoutPrograms.addWidget(self.line, 2, 0, 1, 2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_AdtlExt = QLabel(self.tab_Programs)
        self.label_AdtlExt.setObjectName(u"label_AdtlExt")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_AdtlExt.sizePolicy().hasHeightForWidth())
        self.label_AdtlExt.setSizePolicy(sizePolicy2)
        self.label_AdtlExt.setStyleSheet(u"font: 75 11pt \"Sans Serif\"; font-weight: bold;")

        self.horizontalLayout_2.addWidget(self.label_AdtlExt)


        self.layoutPrograms.addLayout(self.horizontalLayout_2, 5, 0, 1, 2)

        self.tabWidget.addTab(self.tab_Programs, "")
        self.tab_Advanced = QWidget()
        self.tab_Advanced.setObjectName(u"tab_Advanced")
        self.verticalLayout_3 = QVBoxLayout(self.tab_Advanced)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.tab_Advanced)
        self.label.setObjectName(u"label")
        self.label.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label)

        self.checkBox_autoCompleteAddressBar = QCheckBox(self.tab_Advanced)
        self.checkBox_autoCompleteAddressBar.setObjectName(u"checkBox_autoCompleteAddressBar")

        self.verticalLayout_3.addWidget(self.checkBox_autoCompleteAddressBar)

        self.checkBox_teletypeConversion = QCheckBox(self.tab_Advanced)
        self.checkBox_teletypeConversion.setObjectName(u"checkBox_teletypeConversion")

        self.verticalLayout_3.addWidget(self.checkBox_teletypeConversion)

        self.checkBox_syntaxHighlighting = QCheckBox(self.tab_Advanced)
        self.checkBox_syntaxHighlighting.setObjectName(u"checkBox_syntaxHighlighting")

        self.verticalLayout_3.addWidget(self.checkBox_syntaxHighlighting)

        self.checkBox_parseLinks = QCheckBox(self.tab_Advanced)
        self.checkBox_parseLinks.setObjectName(u"checkBox_parseLinks")

        self.verticalLayout_3.addWidget(self.checkBox_parseLinks)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.labelLineLimit = QLabel(self.tab_Advanced)
        self.labelLineLimit.setObjectName(u"labelLineLimit")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.labelLineLimit)

        self.lineLimitHLayout = QHBoxLayout()
        self.lineLimitHLayout.setObjectName(u"lineLimitHLayout")
        self.lineLimitSpinBox = QSpinBox(self.tab_Advanced)
        self.lineLimitSpinBox.setObjectName(u"lineLimitSpinBox")
        self.lineLimitSpinBox.setMaximum(100000000)
        self.lineLimitSpinBox.setValue(10000)

        self.lineLimitHLayout.addWidget(self.lineLimitSpinBox)

        self.lineLimitHSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.lineLimitHLayout.addItem(self.lineLimitHSpacer)


        self.formLayout_2.setLayout(0, QFormLayout.FieldRole, self.lineLimitHLayout)


        self.verticalLayout_3.addLayout(self.formLayout_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.tabWidget.addTab(self.tab_Advanced, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok|QDialogButtonBox.RestoreDefaults)

        self.verticalLayout.addWidget(self.buttonBox)

#if QT_CONFIG(shortcut)
        self.label_showAllMessages.setBuddy(self.checkBox_showAllMessages)
        self.useSpacesLabel.setBuddy(self.useSpacesSpinBox)
        self.labelTextEditor.setBuddy(self.lineEditTextEditor)
        self.labelDiffTool.setBuddy(self.lineEditDiffTool)
        self.labelFont.setBuddy(self.buttonFont)
        self.label_3.setBuddy(self.lineEdit)
        self.labelLineLimit.setBuddy(self.lineLimitSpinBox)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.tabWidget, self.checkBox_newTab)
        QWidget.setTabOrder(self.checkBox_newTab, self.checkBox_lineNumbers)
        QWidget.setTabOrder(self.checkBox_lineNumbers, self.checkBox_showAllMessages)
        QWidget.setTabOrder(self.checkBox_showAllMessages, self.checkBox_showHiddenFiles)
        QWidget.setTabOrder(self.checkBox_showHiddenFiles, self.useSpacesCheckBox)
        QWidget.setTabOrder(self.useSpacesCheckBox, self.useSpacesSpinBox)
        QWidget.setTabOrder(self.useSpacesSpinBox, self.themeWidget)
        QWidget.setTabOrder(self.themeWidget, self.lineEditTextEditor)
        QWidget.setTabOrder(self.lineEditTextEditor, self.lineEditDiffTool)
        QWidget.setTabOrder(self.lineEditDiffTool, self.buttonFont)
        QWidget.setTabOrder(self.buttonFont, self.lineEdit)
        QWidget.setTabOrder(self.lineEdit, self.scrollArea)
        QWidget.setTabOrder(self.scrollArea, self.buttonNewProg)
        QWidget.setTabOrder(self.buttonNewProg, self.checkBox_autoCompleteAddressBar)
        QWidget.setTabOrder(self.checkBox_autoCompleteAddressBar, self.checkBox_teletypeConversion)
        QWidget.setTabOrder(self.checkBox_teletypeConversion, self.checkBox_syntaxHighlighting)
        QWidget.setTabOrder(self.checkBox_syntaxHighlighting, self.checkBox_parseLinks)
        QWidget.setTabOrder(self.checkBox_parseLinks, self.lineLimitSpinBox)
        QWidget.setTabOrder(self.lineLimitSpinBox, self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.rejected.connect(Dialog.reject)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Preferences", None))
#if QT_CONFIG(tooltip)
        self.checkBox_newTab.setToolTip(QCoreApplication.translate("Dialog", u"Open links in new tabs instead of the current tab", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_newTab.setText(QCoreApplication.translate("Dialog", u"Open links in new tabs", None))
        self.checkBox_lineNumbers.setText(QCoreApplication.translate("Dialog", u"Show line numbers", None))
        self.checkBox_showAllMessages.setText(QCoreApplication.translate("Dialog", u"Display success messages", None))
        self.label_showAllMessages.setText(QCoreApplication.translate("Dialog", u"     \u2013 Warnings and errors will always be displayed.", None))
#if QT_CONFIG(tooltip)
        self.checkBox_showHiddenFiles.setToolTip(QCoreApplication.translate("Dialog", u"Show hidden files (on Unix, files starting with a \".\") in file dialogs", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_showHiddenFiles.setText(QCoreApplication.translate("Dialog", u"Show hidden files", None))
#if QT_CONFIG(tooltip)
        self.useSpacesCheckBox.setToolTip(QCoreApplication.translate("Dialog", u"Insert spaces instead of a tab character when the Tab key is pressed", None))
#endif // QT_CONFIG(tooltip)
        self.useSpacesCheckBox.setText(QCoreApplication.translate("Dialog", u"Use spaces instead of tabs", None))
#if QT_CONFIG(tooltip)
        self.useSpacesLabel.setToolTip(QCoreApplication.translate("Dialog", u"The number of spaces equivalent to one tab stop", None))
#endif // QT_CONFIG(tooltip)
        self.useSpacesLabel.setText(QCoreApplication.translate("Dialog", u"Tab spacing", None))
#if QT_CONFIG(tooltip)
        self.checkBox_autoIndent.setToolTip(QCoreApplication.translate("Dialog", u"Automatically indent new lines the same as the line above", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_autoIndent.setText(QCoreApplication.translate("Dialog", u"Use auto indentation", None))
#if QT_CONFIG(tooltip)
        self.themeWidget.setToolTip(QCoreApplication.translate("Dialog", u"Use the dark UI theme. You must restart the application to see any changes for this setting.", None))
#endif // QT_CONFIG(tooltip)
        self.themeWidget.setText(QCoreApplication.translate("Dialog", u"Dark theme (restart to see changes)", None))
        self.labelTextEditor.setText(QCoreApplication.translate("Dialog", u"Text editor:", None))
        self.labelDiffTool.setText(QCoreApplication.translate("Dialog", u"Diff tool:", None))
        self.labelFont.setText(QCoreApplication.translate("Dialog", u"Document font: ", None))
        self.buttonFont.setText(QCoreApplication.translate("Dialog", u"Select Font", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_General), QCoreApplication.translate("Dialog", u"General", None))
#if QT_CONFIG(tooltip)
        self.buttonNewProg.setToolTip(QCoreApplication.translate("Dialog", u"Add another program.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonNewProg.setText(QCoreApplication.translate("Dialog", u"&New", None))
#if QT_CONFIG(tooltip)
        self.labelExtExample.setToolTip(QCoreApplication.translate("Dialog", u"Comma-separated list. Spaces are optional.", None))
#endif // QT_CONFIG(tooltip)
        self.labelExtExample.setText(QCoreApplication.translate("Dialog", u"    .exr, .tx, .tif, .tiff", None))
#if QT_CONFIG(tooltip)
        self.labelProgExample.setToolTip(QCoreApplication.translate("Dialog", u"Command and any additional options.", None))
#endif // QT_CONFIG(tooltip)
        self.labelProgExample.setText(QCoreApplication.translate("Dialog", u"    Example: RV", None))
#if QT_CONFIG(tooltip)
        self.labelExt.setToolTip(QCoreApplication.translate("Dialog", u"Comma-separated list. Spaces are optional.", None))
#endif // QT_CONFIG(tooltip)
        self.labelExt.setText(QCoreApplication.translate("Dialog", u"Extension(s):", None))
#if QT_CONFIG(tooltip)
        self.labelProg.setToolTip(QCoreApplication.translate("Dialog", u"Command and any additional options.", None))
#endif // QT_CONFIG(tooltip)
        self.labelProg.setText(QCoreApplication.translate("Dialog", u"Program:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Extensions that should open in app (ex: .usd, .txt, .xml):", None))
        self.label_AdtlExt.setText(QCoreApplication.translate("Dialog", u"File Associations:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Programs), QCoreApplication.translate("Dialog", u"Programs", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"The following options are primarily meant for debugging or as potential optimizations:", None))
        self.checkBox_autoCompleteAddressBar.setText(QCoreApplication.translate("Dialog", u"Auto complete paths in address bar", None))
#if QT_CONFIG(tooltip)
        self.checkBox_teletypeConversion.setToolTip(QCoreApplication.translate("Dialog", u"Display teletype character codes properly in browse mode. Disable for faster loading of larger files", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_teletypeConversion.setText(QCoreApplication.translate("Dialog", u"Display teletype colors", None))
#if QT_CONFIG(tooltip)
        self.checkBox_syntaxHighlighting.setToolTip(QCoreApplication.translate("Dialog", u"Enable syntax highlighting. Disable for faster loading of larger files", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_syntaxHighlighting.setText(QCoreApplication.translate("Dialog", u"Enable syntax highlighting", None))
#if QT_CONFIG(tooltip)
        self.checkBox_parseLinks.setToolTip(QCoreApplication.translate("Dialog", u"Parse files for links to other files. Disable for faster loading of larger files", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_parseLinks.setText(QCoreApplication.translate("Dialog", u"Parse links", None))
#if QT_CONFIG(tooltip)
        self.labelLineLimit.setToolTip(QCoreApplication.translate("Dialog", u"Number of lines to display before truncating the file. Extremely large files can lead to application lag. If a file is truncated, it will not be editable.", None))
#endif // QT_CONFIG(tooltip)
        self.labelLineLimit.setText(QCoreApplication.translate("Dialog", u"Line Limit:", None))
#if QT_CONFIG(tooltip)
        self.lineLimitSpinBox.setToolTip(QCoreApplication.translate("Dialog", u"Number of lines to display before truncating the file. Extremely large files can lead to application lag. If a file is truncated, it will not be editable.", None))
#endif // QT_CONFIG(tooltip)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Advanced), QCoreApplication.translate("Dialog", u"Advanced", None))
    # retranslateUi

