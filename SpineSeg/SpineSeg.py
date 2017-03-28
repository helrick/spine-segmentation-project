import os
import unittest
import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
import logging
import slicer.util
import SimpleITK as sitk
import sitkUtils
import numpy


#
# SpineSeg
#

class SpineSeg(ScriptedLoadableModule):
  """Uses ScriptedLoadableModule base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def __init__(self, parent):
    ScriptedLoadableModule.__init__(self, parent)
    self.parent.title = "SpineSeg" # TODO make this more human readable by adding spaces
    self.parent.categories = ["Examples"]
    self.parent.dependencies = []
    self.parent.contributors = ["John Doe (AnyWare Corp.)"] # replace with "Firstname Lastname (Organization)"
    self.parent.helpText = """
    This is an example of scripted loadable module bundled in an extension.
    It performs a simple thresholding on the input volume and optionally captures a screenshot.
    """
    self.parent.acknowledgementText = """
    This file was originally developed by Jean-Christophe Fillion-Robin, Kitware Inc.
    and Steve Pieper, Isomics, Inc. and was partially funded by NIH grant 3P41RR013218-12S1.
"""

#
# SpineSegWidget
#

class SpineSegWidget(ScriptedLoadableModuleWidget):
  """Uses ScriptedLoadableModuleWidget base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def setup(self):
    ScriptedLoadableModuleWidget.setup(self)

    # Instantiate and connect widgets ...

    #
    # Parameters Area
    #
    parametersCollapsibleButton = ctk.ctkCollapsibleButton()
    parametersCollapsibleButton.text = "Parameters"
    self.layout.addWidget(parametersCollapsibleButton)





    # Layout within the dummy collapsible button
    parametersFormLayout = qt.QFormLayout(parametersCollapsibleButton)

    #
    # target volume selector
    #
    self.inputSelector = slicer.qMRMLNodeComboBox()
    self.inputSelector.nodeTypes = ( ("vtkMRMLVolumeNode"), "" )
    self.inputSelector.selectNodeUponCreation = True
    self.inputSelector.addEnabled = False
    self.inputSelector.removeEnabled = False
    self.inputSelector.noneEnabled = False
    self.inputSelector.showHidden = False
    self.inputSelector.showChildNodeTypes = True
    self.inputSelector.setMRMLScene( slicer.mrmlScene )
    self.inputSelector.setToolTip( "Pick the input to the algorithm." )
    parametersFormLayout.addRow("Target Volume: ", self.inputSelector)

    self.fiducialSelector = slicer.qMRMLNodeComboBox()
    self.fiducialSelector.nodeTypes = ["vtkMRMLFiducialListNode"]
    self.fiducialSelector.selectNodeUponCreation = True
    self.fiducialSelector.addEnabled = True
    self.fiducialSelector.removeEnabled = True
    self.fiducialSelector.noneEnabled = True
    self.fiducialSelector.showHidden = False
    self.fiducialSelector.showChildNodeTypes = False
    self.fiducialSelector.setMRMLScene( slicer.mrmlScene )
    self.fiducialSelector.setToolTip( "Choose Fiducials for  Seeding" )
    parametersFormLayout.addRow("Choose Fiducials: ", self.fiducialSelector)

    #
    # threshold value
    #
    self.imageThresholdSliderWidget = ctk.ctkSliderWidget()
    self.imageThresholdSliderWidget.singleStep = 0.5
    self.imageThresholdSliderWidget.minimum = 1
    self.imageThresholdSliderWidget.maximum = 10
    self.imageThresholdSliderWidget.value = 0.5
    self.imageThresholdSliderWidget.setToolTip("Set threshold value for computing the output image. Voxels that have intensities lower than this value will set to zero.")
    parametersFormLayout.addRow("Image threshold", self.imageThresholdSliderWidget)

    #
    # Apply Button
    #
    self.applyButton = qt.QPushButton("Apply")
    self.applyButton.toolTip = "Run the algorithm."
    self.applyButton.enabled = False
    parametersFormLayout.addRow(self.applyButton)

    # connections
    self.applyButton.connect('clicked(bool)', self.onApplyButton)
    #self.imageThresholdSliderWidget.connect('change(bool)', self.onA)

    # Add vertical spacer
    self.layout.addStretch(1)

    # Refresh Apply button state
    self.onSelect()

  def cleanup(self):
    pass

  def onSelect(self):
    pass

  def onSliderChange(self):
    pass

  def onApplyButton(self):

    imageThreshold = self.imageThresholdSliderWidget.value
    test.runTest(self)

#
# SpineSegLogic
#

