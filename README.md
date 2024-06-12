# Logging Heatmap

## Table of Contents
- [Project Description](#project-description)
- [How to Install and Run The Project](#how-to-install-and-run-the-project)
- [Credits](#credits)

## Project Description
### What does it do?
The Logging Heatmap keeps track of Illegal Logging activity in the Pu Ngaol area in Cambodia by accepting Data Inputs using a grid system. The input data points are added to a local array which can be saved to and loaded from a local file. The program then uses matplotlib to plot the heatmap using the data stored in the array.

### Why we used these technologies
Throughout this project we used matplotlib for the heatmap functionality and tkinter for the GUI class. We did this to improve accessbility, as these are widely known languages.

### Challenges and future features
From inital design to feedback from User Experience, we have a long list of intended future updates, some of which include:
- Ability to enter multiple co-ordinates at once
- Generating heatmaps based on datapoints in a given range of dates
- Ability to refresh the heatmap and use a clean model without re-executing the program
- Ability to save multiple heatmaps at once
- Cloud-save capabilities
- Implementation of various heatmap categories
    
## How to install and Run The Project
After cloning this repository, ensure all dependencies are installed.

### Dependencies
The only true dependency for this project, that being libraries that do not come packaged with python, is matplotlib. To install matplotlib run the following in the command line:
```pip install matplotlib```

### User Guide
After installing dependencies, run the __main__.py file. Afterwards the step-by-step guide is as follows:
1. Press "Load Data"
2. Choose data.txt
3. Press "Visualize Heatmap"
4. Plot desired Co-ordinate (e.g. A1) and incident description using the entry boxes
5. Press Submit
6. Repeat steps 4 and 5 for all datapoints
7. Press "Save Data" to commit changes to data.txt

## Credits
### Denis Komarovs
- Contributed the GUI code in almost its entirety, safe for a few bug fixes
- Aided with the design phase, commenting on Methodology and Software usefulness
- Designed the low-fi prototype

### Dom Lansdale-Brown
- Aided with the design phase
    - Use Case Diagram
    - Critical Success Factors
    - Empathy Map
    - UML Diagram

### Harry Irving
- Critical research for Problem Context in the following areas 
    - Platforms
    - Software
    - Stakeholders
    - Personas

### Putty Putland
- Critical research for Problem Context and Design Ideas
    - Deforestation, Mining, Poaching
    - Problem Identification
    - Inital concept

### Sunny Ledger
- Contributed the backend code including all funcitonality within the Heatmap class
- Prototype Documentation and Presentation
- Lead finisher

