import streamlit as st
import torch
import torchvision.transforms as transforms
from PIL import Image
from model import AdvancedCNN

# Load model
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = AdvancedCNN().to(device)
model.load_state_dict(torch.load("model_1weights.pth", map_location=device))
model.eval()

class_names = ['plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

#Image preprocessing
transform = transforms.Compose([
    transforms.Resize((32, 32)),
    transforms.ToTensor(),
    transforms.Normalize((0.5,0.5,0.5),(0.5,0.5,0.5))
])


#Streamlit UI
st.title("Image Classification App")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # preprocess
    img = transform(image).unsqueeze(0).to(device)

    # inference
    with torch.no_grad():
        output = model(img)
        _, predicted = torch.max(output, 1)

    predicted_class = class_names[predicted.item()]

    st.write(f"### Prediction: {predicted_class}")