class SpineSegLogic(ScriptedLoadableModuleLogic):
  """
  Uses ScriptedLoadableModuleLogic base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def isValidInputOutputData(self, inputVolumeNode, outputVolumeNode):
    """Validates if the output is not the same as input
    """
    if not inputVolumeNode:
      logging.debug('isValidInputOutputData failed: no input volume node defined')
      return False
    if not outputVolumeNode:
      logging.debug('isValidInputOutputData failed: no output volume node defined')
      return False
    if inputVolumeNode.GetID()==outputVolumeNode.GetID():
      logging.debug('isValidInputOutputData failed: input and output volume is the same. Create a new volume for output to avoid this error.')
      return False
    return True

    # grab and convert to vtk image data
    qpixMap = qt.QPixmap().grabWidget(widget)
    qimage = qpixMap.toImage()
    imageData = vtk.vtkImageData()
    slicer.qMRMLUtils().qImageToVtkImageData(qimage,imageData)

    annotationLogic = slicer.modules.annotations.logic()
    annotationLogic.CreateSnapShot(name, description, type, 1, imageData)



  def run(self, imageThreshold):
    """
    Run the actual algorithm
    """



class SpineSegTest(ScriptedLoadableModuleTest):
  """
  Uses ScriptedLoadableModuleTest base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def loadAndSmoothImageData(self,thePath, func):
    slicer.util.loadVolume(thePath) #must be defined with forward slashes
    inImage = sitkUtils.PullFromSlicer('007') # currently hardcoded, but could be changed to be a parameter of the function
    #check out: https://itk.org/Wiki/ITK/Examples/Smoothing/SmoothingRecursiveGaussianImageFilter
    filter = func #Using a clustering technique
    outImage = filter.Execute(inImage)
    sitkUtils.PushToSlicer(outImage, 'outputImage')

  def loadAndSmooth(self,thePath):
    slicer.util.loadVolume(thePath) #must be defined with forward slashes
    inImage = sitkUtils.PullFromSlicer('007') # currently hardcoded, but could be changed to be a parameter of the function
    #check out: https://itk.org/Wiki/ITK/Examples/Smoothing/SmoothingRecursiveGaussianImageFilter
    filter = sitk.SmoothingRecursiveGaussianImageFilter() #Using a clustering technique
    outImage = filter.Execute(inImage)
    sitkUtils.PushToSlicer(outImage, 'outputImage')

  # Dispatches the calls to loadAndSmoothImageData() with different filters
  # These Filters can be found here: https://www.slicer.org/wiki/Documentation/Nightly/Modules/SimpleFilters
  def dispatchFilters(self, thePath):
    filters = { 'SmoothingRG': sitk.SmoothingRecursiveGaussianImageFilter(),
                'DiscreteG': sitk.DiscreteGaussianImageFilter(),
                'GradientRG': sitk.GradientRecursiveGaussianImageFilter()}
    for name, func in filters.iteritems():
      print func
      self.loadAndSmoothImageData(thePath, func)
    return 0

  def imagePopUpWindow(self,mssg):
    msg = qt.QMessageBox()
    msg.setText(mssg)
    import time

    msg.exec_()
    time.sleep(5)
    return


  #TODO: Fix this, it doesn't work :(
  def thresholdImageData(self,lower,upper):
    imageNode = sitkUtils.PullFromSlicer('007')
    #note: look at the ConnectedThresholdImageFilter if semi-automatic thresholding allowed
    filter =  sitk.BinaryThresholdImageFilter()
    filter.SetLowerThreshold(lower)
    filter.SetUpperThreshold(upper)
    filter.SetInsideValue = lower
    filter.SetOutsideValue = 0
    thresholdedImage = filter.Execute(imageNode,lower,upper,1,0)
    sitkUtils.PushToSlicer(thresholdedImage,'thresholdedImage')

  def getMaxIntensity(self):
    imageNode = slicer.util.getNode('outputImage')
    imageData = imageNode.GetImageData()
    shapeData = list(imageData.GetDimensions())
    shapeData.reverse()
    imageArray = vtk.util.numpy_support.vtk_to_numpy(imageData.GetPointData().GetScalars()).reshape(shapeData)
    return numpy.max(imageArray)

  def getMinIntensity(self):
    imageNode = slicer.util.getNode('outputImage')
    imageData = imageNode.GetImageData()
    shapeData = list(imageData.GetDimensions())
    shapeData.reverse()
    imageArray = vtk.util.numpy_support.vtk_to_numpy(imageData.GetPointData().GetScalars()).reshape(shapeData)
    return numpy.min(imageArray)


  def setUp(self):
    """ Do whatever is needed to reset the state - typically a scene clear will be enough.
    """
    slicer.mrmlScene.Clear(0)

  def runTest(self):
    """Run as few or as many tests as needed here.
    """
    self.setUp()
    imageThreshold = 5
    self.imagePopUpWindow("Starting Test 1")
    self.test_SpineSeg1()
    self.imagePopUpWindow("Starting Test 2")
    self.test_SpineSeg2()

  def test_SpineSeg1(self):
    # Perhaps an idea to work on is to try a few methods and compare the outputs of the segmentations?
    # Some sort of average of the methods that appear to work well could help us to refine our segmentation...
    #TODO: Fix this to work better with the thresholding/decide next steps
    #self.dispatchFilters('/Users/hannahgreer/Documents/SlicerData/007.CTDC.nrrd')
    self.loadAndSmooth('/Users/hannahgreer/Documents/SlicerData/007.CTDC.nrrd')
    #self.loadAndSmooth('C:/Users/O Elrick/Documents/School/SlicerData/007.CTDC.nrrd')
    max = self.getMaxIntensity()
    min = self.getMinIntensity()
    print 'The Maximum Intensity is: ' + str(max)
    print 'The Minimum Intensity is: ' + str(min)
    self.thresholdImageData(int(max/5),int(max))

  def test_SpineSeg2(self):
    # Perhaps an idea to work on is to try a few methods and compare the outputs of the segmentations?
    # Some sort of average of the methods that appear to work well could help us to refine our segmentation...
    #TODO: Fix this to work better with the thresholding/decide next steps
    self.dispatchFilters('/Users/hannahgreer/Documents/SlicerData/007.CTDC.nrrd')
    #self.loadAndSmooth('C:/Users/O Elrick/Documents/School/SlicerData/007.CTDC.nrrd')
    #self.loadAndSmooth('/Users/hannahgreer/Documents/SlicerData/010.CTDC.nrrd')
    max = self.getMaxIntensity()
    min = self.getMinIntensity()
    print 'The Maximum Intensity is: ' + str(max)
    print 'The Minimum Intensity is: ' + str(min)
    print ''
    self.thresholdImageData(int(max/5),int(max))