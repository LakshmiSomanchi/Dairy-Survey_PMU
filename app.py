# app.py (Heritage Specific Streamlit Dairy Survey)

import streamlit as st
import pandas as pd
import datetime
import os

# Ensure save folder exists
SAVE_DIR = 'survey_responses'
os.makedirs(SAVE_DIR, exist_ok=True)

# Multilingual Translations
dict_translations = {
    'English': {
        'Language': 'Language', 'Farmer Profile': 'Farmer Profile', 'BMC Name': 'BMC Name',
        'BMC/MCC Code': 'BMC/MCC Code', 'Types': 'Type', 'BMC': 'BMC', 'MCC': 'MCC',
        'Farmer Name': 'Farmer Name', 'Farmer Code': 'Farmer Code / Pourer ID', 'Gender': 'Gender',
        'Male': 'Male', 'Female': 'Female', 'Farm Details': 'Farm Details',
        'Number of Cows': 'Number of Cows', 'No. of Cattle in Milk': 'No. of Cattle in Milk',
        'No. of Calves/Heifers': 'No. of Calves/Heifers', 'No. of Desi cows': 'No. of Desi cows',
        'No. of Cross breed cows': 'No. of Cross breed cows', 'No. of Buffalo': 'No. of Buffalo',
        'Milk Production': 'Milk Production (liters/day)', 'Specific Questions': 'Specific Questions',
        'Green Fodder': 'Green Fodder', 'Type of Green Fodder': 'Type of Green Fodder (Multiple Select)',
        'Quantity of Green Fodder': 'Quantity of Green Fodder (Kg/day)',
        'Dry Fodder': 'Dry Fodder', 'Type of Dry Fodder': 'Type of Dry Fodder (Multiple Select)',
        'Quantity of Dry Fodder': 'Quantity of Dry Fodder (Kg/day)',
        'Pellet Feed': 'Pellet Feed', 'Pellet Feed Brand': 'Pellet Feed Brand (Multiple Select)',
        'Quantity of Pellet Feed': 'Quantity of Pellet Feed (Kg/day)',
        'Mineral Mixture': 'Mineral Mixture',
        'Mineral Mixture Brand': 'Mineral Mixture Brand',
        'Quantity of Mineral Mixture': 'Quantity of Mineral Mixture (gm/day)',
        'Silage': 'Silage', 'Source and Price of Silage': 'Source and Price of Silage',
        'Quantity of Silage': 'Quantity of Silage (Kg/day)', 'Source of Water': 'Source of Water (Multiple Select)',
        'Name of Surveyor': 'Name of Surveyor', 'Date of Visit': 'Date of Visit',
        'Submit': 'Submit', 'Yes': 'Yes', 'No': 'No', 'Download CSV': 'Download CSV'
    },
    'Hindi': {  
        'Language': 'भाषा', 'Farmer Profile': 'किसान प्रोफ़ाइल', 'BMC Name': 'वीएलसीसी नाम',
        'BMC/MCC Code': 'एचपीसी/एमसीसी कोड', 'Types': 'प्रकार', 'BMC': 'एचपीसी', 'MCC': 'एमसीसी',
        'Farmer Name': 'किसान का नाम', 'Farmer Code': 'किसान कोड/दूधदाता आईडी', 'Gender': 'लिंग',
        'Male': 'पुरुष', 'Female': 'महिला', 'Farm Details': 'फार्म विवरण',
        'Number of Cows': 'गायों की संख्या', 'No. of Cattle in Milk': 'दूध देने वाले मवेशी',
        'No. of Calves/Heifers': 'बछड़े/बछड़ियां', 'No. of Desi cows': 'देसी गायों की संख्या',
        'No. of Cross breed cows': 'क्रॉसब्रीड गायों की संख्या', 'No. of Buffalo': 'भैंसों की संख्या',
        'Milk Production': 'दूध उत्पादन (लीटर/दिन)', 'Specific Questions': 'विशिष्ट प्रश्न',
        'Green Fodder': 'हरा चारा', 'Type of Green Fodder': 'हरे चारे का प्रकार (एकाधिक चयन)',
        'Quantity of Green Fodder': 'हरे चारे की मात्रा (किलो/दिन)',
        'Dry Fodder': 'सूखा चारा', 'Type of Dry Fodder': 'सूखे चारे का प्रकार (एकाधिक चयन)',
        'Quantity of Dry Fodder': 'सूखे चारे की मात्रा (किलो/दिन)',
        'Pellet Feed': 'पेलेट फ़ीड', 'Pellet Feed Brand': 'पेलेट फ़ीड ब्रांड (एकाधिक चयन)',
        'Quantity of Pellet Feed': 'पेलेट फ़ीड मात्रा (किलो/दिन)',
        'Mineral Mixture': 'खनिज मिश्रण',
        'Mineral Mixture Brand': 'खनिज मिश्रण ब्रांड',
        'Quantity of Mineral Mixture': 'खनिज मिश्रण मात्रा (ग्राम/दिन)',
        'Silage': 'सायलेज', 'Source and Price of Silage': 'सायलेज स्रोत और मूल्य',
        'Quantity of Silage': 'सायलेज मात्रा (किलो/दिन)', 'Source of Water': 'पानी का स्रोत (एकाधिक चयन)',
        'Name of Surveyor': 'सर्वेक्षक का नाम', 'Date of Visit': 'दौरे की तिथि',
        'Submit': 'जमा करें', 'Yes': 'हाँ', 'No': 'नहीं', 'Download CSV': 'CSV डाउनलोड करें'
    },
    'Telugu': { 
        'Language': 'భాష', 'Farmer Profile': 'రైతు వివరాలు', 'BMC Name': 'BMC పేరు',
        'BMC/MCC Code': 'HPC/MCC కోడ్', 'Types': 'రకం', 'BMC': 'హెచ్‌పిసి', 'MCC': 'ఎంసిసి',
        'Farmer Name': 'రైతు పేరు', 'Farmer Code': 'రైతు కోడ్ / పోరర్ ఐడి', 'Gender': 'లింగం',
        'Male': 'పురుషుడు', 'Female': 'స్త్రీ', 'Farm Details': 'పంది వివరాలు',
        'Number of Cows': 'ఆవుల సంఖ్య', 'No. of Cattle in Milk': 'పాలలో ఉన్న పశువులు',
        'No. of Calves/Heifers': 'దూడలు/హెఫర్లు సంఖ్య', 'No. of Desi cows': 'దేశీ ఆవుల సంఖ్య',
        'No. of Cross breed cows': 'క్రాస్‌బ్రీడ్ ఆవుల సంఖ్య', 'No. of Buffalo': 'గేదెల సంఖ్య',
        'Milk Production': 'పాల ఉత్పత్తి (లీటర్లు/రోజు)', 'Specific Questions': 'ప్రత్యేక ప్రశ్నలు',
        'Green Fodder': 'పచ్చి మేత', 'Type of Green Fodder': 'పచ్చి మేత రకం (బహుళ ఎంపిక)',
        'Quantity of Green Fodder': 'పచ్చి మేత పరిమాణం (కిలో/రోజు)',
        'Dry Fodder': 'పొడి మేత', 'Type of Dry Fodder': 'పొడి మేత రకం (బహుళ ఎంపిక)',
        'Quantity of Dry Fodder': 'పొడి మేత పరిమాణం (కిలో/రోజు)',
        'Pellet Feed': 'గుళికల దాణా', 'Pellet Feed Brand': 'గుళికల దాణా బ్రాండ్ (బహుళ ఎంపిక)',
        'Quantity of Pellet Feed': 'గుళికల దాణా పరిమాణం (కిలో/రోజు)',
        'Mineral Mixture': 'ఖనిజ మిశ్రమం',
        'Mineral Mixture Brand': 'ఖనిజ మిశ్రమం బ్రాండ్',
        'Quantity of Mineral Mixture': 'ఖనిజ మిశ్రమం పరిమాణం (గ్రాములు/రోజు)',
        'Silage': 'సైలేజ్', 'Source and Price of Silage': 'సైలేజ్ మూలం మరియు ధర',
        'Quantity of Silage': 'సైలేజ్ పరిమాణం (కిలో/రోజు)', 'Source of Water': 'నీటి మూలం (బహుళ ఎంపిక)',
        'Name of Surveyor': 'సర్వేయర్ పేరు', 'Date of Visit': 'సందర్శన తేదీ',
        'Submit': 'సమర్పించండి', 'Yes': 'అవును', 'No': 'కాదు', 'Download CSV': 'CSV డౌన్‌లోడ్ చేయండి'
    }
}

