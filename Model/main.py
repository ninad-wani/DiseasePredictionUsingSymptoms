
from sklearn import metrics
import numpy as np
import pandas as pd
import pickle


from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

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

# TESTING DATA df -------------------------------------------------------------------------------------
df = pd.read_csv("dataset/Training.csv")

df.replace({'label_dis': {'Abscess':0,'Acquired Capillary Haemangioma of Eyelid':1,'Acquired Immuno Deficiency Syndrome':2,'Acute encephalitis syndrome':3,
           'Adult Inclusion Conjunctivitis':4,'Alcohol Abuse and Alcoholism':5,'Alopecia (hair loss)':6,'Alzheimer':7,'Amaurosis Fugax':8,'Amblyopia':9,
           'Amoebiasis':10,'Anaemia':11,'Aniseikonia':12,'Anisometropia':13,'Antepartum hemorrhage (Bleeding in late pregnancy)':14,'Anthrax':15,'Anxiety':16,
           'Appendicitis':17,'Arthritis':18,'Asbestos-related diseases':19,'Aseptic meningitis':20,'Asthma':21,'Astigmatism':22,'Atrophy':23,'Autism':24,'Bad Breath (Halitosis)':25,
           'Bell\'s Palsy':26,'Beriberi':27,'Black Death':28,'Bleeding Gums':29,'Blindness':30,'Botulism':31,'Brain Tumour':32,'Breast Cancer / Carcinoma':33,'Bronchitis':34,
           'Brucellosis':35,'Bubonic plague':36,'Bunion':37,'Burns':38,'Calculi':39,'Campylobacter infection':40,'Cancer':41,'Candidiasis':42,'Carbon monoxide poisoning':43,
           'Carpal Tunnel Syndrome':44,'Cavities':45,'Celiacs disease':46,'Cerebral palsy':47,'Chagas disease':48,'Chalazion':49,'Chickenpox':50,'Chikungunya Fever':51,
           'Childhood Exotropia':52,'Chlamydia':53,'Cholera':54,'Chorea':55,'Chronic fatigue syndrome':56,'Chronic obstructive pulmonary disease (COPD)':57,
           'Cleft Lip and Cleft Palate':58,'Colitis':59,'Colorectal Cancer':60,'Common cold':61,'Condyloma':62,'Congenital anomalies (birth defects)':63,
           'Congestive heart disease':64,'Corneal Abrasion':65,'Coronary Heart Disease':66,'Coronavirus disease 2019 (COVID-19)':67,'Cough':68,
           'Crimean Congo haemorrhagic fever (CCHF)':69,'Dehydration':70,'Dementia':71,'Dengue':72,'Diabetes Mellitus':73,'Diabetic Retinopathy':74,'Diarrhea':75,
           'Diphtheria':76,'Down\'s Syndrome':77,'Dracunculiasis (guinea-worm disease)':78,'Dysentery':79,'Ear infection':80,'Early pregnancy loss':81,'Ebola':82,
           'Eclampsia':83,'Ectopic pregnancy':84,'Eczema':85,'Endometriosis':86,'Epilepsy':87,'Fibroids':88,'Fibromyalgia':89,'Food Poisoning':90,'Frost Bite':91,
           'GERD':92,'Gaming disorder':93,'Gangrene':94,'Gastroenteritis':95,'Genital herpes':96,'Glaucoma':97,'Goitre':98,'Gonorrhea':99,'Guillain Barre syndrome':100,
           'Haemophilia':101,'Hand, Foot and Mouth Disease':102,'Heat-Related Illnesses and Heat waves':103,'Hepatitis':104,'Hepatitis A':105,'Hepatitis B':106,
           'Hepatitis C':107,'Hepatitis D':108,'Hepatitis E':109,'Herpes Simplex':110,'High risk pregnancy':111,'Human papillomavirus':112,'Hypermetropia':113,
           'Hyperthyroidism':114,'Hypothyroid':115,'Hypotonia':116,'Impetigo':117,'Inflammatory Bowel Disease':118,'Influenza':119,'Insomnia':120,'Interstitial cystitis':121,
           'Iritis':122,'Iron Deficiency Anemia':123,'Irritable bowel syndrome':124,'Japanese Encephalitis':125,'Jaundice':126,'Kala-azar/ Leishmaniasis':127,
           'Kaposi Sarcoma':128,'Keratoconjunctivitis Sicca (Dry eye syndrome)':129,'Keratoconus':130,'Kuru':131,'Laryngitis':132,'Lead poisoning':133,'Legionellosis':134,
           'Leprosy':135,'Leptospirosis':136,'Leukemia':137,'Lice':138,'Lung cancer':139,'Lupus erythematosus':140,'Lyme disease':141,'Lymphoma':142,'Mad cow disease':143,'Malaria':144,
           'Marburg fever':145,'Mastitis':146,'Measles':147,'Melanoma':148,'Middle East respiratory syndrome coronavirus':149,'Migraine':150,'Mononucleosis':151,
           'Mouth Breathing':152,'Multiple myeloma':153,'Multiple sclerosis':154,'Mumps':155,'Muscular dystrophy':156,'Myasthenia gravis':157,'Myelitis':158,
           'Myocardial Infarction (Heart Attack)':159,'Myopia':160,'Narcolepsy':161,'Nasal Polyps':162,'Nausea and Vomiting of Pregnancy and  Hyperemesis gravidarum':163,
           'Necrotizing Fasciitis':164,'Neonatal Respiratory Disease Syndrome(NRDS)':165,'Neoplasm':166,'Neuralgia':167,'Nipah virus infection':168,'Obesity':169,
           'Obsessive Compulsive Disorder':170,'Oral Cancer':171,'Orbital Dermoid':172,'Osteoarthritis':173,'Osteomyelitis':174,'Osteoporosis':175,'Paratyphoid fever':176,
           'Parkinson\'s Disease':177,'Pelvic inflammatory disease':178,'Perennial Allergic Conjunctivitis':179,'Pericarditis':180,'Peritonitis':181,'Pinguecula':182,
           'Pneumonia':183,'Poliomyelitis':184,'Polycystic ovary syndrome (PCOS)':185,'Porphyria':186,'Post Menopausal Bleeding':187,'Post-herpetic neuralgia':188,
           'Postpartum depression/ Perinatal depression':189,'Preeclampsia':190,'Premenstrual syndrome':191,'Presbyopia':192,'Preterm birth':193,'Progeria':194,
           'Psoriasis':195,'Puerperal sepsis':196,'Pulmonary embolism':197,'Ques fever':198,'Quinsy':199,'Rabies':200,'Raynaud\'s Phenomenon':201,'Repetitive strain injury':202,
           'Rheumatic fever':203,'Rheumatism':204,'Rickets':205,'Rift Valley fever':206,'Rocky Mountain spotted fever':207,'Rubella':208,'SARS':209,'SIDS':210,'Sarcoidosis':211,
           'Sarcoma':212,'Scabies':213,'Scarlet fever':214,'Schizophrenia':215,'Sciatica':216,'Scrapie':217,'Scrub Typhus':218,'Scurvy':219,'Sepsis':220,
           'Sexually transmitted infections (STIs)':221,'Shaken Baby Syndrome':222,'Shigellosis':223,'Shin splints':224,'Shingles':225,'Sickle-cell anemia':226,'Smallpox':227,
           'Stevens-Johnson syndrome':228,'Stomach ulcers':229,'Strep throat':230,'Stroke':231,'Sub-conjunctival Haemorrhage':232,'Syphilis':233,'Taeniasis':234,
           'Taeniasis/cysticercosis':235,'Tay-Sachs disease':236,'Tennis elbow':237,'Tetanus':238,'Thalassaemia':239,'Tinnitus':240,'Tonsillitis':241,'Toxic shock syndrome':242,
           'Trachoma':243,'Trichinosis':244,'Trichomoniasis':245,'Tuberculosis':246,'Tularemia':247,'Turners Syndrome':248,'Urticaria':249,'Varicose Veins':250,'Vasovagal syncope':251,
           'Vitamin B12 Deficiency':252,'Vitiligo':253,'Warkany syndrome':254,'Warts':255,'Yaws':256,'Yellow Fever':257,'Zika virus disease':258,'lactose intolerance':259,'papilloedema':260}}, inplace=True)

