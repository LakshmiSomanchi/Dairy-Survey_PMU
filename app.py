import streamlit as st
import pandas as pd
import datetime
import os

# Ensure save folder exists
SAVE_DIR = 'survey_responses'
os.makedirs(SAVE_DIR, exist_ok=True)

# Streamlit Page Config
st.set_page_config(page_title="Heritage Dairy Survey", page_icon="🐄", layout="centered")

# --- Language Translations ---
# Define your translations here.
dict_translations = {
    "English": {
        "Farmer Profile": "Farmer Profile",
        "Types": "Types",
        "BMC/MCC Name": "BMC/MCC Name",
        "BMC/MCC Code": "BMC/MCC Code",
        "District": "District",
        "Taluka": "Taluka",
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
        "Milk Production in litres per day-Cross breed(HF/Jersey)-2": "Milk Production in litres per day-Cross breed (HF/Jersey)",
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
        "Quantity ofConcentrate Feed per day (in Kgs)": "Quantity of Concentrate Feed per day (in Kgs)",
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
        "Milk Production in litres per day-Cross breed(HF/Jersey)-2": "क्रॉसब्रीड गायों द्वारा प्रतिदिन दूध उत्पादन (HF/जर्सी)",
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
        "Quantity ofConcentrate Feed per day (in Kgs)": "प्रतिदिन सांद्रित चारे की मात्रा (किलो में)",
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
    "Telugu": {
        "Farmer Profile": "రైతు ప్రొఫైల్",
        "Types": "రకాలు",
        "BMC/MCC Name": "BMC/MCC పేరు",
        "BMC/MCC Code": "BMC/MCC కోడ్",
        "District": "జిల్లా",
        "Taluka": "తాలూకా",
        "Village": "గ్రామం",
        "BCF Name": "BCF పేరు",
        "Energy sources": "శక్తి వనరులు",
        "Number of villages covered by the BMC": "BMC కవర్ చేసిన గ్రామాల సంఖ్య",
        "Name of village": "గ్రామం పేరు",
        "No. of direct pouring farmers": "ప్రత్యక్షంగా పాలు పోసే రైతుల సంఖ్య",
        "No. of Route vehicles pouring milk at BMC": "BMC వద్ద పాలు పోసే రూట్ వాహనాల సంఖ్య",
        "No. of farmers under each Route vehicle": "ప్రతి రూట్ వాహనం కింద రైతుల సంఖ్య",
        "Farmer Name": "రైతు పేరు",
        "Farmer Code / Pourer Id": "రైతు కోడ్ / పోసే వారి ID",
        "Gender": "లింగం",
        "Services provided by BMC to farmer": "రైతుకు BMC అందించే సేవలు",
        "Other Services (if selected above)": "ఇతర సేవలు (పైన ఎంచుకుంటే)",
        "Number of Cows": "ఆవుల సంఖ్య",
        "No. of Cattle in Milk": "పాలు ఇచ్చే పశువుల సంఖ్య",
        "No. of Calves/Heifers": "దూడలు/పెయ్యలు",
        "No. of Desi cows": "దేశీ ఆవుల సంఖ్య",
        "Milk Production in litres per day-Desi cows": "దేశీ ఆవుల నుండి రోజుకు లీటర్లలో పాలు ఉత్పత్తి",
        "No. of Cross breed cows": "క్రాస్ బ్రీడ్ ఆవుల సంఖ్య",
        "Type of cross breed(HF/Jersey)": "క్రాస్ బ్రీడ్ రకం (HF/Jersey)",
        "Milk Production in litres per day-Cross breed(HF/Jersey)-2": "క్రాస్ బ్రీడ్ ఆవుల నుండి రోజుకు లీటర్లలో పాలు ఉత్పత్తి (HF/Jersey)",
        "No. of Buffalo": "గేదెల సంఖ్య",
        "Milk Production in liters per day-buffalo": "గేదెల నుండి రోజుకు లీటర్లలో పాలు ఉత్పత్తి",
        "Specific Questions": "నిర్దిష్ట ప్రశ్నలు",
        "Green Fodder": "పచ్చ గడ్డి",
        "If yes, type of Green Fodder": "అవును అయితే, పచ్చ గడ్డి రకం",
        "Quantity of Green Fodder per day (in Kgs)": "రోజుకు పచ్చ గడ్డి పరిమాణం (కిలోలలో)",
        "Dry Fodder": "పొడి గడ్డి",
        "If yes, type of Dry Fodder": "అవును అయితే, పొడి గడ్డి రకం",
        "Quantity of Dry Fodder per day (in Kgs)": "రోజుకు పొడి గడ్డి పరిమాణం (కిలోలలో)",
        "Concentrate Feed": "సాంద్రత కలిగిన దాణా",
        "If yes, which brand": "అవును అయితే, ఏ బ్రాండ్",
        "Quantity ofConcentrate Feed per day (in Kgs)": "రోజుకు సాంద్రత కలిగిన దాణా పరిమాణం (కిలోలలో)",
        "Mineral Mixture": "ఖనిజ మిశ్రమం",
        "If yes, which brand_mineral": "అవును అయితే, ఏ బ్రాండ్",
        "Quantity of Mineral Mixture per day (in gms)": "రోజుకు ఖనిజ మిశ్రమం పరిమాణం (గ్రాములలో)",
        "Silage": "సైలేజ్",
        "If yes, what is the source and price": "అవును అయితే, మూలం మరియు ధర ఏమిటి",
        "Quantity of Silage per day (in Kgs)": "రోజుకు సైలేజ్ పరిమాణం (కిలోలలో)",
        "Type of Farm": "ఫారం రకం",
        "Other Type of Farm (if selected above)": "ఇతర ఫారం రకం (పైన ఎంచుకుంటే)",
        "Source of Water": "నీటి వనరు",
        "Preventive health care measures-Annual cycle": "నివారణ ఆరోగ్య సంరక్షణ చర్యలు - వార్షిక చక్రం",
        "If Other Preventive health care measures, specify": "ఇతర నివారణ ఆరోగ్య సంరక్షణ చర్యలు అయితే, పేర్కొనండి",
        "Have they previously used Ethno veterinary resources": "వారు గతంలో ఎథ్నో వెటర్నరీ వనరులను ఉపయోగించారా",
        "If yes, what disease/text": "అవును అయితే, ఏ వ్యాధి/పాఠం",
        "Women entrepreneur providing banking services": "బ్యాంకింగ్ సేవలను అందించే మహిళా వ్యాపారవేత్త",
        "If Yes, Banking Services Provided by Women Entrepreneur": "అవును అయితే, మహిళా వ్యాపారవేత్త అందించిన బ్యాంకింగ్ సేవలు",
        "If Other Banking Services, specify": "ఇతర బ్యాంకింగ్ సేవలు అయితే, పేర్కొనండి",
        "Extension services": "విస్తరణ సేవలు",
        "If Other Extension Services, specify": "ఇతర విస్తరణ సేవలు అయితే, పేర్కొనండి",
        "Survey Details": "సర్వే వివరాలు",
        "Name of Surveyor": "సర్వేయర్ పేరు",
        "Photo / Timestamp": "ఫోటో / టైమ్‌స్టాంప్",
        "Date of Visit": "సందర్శన తేదీ",
        "Submit Survey": "సర్వే సమర్పించండి",
        "Survey Saved!": "సర్వే సేవ్ చేయబడింది!",
        "Error saving survey": "సర్వే సేవ్ చేయడంలో లోపం",
        "Click to Review Baseline Responses": "బేస్లైన్ ప్రతిస్పందనలను సమీక్షించడానికి క్లిక్ చేయండి",
        "Baseline Survey Questions": "బేస్లైన్ సర్వే ప్రశ్నలు",
        "Admin Real-Time Access": "అడ్మిన్ రియల్ టైమ్ యాక్సెస్",
        "Enter your Admin Email to unlock extra features:": "అదనపు ఫీచర్లను అన్‌లాక్ చేయడానికి మీ అడ్మిన్ ఇమెయిల్‌ను నమోదు చేయండి:",
        "Admin access granted! Real-time view enabled.": "అడ్మిన్ యాక్సెస్ మంజూరు చేయబడింది! రియల్ టైమ్ వీక్షణ ప్రారంభించబడింది.",
        "Not an authorized admin.": "అధీకృత అడ్మిన్ కాదు.",
        "View and Download Uploaded Images": "అప్‌లోడ్ చేసిన చిత్రాలను చూడండి మరియు డౌన్‌లోడ్ చేయండి",
        "No images found.": "చిత్రాలు కనుగొనబడలేదు.",
        "Download": "డౌన్‌లోడ్ చేయండి",
        "View Past Submissions": "గత సమర్పణలను చూడండి",
        "No submissions found yet.": "ఇప్పటివరకు సమర్పణలు కనుగొనబడలేదు.",
        "Download All Responses": "అన్ని ప్రతిస్పందనలను డౌన్‌లోడ్ చేయండి",
    }
}

lang = st.selectbox("Language / भाषा / భాష", ("English", "Hindi", "Telugu"))
labels = dict_translations.get(lang, dict_translations['English']) # Fallback to English

# Title
st.title(labels['Farmer Profile'])

# --- Data extracted from the provided image ---
# This would ideally be loaded from a CSV/DB in a real app.
# Using a DataFrame here for easier processing, but you could just use lists.
data = {
    'S.No.': [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65],
    'MCC Code': [5015,5090,5112,5117,5120,5121,5300,5315,9008,5093,5094,5143,5140,5142,5141,5082,5035,5042,5044,5146,5147,5148,5187,1205,1203,1204,1206,5478,5022,5033,5337,5330,5150,5400,5401,5402,5404,5405,5144,5406,5407,5408,5409,5410,5411,5412,5413,5480,5481,5276,5278,5283,5284,5285,5301,5304,5305,5306,5307,5308,5309,6200,5111,5398,5114,5115,5145,5113,5116],
    'VILLAGE': ['SASTEWADI','BHAGDEWALA','HINGANGAON','MUNDWAD','WANJALWADI','SAWAD','BARAD','DEGAON','HOL','VANJALEGAON','DONGARWADI','MATHACHIWADI','GIRAVI','VIRANI','BORALE','VANJALE (Dudhebab','SOMANTHALI','BHAGWAKHADAK','PINGLEWADI','WAGHJWADI','MARDHE','KADBNHAVNAGAR','MALSHIRAS','PATALWADI','AKSHIV','PACWAD','DEVULGAON RAJE','Hingani Lingale','BORIBEL','MAYURESHWAR','WAI','BHUINJ','CHILEWADI','WAI','SATARAROAD','BUDH','WALKALI','MAHGAON','MOHI','MALWADI','GHULEWADI','AZADPUR','BHATKI','MARDHE','RANANG','WALHEWADI','ANPATWADI','DHAIGULEMALA','WAI PHALTAN','KHONDSHIRAS','SHIRSATWADI','KHARALE','KATALE','WATHARPHATA','JALGAON','BHIMAKWADI','PIMPRAD','DALWADI','HNTI','MIRDE','AKOLI','SOMANTHALI','Sankatesh Agro'],
    'Approved Status': ['Approved'] * 65, # Assuming all are 'Approved' for simplicity from the image
    'BMC Name': ['Shree Ganesh Dudh sankalan kendra - Sastewadi', 'Jay Malhar Dudh sankalan kendra, Bhagdewala', 'Bhairavnath Dudh Sankalan Kendra, Hingan Gaon', 'Mayuresh Dudh Sankalan Kendra, Mundwad', 'Shree Ganesh Dudh Sankalan Kendra, Wanjalwadi', 'Datta Dudh Sankalan Kendra, Sawad', 'HANUMAN DUDH BARAD', 'SHREECHANDRA DUDH BARAD', 'Govind Sweekarani Dudh sankalan kendra - Hol', 'VAJUBHAI DUDH VAJAEGOAN', 'DURGADEEVI DUDH DONGARWADI', 'SAKHALI DUDH SANKALAN KENDRA - Mathachiwadi', 'JAY TUJABHAVANI DUDH GIRAVI', 'VISHWASHAKTA DUDH VIRONI', 'MEGHDUT DUDH BORALI', 'GOVIND MAHILA SHEWATH KRANTI', 'Sampurn Duche Dudh Sankalan Kendra, Somanthali', 'BHAIRAVNATH DHUDH BHAGWAKHADAK COOLER', 'Bhairavnath Dudh Sankalan, Pinglewasti', 'Govind Dudh Sankalan, Waghwadi', 'Yash Dudh Sankalan Kendra, Markhel', 'Govind Milk & Milk products MMC Sadashivnagar', 'Govind Milk and Milk products MCC - Malshiras', 'Govind Dudh Sankalan Kendra - Motejwadi (Gokulnagar)', 'Jothaling Dudh sankalan kendra, Akshiv', 'JAY BHAVANI DUDH SAN.KEN.ANBHULEWADI PACHWAD', 'Bhairavnath Dudh Sankalan va Shitkaran Kendra - Devulgaon Raje', 'Jay Hanuman Dudh sankalan kendra, Hingani Lingale', 'Shivtej Dudh Sankalan Kendra, Boribel', 'MAYURESHWAR DAIRY', 'OM BHAKTI DUDH WAI COW', 'YASHODHAN MILK & MILK PROD. PACWAD', 'SHRIRAM DUDH SANKALAN & SHIT.BHUINJ', 'Omkarm Dairy Farm', 'Wansagar Dudh Sankalan Kendra', 'Govardhan Dudh Sankalan', 'Shivani Dudh Budh', 'BHAVYA MILK', 'MAULI DUDH SANKALAN KENDRA', 'MAHALAXMI DUDH MOHI', 'Bhimashankarlang Milk & Milk products Pvt. Ltd.', 'SHRI SAMARTH DUDH SANKALAN KENDRA', 'Shri Datta Dudh sankalan kendra', 'JAGDAMBA DUDH BHATKI', 'JAGDAMBA DUDH MARDHE', 'SUDARSHAN DUDH SANKALAN KEND.MARDI', 'RANANA MCC', 'VAJRINATH DUDH SANK.KENDRA WAHEWADI', 'Shree Datta Dudh sankalan kendra', 'Shri ram dudh sankala', 'Govind Milk Cc - Vanarmala', 'Shree Hanuman Dudh sankalan kendra, Phondshiras', 'Shivkrupa Dudh Sankalan va Shitkaran Kendra, Shirsatwadi', 'Vinayak Dudh Sankalan va Shitkaran Kendra, Kharale', 'Vinayak Dudh Sankalan Kendra Shirale', 'Rajmudra Dudh sankalan', 'Jay Hanuman Dudh Sankalan Kendra, Jambgaon', 'JAY BHAVANI BMC NAIKBAGWADI', 'Chandrabhaga Dudh sankalan kendra', 'SHRINATH ROKADESHWAR DALWADI BMC', 'Ittehad Dudh Sankalan Kendra, HNTI', 'JANAI DUDH SANKALAN KENDRA MIRDE', 'Sant BhagwanbabaDudh Sankalan Kendra - Akole', 'JAGDAMBA DUDH SOMANTHALI', 'Shrinath Mhasoba Dudh Sankalan Karanje'],
    'Tehsil': ['PHALTAN', 'PHALTAN', 'PHALTAN', 'PHALTAN', 'PHALTAN', 'PHALTAN', 'PHALTAN', 'PHALTAN', 'PHALTAN', 'PHALTAN', 'PHALTAN', 'PHALTAN', 'PHALTAN', 'PHALTAN', 'PHALTAN', 'BARAMATI', 'BARAMATI', 'BARAMATI', 'BARAMATI', 'BARAMATI', 'BARAMATI', 'BARAMATI', 'BARAMATI', 'MALSHIRAS', 'MALSHIRAS', 'MALSHIRAS', 'MALSHIRAS', 'MAN', 'DAUND', 'DAUND', 'DAUND', 'DAUND', 'WAI', 'WAI', 'WAI', 'KOREGAON', 'KOREGAON', 'KOREGAON', 'KOREGAON', 'MAN', 'MAN', 'MAN', 'MAN', 'KOREGAON', 'KOREGAON', 'KHANDALA', 'KHANDALA', 'MALSHIRAS', 'MALSHIRAS', 'INDAPUR', 'INDAPUR', 'SHRIRAS', 'SHRIRAS', 'PHALTAN', 'PHALTAN', 'PHALTAN', 'PHALTAN', 'PHALTAN', 'PHALTAN', 'DAUND', 'PHALTAN', 'PHALTAN', 'BARAMATI'],
}
df_locations = pd.DataFrame(data)

# Extract unique options for dropdowns
bmc_mcc_names = sorted(df_locations['BMC Name'].unique().tolist())
villages = sorted(df_locations['VILLAGE'].unique().tolist())
tehsils = sorted(df_locations['Tehsil'].unique().tolist()) # This will be for Taluka
# Assuming Tehsil also represents District for now based on the data provided
districts = sorted(df_locations['Tehsil'].unique().tolist()) # You might need a separate 'District' column if distinct from Tehsil

lang = st.selectbox("Language / भाषा / భాష", ("English", "Hindi", "Telugu"))
labels = dict_translations.get(lang, dict_translations['English']) # Fallback to English

# Title
st.title(labels['Farmer Profile'])

# --- Updated BASELINE_QUESTIONS with new sections ---
BASELINE_QUESTIONS = [
    # Farmer Profile Section
    {"label": {"English": "Types", "Hindi": "प्रकार", "Telugu": "రకాలు"}, "type": "text"},
    # Now using the extracted data for dropdowns
    {"label": {"English": "BMC/MCC Name", "Hindi": "बीएमसी/एमसीसी नाम", "Telugu": "BMC/MCC పేరు"}, "type": "select", "options": bmc_mcc_names},
    {"label": {"English": "BMC/MCC Code", "Hindi": "बीएमसी/एमसीसी कोड", "Telugu": "BMC/MCC కోడ్"}, "type": "text"},
    {"label": {"English": "District", "Hindi": "जिला", "Telugu": "జిల్లా"}, "type": "select", "options": districts},
    {"label": {"English": "Taluka", "Hindi": "तालुका", "Telugu": "తాలూకా"}, "type": "select", "options": tehsils},
    {"label": {"English": "Village", "Hindi": "गांव", "Telugu": "గ్రామం"}, "type": "select", "options": villages},
    {"label": {"English": "BCF Name", "Hindi": "बीसीएफ का नाम", "Telugu": "BCF పేరు"}, "type": "text"},
    {"label": {"English": "Energy sources", "Hindi": "ऊर्जा स्रोत", "Telugu": "శక్తి వనరులు"}, "type": "multiselect", "options": ["Solar", "Main electricity", "Both", "Generator"]},
    {"label": {"English": "Number of villages covered by the BMC", "Hindi": "बीएमसी द्वारा कवर किए गए गांवों की संख्या", "Telugu": "BMC కవర్ చేసిన గ్రామాల సంఖ్య"}, "type": "number"},
    {"label": {"English": "Name of village", "Hindi": "गांव का नाम", "Telugu": "గ్రామం పేరు"}, "type": "text"},
    {"label": {"English": "No. of direct pouring farmers", "Hindi": "प्रत्यक्ष दूध देने वाले किसानों की संख्या", "Telugu": "ప్రత్యక్షంగా పాలు పోసే రైతుల సంఖ్య"}, "type": "number"},
    {"label": {"English": "No. of Route vehicles pouring milk at BMC", "Hindi": "बीएमसी में दूध डालने वाले रूट वाहन", "Telugu": "BMC వద్ద పాలు పోసే రూట్ వాహనాల సంఖ్య"}, "type": "number"},
    {"label": {"English": "No. of farmers under each Route vehicle", "Hindi": "प्रत्येक रूट वाहन के तहत किसानों की संख्या", "Telugu": "ప్రతి రూట్ వాహనం కింద రైతుల సంఖ్య"}, "type": "number"},
    {"label": {"English": "Farmer Name", "Hindi": "किसान का नाम", "Telugu": "రైతు పేరు"}, "type": "text"},
    {"label": {"English": "Farmer Code / Pourer Id", "Hindi": "किसान कोड / दूध देने वाला आईडी", "Telugu": "రైతు కోడ్ / పోసే వారి ID"}, "type": "text"},
    {"label": {"English": "Gender", "Hindi": "लिंग", "Telugu": "లింగం"}, "type": "select", "options": ["Male", "Female"]},
    {"label": {"English": "Services provided by BMC to farmer", "Hindi": "किसान को बीएमसी द्वारा दी जाने वाली सेवाएं", "Telugu": "రైతుకు BMC అందించే सేవలు"}, "type": "multiselect", "options": ["AI", "Vaccination", "Feed supply", "Silage", "None", "Other (specify)"]},
    {"label": {"English": "Other Services (if selected above)", "Hindi": "अन्य सेवाएं (यदि ऊपर चुना गया हो)", "Telugu": "ఇతర సేవలు (పైన ఎంచుకుంటే)"}, "type": "text", "depends_on": {"Services provided by BMC to farmer": "Other (specify)"}},

    # Farm Details Section
    {"label": {"English": "Number of Cows", "Hindi": "गायों की संख्या", "Telugu": "ఆవుల సంఖ్య"}, "type": "number"},
    {"label": {"English": "No. of Cattle in Milk", "Hindi": "दूध देणारे जनावरे", "Telugu": "పాలు ఇచ్చే పశువుల సంఖ్య"}, "type": "number"},
    {"label": {"English": "No. of Calves/Heifers", "Hindi": "बछड़े/बछड़ियां", "Telugu": "దూడలు/పెయ్యలు"}, "type": "number"},
    {"label": {"English": "No. of Desi cows", "Hindi": "देसी गायों की संख्या", "Telugu": "దేశీ ఆవుల సంఖ్య"}, "type": "number"},
    {"label": {"English": "Milk Production in litres per day-Desi cows", "Hindi": "देसी गायों द्वारा प्रतिदिन दूध उत्पादन (लीटर में)", "Telugu": "దేశీ ఆవుల నుండి రోజుకు లీటర్లలో పాలు ఉత్పత్తి"}, "type": "number"},
    {"label": {"English": "No. of Cross breed cows", "Hindi": "क्रॉसब्रीड गायों की संख्या", "Telugu": "క్రాస్ బ్రీడ్ ఆవుల సంఖ్య"}, "type": "number"},
    {"label": {"English": "Type of cross breed(HF/Jersey)", "Hindi": "क्रॉसब्रीड प्रकार (HF/जर्सी)", "Telugu": "క్రాస్ బ్రీడ్ రకం (HF/Jersey)"}, "type": "text"},
    {"label": {"English": "Milk Production in litres per day-Cross breed(HF/Jersey)-2", "Hindi": "क्रॉसब्रीड गायों द्वारा प्रतिदिन दूध उत्पादन (HF/जर्सी)", "Telugu": "క్రాస్ బ్రీడ్ ఆవుల నుండి రోజుకు లీటర్లలో పాలు ఉత్పత్తి (HF/Jersey)"}, "type": "number"},
    {"label": {"English": "No. of Buffalo", "Hindi": "भैंसों की संख्या", "Telugu": "గేదెల సంఖ్య"}, "type": "number"},
    {"label": {"English": "Milk Production in liters per day-buffalo", "Hindi": "भैंसों द्वारा प्रतिदिन दूध उत्पादन (लीटर में)", "Telugu": "గేదెల నుండి రోజుకు లీటర్లలో పాలు ఉత్పత్తి"}, "type": "number"},

    # Specific Questions Section (New Section)
    {"section": "Specific Questions"},
    {"label": {"English": "Green Fodder", "Hindi": "हरा चारा", "Telugu": "పచ్చ గడ్డి"}, "type": "select", "options": ["Yes", "No"]},
    {"label": {"English": "If yes, type of Green Fodder", "Hindi": "यदि हाँ, तो हरे चारे का प्रकार", "Telugu": "అవును అయితే, పచ్చ గడ్డి రకం"}, "type": "text", "depends_on": {"Green Fodder": "Yes"}},
    {"label": {"English": "Quantity of Green Fodder per day (in Kgs)", "Hindi": "प्रतिदिन हरे चारे की मात्रा (किलो में)", "Telugu": "రోజుకు పచ్చ గడ్డి పరిమాణం (కిలోలలో)"}, "type": "number", "depends_on": {"Green Fodder": "Yes"}},
    {"label": {"English": "Dry Fodder", "Hindi": "सूखा चारा", "Telugu": "పొడి గడ్డి"}, "type": "select", "options": ["Yes", "No"]},
    {"label": {"English": "If yes, type of Dry Fodder", "Hindi": "यदि हाँ, तो सूखे चारे का प्रकार", "Telugu": "అవును అయితే, పొడి గడ్డి రకం"}, "type": "text", "depends_on": {"Dry Fodder": "Yes"}},
    {"label": {"English": "Quantity of Dry Fodder per day (in Kgs)", "Hindi": "प्रतिदिन सूखे चारे की मात्रा (किलो में)", "Telugu": "రోజుకు పొడి గడ్డి పరిమాణం (కిలోలలో)"}, "type": "number", "depends_on": {"Dry Fodder": "Yes"}},
    {"label": {"English": "Concentrate Feed", "Hindi": "सांद्रित चारा", "Telugu": "సాంద్రత కలిగిన దాణా"}, "type": "select", "options": ["Yes", "No"]},
    {"label": {"English": "If yes, which brand", "Hindi": "यदि हाँ, तो कौन सा ब्रांड", "Telugu": "అవును అయితే, ఏ బ్రాండ్"}, "type": "text", "depends_on": {"Concentrate Feed": "Yes"}},
    {"label": {"English": "Quantity ofConcentrate Feed per day (in Kgs)", "Hindi": "प्रतिदिन सांद्रित चारे की मात्रा (किलो में)", "Telugu": "రోజుకు సాంద్రత కలిగిన దాణా పరిమాణం (కిలోలలో)"}, "type": "number", "depends_on": {"Concentrate Feed": "Yes"}},
    {"label": {"English": "Mineral Mixture", "Hindi": "खनिज मिश्रण", "Telugu": "ఖనిజ మిశ్రమం"}, "type": "select", "options": ["Yes", "No"]},
    {"label": {"English": "If yes, which brand_mineral", "Hindi": "यदि हाँ, तो कौन सा ब्रांड", "Telugu": "అవును అయితే, ఏ బ్రాండ్"}, "type": "text", "depends_on": {"Mineral Mixture": "Yes"}},
    {"label": {"English": "Quantity of Mineral Mixture per day (in gms)", "Hindi": "प्रतिदिन खनिज मिश्रण की मात्रा (ग्राम में)", "Telugu": "రోజుకు ఖనిజ మిశ్రమం పరిమాణం (గ్రాములలో)"}, "type": "number", "depends_on": {"Mineral Mixture": "Yes"}},
    {"label": {"English": "Silage", "Hindi": "साइलेज", "Telugu": "సైలేజ్"}, "type": "select", "options": ["Yes", "No"]},
    {"label": {"English": "If yes, what is the source and price", "Hindi": "यदि हाँ, तो स्रोत और कीमत क्या है", "Telugu": "అవును అయితే, మూలం మరియు ధర ఏమిటి"}, "type": "text", "depends_on": {"Silage": "Yes"}},
    {"label": {"English": "Quantity of Silage per day (in Kgs)", "Hindi": "प्रतिदिन साइलेज की मात्रा (किलो में)", "Telugu": "రోజుకు సైలేజ్ పరిమాణం (కిలోలలో)"}, "type": "number", "depends_on": {"Silage": "Yes"}},
    {"label": {"English": "Type of Farm", "Hindi": "खेत का प्रकार", "Telugu": "ఫారం రకం"}, "type": "multiselect", "options": ["Conventional", "Animal Welfare Farm", "Other (specify)"]},
    {"label": {"English": "Other Type of Farm (if selected above)", "Hindi": "अन्य खेत का प्रकार (यदि ऊपर चुना गया हो)", "Telugu": "ఇతర ఫారం రకం (పైన ఎంచుకుంటే)"}, "type": "text", "depends_on": {"Type of Farm": "Other (specify)"}},
    {"label": {"English": "Source of Water", "Hindi": "पानी का स्रोत", "Telugu": "నీటి వనరు"}, "type": "text"},
    {"label": {"English": "Preventive health care measures-Annual cycle", "Hindi": "रोकथाम स्वास्थ्य देखभाल उपाय - वार्षिक चक्र", "Telugu": "నివారణ ఆరోగ్య సంరక్షణ చర్యలు - వార్షిక చక్రం"}, "type": "multiselect", "options": ["Deworming", "Vaccination", "Health checkup", "Other (specify)"]},
    {"label": {"English": "If Other Preventive health care measures, specify", "Hindi": "यदि अन्य निवारक स्वास्थ्य देखभाल उपाय, तो निर्दिष्ट करें", "Telugu": "ఇతర నివారణ ఆరోగ్య సంరక్షణ చర్యలు అయితే, పేర్కొనండి"}, "type": "text", "depends_on": {"Preventive health care measures-Annual cycle": "Other (specify)"}},
    {"label": {"English": "Have they previously used Ethno veterinary resources", "Hindi": "क्या उन्होंने पहले एथनो पशु चिकित्सा संसाधनों का उपयोग किया है", "Telugu": "వారు గతంలో ఎథ్నో వెటర్నరీ వనరులను ఉపయోగించారా"}, "type": "select", "options": ["Yes", "No"]},
    {"label": {"English": "If yes, what disease/text", "Hindi": "यदि हाँ, तो कौन सी बीमारी/पाठ", "Telugu": "అవును అయితే, ఏ వ్యాధి/పాఠం"}, "type": "text", "depends_on": {"Have they previously used Ethno veterinary resources": "Yes"}},
    {"label": {"English": "Women entrepreneur providing banking services", "Hindi": "महिला उद्यमी जो बैंकिंग सेवाएं प्रदान करती हैं", "Telugu": "బ్యాంకింగ్ సేవలను అందించే మహిళా వ్యాపారవేత్త"}, "type": "select", "options": ["Yes", "No"]},
    {"label": {"English": "If Yes, Banking Services Provided by Women Entrepreneur", "Hindi": "यदि हाँ, तो महिला उद्यमी द्वारा प्रदान की जाने वाली बैंकिंग सेवाएं", "Telugu": "అవును అయితే, మహిళా వ్యాపారవేత్త అందించిన బ్యాంకింగ్ సేవలు"}, "type": "multiselect", "options": ["Yes-Bank", "MF", "Other (specify)"]},
    {"label": {"English": "If Other Banking Services, specify", "Hindi": "यदि अन्य बैंकिंग सेवाएं, तो निर्दिष्ट करें", "Telugu": "ఇతర బ్యాంకింగ్ సేవలు అయితే, పేర్కొనండి"}, "type": "text", "depends_on": {"If Yes, Banking Services Provided by Women Entrepreneur": "Other (specify)"}},
    {"label": {"English": "Extension services", "Hindi": "विस्तार सेवाएं", "Telugu": "విస్తరణ సేవలు"}, "type": "multiselect", "options": ["Training", "Concentrate Feed Supply", "Mineral Mixture", "AI Services", "Health Camps", "No Services", "Others (specify)"]},
    {"label": {"English": "If Other Extension Services, specify", "Hindi": "यदि अन्य विस्तार सेवाएं, तो निर्दिष्ट करें", "Telugu": "ఇతర విస్తరణ సేవలు అయితే, పేర్కొనండి"}, "type": "text", "depends_on": {"Extension services": "Others (specify)"}},

    # Final Fields
    {"section": "Survey Details"},
    {"label": {"English": "Name of Surveyor", "Hindi": "सर्वेक्षक का नाम", "Telugu": "సర్వేయర్ పేరు"}, "type": "text"},
    {"label": {"English": "Photo / Timestamp", "Hindi": "फोटो / टाइमस्टैम्प", "Telugu": "ఫోటో / టైమ్‌స్టాంప్"}, "type": "text"}, # Consider st.camera_input
    {"label": {"English": "Date of Visit", "Hindi": "यात्रा की तारीख", "Telugu": "సందర్శన తేదీ"}, "type": "date"},
]

# Collect answers
baseline_answers = {}

# Render form UI
st.header(labels["Baseline Survey Questions"])

previous_answers = {}

for idx, q in enumerate(BASELINE_QUESTIONS):
    if "section" in q:
        st.subheader(labels[q["section"]])
        continue

    display_question = True
    if "depends_on" in q:
        dependency_key_english = list(q["depends_on"].keys())[0] # The dependency is always based on the English label
        expected_value = q["depends_on"][dependency_key_english]

        dependent_q_value = previous_answers.get(dependency_key_english)

        if dependent_q_value is not None:
            if isinstance(dependent_q_value, list): # Multi-select dependency
                if expected_value not in dependent_q_value:
                    display_question = False
            else: # Single select, text, number dependency
                if dependent_q_value != expected_value:
                    display_question = False
        else: # If the dependent question hasn't been answered yet (e.g., page load before interaction)
            display_question = False

    label = q['label'].get(lang, q['label']['English'])
    key = f"baseline_q_{idx}_{lang}"

    if display_question:
        if q['type'] == 'text':
            current_value = baseline_answers.get(label, "") # Initialize with empty string
            baseline_answers[label] = st.text_input(label, value=current_value, key=key)
        elif q['type'] == 'number':
            current_value = baseline_answers.get(label, 0.0) # Initialize with 0.0
            baseline_answers[label] = st.number_input(label, min_value=0.0, value=current_value, key=key)
        elif q['type'] == 'select':
            current_value = baseline_answers.get(label, q['options'][0] if q['options'] else None) # Default to first option
            # Find index of current_value to set default for selectbox
            try:
                default_index = q['options'].index(current_value) if current_value in q['options'] else 0
            except ValueError:
                default_index = 0 # Fallback if current_value isn't in options
            baseline_answers[label] = st.selectbox(label, q['options'], index=default_index, key=key)
        elif q['type'] == 'multiselect':
            current_value = baseline_answers.get(label, []) # Initialize with empty list
            baseline_answers[label] = st.multiselect(label, q['options'], default=current_value, key=key)
        elif q['type'] == 'date':
            current_value = baseline_answers.get(label, datetime.date.today()) # Default to today's date
            baseline_answers[label] = st.date_input(label, value=current_value, key=key)

        # Update previous_answers for the *next* conditional question
        previous_answers[q['label']['English']] = baseline_answers[label]
    else:
        # If the question is not displayed, ensure its value is removed from answers
        if label in baseline_answers:
            del baseline_answers[label]
        # Also remove from previous_answers so it doesn't incorrectly trigger other dependencies
        if q['label']['English'] in previous_answers:
            del previous_answers[q['label']['English']]


# --- Survey Submission ---
if st.button(labels["Submit Survey"]):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = os.path.join(SAVE_DIR, f"survey_response_{timestamp}.csv")
    try:
        data_to_save = {k: v for k, v in baseline_answers.items() if v is not None}
        df = pd.DataFrame([data_to_save])
        df.to_csv(file_name, index=False)
        st.success(labels["Survey Saved!"])
    except Exception as e:
        st.error(f"{labels['Error saving survey']}: {e}")

# Display responses in summary
if 'data' not in st.session_state:
    st.session_state.data = {}

# Update session state with current answers, filtered to avoid displaying None values
st.session_state.data.update({k: v for k, v in baseline_answers.items() if v is not None})


with st.expander(labels["Click to Review Baseline Responses"]):
    st.subheader(labels["Baseline Survey Questions"])
    for k, v in st.session_state.data.items():
        st.markdown(f"**{k}**: {v}")


st.divider()
st.header(labels["Admin Real-Time Access"])

# Allowed Emails
ALLOWED_EMAILS = ["shifalis@tns.org", "rmukherjee@tns.org","rsomanchi@tns.org", "mkaushal@tns.org"]
admin_email = st.text_input(labels["Enter your Admin Email to unlock extra features:"])

if admin_email in ALLOWED_EMAILS:
    st.success(labels["Admin access granted! Real-time view enabled."])

    if st.checkbox(labels["View and Download Uploaded Images"]):
        image_files = [f for f in os.listdir(SAVE_DIR) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        if image_files:
            for img_file in image_files:
                img_path = os.path.join(SAVE_DIR, img_file)
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
        files = [f for f in os.listdir(SAVE_DIR) if f.endswith('.csv')]
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
