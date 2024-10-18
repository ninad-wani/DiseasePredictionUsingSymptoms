import sys

from flask import Flask, request
import pickle
import pandas as pd
import main

l1 = ['abdominal cramp','abdominal distention','abnormal behavior','abnormal bleeding','abnormal sensation','abnormally frequent',
      'abscess','aching','acne','acquiring drinking alcohol taking lot time','affected part turning white','anemia','anxiety','arm',
      'attack pain','back','bacterial infection','bad breath','bad smelling thin vaginal discharge','bad smelling vaginal discharge',
      'barky cough','belching','better sitting worse lying','birth baby younger week gestational age','bleeding gum','bleeding skin',
      'blindness','blindness one eye','blister sunlight','bloating','blood stool','blood urine','bloody diarrhea','blue',
      'bluish skin coloration','blurred vision','blurry vision','body tremor','bone pain','bowed leg','breakdown skeletal muscle',
      'breathing problem','bruising','burning','burning redness eye','burning stabbing pain','burning urination','certain thought repeatedly',
      'change bowel movement','change breast shape','change color','change hair','change reflex','change skin color red black',
      'change sleeping eating pattern','change taste','change voice','characteristic facial feature','characteristic rash','chest discomfort',
      'chest pain','chest tightness','chill','chronic cough','chronic pain bladder','clenched fist overlapping finger','close object appear blurry',
      'clumsy','cm lump skin','cold sweat','coma','confused thinking','confusion','constipation','coolness','coordination','cough bloody mucus',
      'cough sputum production','coughing','coughing blood','coughing including coughing blood','coughing mucus','crawl','cry episode',
      'dark urine','darker','daytime sleepiness','death child le one year age','decreased ability feel pain','decreased ability see',
      'decreased ability think','decreased ability think remember','decreased ability turn','decreased appetite','decreased motivation',
      'decreased range motion','decreased taste','decreased vision','dehydration','delayed physical growth','delirium','delusion','dementia',
      'depending subtype abdominal pain','depends organ involved','depressed mood','depression','dermatitis herpetiformis',
      'developmental disability','diarrhea','diarrhea may bloody','diarrhea mixed blood','diarrhoea','difficulty breathing',
      'difficulty cutting','difficulty eating','difficulty getting pregnant','difficulty remembering recent event','difficulty swallowing',
      'difficulty walking','dimpling skin','discharge penis','disorientation','distant object appear blurry','distorted blurred vision distance',
      'dizziness','double vision','drinking large amount alcohol long period','drooping eyelid','dry cough','dry damp skin','dry eye',
      'dry mouth','ear pain','easy prolonged bleeding','emotional problem','enlarged lymph node neck','enlarged spleen','enlarged thyroid',
      'enlargement thyroid','enlargement tonsil','episode severe','erythema marginatum','excess hair','excessive amount uterine bleeding',
      'excessive daytime sleepiness','excessive salivation','expanding area redness site tick bite','extreme sadness','extremity weakness',
      'eye pain','eye strain','eyestrain','fast heart rate','fast heartbeat','fatigue','fear water','feel need check thing repeatedly',
      'feeling cold','feeling faint upon standing','feeling generally unwell','feeling like passing','feeling need urinate right away',
      'feeling tired','feeling tired time','fever','firm','flat discolored spot bump may blister','flu like illness','flu like symptom',
      'fluid filled blister scab','fluid nipple','frequent infection','frequent urination','fullness','gas','gradual loss coordination',
      'growth delay','gum disease','hair loss','half ring finger','hallucination','hallucination usually hearing voice','hard swelling skin',
      'hard time reading small print','headache','hearing loss','hearing sound external sound present','heartburn','heat intolerance',
      'heavy period','high blood pressure','high body temperature','hoarse voice','hold reading material farther away','impaired communication',
      'inability child','inability move facial muscle one side','inability move feel one side body','increased breath rate',
      'increased breathing rate','increased fat','increased heart rate','increased hunger','increased risk broken bone',
      'increased risk infection','increased thirst','increasing weakening','index','infertility','inflamed eye','insomnia',
      'intellectual disability','involuntary muscle movement','involuntary sleep episode','irregular edge','irregular menstrual period',
      'irregular menstruation','irritability','irritation','itchiness','itching','itching genital area','itching result trouble sleeping',
      'itchy','itchy blister','itchy bump','itchy ear','jaundice','jaw','jerky body movement','joint bone pain','joint swelling',
      'large amount watery diarrhea','large forehead','large lymph node','large lymph node around neck','leg swelling','light sensitivity',
      'little pain','localized breast pain redness','long term fatigue','loose frequent bowel movement','loose teeth','loss appetite',
      'loss consciousness may sweating','loss hair part head body','loss lot blood childbirth','loss smell','loss vision one side',
      'low blood pressure','low energy','low red blood cell','lower abdominal pain','lump breast','lump bump neck','maculopapular rash',
      'malabsorption','may symptom','memory problem','mental ability','mental change','mid dilated pupil','middle finger',
      'mild moderate intellectual disability','minimal','missed period','mole increasing size','mood change','mood swing','mouth sore',
      'mouth ulcer','multiple painful joint','muscle ache difficulty breathing','muscle cramp','muscle joint pain','muscle spasm',
      'muscle weakness','muscle weakness beginning foot hand','muscle weakness resulting inability move','muscular pain','myalgia',
      'nausea','nausea vomiting','nausea vomiting weight loss dehydration occur','nearly undetectable spell','nearsightedness','neck',
      'neck stiffness','needing urinate often','newly inverted nipple','non itchy skin ulcer','non painful cyst middle eyelid',
      'nonaligned eye','none non specific','numbness','object different size eye','one eye myopia eye hyperopia',
      'opening upper lip may extend nose palate','others','overlying redness','pain along inside edge shinbone','pain area','pain around ear',
      'pain doesnt go shingle','pain going leg lower back','pain sex','pain specific bone','painful','painful blister lower leg',
      'painful heavy period','painful joint base big toe','painful rash occurring stripe','painful skin','painful swelling parotid gland',
      'painful swollen joint','painful tender outer part elbow','painless','painless lump','pale color','pale skin','pallor','paralysis',
      'patch thick','patch white skin','perform certain routine repeatedly','period vigorous shaking',
      'persistent rough white red patch mouth lasting longer week','photophobia','physical disability','pimple like rash','pinkish',
      'playing video game extremely long period time','poor ability tolerate cold','poor appetite','poor coordination','poor tolerance heat',
      'post nasal drip','problem language','problem mood','problem understanding speaking','problem vision','profuse sweating',
      'progressive muscle weakness','prolonged','prolonged cough','prominent','protein urine','psychosis','pulsing pain',
      'purple colored skin affected area','purple colored skin lesion','raised','raised red blue lesion','random outburst laughter',
      'rapid breathing','recurring episode wheezing','red','red eye','red purple darker skin','red rash','red scaly patch skin breast',
      'red skin','red spot white eye','red without blister','reddish eye','redness','redness eye','repetitive behavior','restricted interest',
      'right lower abdominal pain','rigidity','ringing ear heartbeat','rough skin growth','runny nose','scaly patch skin','scratchiness',
      'seizure','sensitivity smell','sensitivity sound','severe intellectual disability','severe pain','severe pain lower back abdomen',
      'shakiness','shaking','sharp chest pain','shivering','shock like pain one side face last second minute','short height','short stature',
      'shortness breath','sit','skin blister','skin breakdown','skin lesion generally pink color project outward','skin peeling',
      'sleep problem','sleeping problem','slowness movement','small','small blister break open form painful ulcer',
      'small blister surrounding swelling','small face','small head','small jaw','sneezing','social withdrawal','sometimes symptom',
      'sore arm leg','sore throat','sore wrist','stiff muscle','stiff neck','stiffness','stomach pain','stroke','stuffy itchy nose',
      'stunted growth','sudden','sudden loss muscle strength','sweat','swell pain near tumor','swelling','swelling abdomen',
      'swelling around eye','swelling hand foot','swollen','swollen hand foot','swollen lymph node','taste acid',
      'temporary fleeting vision one eye','tender breast','testicular pain','tingling','tingling hand foot','tingling thumb','tiredness',
      'tooth loss','tremor','triangular tissue growth cornea','trouble breathing nose','trouble coordination','trouble opening mouth',
      'trouble seeing','trouble sensation','trouble sleeping','trouble social interaction','trouble speaking','trouble swallowing',
      'trouble talking','trouble walking','typically none','ulcer','ulcer around genitals','ulceration','unable move','unexplained weight loss',
      'unintended weight loss','unpleasant smell present breath','upper abdominal pain','usage resulting problem','vaginal bleeding',
      'vaginal bleeding without pain','vaginal discharge','variable','vary depending part brain involved','varying degree muscle weakness',
      'velvety skin','vision loss','vomiting','warm','wart','watery eye','weak grip','weak muscle','weakness limb','weakness numbness affected leg',
      'webbed neck','weight gain','wet','wheezing','white patch vaginal discharge','widespread pain','withdrawal occurring stopping',
      'worrying','yellow skin','yellowish coloration skin white eye','yellowish skin','yellowish skin crust']