# Streamlit Page Config
st.set_page_config(page_title="ks 2.0", page_icon="🐄", layout="centered")

# Language Selection
lang = st.selectbox("Language / भाषा / భాష", ("English", "Hindi", "Telugu"))
labels = dict_translations.get(lang, dict_translations['English'])

# Title
st.title(labels['Farmer Profile'])

# ---  Specific Data ---
BMC_NAMES = ["Shree Ganesh Dudh sankalan kendra Sastewadi-5015","Jay Malhar Dudh sankalan kendra, Ghadgemala -5090","Bhairavnath Dudh Sankalan Kendra, Hingangaon-5112","Wageshwari Dudh sankalan va Shitkaran Kendra, Zanzane Saswad-5107","SAYALI DUDH MUNJAWADI-5124",
"Govind Dudh Sankalan Kendra Zanzane Saswad -5450","HANUMAN DUDH BARAD	5115","SHIVSHANKAR DUDH BARAD	5302","Govind Shwetkranti Dudh sankalan kendra - Hol-0008","VAJUBAI DUDH VAJEGOAN	5493","DURGADEVI DUDH SONWADI	5590",
"Gokul Dudh sankalan kendra - Mathachiwadi 	5145","JAY TULJABHAVANI DUDH GIRVI-5404","VIGHNAHARTA DUDH VIDNI	5142","MEGHRAJ DUDH GIRVI	5085","GOVIND MAHILA SHEWATH KRANTI-5435","Sampat Karche Dudh sankalan kendra Somanthali-5092",
"BHAIRAVNATH MANDAVKHADAK COOLER-5565","Bhairavnath Dudh Sankalan, Pinglewasti	5546","Shridatt Dudh Sankalan, Waghwasti	5337","Yash Dudh sankalan kendra, Karkhel	5188","Govind Milk & Milk products MMC Sadashivnagar-1205","Govind Milk and Milk products MCC - Malshiras -1203",
"Govind Dudh sankalan Kendra - Motewadi (Gokulnagar)-1204",
"Joterling Dudh sankalan kendra, Ekshiv	5474","JAY BHAVANI DUDH SAN.KEN.ANBHULEWADI PACHWAD	5022","Bhairavnath Dudh sankalan va Shitkaran Kendra - Devulgaon raje	5445","Jay Hanuman Dudh sankalan va Shitkaran Kendra, Hingani Lingale	5337",
"Shivtej Dudh Sankalan Kendra, Boribel	5300","MAYURESHWAR DAIRY	5150","OM BHAKTI DUDH WAI COW	5460",
"YASHODHAN MILK & MILK PROD. PACWAD	5343","SHRIRAM DUDH SANKALAN & SHIT.BHUINJ	5408","Gomata Dairy Farm	5399","Wangana Dudh sankalan Kendra	5573",
"Govardhan Dudh Sankalan	5144","Shivam Dudh Budh	5505","SUPRIYA MILK	5109","MAULI DUDH SANKALAN KENDRA	5405","MAHALAXMI DUDH MOHI	5490","Bramhachaitanya Milk & Milk Products Pvt. Ltd.	1201",
"SHRI GANESH DUDH SAK VARKUTE MASWAD	5582",
"Shri Datta dudh sankalan kendra	5406","JAGDAMBA DUDH BHATKI	5647","Jyotirling Dudh Sakalan 	5488",
"SUDARSHAN DUDH SANKALAN KEND.MARDI	5413","Ranand MCC	5556","SHRINATH DUDH SANK.KENDRA WAVARHIRE	5301","Shree Datta dudh sankalan kendra 	5347","Shri ram dudh sankalan	5131",
"Govind Milk CC - Vanemala	1211","Shambu Mahadev Dudh sankalan kendra, Phondshiras	5480",
"Shivkrupa Dudh sankalan va Shitkaran Kendra, Shirsatwadi	5381","Hindavi Dudh sankalan va Shitkaran Kendra, Khadaki	5376","Vishnu Narayan Dudh Sankalan Kendra Pirale	5273",
"Rajmudra Dudh Sankalan 	5283","NIRAI DUDH SANKALAN KEND.PANCABIGA	5284","JAY HANUMAN BMC NAIKBOMWADI	5306",
"Chandrabhaga Dudh sankalan kendra	5586","SHRINATH ROKADESHOR DALAWDI BMC	5320","Jitoba Didh Sankalan Kendra, Jinti	5049","JANAI DUDH SANKLAN KENDRA MIRDE	5398",
"Sant BhagwanbabaDudh Sankalan Kendra - Akole-5111","SHREE DATTA SOMANTHALI	5125","Shrinath Mhasoba Dudh Sankalan Karanje	5143"

] 
GREEN_FODDER_OPTIONS = ["Napier", "Maize", "Sorghum"]
DRY_FODDER_OPTIONS = ["Paddy Straw", "Maize Straw", "Ragi Straw", "Ground Nut Crop Residues"]
PELLET_FEED_BRANDS = ["Heritage Milk Rich", "Heritage Milk Joy", "Heritage Power Plus", "Kamadhenu", "Godrej", "Sreeja", "Vallabha-Panchamruth", "Vallabha-Subham Pusti"]
MINERAL_MIXTURE_BRANDS = ["Herita Vit", "Herita Min", "Other (Specify)"]
WATER_SOURCE_OPTIONS = ["Panchayat", "Borewell", "Water Streams"]
SURVEYOR_NAMES = ["Shiva Shankaraiah", "Reddisekhar", "Balakrishna", "Somasekhar", "Mahesh Kumar", "Dr Swaran Raj Nayak", "Ram Prasad", "K Balaji"]
# Form Start
with st.form("survey_form"):
    st.header(labels['Farmer Profile'])
    vlcc_name = st.selectbox(labels['VLCC Name'], VLCC_NAMES)
    hpc_code = st.text_input(labels['HPC/MCC Code'])
    types = st.selectbox(labels['Types'], (labels['HPC'], labels['MCC']))
    farmer_name = st.text_input(labels['Farmer Name'])
    farmer_code = st.text_input(labels['Farmer Code'])
    gender = st.selectbox(labels['Gender'], (labels['Male'], labels['Female']))

    st.header(labels['Farm Details'])
    cows = st.number_input(labels['Number of Cows'], min_value=0)
    cattle_in_milk = st.number_input(labels['No. of Cattle in Milk'], min_value=0)
    calves = st.number_input(labels['No. of Calves/Heifers'], min_value=0)
    desi_cows = st.number_input(labels['No. of Desi cows'], min_value=0)
    crossbreed_cows = st.number_input(labels['No. of Cross breed cows'], min_value=0)
    buffalo = st.number_input(labels['No. of Buffalo'], min_value=0)
    milk_production = st.number_input(labels['Milk Production'], min_value=0.0)

    st.header(labels['Specific Questions'])
    green_fodder = st.selectbox(labels['Green Fodder'], (labels['Yes'], labels['No']))
    green_fodder_types = st.multiselect(labels['Type of Green Fodder'], GREEN_FODDER_OPTIONS)
    green_fodder_qty = st.number_input(labels['Quantity of Green Fodder'], min_value=0.0)
    dry_fodder = st.selectbox(labels['Dry Fodder'], (labels['Yes'], labels['No']))
    dry_fodder_types = st.multiselect(labels['Type of Dry Fodder'], DRY_FODDER_OPTIONS)
    dry_fodder_qty = st.number_input(labels['Quantity of Dry Fodder'], min_value=0.0)

    pellet_feed = st.selectbox(labels['Pellet Feed'], (labels['Yes'], labels['No']))
    pellet_feed_brands = st.multiselect(labels['Pellet Feed Brand'], PELLET_FEED_BRANDS)
    pellet_feed_qty = st.number_input(labels['Quantity of Pellet Feed'], min_value=0.0)

    mineral_mixture = st.selectbox(labels['Mineral Mixture'], (labels['Yes'], labels['No']))
    mineral_brand = st.selectbox(labels['Mineral Mixture Brand'], MINERAL_MIXTURE_BRANDS)
    mineral_qty = st.number_input(labels['Quantity of Mineral Mixture'], min_value=0.0)

    silage = st.selectbox(labels['Silage'], (labels['Yes'], labels['No']))
    silage_source = st.text_input(labels['Source and Price of Silage'])
    silage_qty = st.number_input(labels['Quantity of Silage'], min_value=0.0)

    water_sources = st.multiselect(labels['Source of Water'], WATER_SOURCE_OPTIONS)
    surveyor_name = st.selectbox(labels['Name of Surveyor'], SURVEYOR_NAMES)
    visit_date = st.date_input(labels['Date of Visit'])

    # Photo Upload - placed before submit and uses a unique key
    st.subheader("Upload Farm Photo")
    farm_photo = st.file_uploader("Choose a farm photo (JPG/PNG)", type=["jpg", "jpeg", "png"], key="farm_photo_uploader")

    submit = st.form_submit_button(labels['Submit'])

