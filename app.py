import streamlit as st
import pandas as pd
import datetime
import os

# Ensure save folder exists
SAVE_DIR = 'survey_responses'
os.makedirs(SAVE_DIR, exist_ok=True)
IMAGE_SAVE_DIR = os.path.join(SAVE_DIR, 'images')
os.makedirs(IMAGE_SAVE_DIR, exist_ok=True)


# Streamlit Page Config
st.set_page_config(page_title="Ksheersagar 2.0 Dairy Survey", page_icon="🐄", layout="centered")

# --- Language Translations ---
dict_translations = {
    "English": {
        "Farmer Profile": "Farmer Profile",
        "Types": "Types",
        "BMC/MCC Name": "BMC/MCC Name",
        "BMC/MCC Code": "BMC/MCC Code",
        "District": "District",
        "Taluka": "Taluka", # Keep in translations for questions, even if not in df_locations
        "Village": "Village",
        "BCF Name": "BCF Name",
        "Energy sources": "Energy sources",
        "Number of villages covered by the BMC": "Number of villages covered by the BMC",
        "Name of village": "Name of village",
        "No. of direct pouring farmers": "No. of direct pouring farmers",
        "No. of Route vehicles pouring milk at BMC": "No. of Route vehicles pouring milk at BMC",
        "No. of farmers under each Route vehicle": "No. of farmers under each Route vehicle",
        "Farmer Name": "Farmer Name",
        "Farmer Code / Pourer Id": "Farmer Code / Pourer Id",
        "Gender": "Gender",
        "Services provided by BMC to farmer": "Services provided by BMC to farmer",
        "Other Services (if selected above)": "Other Services (if selected above)",
        "Number of Cows": "Number of Cows",
        "No. of Cattle in Milk": "No. of Cattle in Milk",
        "No. of Calves/Heifers": "No. of Calves/Heifers",
        "No. of Desi cows": "No. of Desi cows",
        "Milk Production in litres per day-Desi cows": "Milk Production in litres per day-Desi cows",
        "No. of Cross breed cows": "No. of Cross breed cows",
        "Type of cross breed(HF/Jersey)": "Type of cross breed (HF/Jersey)",
        "Milk Production in litres per day-Cross breed(HF/Jersey)": "Milk Production in litres per day-Cross breed (HF/Jersey)",
        "No. of Buffalo": "No. of Buffalo",
        "Milk Production in liters per day-buffalo": "Milk Production in liters per day-buffalo",
        "Specific Questions": "Specific Questions",
        "Green Fodder": "Green Fodder",
        "If yes, type of Green Fodder": "If yes, type of Green Fodder",
        "Quantity of Green Fodder per day (in Kgs)": "Quantity of Green Fodder per day (in Kgs)",
        "Dry Fodder": "Dry Fodder",
        "If yes, type of Dry Fodder": "If yes, type of Dry Fodder",
        "Quantity of Dry Fodder per day (in Kgs)": "Quantity of Dry Fodder per day (in Kgs)",
        "Concentrate Feed": "Concentrate Feed",
        "If yes, which brand": "If yes, which brand",
        "Quantity of Concentrate Feed per day (in Kgs)": "Quantity of Concentrate Feed per day (in Kgs)",
        "Mineral Mixture": "Mineral Mixture",
        "If yes, which brand_mineral": "If yes, which brand",
        "Quantity of Mineral Mixture per day (in gms)": "Quantity of Mineral Mixture per day (in gms)",
        "Silage": "Silage",
        "If yes, what is the source and price": "If yes, what is the source and price",
        "Quantity of Silage per day (in Kgs)": "Quantity of Silage per day (in Kgs)",
        "Type of Farm": "Type of Farm",
        "Other Type of Farm (if selected above)": "Other Type of Farm (if selected above)",
        "Source of Water": "Source of Water",
        "Preventive health care measures-Annual cycle": "Preventive health care measures-Annual cycle",
        "If Other Preventive health care measures, specify": "If Other Preventive health care measures, specify",
        "Have they previously used Ethno veterinary resources": "Have they previously used Ethno veterinary resources",
        "If yes, what disease/text": "If yes, what disease/text",
        "Women entrepreneur providing banking services": "Women entrepreneur providing banking services",
        "If Yes, Banking Services Provided by Women Entrepreneur": "If Yes, Banking Services Provided by Women Entrepreneur",
        "If Other Banking Services, specify": "If Other Banking Services, specify",
        "Extension services": "Extension services",
        "If Other Extension Services, specify": "If Other Extension Services, specify",
        "Survey Details": "Survey Details",
        "Name of Surveyor": "Name of Surveyor",
        "Photo / Timestamp": "Photo / Timestamp",
        "Date of Visit": "Date of Visit",
        "Submit Survey": "Submit Survey",
        "Survey Saved!": "Survey Saved!",
        "Error saving survey": "Error saving survey",
        "Click to Review Baseline Responses": "Click to Review Baseline Responses",
        "Baseline Survey Questions": "Baseline Survey Questions",
        "Admin Real-Time Access": "Admin Real-Time Access",
        "Enter your Admin Email to unlock extra features:": "Enter your Admin Email to unlock extra features:",
        "Admin access granted! Real-time view enabled.": "Admin access granted! Real-time view enabled.",
        "Not an authorized admin.": "Not an authorized admin.",
        "View and Download Uploaded Images": "View and Download Uploaded Images",
        "No images found.": "No images found.",
        "Download": "Download",
        "View Past Submissions": "View Past Submissions",
        "No submissions found yet.": "No submissions found yet.",
        "Download All Responses": "Download All Responses",
    },
    "Hindi": {
        "Farmer Profile": "किसान प्रोफाइल",
        "Types": "प्रकार",
        "BMC/MCC Name": "बीएमसी/एमसीसी नाम",
        "BMC/MCC Code": "बीएमसी/एमसीसी कोड",
        "District": "जिला",
        "Taluka": "तालुका",
        "Village": "गांव",
        "BCF Name": "बीसीएफ का नाम",
        "Energy sources": "ऊर्जा स्रोत",
        "Number of villages covered by the BMC": "बीएमसी द्वारा कवर किए गए गांवों की संख्या",
        "Name of village": "गांव का नाम",
        "No. of direct pouring farmers": "प्रत्यक्ष दूध देने वाले किसानों की संख्या",
        "No. of Route vehicles pouring milk at BMC": "बीएमसी में दूध डालने वाले रूट वाहन",
        "No. of farmers under each Route vehicle": "प्रत्येक रूट वाहन के तहत किसानों की संख्या",
        "Farmer Name": "किसान का नाम",
        "Farmer Code / Pourer Id": "किसान कोड / दूध देने वाला आईडी",
        "Gender": "लिंग",
        "Services provided by BMC to farmer": "किसान को बीएमसी द्वारा दी जाने वाली सेवाएं",
        "Other Services (if selected above)": "अन्य सेवाएं (यदि ऊपर चुना गया हो)",
        "Number of Cows": "गायों की संख्या",
        "No. of Cattle in Milk": "दूध देणारे जनावरे",
        "No. of Calves/Heifers": "बछड़े/बछड़ियां",
        "No. of Desi cows": "देसी गायों की संख्या",
        "Milk Production in litres per day-Desi cows": "देसी गायों द्वारा प्रतिदिन दूध उत्पादन (लीटर में)",
        "No. of Cross breed cows": "क्रॉसब्रीड गायों की संख्या",
        "Type of cross breed(HF/Jersey)": "क्रॉसब्रीड प्रकार (HF/जर्सी)",
        "Milk Production in litres per day-Cross breed(HF/Jersey)": "क्रॉसब्रीड गायों द्वारा प्रतिदिन दूध उत्पादन (HF/जर्सी)",
        "No. of Buffalo": "भैंसों की संख्या",
        "Milk Production in liters per day-buffalo": "भैंसों द्वारा प्रतिदिन दूध उत्पादन (लीटर में)",
        "Specific Questions": "विशिष्ट प्रश्न",
        "Green Fodder": "हरा चारा",
        "If yes, type of Green Fodder": "यदि हाँ, तो हरे चारे का प्रकार",
        "Quantity of Green Fodder per day (in Kgs)": "प्रतिदिन हरे चारे की मात्रा (किलो में)",
        "Dry Fodder": "सूखा चारा",
        "If yes, type of Dry Fodder": "यदि हाँ, तो सूखे चारे का प्रकार",
        "Quantity of Dry Fodder per day (in Kgs)": "प्रतिदिन सूखे चारे की मात्रा (किलो में)",
        "Concentrate Feed": "सांद्रित चारा",
        "If yes, which brand": "यदि हाँ, तो कौन सा ब्रांड",
        "Quantity of Concentrate Feed per day (in Kgs)": "प्रतिदिन सांद्रित चारे की मात्रा (किलो में)",
        "Mineral Mixture": "खनिज मिश्रण",
        "If yes, which brand_mineral": "यदि हाँ, तो कौन सा ब्रांड",
        "Quantity of Mineral Mixture per day (in gms)": "प्रतिदिन खनिज मिश्रण की मात्रा (ग्राम में)",
        "Silage": "साइलेज",
        "If yes, what is the source and price": "यदि हाँ, तो स्रोत और कीमत क्या है",
        "Quantity of Silage per day (in Kgs)": "प्रतिदिन साइलेज की मात्रा (किलो में)",
        "Type of Farm": "खेत का प्रकार",
        "Other Type of Farm (if selected above)": "अन्य खेत का प्रकार (यदि ऊपर चुना गया हो)",
        "Source of Water": "पानी का स्रोत",
        "Preventive health care measures-Annual cycle": "रोकथाम स्वास्थ्य देखभाल उपाय - वार्षिक चक्र",
        "If Other Preventive health care measures, specify": "यदि अन्य निवारक स्वास्थ्य देखभाल उपाय, तो निर्दिष्ट करें",
        "Have they previously used Ethno veterinary resources": "क्या उन्होंने पहले एथनो पशु चिकित्सा संसाधनों का उपयोग किया है",
        "If yes, what disease/text": "यदि हाँ, तो कौन सी बीमारी/पाठ",
        "Women entrepreneur providing banking services": "महिला उद्यमी जो बैंकिंग सेवाएं प्रदान करती हैं",
        "If Yes, Banking Services Provided by Women Entrepreneur": "यदि हाँ, तो महिला उद्यमी द्वारा प्रदान की जाने वाली बैंकिंग सेवाएं",
        "If Other Banking Services, specify": "यदि अन्य बैंकिंग सेवाएं, तो निर्दिष्ट करें",
        "Extension services": "विस्तार सेवाएं",
        "If Other Extension Services, specify": "यदि अन्य विस्तार सेवाएं, तो निर्दिष्ट करें",
        "Survey Details": "सर्वेक्षण विवरण",
        "Name of Surveyor": "सर्वेक्षक का नाम",
        "Photo / Timestamp": "फोटो / टाइमस्टैम्प",
        "Date of Visit": "यात्रा की तारीख",
        "Submit Survey": "सर्वेक्षण जमा करें",
        "Survey Saved!": "सर्वेक्षण सहेजा गया!",
        "Error saving survey": "सर्वेक्षण सहेजने में त्रुटि",
        "Click to Review Baseline Responses": "बेसलाइन प्रतिक्रियाओं की समीक्षा करने के लिए क्लिक करें",
        "Baseline Survey Questions": "बेसलाइन सर्वेक्षण प्रश्न",
        "Admin Real-Time Access": "व्यवस्थापक वास्तविक समय पहुंच",
        "Enter your Admin Email to unlock extra features:": "अतिरिक्त सुविधाओं को अनलॉक करने के लिए अपना व्यवस्थापक ईमेल दर्ज करें:",
        "Admin access granted! Real-time view enabled.": "व्यवस्थापक पहुंच प्रदान की गई! वास्तविक समय दृश्य सक्षम किया गया।",
        "Not an authorized admin.": "अधिकृत व्यवस्थापक नहीं।",
        "View and Download Uploaded Images": "अपलोड की गई छवियां देखें और डाउनलोड करें",
        "No images found.": "कोई छवि नहीं मिली।",
        "Download": "डाउनलोड करें",
        "View Past Submissions": "पिछले सबमिशन देखें",
        "No submissions found yet.": "अभी तक कोई सबमिशन नहीं मिला।",
        "Download All Responses": "सभी प्रतिक्रियाएं डाउनलोड करें",
    },
    "Marathi": {
        "Farmer Profile": "शेतकरी प्रोफाइल",
        "Types": "प्रकार",
        "BMC/MCC Name": "बीएमसी/एमसीसी नाव",
        "BMC/MCC Code": "बीएमसी/एमसीसी कोड",
        "District": "जिल्हा",
        "Taluka": "तालुका",
        "Village": "गाव",
        "BCF Name": "बीसीएफचे नाव",
        "Energy sources": "ऊर्जेचे स्रोत",
        "Number of villages covered by the BMC": "बीएमसीने व्यापलेली गावांची संख्या",
        "Name of village": "गावाचे नाव",
        "No. of direct pouring farmers": "थेट दूध देणाऱ्या शेतकऱ्यांची संख्या",
        "No. of Route vehicles pouring milk at BMC": "बीएमसीमध्ये दूध आणणाऱ्या मार्ग वाहनांची संख्या",
        "No. of farmers under each Route vehicle": "प्रत्येक मार्ग वाहनाखालील शेतकऱ्यांची संख्या",
        "Farmer Name": "शेतकऱ्याचे नाव",
        "Farmer Code / Pourer Id": "शेतकरी कोड / दूध देणारा आयडी",
        "Gender": "लिंग",
        "Services provided by BMC to farmer": "शेतकऱ्याला बीएमसीने दिलेल्या सेवा",
        "Other Services (if selected above)": "इतर सेवा (वर निवडल्यास)",
        "Number of Cows": "गायांची संख्या",
        "No. of Cattle in Milk": "दूध देणाऱ्या जनावरांची संख्या",
        "No. of Calves/Heifers": "कालवडे/कालवडी",
        "No. of Desi cows": "देशी गायांची संख्या",
        "Milk Production in litres per day-Desi cows": "देशी गायींकडून दररोज दूध उत्पादन (लिटर मध्ये)",
        "No. of Cross breed cows": "क्रॉसब्रीड गायांची संख्या",
        "Type of cross breed(HF/Jersey)": "क्रॉसब्रीड प्रकार (HF/जर्सी)",
        "Milk Production in litres per day-Cross breed(HF/Jersey)": "क्रॉसब्रीड गायींकडून दररोज दूध उत्पादन (HF/जर्सी)",
        "No. of Buffalo": "म्हशींची संख्या",
        "Milk Production in liters per day-buffalo": "म्हशींकडून दररोज दूध उत्पादन (लिटर मध्ये)",
        "Specific Questions": "विशिष्ट प्रश्न",
        "Green Fodder": "हिरवा चारा",
        "If yes, type of Green Fodder": "होय असल्यास, हिरव्या चाऱ्याचा प्रकार",
        "Quantity of Green Fodder per day (in Kgs)": "दररोज हिरव्या चाऱ्याचे प्रमाण (किलोमध्ये)",
        "Dry Fodder": "सुक्या चाऱ्या",
        "If yes, type of Dry Fodder": "होय असल्यास, सुक्या चाऱ्याचा प्रकार",
        "Quantity of Dry Fodder per day (in Kgs)": "दररोज सुक्या चाऱ्याचे प्रमाण (किलोमध्ये)",
        "Concentrate Feed": "केंद्रित चारा",
        "If yes, which brand": "होय असल्यास, कोणता ब्रँड",
        "Quantity of Concentrate Feed per day (in Kgs)": "दररोज केंद्रित चाऱ्याचे प्रमाण (किलोमध्ये)",
        "Mineral Mixture": "खनिज मिश्रण",
        "If yes, which brand_mineral": "होय असल्यास, कोणता ब्रँड",
        "Quantity of Mineral Mixture per day (in gms)": "दररोज खनिज मिश्रणाचे प्रमाण (ग्राम मध्ये)",
        "Silage": "सायलेज",
        "If yes, what is the source and price": "होय असल्यास, स्त्रोत आणि किंमत काय आहे",
        "Quantity of Silage per day (in Kgs)": "दररोज सायलेजचे प्रमाण (किलोमध्ये)",
        "Type of Farm": "शेताचा प्रकार",
        "Other Type of Farm (if selected above)": "इतर शेताचा प्रकार (वर निवडल्यास)",
        "Source of Water": "पाण्याचा स्त्रोत",
        "Preventive health care measures-Annual cycle": "प्रतिबंधात्मक आरोग्य सेवा उपाय - वार्षिक चक्र",
        "If Other Preventive health care measures, specify": "इतर प्रतिबंधात्मक आरोग्य सेवा उपाय असल्यास, निर्दिष्ट करा",
        "Have they previously used Ethno veterinary resources": "त्यांनी पूर्वी पारंपरिक पशुवैद्यकीय साधने वापरली आहेत का",
        "If yes, what disease/text": "होय असल्यास, कोणता आजार/मजकूर",
        "Women entrepreneur providing banking services": "बँकिंग सेवा पुरवणाऱ्या महिला उद्योजिका",
        "If Yes, Banking Services Provided by Women Entrepreneur": "होय असल्यास, महिला उद्योजिकाद्वारे प्रदान केलेल्या बँकिंग सेवा",
        "If Other Banking Services, specify": "इतर बँकिंग सेवा असल्यास, निर्दिष्ट करा",
        "Extension services": "विस्तार सेवा",
        "If Other Extension Services, specify": "इतर विस्तार सेवा असल्यास, निर्दिष्ट करा",
        "Survey Details": "सर्वेक्षण तपशील",
        "Name of Surveyor": "सर्वेक्षकाचे नाव",
        "Photo / Timestamp": "फोटो / वेळ",
        "Date of Visit": "भेटीची तारीख",
        "Submit Survey": "सर्वेक्षण सादर करा",
        "Survey Saved!": "सर्वेक्षण जतन केले!",
        "Error saving survey": "सर्वेक्षण जतन करण्यात त्रुटी",
        "Click to Review Baseline Responses": "बेसलाइन प्रतिसाद पाहण्यासाठी क्लिक करा",
        "Baseline Survey Questions": "बेसलाइन सर्वेक्षण प्रश्न",
        "Admin Real-Time Access": "प्रशासक रिअल-टाइम प्रवेश",
        "Enter your Admin Email to unlock extra features:": "अतिरिक्त वैशिष्ट्ये अनलॉक करण्यासाठी आपला व्यवस्थापक ईमेल प्रविष्ट करा:",
        "Admin access granted! Real-time view enabled.": "प्रशासक प्रवेश मंजूर! रिअल-टाइम दृश्य सक्षम केले.",
        "Not an authorized admin.": "अधिकृत प्रशासक नाही.",
        "View and Download Uploaded Images": "अपलोड केलेल्या प्रतिमा पहा आणि डाउनलोड करा",
        "No images found.": "कोणत्याही प्रतिमा आढळल्या नाहीत.",
        "Download": "डाउनलोड करा",
        "View Past Submissions": "मागील सबमिशन पहा",
        "No submissions found yet.": "आत्तापर्यंत कोणतेही सबमिशन आढळले नाही.",
        "Download All Responses": "सर्व प्रतिसाद डाउनलोड करा",
    }
}

