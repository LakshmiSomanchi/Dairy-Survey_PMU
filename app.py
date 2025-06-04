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
# Define your translations here. You had dict_translations undefined.
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
        "Preventive health care measures-Annual cycle": "Preventive health care measures-Annual cycle",
        "Have they previously used Ethno veterinary resources": "Have they previously used Ethno veterinary resources",
        "Women entrepreneur providing banking services": "Women entrepreneur providing banking services",
        "Extension services": "Extension services",
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
        "Preventive health care measures-Annual cycle": "रोकथाम स्वास्थ्य देखभाल उपाय - वार्षिक चक्र",
        "Have they previously used Ethno veterinary resources": "क्या उन्होंने पहले एथनो पशु चिकित्सा संसाधनों का उपयोग किया है",
        "Women entrepreneur providing banking services": "महिला उद्यमी जो बैंकिंग सेवाएं प्रदान करती हैं",
        "Extension services": "विस्तार सेवाएं",
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
        "Preventive health care measures-Annual cycle": "నివారణ ఆరోగ్య సంరక్షణ చర్యలు - వార్షిక చక్రం",
        "Have they previously used Ethno veterinary resources": "వారు గతంలో ఎథ్నో వెటర్నరీ వనరులను ఉపయోగించారా",
        "Women entrepreneur providing banking services": "బ్యాంకింగ్ సేవలను అందించే మహిళా వ్యాపారవేత్త",
        "Extension services": "విస్తరణ సేవలు",
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

# Corrected BASELINE_QUESTIONS to use 'English' key for labels where Marathi is present
# This ensures consistency with your translation dictionary structure
BASELINE_QUESTIONS = [
    # Farmer Profile Section
    {"label": {"English": "Types", "Hindi": "प्रकार", "Telugu": "రకాలు"}, "type": "text"},
    {"label": {"English": "BMC/MCC Name", "Hindi": "बीएमसी/एमसीसी नाम", "Telugu": "BMC/MCC పేరు"}, "type": "text"},
    {"label": {"English": "BMC/MCC Code", "Hindi": "बीएमसी/एमसीसी कोड", "Telugu": "BMC/MCC కోడ్"}, "type": "text"},
    {"label": {"English": "District", "Hindi": "जिला", "Telugu": "జిల్లా"}, "type": "text"},
    {"label": {"English": "Taluka", "Hindi": "तालुका", "Telugu": "తాలూకా"}, "type": "text"},
    {"label": {"English": "Village", "Hindi": "गांव", "Telugu": "గ్రామం"}, "type": "text"},
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
    {"label": {"English": "Services provided by BMC to farmer", "Hindi": "किसान को बीएमसी द्वारा दी जाने वाली सेवाएं", "Telugu": "రైతుకు BMC అందించే సేవలు"}, "type": "text"},

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

    # Remaining questions...
    {"label": {"English": "Preventive health care measures-Annual cycle", "Hindi": "रोकथाम स्वास्थ्य देखभाल उपाय - वार्षिक चक्र", "Telugu": "నివారణ ఆరోగ్య సంరక్షణ చర్యలు - వార్షిక చక్రం"}, "type": "text"},
    {"label": {"English": "Have they previously used Ethno veterinary resources", "Hindi": "क्या उन्होंने पहले एथनो पशु चिकित्सा संसाधनों का उपयोग किया है", "Telugu": "వారు గతంలో ఎథ్నో వెటర్నరీ వనరులను ఉపయోగించారా"}, "type": "select", "options": ["Yes", "No"]},
    {"label": {"English": "Women entrepreneur providing banking services", "Hindi": "महिला उद्यमी जो बैंकिंग सेवाएं प्रदान करती हैं", "Telugu": "బ్యాంకింగ్ సేవలను అందించే మహిళా వ్యాపారవేత్త"}, "type": "select", "options": ["Yes", "No"]},
    {"label": {"English": "Extension services", "Hindi": "विस्तार सेवाएं", "Telugu": "విస్తరణ సేవలు"}, "type": "text"}
]

# Initialize baseline_answers to store survey data
baseline_answers = {}

# Render form UI
st.header(labels["Baseline Survey Questions"])
for idx, q in enumerate(BASELINE_QUESTIONS):
    # Get the label for the current language, fallback to English if not found
    label = q['label'].get(lang, q['label']['English'])
    key = f"baseline_q_{idx}_{lang}" # Added lang to key for uniqueness across language changes

    # Corrected indentation: this block must be inside the for loop
    if q['type'] == 'text':
        baseline_answers[label] = st.text_input(label, key=key)
    elif q['type'] == 'number':
        baseline_answers[label] = st.number_input(label, min_value=0.0, key=key)
    elif q['type'] == 'select':
        baseline_answers[label] = st.selectbox(label, q['options'], key=key)
    elif q['type'] == 'multiselect':
        baseline_answers[label] = st.multiselect(label, q['options'], key=key)

# --- Survey Submission ---
# Add a submit button to save the survey data
if st.button(labels["Submit Survey"]):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = os.path.join(SAVE_DIR, f"survey_response_{timestamp}.csv")
    try:
        # Convert baseline_answers to a DataFrame and save
        df = pd.DataFrame([baseline_answers])
        df.to_csv(file_name, index=False)
        st.success(labels["Survey Saved!"])
    except Exception as e:
        st.error(f"{labels['Error saving survey']}: {e}")

# Display responses in summary
# Initialize st.session_state.data if it doesn't exist
if 'data' not in st.session_state:
    st.session_state.data = {}

# Update st.session_state.data with current baseline_answers
st.session_state.data.update(baseline_answers)

with st.expander(labels["Click to Review Baseline Responses"]):
    st.subheader(labels["Baseline Survey Questions"])
    for k, v in st.session_state.data.items(): # Iterate over items to get both key and value
        st.markdown(f"**{k}**: {v}")

st.divider()
st.header(labels["Admin Real-Time Access"])

# Allowed Emails
ALLOWED_EMAILS = ["shifalis@tns.org", "rmukherjee@tns.org","rsomanchi@tns.org", "mkaushal@tns.org"]
admin_email = st.text_input(labels["Enter your Admin Email to unlock extra features:"])

if admin_email in ALLOWED_EMAILS:
    st.success(labels["Admin access granted! Real-time view enabled."])

    # Move admin-specific features inside this block
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
                key='admin_csv_download' # Changed key for clarity
            )
        else:
            st.warning(labels["No submissions found yet."])
else:
    if admin_email: # Only show error if an email was actually entered
        st.error(labels["Not an authorized admin."])
