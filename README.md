# CIFAR-10 Image Classification using Deep Learning

## Overview
This project focuses on improving image classification performance on the CIFAR-10 dataset using deep learning techniques and advanced training strategies.

The project started with a baseline CNN model that achieved moderate performance. After redesigning the architecture and applying optimization techniques such as data augmentation and learning rate annealing, the model achieved significantly higher accuracy and better generalization.

---

## Dataset
This project uses the CIFAR-10 dataset, which contains 60,000 RGB images classified into 10 categories:

- Airplane
- Automobile
- Bird
- Cat
- Deer
- Dog
- Frog
- Horse
- Ship
- Truck

Each image has a resolution of **32×32 pixels**.

---

## Baseline Results

| Metric | Accuracy |
|---|---|
| Train Accuracy | 73% |
| Test Accuracy | 70% |

The baseline model suffered from limited feature extraction capability and weaker generalization performance.

---

## Improvements Applied

### Advanced CNN Architecture
A deeper and more optimized convolutional neural network architecture was implemented to improve feature extraction and learning capacity.

### Data Augmentation
To improve generalization and reduce overfitting, multiple augmentation techniques were applied during training:
- Random Horizontal Flip
- Random Crop
- Rotation
- Normalization

These augmentations helped the model learn more robust visual patterns.

### Learning Rate Annealing
Learning rate scheduling was introduced to stabilize training and improve convergence.

Benefits:
- Faster early-stage learning
- Better convergence
- More stable optimization process

### Training Optimization
Additional optimization strategies were used to improve performance and training stability.

---

## Final Results

| Metric | Accuracy |
|---|---|
| Train Accuracy | 97% |
| Test Accuracy | 92% |

The optimized model achieved a major improvement over the baseline model while maintaining strong generalization on unseen data.

---

## Overfitting Analysis
The final model shows:
- **97% Training Accuracy**
- **92% Testing Accuracy**

The difference between training and testing accuracy is approximately **5%**, which is considered acceptable for the CIFAR-10 dataset.

This indicates:
- Strong feature learning
- Good generalization
- Slight but acceptable overfitting

---

## Conclusion
This project demonstrates how architectural improvements and advanced training strategies can significantly improve image classification performance.

By combining:
- Advanced CNN architecture
- Data augmentation
- Learning rate annealing

the model improved from **70% test accuracy** to **92% test accuracy** while maintaining strong generalization performance.