# Language Selection - Restricted to English, Hindi, Marathi
lang = st.selectbox("Language / भाषा / भाषा", ("English", "Hindi", "Marathi"))
labels = dict_translations.get(lang, dict_translations['English']) # Fallback to English

st.title(labels['Farmer Profile'])

# --- Data extracted from the provided image ---
# IMPORTANT: 'Tehsil' column is removed.
# The lists below are taken directly from your last provided code.
data = {
    'S.No.': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65],
    'MCC Code': [5015, 5090, 5112, 5117, 5120, 5121, 5300, 5315, 9008, 5093, 5094, 5143, 5140, 5142, 5141, 5082, 5035, 5042, 5044, 5146, 5147, 5148, 5187, 1205, 1203, 1204, 1206, 5478, 5022, 5033, 5337, 5330, 5150, 5400, 5401, 5402, 5404, 5405, 5144, 5406, 5407, 5408, 5409, 5410, 5411, 5412, 5413, 5480, 5481, 5276, 5278, 5283, 5284, 5285, 5301, 5304, 5305, 5306, 5307, 5308, 5309, 6200, 5111, 5398, 5114, 5115, 5145, 5113, 5116],
    'VILLAGE': ['SASTEWADI', 'BHAGDEWALA', 'HINGANGAON', 'MUNDWAD', 'WANJALWADI', 'SAWAD', 'BARAD', 'DEGAON', 'HOL', 'VANJALEGAON', 'DONGARWADI', 'MATHACHIWADI', 'GIRAVI', 'VIRANI', 'BORALE', 'VANJALE (Dudhebab', 'SOMANTHALI', 'BHAGWAKHADAK', 'PINGLEWADI', 'WAGHJWADI', 'MARDHE', 'KADBNHAVNAGAR', 'MALSHIRAS', 'MALSHIRAS', 'PATALWADI', 'AKSHIV', 'PACWAD', 'DEVULGAON RAJE', 'Hingani Lingale', 'BORIBEL', 'MAYURESHWAR', 'WAI', 'BHUINJ', 'CHILEWADI', 'WAI', 'SATARAROAD', 'BUDH', 'WALKALI', 'MAHGAON', 'MOHI', 'MALWADI', 'GHULEWADI', 'AZADPUR', 'BHATKI', 'MARDHE', 'RANANG', 'WALHEWADI', 'ANPATWADI', 'DHAIGULEMALA', 'WAI PHALTAN', 'KHONDSHIRAS', 'SHIRSATWADI', 'KHARALE', 'KATALE', 'WATHARPHATA', 'JALGAON', 'BHIMAKWADI', 'PIMPRAD', 'DALWADI', 'HNTI', 'MIRDE', 'AKOLI', 'SOMANTHALI', 'Sankatesh Agro'],
    'Approved Status': ['Approved'] * 65,
    'BMC Name': [
        'Shree Ganesh Dudh sankalan kendra - Sastewadi', 'Jay Malhar Dudh sankalan kendra, Bhagdewala', 'Bhairavnath Dudh Sankalan Kendra, Hingan Gaon',
        'Mayuresh Dudh Sankalan Kendra, Mundwad', 'Shree Ganesh Dudh Sankalan Kendra, Wanjalwadi', 'Datta Dudh Sankalan Kendra, Sawad',
        'HANUMAN DUDH BARAD', 'SHREECHANDRA DUDH BARAD', 'Govind Sweekarani Dudh sankalan kendra - Hol',
        'VAJUBHAI DUDH VAJAEGOAN', 'DURGADEEVI DUDH DONGARWADI', 'SAKHALI DUDH SANKALAN KENDRA - Mathachiwadi',
        'JAY TUJABHAVANI DUDH GIRAVI', 'VISHWASHAKTA DUDH VIRONI', 'MEGHDUT DUDH BORALI',
        'GOVIND MAHILA SHEWATH KRANTI', 'Sampurn Duche Dudh Sankalan Kendra, Somanthali', 'BHAIRAVNATH DHUDH BHAGWAKHADAK COOLER',
        'Bhairavnath Dudh Sankalan, Pinglewasti', 'Govind Dudh Sankalan, Waghwadi', 'Yash Dudh Sankalan Kendra, Markhel',
        'Govind Milk & Milk products MCC Sadashivnagar', 'Govind Milk and Milk products MCC - Malshiras', 'Govind Dudh Sankalan Kendra - Motejwadi (Gokulnagar)',
        'Jothaling Dudh sankalan kendra, Akshiv', 'JAY BHAVANI DUDH SAN.KEN.ANBHULEWADI PACHWAD', 'Bhairavnath Dudh Sankalan va Shitkaran Kendra - Devulgaon Raje',
        'Jay Hanuman Dudh sankalan kendra, Hingani Lingale', 'Shivtej Dudh Sankalan Kendra, Boribel', 'MAYURESHWAR DAIRY',
        'OM BHAKTI DUDH WAI COW', 'YASHODHAN MILK & MILK PROD. PACWAD', 'SHRIRAM DUDH SANKALAN & SHIT.BHUINJ',
        'Omkarm Dairy Farm', 'Wansagar Dudh Sankalan Kendra', 'Govardhan Dudh Sankalan',
        'Shivani Dudh Budh', 'BHAVYA MILK', 'MAULI DUDH SANKALAN KENDRA',
        'MAHALAXMI DUDH MOHI', 'Bhimashankarlang Milk & Milk products Pvt. Ltd.', 'SHRI SAMARTH DUDH SANKALAN KENDRA',
        'Shri Datta Dudh sankalan kendra', 'JAGDAMBA DUDH BHATKI', 'JAGDAMBA DUDH MARDHE',
        'SUDARSHAN DUDH SANKALAN KEND.MARDI', 'RANANA MCC', 'VAJRINATH DUDH SANK.KENDRA WAHEWADI',
        'Shree Datta Dudh sankalan kendra', 'Shri ram dudh sankala', 'Govind Milk Cc - Vanarmala',
        'Shree Hanuman Dudh sankalan kendra, Phondshiras', 'Shivkrupa Dudh Sankalan va Shitkaran Kendra, Shirsatwadi',
        'Vinayak Dudh Sankalan va Shitkaran Kendra, Kharale', 'Vinayak Dudh Sankalan Kendra Shirale', 'Rajmudra Dudh sankalan',
        'Jay Hanuman Dudh Sankalan Kendra, Jambgaon', 'JAY BHAVANI BMC NAIKBAGWADI', 'Chandrabhaga Dudh sankalan kendra',
        'SHRINATH ROKADESHWAR DALWADI BMC', 'Ittehad Dudh Sankalan Kendra, HNTI', 'JANAI DUDH SANKALAN KENDRA MIRDE',
        'Sant BhagwanbabaDudh Sankalan Kendra - Akole', 'JAGDAMBA DUDH SOMANTHALI', 'Shrinath Mhasoba Dudh Sankalan Karanje'
    ],
    'District': [
        'SATARA', 'SATARA', 'SATARA', 'SATARA', 'SATARA', 'SATARA', 'SATARA', 'SATARA', 'SATARA', 'SATARA',
        'SATARA', 'SATARA', 'SATARA', 'SATARA', 'SATARA', 'PUNE', 'PUNE', 'PUNE', 'PUNE', 'PUNE',
        'PUNE', 'PUNE', 'PUNE', 'SOLAPUR', 'SOLAPUR', 'SOLAPUR', 'SOLAPUR', 'SATARA', 'PUNE', 'PUNE',
        'PUNE', 'PUNE', 'SATARA', 'SATARA', 'SATARA', 'SATARA', 'SATARA', 'SATARA', 'SATARA', 'SATARA',
        'SATARA', 'SATARA', 'SATARA', 'SATARA', 'SATARA', 'SATARA', 'SATARA', 'SOLAPUR', 'SOLAPUR', 'PUNE',
        'PUNE', 'SOLAPUR', 'SOLAPUR', 'SATARA', 'SATARA', 'SATARA', 'SATARA', 'SATARA', 'SATARA', 'PUNE',
        'SATARA', 'SATARA', 'PUNE', '', ''
    ]
}

