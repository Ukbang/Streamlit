import streamlit as st
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.applications import VGG16
from tensorflow.keras.applications.vgg16 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
from googletrans import Translator
import koreanize_matplotlib
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

col1, col2, col3 = st.columns(3)

col1.header("Image Classifier with VGG16")
# 공백 조절
col2.markdown("<br><br>", unsafe_allow_html=True)

model = VGG16(include_top=True, weights='imagenet', input_shape=(224, 224, 3))
translator = Translator()

with st.sidebar:
    upload_img = st.file_uploader("Upload Your File...")

try:
    if upload_img:
        img = image.load_img(upload_img, target_size=(224, 224))
        col1.image(img, width=512)
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)

        predictions = model.predict(x)
        
        pred_label = decode_predictions(predictions, top=3)[0]
        label_df = pd.DataFrame(pred_label)
        del label_df[0]

        for i in range(len(label_df)):
            pred = label_df[1][i].replace("_", " ")
            trans_pred = translator.translate(pred, src="en", dest="ko")
            trans_pred = trans_pred.text
            label_df[1][i] = trans_pred+f"({pred})"

        col1.write(f'이 사진은 **{label_df[1][0]}** 입니다.')

        # 파이 차트 생성
        plt.figure(figsize=(18, 18))  # 차트의 크기 설정
        plt.title("레이블 당 확률", fontsize=48)
        plt.pie(label_df[2], labels=label_df[1], autopct='%1.1f%%', shadow=True, textprops={"fontsize":36})
        plt.legend(fontsize=30, bbox_to_anchor=(1.3,1.3))

        # Streamlit 앱에 차트 표시
        col2.pyplot(plt)
    else:
        pass
except:
    st.write("일시적인 오류입니다. 다시 업로드해주세요.")
