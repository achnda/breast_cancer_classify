# Breast Cancer Classification Project

## Overview
This project implements a deep learning neural network for classifying breast cancer tumors using the University of Wisconsin Breast Cancer dataset. The model aims to predict whether a tumor is malignant or benign based on various features extracted from cell nuclei.

## Dataset
- **Source**: University of Wisconsin Breast Cancer Dataset (from Scikit-learn)
- **Features**: 30 numerical features computed from digitized images of cell nuclei
- **Target**: Binary classification (Malignant or Benign)

## Project Structure
- `breastcancerclassify.ipynb`: Main Jupyter notebook containing model training
- `ModelLoadal.ipynb`: Model loading and evaluation script
- `model.h5`: Saved trained neural network model

## Model Architecture
The neural network uses the following architecture:
- Input layer: 30 features
- Hidden layers:
  - 1st layer: 25 neurons with LeakyReLU activation
  - 2nd layer: 12 neurons with LeakyReLU activation
  - 3rd layer: 6 neurons with LeakyReLU activation
  - 4th layer: 3 neurons with LeakyReLU activation
- Output layer: 1 neuron with sigmoid activation

## Training Details
- **Optimizer**: RMSprop
- **Loss Function**: Binary Crossentropy
- **Metrics**: Accuracy, Precision, Recall
- **Epochs**: 100
- **Batch Size**: 32

## Performance Metrics
- **Test Accuracy**: 97.37%
- **Test Precision**: 98.57%
- **Test Recall**: 97.18%
- **Test F1 Score**: 97.87%

## Dependencies
- TensorFlow
- Keras
- Scikit-learn
- NumPy

## How to Use
1. Clone the repository
2. Install required dependencies
3. Run the Jupyter notebook to train or load the model
4. Use the saved `model.h5` for predictions

## Key Observations
- The model demonstrates high performance in distinguishing between malignant and benign tumors
- High precision and recall indicate robust classification capabilities
- Dropout layers used to prevent overfitting

## Potential Improvements
- Experiment with different network architectures
- Try data augmentation techniques
- Implement cross-validation

## License
[Specify your license here]

## Acknowledgments
- University of Wisconsin for the original dataset
- Scikit-learn for providing the dataset