# --- PROGRAMMATIC LENGTH CORRECTION FOR ROBUSTNESS ---
# This loop finds the maximum length and pads shorter lists.
# This ensures the DataFrame creation will not fail due to length mismatch.
max_len = 0
for key, value in data.items():
    if isinstance(value, list):
        max_len = max(max_len, len(value))

for key, value in data.items():
    if isinstance(value, list) and len(value) < max_len:
        # Pad with empty string for consistency, as most values are text.
        # If any column is strictly numeric, consider padding with 0 or None.
        data[key].extend([''] * (max_len - len(value)))
    elif not isinstance(value, list):
        # This case is less likely with the current data structure,
        # but handles if a value was a single non-list item by mistake.
        data[key] = [value] * max_len


df_locations = pd.DataFrame(data)

# Extract unique options for dropdowns
bmc_mcc_names = sorted(df_locations['BMC Name'].unique().tolist())
villages = sorted(df_locations['VILLAGE'].unique().tolist())
districts = sorted(df_locations['District'].unique().tolist())


# Initialize session state for baseline answers if not already present
if 'baseline_answers' not in st.session_state:
    st.session_state.baseline_answers = {}
if 'uploaded_image_filename' not in st.session_state:
    st.session_state.uploaded_image_filename = None


# --- Updated BASELINE_QUESTIONS ---
BASELINE_QUESTIONS = [
    # Farmer Profile Section
    {"label": {"English": "Types", "Hindi": "प्रकार", "Marathi": "प्रकार"}, "type": "text"},
    {"label": {"English": "BMC/MCC Name", "Hindi": "बीएमसी/एमसीसी नाम", "Marathi": "बीएमसी/एमसीसी नाव"}, "type": "select", "options": bmc_mcc_names},
    {"label": {"English": "BMC/MCC Code", "Hindi": "बीएमसी/एमसीसी कोड", "Marathi": "बीएमसी/एमसीसी कोड"}, "type": "text"},
    {"label": {"English": "District", "Hindi": "जिला", "Marathi": "जिल्हा"}, "type": "select", "options": districts},
    {"label": {"English": "Taluka", "Hindi": "तालुका", "Marathi": "तालुका"}, "type": "text"}, # Now a text input
    {"label": {"English": "Village", "Hindi": "गांव", "Marathi": "गाव"}, "type": "select", "options": villages},
    {"label": {"English": "BCF Name", "Hindi": "बीसीएफ का नाम", "Marathi": "बीसीएफचे नाव"}, "type": "text"},
    {"label": {"English": "Energy sources", "Hindi": "ऊर्जा स्रोत", "Marathi": "ऊर्जेचे स्रोत"}, "type": "multiselect", "options": ["Solar", "Main electricity", "Both", "Generator"]},
    {"label": {"English": "Number of villages covered by the BMC", "Hindi": "बीएमसी द्वारा कवर किए गए गांवों की संख्या", "Marathi": "बीएमसीने व्यापलेली गावांची संख्या"}, "type": "number"},
    {"label": {"English": "Name of village", "Hindi": "गांव का नाम", "Marathi": "गावाचे नाव"}, "type": "text"},
    {"label": {"English": "No. of direct pouring farmers", "Hindi": "प्रत्यक्ष दूध देने वाले किसानों की संख्या", "Marathi": "थेट दूध देणाऱ्या शेतकऱ्यांची संख्या"}, "type": "number"},
    {"label": {"English": "No. of Route vehicles pouring milk at BMC", "Hindi": "बीएमसी में दूध डालने वाले रूट वाहन", "Marathi": "बीएमसीमध्ये दूध आणणाऱ्या मार्ग वाहनांची संख्या"}, "type": "number"},
    {"label": {"English": "No. of farmers under each Route vehicle", "Hindi": "प्रत्येक रूट वाहन के तहत किसानों की संख्या", "Marathi": "प्रत्येक मार्ग वाहनाखालील शेतकऱ्यांची संख्या"}, "type": "number"},
    {"label": {"English": "Farmer Name", "Hindi": "किसान का नाम", "Marathi": "शेतकऱ्याचे नाव"}, "type": "text"},
    {"label": {"English": "Farmer Code / Pourer Id", "Hindi": "किसान कोड / दूध देने वाला आईडी", "Marathi": "शेतकरी कोड / दूध देणारा आयडी"}, "type": "text"},
    {"label": {"English": "Gender", "Hindi": "लिंग", "Marathi": "लिंग"}, "type": "select", "options": ["Male", "Female"]},
    {"label": {"English": "Services provided by BMC to farmer", "Hindi": "किसान को बीएमसी द्वारा दी जाने वाली सेवाएं", "Marathi": "शेतकऱ्याला बीएमसीने दिलेल्या सेवा"}, "type": "multiselect", "options": ["AI", "Vaccination", "Feed supply", "Silage", "None", "Other (specify)"]},
    {"label": {"English": "Other Services (if selected above)", "Hindi": "अन्य सेवाएं (यदि ऊपर चुना गया हो)", "Marathi": "इतर सेवा (वर निवडल्यास)"}, "type": "text", "depends_on": {"Services provided by BMC to farmer": "Other (specify)"}},

    # Farm Details Section
    {"label": {"English": "Number of Cows", "Hindi": "गायों की संख्या", "Marathi": "गायांची संख्या"}, "type": "number"},
    {"label": {"English": "No. of Cattle in Milk", "Hindi": "दूध देणारे जनावरे", "Marathi": "दूध देणाऱ्या जनावरांची संख्या"}, "type": "number"},
    {"label": {"English": "No. of Calves/Heifers", "Hindi": "बछड़े/बछड़ियां", "Marathi": "कालवडे/कालवडी"}, "type": "number"},
    {"label": {"English": "No. of Desi cows", "Hindi": "देसी गायों की संख्या", "Marathi": "देशी गायांची संख्या"}, "type": "number"},
    {"label": {"English": "Milk Production in litres per day-Desi cows", "Hindi": "देसी गायों द्वारा प्रतिदिन दूध उत्पादन (लीटर में)", "Marathi": "देशी गायींकडून दररोज दूध उत्पादन (लिटर मध्ये)"}, "type": "number"},
    {"label": {"English": "No. of Cross breed cows", "Hindi": "क्रॉसब्रीड गायों की संख्या", "Marathi": "क्रॉसब्रीड गायांची संख्या"}, "type": "number"},
    {"label": {"English": "Type of cross breed(HF/Jersey)", "Hindi": "क्रॉसब्रीड प्रकार (HF/जर्सी)", "Marathi": "क्रॉसब्रीड प्रकार (HF/जर्सी)"}, "type": "text"},
    {"label": {"English": "Milk Production in litres per day-Cross breed(HF/Jersey)", "Hindi": "क्रॉसब्रीड गायों द्वारा प्रतिदिन दूध उत्पादन (HF/जर्सी)", "Marathi": "क्रॉसब्रीड गायींकडून दररोज दूध उत्पादन (HF/जर्सी)"}, "type": "number"},
    {"label": {"English": "No. of Buffalo", "Hindi": "भैंसों की संख्या", "Marathi": "म्हशींची संख्या"}, "type": "number"},
    {"label": {"English": "Milk Production in liters per day-buffalo", "Hindi": "भैंसों द्वारा प्रतिदिन दूध उत्पादन (लीटर में)", "Marathi": "म्हशींकडून दररोज दूध उत्पादन (लिटर मध्ये)"}, "type": "number"},

    # Specific Questions Section
    {"section": "Specific Questions"},
    {"label": {"English": "Green Fodder", "Hindi": "हरा चारा", "Marathi": "हिरवा चारा"}, "type": "select", "options": ["Yes", "No"]},
    {"label": {"English": "If yes, type of Green Fodder", "Hindi": "यदि हाँ, तो हरे चारे का प्रकार", "Marathi": "होय असल्यास, हिरव्या चाऱ्याचा प्रकार"}, "type": "text", "depends_on": {"Green Fodder": "Yes"}},
    {"label": {"English": "Quantity of Green Fodder per day (in Kgs)", "Hindi": "प्रतिदिन हरे चारे की मात्रा (किलो में)", "Marathi": "दररोज हिरव्या चाऱ्याचे प्रमाण (किलोमध्ये)"}, "type": "number", "depends_on": {"Green Fodder": "Yes"}},
    {"label": {"English": "Dry Fodder", "Hindi": "सूखा चारा", "Marathi": "सुक्या चाऱ्या"}, "type": "select", "options": ["Yes", "No"]},
    {"label": {"English": "If yes, type of Dry Fodder", "Hindi": "यदि हाँ, तो सूखे चारे का प्रकार", "Marathi": "होय असल्यास, सुक्या चाऱ्याचा प्रकार"}, "type": "text", "depends_on": {"Dry Fodder": "Yes"}},
    {"label": {"English": "Quantity of Dry Fodder per day (in Kgs)", "Hindi": "प्रतिदिन सूखे चारे की मात्रा (किलो में)", "Marathi": "दररोज सुक्या चाऱ्याचे प्रमाण (किलोमध्ये)"}, "type": "number", "depends_on": {"Dry Fodder": "Yes"}},
    {"label": {"English": "Concentrate Feed", "Hindi": "सांद्रित चारा", "Marathi": "केंद्रित चारा"}, "type": "select", "options": ["Yes", "No"]},
    {"label": {"English": "If yes, which brand", "Hindi": "यदि हाँ, तो कौन सा ब्रांड", "Marathi": "होय असल्यास, कोणता ब्रँड"}, "type": "text", "depends_on": {"Concentrate Feed": "Yes"}},
    {"label": {"English": "Quantity of Concentrate Feed per day (in Kgs)", "Hindi": "प्रतिदिन सांद्रित चारे की मात्रा (किलो में)", "Marathi": "दररोज केंद्रित चाऱ्याचे प्रमाण (किलोमध्ये)"}, "type": "number", "depends_on": {"Concentrate Feed": "Yes"}},
    {"label": {"English": "Mineral Mixture", "Hindi": "खनिज मिश्रण", "Marathi": "खनिज मिश्रण"}, "type": "select", "options": ["Yes", "No"]},
    {"label": {"English": "If yes, which brand_mineral", "Hindi": "यदि हाँ, तो कौन सा ब्रांड", "Marathi": "होय असल्यास, कोणता ब्रँड"}, "type": "text", "depends_on": {"Mineral Mixture": "Yes"}},
    {"label": {"English": "Quantity of Mineral Mixture per day (in gms)", "Hindi": "प्रतिदिन खनिज मिश्रण की मात्रा (ग्राम में)", "Marathi": "दररोज खनिज मिश्रणाचे प्रमाण (ग्राम मध्ये)"}, "type": "number", "depends_on": {"Mineral Mixture": "Yes"}},
    {"label": {"English": "Silage", "Hindi": "साइलेज", "Marathi": "सायलेज"}, "type": "select", "options": ["Yes", "No"]},
    {"label": {"English": "If yes, what is the source and price", "Hindi": "यदि हाँ, तो स्रोत और कीमत क्या है", "Marathi": "होय असल्यास, स्त्रोत आणि किंमत काय आहे"}, "type": "text", "depends_on": {"Silage": "Yes"}},
    {"label": {"English": "Quantity of Silage per day (in Kgs)", "Hindi": "प्रतिदिन साइलेज की मात्रा (किलो में)", "Marathi": "दररोज सायलेजचे प्रमाण (किलोमध्ये)"}, "type": "number", "depends_on": {"Silage": "Yes"}},
    {"label": {"English": "Type of Farm", "Hindi": "खेत का प्रकार", "Marathi": "शेताचा प्रकार"}, "type": "multiselect", "options": ["Conventional", "Animal Welfare Farm", "Other (specify)"]},
    {"label": {"English": "Other Type of Farm (if selected above)", "Hindi": "अन्य खेत का प्रकार (यदि ऊपर चुना गया हो)", "Marathi": "इतर शेताचा प्रकार (वर निवडल्यास)"}, "type": "text", "depends_on": {"Type of Farm": "Other (specify)"}},
    {"label": {"English": "Source of Water", "Hindi": "पानी का स्रोत", "Marathi": "पाण्याचा स्त्रोत"}, "type": "text"},
    {"label": {"English": "Preventive health care measures-Annual cycle", "Hindi": "रोकथाम स्वास्थ्य देखभाल उपाय - वार्षिक चक्र", "Marathi": "प्रतिबंधात्मक आरोग्य सेवा उपाय - वार्षिक चक्र"}, "type": "multiselect", "options": ["Vaccination", "Deworming", "Preventive Health checkup", "Other (specify)"]},
    {"label": {"English": "If Other Preventive health care measures, specify", "Hindi": "यदि अन्य निवारक स्वास्थ्य देखभाल उपाय, तो निर्दिष्ट करें", "Marathi": "इतर प्रतिबंधात्मक आरोग्य सेवा उपाय असल्यास, निर्दिष्ट करा"}, "type": "text", "depends_on": {"Preventive health care measures-Annual cycle": "Other (specify)"}},
    {"label": {"English": "Have they previously used Ethno veterinary resources", "Hindi": "क्या उन्होंने पहले एथनो पशु चिकित्सा संसाधनों का उपयोग किया है", "Marathi": "त्यांनी पूर्वी पारंपरिक पशुवैद्यकीय साधने वापरली आहेत का"}, "type": "select", "options": ["Yes", "No"]},
    {"label": {"English": "If yes, what disease/text", "Hindi": "यदि हाँ, तो कौन सी बीमारी/पाठ", "Marathi": "होय असल्यास, कोणता आजार/मजकूर"}, "type": "text", "depends_on": {"Have they previously used Ethno veterinary resources": "Yes"}},
    {"label": {"English": "Women entrepreneur providing banking services", "Hindi": "महिला उद्यमी जो बैंकिंग सेवाएं प्रदान करती हैं", "Marathi": "बँकिंग सेवा पुरवणाऱ्या महिला उद्योजिका"}, "type": "select", "options": ["Yes", "No"]},
    {"label": {"English": "If Yes, Banking Services Provided by Women Entrepreneur", "Hindi": "यदि हाँ, तो महिला उद्यमी द्वारा प्रदान की जाने वाली बैंकिंग सेवाएं", "Marathi": "होय असल्यास, महिला उद्योजिकाद्वारे प्रदान केलेल्या बँकिंग सेवा"}, "type": "multiselect", "options": ["Yes-Bank", "MF", "Other (specify)"]},
    {"label": {"English": "If Other Banking Services, specify", "Hindi": "यदि अन्य बैंकिंग सेवाएं, तो निर्दिष्ट करें", "Marathi": "इतर बँकिंग सेवा असल्यास, निर्दिष्ट करा"}, "type": "text", "depends_on": {"If Yes, Banking Services Provided by Women Entrepreneur": "Other (specify)"}},
    {"label": {"English": "Extension services", "Hindi": "विस्तार सेवाएं", "Marathi": "विस्तार सेवा"}, "type": "multiselect", "options": ["Training", "Concentrate Feed Supply", "Mineral Mixture", "AI Services", "Health Camps", "No Services", "Others (specify)"]},
    {"label": {"English": "If Other Extension Services, specify", "Hindi": "यदि अन्य विस्तार सेवाएं, तो निर्दिष्ट करें", "Marathi": "इतर विस्तार सेवा असल्यास, निर्दिष्ट करा"}, "type": "text", "depends_on": {"Extension services": "Others (specify)"}},

    # Final Fields
    {"section": "Survey Details"},
    {"label": {"English": "Name of Surveyor", "Hindi": "सर्वेक्षक का नाम", "Marathi": "सर्वेक्षकाचे नाव"}, "type": "text"},
    {"label": {"English": "Photo / Timestamp", "Hindi": "फोटो / टाइमस्टैम्प", "Marathi": "फोटो / वेळ"}, "type": "camera_input"},
    {"label": {"English": "Date of Visit", "Hindi": "यात्रा की तारीख", "Marathi": "भेटीची तारीख"}, "type": "date"},
]