# Process submission
if submit:
    now = datetime.datetime.now()
    data = {
        'Timestamp': now.isoformat(),
        'Language': lang,
        'VLCC Name': vlcc_name,
        'HPC/MCC Code': hpc_code,
        'Types': types,
        'Farmer Name': farmer_name,
        'Farmer Code': farmer_code,
        'Gender': gender,
        'Number of Cows': cows,
        'No. of Cattle in Milk': cattle_in_milk,
        'No. of Calves/Heifers': calves,
        'No. of Desi cows': desi_cows,
        'No. of Cross breed cows': crossbreed_cows,
        'No. of Buffalo': buffalo,
        'Milk Production (liters/day)': milk_production,
        'Green Fodder': green_fodder,
        'Type of Green Fodder': ", ".join(green_fodder_types),
        'Quantity of Green Fodder (Kg/day)': green_fodder_qty,
        'Dry Fodder': dry_fodder,
        'Type of Dry Fodder': ", ".join(dry_fodder_types),
        'Quantity of Dry Fodder (Kg/day)': dry_fodder_qty,
        'Pellet Feed': pellet_feed,
        'Pellet Feed Brand': ", ".join(pellet_feed_brands),
        'Quantity of Pellet Feed (Kg/day)': pellet_feed_qty,
        'Mineral Mixture': mineral_mixture,
        'Mineral Mixture Brand': mineral_brand,
        'Quantity of Mineral Mixture (gm/day)': mineral_qty,
        'Silage': silage,
        'Source and Price of Silage': silage_source,
        'Quantity of Silage (Kg/day)': silage_qty,
        'Source of Water': ", ".join(water_sources),
        'Surveyor Name': surveyor_name,
        'Date of Visit': visit_date.isoformat()
    }

    if farm_photo is not None:
        photo_path = os.path.join(SAVE_DIR, f"farm_photo_{now.strftime('%Y%m%d_%H%M%S')}_{farm_photo.name}")
        with open(photo_path, "wb") as f:
            f.write(farm_photo.getbuffer())
        st.success("Farm photo uploaded successfully!")
        data['Farm Photo Filename'] = photo_path

    df = pd.DataFrame([data])
    filename = f"survey_{now.strftime('%Y%m%d_%H%M%S')}.csv"
    df.to_csv(os.path.join(SAVE_DIR, filename), index=False, encoding='utf-8')
    st.success("📈 Survey Submitted and Saved!")

    with st.expander("🔍 Click to Review Your Submission"):
        for section, keys in {
            "📄 Farmer Profile": [
                'VLCC Name', 'HPC/MCC Code', 'Types', 'Farmer Name', 'Farmer Code', 'Gender'
            ],
            "🐄 Farm Details": [
                'Number of Cows', 'No. of Cattle in Milk', 'No. of Calves/Heifers',
                'No. of Desi cows', 'No. of Cross breed cows', 'No. of Buffalo', 'Milk Production (liters/day)'
            ],
            "🌿 Feed Details": [
                'Green Fodder', 'Type of Green Fodder', 'Quantity of Green Fodder (Kg/day)',
                'Dry Fodder', 'Type of Dry Fodder', 'Quantity of Dry Fodder (Kg/day)',
                'Pellet Feed', 'Pellet Feed Brand', 'Quantity of Pellet Feed (Kg/day)',
                'Mineral Mixture', 'Mineral Mixture Brand', 'Quantity of Mineral Mixture (gm/day)',
                'Silage', 'Source and Price of Silage', 'Quantity of Silage (Kg/day)'
            ],
            "😀 Water & Survey": [
                'Source of Water', 'Surveyor Name', 'Date of Visit', 'Language'
            ]
        }.items():
            st.subheader(section)
            for k in keys:
                st.markdown(f"**{k}**: {data.get(k)}")
st.divider()
st.header("🔐 Admin Real-Time Access")

# Allowed Emails
ALLOWED_EMAILS = ["shifalis@tns.org", "rmukherjee@tns.org","rsomanchi@tns.org", "mkaushal@tns.org"]
admin_email = st.text_input("Enter your Admin Email to unlock extra features:")

if admin_email in ALLOWED_EMAILS:
    st.success("✅ Admin access granted! Real-time view enabled.")
    # Add image access for admin
if st.checkbox("🖼️ View and Download Uploaded Images"):
    # List all image files in the SAVE_DIR folder
    image_files = [f for f in os.listdir(SAVE_DIR) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    if image_files:
        for img_file in image_files:
            img_path = os.path.join(SAVE_DIR, img_file)
            
            # Display image
            st.image(img_path, caption=img_file, use_column_width=True)
            
            # Provide download button for the image
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
