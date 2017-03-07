# Spine Segmentation in 3D Slicer
## Final Project for CISC 472, Medical Informatics
### By Hannah Greer and Hillary Elrick

From Wikipedia:
"Segmentation is the process of partitioning an image into different segments. More precisely, image segmentation is the process of assigning a label to every pixel in an image such that pixels with the same label share certain characteristics. The goal of segmentation is to simplify and/or change the representation of an image into something that is more meaningful and easier to analyze. In medical imaging, these segments often correspond to different tissue classes, organs, pathologies, or other biologically relevant structures. Medical image segmentation is made difficult by low contrast, noise, and other imaging ambiguities."

Medical Segmentation can be done manually by someone trained to recognized the features of interest, automatically by an algorithm, or semi-automatically. Methods for automatic segmentation include:
- Region Based Methods
  - Thresholding
  - Region Growing
- Classification Methods
  - k-Nearest Neighbours
  - Maximum Likelihood 
- Clustering Mehods
  - k-Means
  - Fuzzy C-Mean
  - Expectation Maximization
- Hybrid Methods

#####Known Difficulties for Spinal Segmentation
- Variation in human anatomy within the spine; very computationally complex
- Variety in MRI contrasts in the structure and against the cerebrospinal fluid

#####Anatomy
The Spine is very anatomically complex. There are 5 major regions of the spinal column: 
- Cervical; the 7 vertebrae in the neck
- Thoracic; the 12 vertebrae of the chest region
- Lumbar; the 5 vertebrae of the lower back, which are larger and stronger than the Thoracic
- Sacral; consisting only of the sacrum, the fusion of 5 smaller vertebrae into one bone during adolesence
- Coccygeal; consisting of only 1 bone, the cocctheyx, which, are 4 vertebrae fused together during adolesence, similar to the sacrum

The small spaces between the vertebrae are called intravertbral canals.

#####References and Further Reading:
  - http://airccj.org/CSCP/vol6/csit65109.pdf 
    - fuzzy C means example
  - https://books.google.ca/books?id=qGSYBgAAQBAJ&pg=PA117&lpg=PA117&dq=why+is+spine+segmentation+hard&source=bl&ots=fkcBgiNPH4&sig=yi_Hj9a7tMjfo9_ka0_JunFCmpk&hl=en&sa=X&ved=0ahUKEwjtpp2xzcPSAhUj8IMKHfheCZ0Q6AEISTAH#v=onepage&q=why%20is%20spine%20segmentation%20hard&f=false 
    - adaption of the max-flow approach
  - http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0139323
  