# Render form UI
st.header(labels["Baseline Survey Questions"])

# Use st.session_state.baseline_answers to persist inputs across reruns
baseline_answers = st.session_state.baseline_answers

# Keep track of previous answers for dependency checking
previous_answers = {}

for idx, q in enumerate(BASELINE_QUESTIONS):
    # Only try to update previous_answers if the dictionary item 'q' has a 'label' key
    if "label" in q:
        previous_answers[q['label']['English']] = baseline_answers.get(q['label']['English'])

    if "section" in q:
        st.subheader(labels[q["section"]])
        continue

    # Proceed only if the question has a 'label' (i.e., it's a real input field)
    if "label" in q:
        display_question = True
        if "depends_on" in q:
            dependency_key_english = list(q["depends_on"].keys())[0]
            expected_value = q["depends_on"][dependency_key_english]

            # Get the value of the parent question from the current baseline_answers
            dependent_q_value = baseline_answers.get(dependency_key_english)

            if dependent_q_value is not None:
                if isinstance(dependent_q_value, list): # Multi-select dependency
                    if expected_value not in dependent_q_value:
                        display_question = False
                else: # Single select, text, number dependency
                    if dependent_q_value != expected_value:
                        display_question = False
            else:
                display_question = False

        label = q['label'].get(lang, q['label']['English'])
        key = f"baseline_q_{idx}_{lang}"

        if display_question:
            # Retrieve current value from baseline_answers for sticky inputs
            current_val_for_widget = baseline_answers.get(q['label']['English'])

            if q['type'] == 'text':
                baseline_answers[q['label']['English']] = st.text_input(label, value=current_val_for_widget if current_val_for_widget is not None else "", key=key)
            elif q['type'] == 'number':
                baseline_answers[q['label']['English']] = st.number_input(label, min_value=0.0, value=current_val_for_widget if current_val_for_widget is not None else 0.0, key=key)
            elif q['type'] == 'select':
                default_index = 0
                if q['options']:
                    if current_val_for_widget in q['options']:
                        default_index = q['options'].index(current_val_for_widget)
                    elif current_val_for_widget is None and "" in q['options']:
                        default_index = q['options'].index("")
                    elif current_val_for_widget is None:
                        default_index = 0
                else:
                    baseline_answers[q['label']['English']] = None
                    continue
                baseline_answers[q['label']['English']] = st.selectbox(label, q['options'], index=default_index, key=key)
            elif q['type'] == 'multiselect':
                baseline_answers[q['label']['English']] = st.multiselect(label, q['options'], default=current_val_for_widget if current_val_for_widget is not None else [], key=key)
            elif q['type'] == 'date':
                baseline_answers[q['label']['English']] = st.date_input(label, value=current_val_for_widget if current_val_for_widget is not None else datetime.date.today(), key=key)
            elif q['type'] == 'camera_input':
                uploaded_image = st.camera_input(label, key=key)
                if uploaded_image is not None:
                    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                    image_filename = f"photo_{timestamp}.jpg"
                    image_path = os.path.join(IMAGE_SAVE_DIR, image_filename)
                    with open(image_path, "wb") as f:
                        f.write(uploaded_image.getbuffer())
                    baseline_answers[q['label']['English']] = image_filename
                    st.session_state.uploaded_image_filename = image_filename
                else:
                    baseline_answers[q['label']['English']] = None
                    st.session_state.uploaded_image_filename = None

        else:
            if q['label']['English'] in baseline_answers:
                del baseline_answers[q['label']['English']]
                if q['type'] == 'camera_input':
                    st.session_state.uploaded_image_filename = None


