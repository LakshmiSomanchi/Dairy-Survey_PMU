import streamlit as st
BASELINE_QUESTIONS = [
    # Farmer Profile Section
    {"label": {"English": "Types", "Hindi": "प्रकार", "Marathi": "प्रकार"}, "type": "text"},
    {"label": {"English": "BMC/MCC Name", "Hindi": "बीएमसी/एमसीसी नाम", "Marathi": "बीएमसी/एमसीसी नाव"}, "type": "text"},
    {"label": {"English": "BMC/MCC Code", "Hindi": "बीएमसी/एमसीसी कोड", "Marathi": "बीएमसी/एमसीसी कोड"}, "type": "text"},
    {"label": {"English": "District", "Hindi": "जिला", "Marathi": "जिल्हा"}, "type": "text"},
    {"label": {"English": "Taluka", "Hindi": "तालुका", "Marathi": "तालुका"}, "type": "text"},
    {"label": {"English": "Village", "Hindi": "गांव", "Marathi": "गाव"}, "type": "text"},
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
    {"label": {"English": "Services provided by BMC to farmer", "Hindi": "किसान को बीएमसी द्वारा दी जाने वाली सेवाएं", "Marathi": "शेतकऱ्याला बीएमसीने दिलेल्या सेवा"}, "type": "text"},

    # Farm Details Section
    {"label": {"English": "Number of Cows", "Hindi": "गायों की संख्या", "Marathi": "गायांची संख्या"}, "type": "number"},
    {"label": {"English": "No. of Cattle in Milk", "Hindi": "दूध देणारे जनावरे", "Marathi": "दूध देणाऱ्या जनावरांची संख्या"}, "type": "number"},
    {"label": {"English": "No. of Calves/Heifers", "Hindi": "बछड़े/बछड़ियां", "Marathi": "कालवडे/कालवडी"}, "type": "number"},
    {"label": {"English": "No. of Desi cows", "Hindi": "देसी गायों की संख्या", "Marathi": "देशी गायांची संख्या"}, "type": "number"},
    {"label": {"English": "Milk Production in litres per day-Desi cows", "Hindi": "देसी गायों द्वारा प्रतिदिन दूध उत्पादन (लीटर में)", "Marathi": "देशी गायींकडून दररोज दूध उत्पादन (लिटर मध्ये)"}, "type": "number"},
    {"label": {"English": "No. of Cross breed cows", "Hindi": "क्रॉसब्रीड गायों की संख्या", "Marathi": "क्रॉसब्रीड गायांची संख्या"}, "type": "number"},
    {"label": {"English": "Type of cross breed(HF/Jersey)", "Hindi": "क्रॉसब्रीड प्रकार (HF/जर्सी)", "Marathi": "क्रॉसब्रीड प्रकार (HF/जर्सी)"}, "type": "text"},
    {"label": {"English": "Milk Production in litres per day-Cross breed(HF/Jersey)-2", "Hindi": "क्रॉसब्रीड गायों द्वारा प्रतिदिन दूध उत्पादन (HF/जर्सी)", "Marathi": "क्रॉसब्रीड गायींकडून दररोज दूध उत्पादन (HF/जर्सी)"}, "type": "number"},
    {"label": {"English": "No. of Buffalo", "Hindi": "भैंसों की संख्या", "Marathi": "म्हशींची संख्या"}, "type": "number"},
    {"label": {"English": "Milk Production in liters per day-buffalo", "Hindi": "भैंसों द्वारा प्रतिदिन दूध उत्पादन (लीटर में)", "Marathi": "म्हशींकडून दररोज दूध उत्पादन (लिटर मध्ये)"}, "type": "number"},

    # Remaining questions...
    {"label": {"English": "Preventive health care measures-Annual cycle", "Hindi": "रोकथाम स्वास्थ्य देखभाल उपाय - वार्षिक चक्र", "Marathi": "प्रतिबंधात्मक आरोग्य सेवा उपाय - वार्षिक चक्र"}, "type": "text"},
    {"label": {"English": "Have they previously used Ethno veterinary resources", "Hindi": "क्या उन्होंने पहले एथनो पशु चिकित्सा संसाधनों का उपयोग किया है", "Marathi": "त्यांनी पूर्वी पारंपरिक पशुवैद्यकीय साधने वापरली आहेत का"}, "type": "select", "options": ["Yes", "No"]},
    {"label": {"English": "Women entrepreneur providing banking services", "Hindi": "महिला उद्यमी जो बैंकिंग सेवाएं प्रदान करती हैं", "Marathi": "बँकिंग सेवा पुरवणाऱ्या महिला उद्योजिका"}, "type": "select", "options": ["Yes", "No"]},
    {"label": {"English": "Extension services", "Hindi": "विस्तार सेवाएं", "Marathi": "विस्तार सेवा"}, "type": "text"}
]

# Collect answers
baseline_answers = {}

# Render form UI
st.header("📋 Baseline Survey Questions")
for idx, q in enumerate(BASELINE_QUESTIONS):
    label = q['label'].get(lang, q['label']['English'])
    key = f"baseline_q_{idx}"

if q['type'] == 'text':
    baseline_answers[label] = st.text_input(label, key=key)
elif q['type'] == 'number':
    baseline_answers[label] = st.number_input(label, min_value=0.0, key=key)
elif q['type'] == 'select':
    baseline_answers[label] = st.selectbox(label, q['options'], key=key)
elif q['type'] == 'multiselect':
    baseline_answers[label] = st.multiselect(label, q['options'], key=key)

# Display responses in summary (to integrate into app.py)
if 'data' in globals():
    data.update(baseline_answers)
    with st.expander("🔍 Click to Review Baseline Responses"):
        st.subheader("📋 Baseline Questions")
        for k in baseline_answers:
            st.markdown(f"**{k}**: {data.get(k)}")

st.divider()
st.header("🔐 Admin Real-Time Access")

# Allowed Emails
ALLOWED_EMAILS = ["shifalis@tns.org", "rmukherjee@tns.org","rsomanchi@tns.org", "mkaushal@tns.org"]
admin_email = st.text_input("Enter your Admin Email to unlock extra features:")

if admin_email in ALLOWED_EMAILS:
    st.success("✅ Admin access granted! Real-time view enabled.")

if st.checkbox("🖼️ View and Download Uploaded Images"):
    image_files = [f for f in os.listdir(SAVE_DIR) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    if image_files:
        for img_file in image_files:
            img_path = os.path.join(SAVE_DIR, img_file)
            st.image(img_path, caption=img_file, use_column_width=True)
            with open(img_path, "rb") as img:
                st.download_button(
                    label=f"⬇️ Download {img_file}",
                    data=img,
                    file_name=img_file,
                    mime="image/jpeg" if img_file.lower().endswith('.jpg') else "image/png"
                )
    else:
        st.warning("⚠️ No images found.")
else:
    if admin_email:
        st.error("❌ Not an authorized admin.")

if st.checkbox("📄 View Past Submissions"):
    files = [f for f in os.listdir(SAVE_DIR) if f.endswith('.csv')]
    if files:
        all_data = pd.concat([pd.read_csv(os.path.join(SAVE_DIR, f)) for f in files], ignore_index=True)
        st.dataframe(all_data)
        csv = all_data.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="⬇️ Download All Responses",
            data=csv,
            file_name='all_survey_responses.csv',
            mime='text/csv',
            key='public_csv_download'
        )
    else:
        st.warning("⚠️ No submissions found yet.")