disease = ['Abscess','Acquired Capillary Haemangioma of Eyelid','Acquired Immuno Deficiency Syndrome','Acute encephalitis syndrome',
           'Adult Inclusion Conjunctivitis','Alcohol Abuse and Alcoholism','Alopecia (hair loss)','Alzheimer','Amaurosis Fugax','Amblyopia',
           'Amoebiasis','Anaemia','Aniseikonia','Anisometropia','Antepartum hemorrhage (Bleeding in late pregnancy)','Anthrax','Anxiety',
           'Appendicitis','Arthritis','Asbestos-related diseases','Aseptic meningitis','Asthma','Astigmatism','Atrophy','Autism','Bad Breath (Halitosis)',
           'Bell\'s Palsy','Beriberi','Black Death','Bleeding Gums','Blindness','Botulism','Brain Tumour','Breast Cancer / Carcinoma','Bronchitis',
           'Brucellosis','Bubonic plague','Bunion','Burns','Calculi','Campylobacter infection','Cancer','Candidiasis','Carbon monoxide poisoning',
           'Carpal Tunnel Syndrome','Cavities','Celiacs disease','Cerebral palsy','Chagas disease','Chalazion','Chickenpox','Chikungunya Fever',
           'Childhood Exotropia','Chlamydia','Cholera','Chorea','Chronic fatigue syndrome','Chronic obstructive pulmonary disease (COPD)',
           'Cleft Lip and Cleft Palate','Colitis','Colorectal Cancer','Common cold','Condyloma','Congenital anomalies (birth defects)',
           'Congestive heart disease','Corneal Abrasion','Coronary Heart Disease','Coronavirus disease 2019 (COVID-19)','Cough',
           'Crimean Congo haemorrhagic fever (CCHF)','Dehydration','Dementia','Dengue','Diabetes Mellitus','Diabetic Retinopathy','Diarrhea',
           'Diphtheria','Down\'s Syndrome','Dracunculiasis (guinea-worm disease)','Dysentery','Ear infection','Early pregnancy loss','Ebola',
           'Eclampsia','Ectopic pregnancy','Eczema','Endometriosis','Epilepsy','Fibroids','Fibromyalgia','Food Poisoning','Frost Bite',
           'GERD','Gaming disorder','Gangrene','Gastroenteritis','Genital herpes','Glaucoma','Goitre','Gonorrhea','Guillain Barre syndrome',
           'Haemophilia','Hand, Foot and Mouth Disease','Heat-Related Illnesses and Heat waves','Hepatitis','Hepatitis A','Hepatitis B',
           'Hepatitis C','Hepatitis D','Hepatitis E','Herpes Simplex','High risk pregnancy','Human papillomavirus','Hypermetropia',
           'Hyperthyroidism','Hypothyroid','Hypotonia','Impetigo','Inflammatory Bowel Disease','Influenza','Insomnia','Interstitial cystitis',
           'Iritis','Iron Deficiency Anemia','Irritable bowel syndrome','Japanese Encephalitis','Jaundice','Kala-azar/ Leishmaniasis',
           'Kaposi Sarcoma','Keratoconjunctivitis Sicca (Dry eye syndrome)','Keratoconus','Kuru','Laryngitis','Lead poisoning','Legionellosis',
           'Leprosy','Leptospirosis','Leukemia','Lice','Lung cancer','Lupus erythematosus','Lyme disease','Lymphoma','Mad cow disease','Malaria',
           'Marburg fever','Mastitis','Measles','Melanoma','Middle East respiratory syndrome coronavirus','Migraine','Mononucleosis',
           'Mouth Breathing','Multiple myeloma','Multiple sclerosis','Mumps','Muscular dystrophy','Myasthenia gravis','Myelitis',
           'Myocardial Infarction (Heart Attack)','Myopia','Narcolepsy','Nasal Polyps','Nausea and Vomiting of Pregnancy and  Hyperemesis gravidarum',
           'Necrotizing Fasciitis','Neonatal Respiratory Disease Syndrome(NRDS)','Neoplasm','Neuralgia','Nipah virus infection','Obesity',
           'Obsessive Compulsive Disorder','Oral Cancer','Orbital Dermoid','Osteoarthritis','Osteomyelitis','Osteoporosis','Paratyphoid fever',
           'Parkinson\'s Disease','Pelvic inflammatory disease','Perennial Allergic Conjunctivitis','Pericarditis','Peritonitis','Pinguecula',
           'Pneumonia','Poliomyelitis','Polycystic ovary syndrome (PCOS)','Porphyria','Post Menopausal Bleeding','Post-herpetic neuralgia',
           'Postpartum depression/ Perinatal depression','Preeclampsia','Premenstrual syndrome','Presbyopia','Preterm birth','Progeria',
           'Psoriasis','Puerperal sepsis','Pulmonary embolism','Ques fever','Quinsy','Rabies','Raynaud\'s Phenomenon','Repetitive strain injury',
           'Rheumatic fever','Rheumatism','Rickets','Rift Valley fever','Rocky Mountain spotted fever','Rubella','SARS','SIDS','Sarcoidosis',
           'Sarcoma','Scabies','Scarlet fever','Schizophrenia','Sciatica','Scrapie','Scrub Typhus','Scurvy','Sepsis',
           'Sexually transmitted infections (STIs)','Shaken Baby Syndrome','Shigellosis','Shin splints','Shingles','Sickle-cell anemia','Smallpox',
           'Stevens-Johnson syndrome','Stomach ulcers','Strep throat','Stroke','Sub-conjunctival Haemorrhage','Syphilis','Taeniasis',
           'Taeniasis/cysticercosis','Tay-Sachs disease','Tennis elbow','Tetanus','Thalassaemia','Tinnitus','Tonsillitis','Toxic shock syndrome',
           'Trachoma','Trichinosis','Trichomoniasis','Tuberculosis','Tularemia','Turners Syndrome','Urticaria','Varicose Veins','Vasovagal syncope',
           'Vitamin B12 Deficiency','Vitiligo','Warkany syndrome','Warts','Yaws','Yellow Fever','Zika virus disease','lactose intolerance','papilloedema']

l2 = []
for x in range(0, len(l1)):
    l2.append(0)


model = pickle.load(open('decmodel.pkl','rb'))
app = Flask(__name__)

@app.route('/pred',methods=["POST","GET"])
def pred():
    value=request.form['symptoms']
    li = value.split(',')
    #psymptoms = li

    for k in range(0, len(l1)):
        # print (k,)
        for z in li:
            if (z == l1[k]):
                l2[k] = 1

    inputtest = [l2]

    predict = model.predict(inputtest)
    predicted = predict[0]

    h = 'no'
    for a in range(0, len(disease)):
        if (predicted == a):
            h = 'yes'
            break

    if (h == 'yes'):
        result = disease[a]
    else:
        result = "Not found"

    return (result)

if __name__=="__main__":
    app.run()