# --- Survey Submission ---
if st.button(labels["Submit Survey"]):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = os.path.join(SAVE_DIR, f"survey_response_{timestamp}.csv")
    try:
        data_to_save = {k: v for k, v in baseline_answers.items() if v is not None}
        df = pd.DataFrame([data_to_save])
        df.to_csv(file_name, index=False)
        st.success(labels["Survey Saved!"])
        st.session_state.baseline_answers = {}
        st.session_state.uploaded_image_filename = None
        st.experimental_rerun()
    except Exception as e:
        st.error(f"{labels['Error saving survey']}: {e}")

# Display responses in summary
with st.expander(labels["Click to Review Baseline Responses"]):
    st.subheader(labels["Baseline Survey Questions"])
    if st.session_state.baseline_answers:
        for k, v in st.session_state.baseline_answers.items():
            st.markdown(f"**{k}**: {v}")
    else:
        st.info("No responses to display yet. Fill out the form and submit.")


st.divider()
st.header(labels["Admin Real-Time Access"])

# Allowed Emails
ALLOWED_EMAILS = ["shifalis@tns.org", "rmukherjee@tns.org","rsomanchi@tns.org", "mkaushal@tns.org"]
admin_email = st.text_input(labels["Enter your Admin Email to unlock extra features:"], key="admin_email_input")