# print(df.head())

X = df[l1]
y = df[["label_dis"]]
y = y.astype('int')
np.ravel(y)

#print(y)

# TRAINING DATA tr --------------------------------------------------------------------------------
tr = pd.read_csv("dataset/Testing.csv")
tr.replace({'label_dis': {'Abscess':0,'Acquired Capillary Haemangioma of Eyelid':1,'Acquired Immuno Deficiency Syndrome':2,'Acute encephalitis syndrome':3,
           'Adult Inclusion Conjunctivitis':4,'Alcohol Abuse and Alcoholism':5,'Alopecia (hair loss)':6,'Alzheimer':7,'Amaurosis Fugax':8,'Amblyopia':9,
           'Amoebiasis':10,'Anaemia':11,'Aniseikonia':12,'Anisometropia':13,'Antepartum hemorrhage (Bleeding in late pregnancy)':14,'Anthrax':15,'Anxiety':16,
           'Appendicitis':17,'Arthritis':18,'Asbestos-related diseases':19,'Aseptic meningitis':20,'Asthma':21,'Astigmatism':22,'Atrophy':23,'Autism':24,'Bad Breath (Halitosis)':25,
           'Bell\'s Palsy':26,'Beriberi':27,'Black Death':28,'Bleeding Gums':29,'Blindness':30,'Botulism':31,'Brain Tumour':32,'Breast Cancer / Carcinoma':33,'Bronchitis':34,
           'Brucellosis':35,'Bubonic plague':36,'Bunion':37,'Burns':38,'Calculi':39,'Campylobacter infection':40,'Cancer':41,'Candidiasis':42,'Carbon monoxide poisoning':43,
           'Carpal Tunnel Syndrome':44,'Cavities':45,'Celiacs disease':46,'Cerebral palsy':47,'Chagas disease':48,'Chalazion':49,'Chickenpox':50,'Chikungunya Fever':51,
           'Childhood Exotropia':52,'Chlamydia':53,'Cholera':54,'Chorea':55,'Chronic fatigue syndrome':56,'Chronic obstructive pulmonary disease (COPD)':57,
           'Cleft Lip and Cleft Palate':58,'Colitis':59,'Colorectal Cancer':60,'Common cold':61,'Condyloma':62,'Congenital anomalies (birth defects)':63,
           'Congestive heart disease':64,'Corneal Abrasion':65,'Coronary Heart Disease':66,'Coronavirus disease 2019 (COVID-19)':67,'Cough':68,
           'Crimean Congo haemorrhagic fever (CCHF)':69,'Dehydration':70,'Dementia':71,'Dengue':72,'Diabetes Mellitus':73,'Diabetic Retinopathy':74,'Diarrhea':75,
           'Diphtheria':76,'Down\'s Syndrome':77,'Dracunculiasis (guinea-worm disease)':78,'Dysentery':79,'Ear infection':80,'Early pregnancy loss':81,'Ebola':82,
           'Eclampsia':83,'Ectopic pregnancy':84,'Eczema':85,'Endometriosis':86,'Epilepsy':87,'Fibroids':88,'Fibromyalgia':89,'Food Poisoning':90,'Frost Bite':91,
           'GERD':92,'Gaming disorder':93,'Gangrene':94,'Gastroenteritis':95,'Genital herpes':96,'Glaucoma':97,'Goitre':98,'Gonorrhea':99,'Guillain Barre syndrome':100,
           'Haemophilia':101,'Hand, Foot and Mouth Disease':102,'Heat-Related Illnesses and Heat waves':103,'Hepatitis':104,'Hepatitis A':105,'Hepatitis B':106,
           'Hepatitis C':107,'Hepatitis D':108,'Hepatitis E':109,'Herpes Simplex':110,'High risk pregnancy':111,'Human papillomavirus':112,'Hypermetropia':113,
           'Hyperthyroidism':114,'Hypothyroid':115,'Hypotonia':116,'Impetigo':117,'Inflammatory Bowel Disease':118,'Influenza':119,'Insomnia':120,'Interstitial cystitis':121,
           'Iritis':122,'Iron Deficiency Anemia':123,'Irritable bowel syndrome':124,'Japanese Encephalitis':125,'Jaundice':126,'Kala-azar/ Leishmaniasis':127,
           'Kaposi Sarcoma':128,'Keratoconjunctivitis Sicca (Dry eye syndrome)':129,'Keratoconus':130,'Kuru':131,'Laryngitis':132,'Lead poisoning':133,'Legionellosis':134,
           'Leprosy':135,'Leptospirosis':136,'Leukemia':137,'Lice':138,'Lung cancer':139,'Lupus erythematosus':140,'Lyme disease':141,'Lymphoma':142,'Mad cow disease':143,'Malaria':144,
           'Marburg fever':145,'Mastitis':146,'Measles':147,'Melanoma':148,'Middle East respiratory syndrome coronavirus':149,'Migraine':150,'Mononucleosis':151,
           'Mouth Breathing':152,'Multiple myeloma':153,'Multiple sclerosis':154,'Mumps':155,'Muscular dystrophy':156,'Myasthenia gravis':157,'Myelitis':158,
           'Myocardial Infarction (Heart Attack)':159,'Myopia':160,'Narcolepsy':161,'Nasal Polyps':162,'Nausea and Vomiting of Pregnancy and  Hyperemesis gravidarum':163,
           'Necrotizing Fasciitis':164,'Neonatal Respiratory Disease Syndrome(NRDS)':165,'Neoplasm':166,'Neuralgia':167,'Nipah virus infection':168,'Obesity':169,
           'Obsessive Compulsive Disorder':170,'Oral Cancer':171,'Orbital Dermoid':172,'Osteoarthritis':173,'Osteomyelitis':174,'Osteoporosis':175,'Paratyphoid fever':176,
           'Parkinson\'s Disease':177,'Pelvic inflammatory disease':178,'Perennial Allergic Conjunctivitis':179,'Pericarditis':180,'Peritonitis':181,'Pinguecula':182,
           'Pneumonia':183,'Poliomyelitis':184,'Polycystic ovary syndrome (PCOS)':185,'Porphyria':186,'Post Menopausal Bleeding':187,'Post-herpetic neuralgia':188,
           'Postpartum depression/ Perinatal depression':189,'Preeclampsia':190,'Premenstrual syndrome':191,'Presbyopia':192,'Preterm birth':193,'Progeria':194,
           'Psoriasis':195,'Puerperal sepsis':196,'Pulmonary embolism':197,'Ques fever':198,'Quinsy':199,'Rabies':200,'Raynaud\'s Phenomenon':201,'Repetitive strain injury':202,
           'Rheumatic fever':203,'Rheumatism':204,'Rickets':205,'Rift Valley fever':206,'Rocky Mountain spotted fever':207,'Rubella':208,'SARS':209,'SIDS':210,'Sarcoidosis':211,
           'Sarcoma':212,'Scabies':213,'Scarlet fever':214,'Schizophrenia':215,'Sciatica':216,'Scrapie':217,'Scrub Typhus':218,'Scurvy':219,'Sepsis':220,
           'Sexually transmitted infections (STIs)':221,'Shaken Baby Syndrome':222,'Shigellosis':223,'Shin splints':224,'Shingles':225,'Sickle-cell anemia':226,'Smallpox':227,
           'Stevens-Johnson syndrome':228,'Stomach ulcers':229,'Strep throat':230,'Stroke':231,'Sub-conjunctival Haemorrhage':232,'Syphilis':233,'Taeniasis':234,
           'Taeniasis/cysticercosis':235,'Tay-Sachs disease':236,'Tennis elbow':237,'Tetanus':238,'Thalassaemia':239,'Tinnitus':240,'Tonsillitis':241,'Toxic shock syndrome':242,
           'Trachoma':243,'Trichinosis':244,'Trichomoniasis':245,'Tuberculosis':246,'Tularemia':247,'Turners Syndrome':248,'Urticaria':249,'Varicose Veins':250,'Vasovagal syncope':251,
           'Vitamin B12 Deficiency':252,'Vitiligo':253,'Warkany syndrome':254,'Warts':255,'Yaws':256,'Yellow Fever':257,'Zika virus disease':258,'lactose intolerance':259,'papilloedema':260}}, inplace=True)

X_test = tr[l1]
y_test = tr[["label_dis"]]
np.ravel(y_test)



# ------------------------------------------------------------------------------------------------------


def DecisionTree():
    from sklearn import tree

    clf3 = tree.DecisionTreeClassifier()  # empty model of the decision tree
    clf3 = clf3.fit(X, y)

    from sklearn.metrics import accuracy_score
    y_pred = clf3.predict(X_test)

    print(accuracy_score(y_test, y_pred)*100)
    print(accuracy_score(y_test, y_pred, normalize=False))

    #pickle.dump(clf3,open('decmodel.pkl','wb'))

    # -----------------------------------------------------

    """psymptoms = [input()]

    for k in range(0, len(l1)):
        # print (k,)
        for z in psymptoms:
            if (z == l1[k]):
                l2[k] = 1

    inputtest = [l2]
    predict = clf3.predict(inputtest)
    predicted = predict[0]

    h = 'no'
    for a in range(0, len(disease)):
        if (predicted == a):
            h = 'yes'
            break

    if (h == 'yes'):
        print(disease[a])
    else:
        print("Not Found")""



    #printing scatter plot of disease predicted vs its symptoms
    #scatterplt(pred4.get())"""
    return

DecisionTree()