import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications import VGG16
from tensorflow.keras.applications.vgg16 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
from googletrans import Translator


st.header("이미지 분류기 사용해보기")

st.write("이번엔 Tensorflow에서 VGG16을 가져와 사용해보도록 하겠습니다.")

model = VGG16(include_top=True, weights='imagenet', input_shape=(224, 224, 3))
translator = Translator()

upload_img = st.file_uploader("Upload Your File...")

st.button("Memory Clear")

upload_file_name = {}

@st.cache_resource
def file_cashing(file_name, pred_label):
    if file_cashing:
        upload_file_name = upload_file_name
    else:
        upload_file_name = {}

try:
    if upload_img:
        img = image.load_img(upload_img, target_size=(224, 224))
        st.image(img, width=512)
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)

        predictions = model.predict(x)
        
        pred_label = decode_predictions(predictions, top=3)[0]

        pred_label = pred_label.replace("_", " ")
        trans_label = translator.translate(pred_label, src="en", dest="ko")
        trans_label = trans_label.text

        st.write(f'이 사진은 **{trans_label} ({pred_label})** 입니다.')

        # 저장이 안됨.
        upload_file_name.update({upload_img.name:trans_label})
        st.write(upload_file_name)
        file_cashing = True
    else:
        pass
except:
    st.write("일시적인 오류입니다. 다시 업로드해주세요.")