if admin_email in ALLOWED_EMAILS:
    st.success(labels["Admin access granted! Real-time view enabled."])

    if st.checkbox(labels["View and Download Uploaded Images"]):
        image_files = [f for f in os.listdir(IMAGE_SAVE_DIR) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        if image_files:
            for img_file in image_files:
                img_path = os.path.join(IMAGE_SAVE_DIR, img_file)
                st.image(img_path, caption=img_file, use_column_width=True)
                with open(img_path, "rb") as img:
                    st.download_button(
                        label=f"⬇️ {labels['Download']} {img_file}",
                        data=img,
                        file_name=img_file,
                        mime="image/jpeg" if img_file.lower().endswith(('.jpg', '.jpeg')) else "image/png"
                    )
        else:
            st.warning(labels["No images found."])

    if st.checkbox(labels["View Past Submissions"]):
        # Filter for CSV files that start with 'survey_response_' to avoid other CSVs
        files = [f for f in os.listdir(SAVE_DIR) if f.endswith('.csv') and f.startswith('survey_response_')]
        if files:
            all_data = pd.concat([pd.read_csv(os.path.join(SAVE_DIR, f)) for f in files], ignore_index=True)
            st.dataframe(all_data)
            csv = all_data.to_csv(index=False).encode('utf-8')
            st.download_button(
                label=f"⬇️ {labels['Download All Responses']}",
                data=csv,
                file_name='all_survey_responses.csv',
                mime='text/csv',
                key='admin_csv_download'
            )
        else:
            st.warning(labels["No submissions found yet."])
else:
    if admin_email:
        st.error(labels["Not an authorized admin."])
