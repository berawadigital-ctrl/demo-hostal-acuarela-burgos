# Contenido de la demo Hostal Acuarela (Burgos) (es/en/fr/de). Hechos de hostalacuarela.com leidos el 30/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma; sin valoraciones.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.','de':' Die Bilder sind Illustrationen und zeigen nicht die tatsächlichen Zimmer.'}
H={'es':['Individual, doble y familiar','Estudio-Suite'],'en':['Single, double and family','Studio-Suite'],'fr':['Individuelle, double et familiale','Studio-Suite'],'de':['Einzel-, Doppel- und Familienzimmer','Studio-Suite']}
RD={
'es':['29 habitaciones exteriores decoradas con cuadros cabeceros de autor de la serie Mantón, de Ana Sanz. Todas con ducha hidromasaje, hilo musical, ordenador portátil y WiFi gratuito de alta velocidad.','Ático de lujo con terraza privada, totalmente equipado.'],
'en':['29 exterior rooms decorated with paintings and headboards from the Mantón series by Ana Sanz. All with hydro-massage shower, piped music, laptop and free high-speed WiFi.','Luxury penthouse with private terrace, fully equipped.'],
'fr':['29 chambres extérieures décorées de tableaux-têtes de lit de la série Mantón, d\'Ana Sanz. Toutes avec douche hydromassage, musique d\'ambiance, ordinateur portable et WiFi haut débit gratuit.','Penthouse de luxe avec terrasse privée, entièrement équipé.'],
'de':['29 Außenzimmer mit Kopfteil-Bildern der Serie Mantón von Ana Sanz. Alle mit Hydromassage-Dusche, Musikanlage, Laptop und kostenlosem Highspeed-WLAN.','Luxus-Penthouse mit privater Terrasse, voll ausgestattet.']}
ART={
'hero':('waves',9501,['#ecf0f2','#f6f3ec','#2d4f73','#1e3550','#101f30']),
'intro':('arches',9502,['#eef0ec','#e6b37e','#2d4f73','#1e3550','#101f30']),
'r1':('skyline',9511,['#1e3550','#e5a86b','#f4d6a6','#7a3e5a','#633149','#401f30']),
'r2':('hills',9512,['#eceff2','#f1e6d0','#e3b273','#9fb2c4','#6f88a0','#4a627a']),
'g1':('waves',9521,['#2d4f73','#ecbf88','#f6deb8','#3f6690','#2d4f73','#1a3048']),
'g2':('columns',9522,['#edeae2','#f7f4ee','#7a3e5a','#1e3550','#101f30']),
'g3':('arches',9523,['#ecdfca','#dcab76','#7a3e5a','#1e3550','#101f30']),
'g4':('skyline',9524,['#1e3550','#e0a064','#f2cf9c','#6e3a55','#5a2f46','#3a1d2d'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hostal Acuarela · Hostal de diseño en el centro de Burgos',see_rooms='Ver las habitaciones',hero_k='Burgos · Centro',hero_t='Reinventamos el concepto de hostal',hero_s='Hostal de diseño en el corazón comercial de Burgos, muy próximo al casco histórico.',
 intro_t='Diseño emocional',intro_p1='29 habitaciones exteriores y un Estudio-Suite con un interiorismo delicado y atrevido, todas con ducha hidromasaje e hilo musical.',
 intro_p2='En la tercera planta, una terraza acristalada con zona común gratuita: mesas, sillas, microondas, tostador, frigorífico y unas preciosas vistas.',
 stats=['29 habitaciones + Estudio-Suite','Ducha hidromasaje','WiFi gratuito','Se admiten mascotas'],nav_rooms='Habitaciones',rooms_t='Nuestras habitaciones',rooms_s='Individual, doble, familiar y un ático con terraza privada.',
 svcs=['Terraza acristalada en la tercera planta','Zona común con microondas y frigorífico','Ordenador portátil en la habitación','Máquina de vending','Posibilidad de parking en Virgen del Manzano','Se admiten animales de compañía'],
 around_s='En el corazón comercial de Burgos y muy próximo al casco histórico.',
 loc_p='Calle Guardia Civil 7 · Burgos, en el corazón comercial de la ciudad.',
 chips=['¿Qué habitaciones tenéis?','¿Cuánto cuesta una habitación?','¿A qué hora es el check-in?','¿Puedo ir con mi perro?']),
'en':dict(title='Hostal Acuarela · Design hostel in the centre of Burgos',see_rooms='See the rooms',hero_k='Burgos · Centre',hero_t='Innovating the hostel concept',hero_s='A design hostel in the commercial heart of Burgos, very close to the historic centre.',
 intro_t='Emotional design',intro_p1='29 exterior rooms and a Studio-Suite with delicate, daring interior design, all with hydro-massage shower and piped music.',
 intro_p2='On the third floor, a glazed terrace with a free common area: tables, chairs, microwave, toaster, fridge and beautiful views.',
 stats=['29 rooms + Studio-Suite','Hydro-massage shower','Free WiFi','Pets welcome'],nav_rooms='Rooms',rooms_t='Our rooms',rooms_s='Single, double, family and a penthouse with private terrace.',
 svcs=['Glazed terrace on the third floor','Common area with microwave and fridge','Laptop in the room','Vending machine','Parking possible at Virgen del Manzano','Pets welcome'],
 around_s='In the commercial heart of Burgos and very close to the historic centre.',
 loc_p='Calle Guardia Civil 7 · Burgos, in the commercial heart of the city.',
 chips=['Which rooms do you have?','How much is a room?','What time is check-in?','Can I bring my dog?']),
'fr':dict(title='Hostal Acuarela · Hostal design au centre de Burgos',see_rooms='Voir les chambres',hero_k='Burgos · Centre',hero_t='Nous réinventons le concept de hostal',hero_s='Un hostal design au cœur commerçant de Burgos, tout près du centre historique.',
 intro_t='Design émotionnel',intro_p1='29 chambres extérieures et un Studio-Suite au design intérieur délicat et audacieux, toutes avec douche hydromassage et musique d\'ambiance.',
 intro_p2='Au troisième étage, une terrasse vitrée avec espace commun gratuit : tables, chaises, micro-ondes, grille-pain, réfrigérateur et une belle vue.',
 stats=['29 chambres + Studio-Suite','Douche hydromassage','WiFi gratuit','Animaux acceptés'],nav_rooms='Chambres',rooms_t='Nos chambres',rooms_s='Individuelle, double, familiale et un penthouse avec terrasse privée.',
 svcs=['Terrasse vitrée au troisième étage','Espace commun avec micro-ondes et réfrigérateur','Ordinateur portable en chambre','Distributeur automatique','Parking possible à Virgen del Manzano','Animaux de compagnie acceptés'],
 around_s='Au cœur commerçant de Burgos et tout près du centre historique.',
 loc_p='Calle Guardia Civil 7 · Burgos, au cœur commerçant de la ville.',
 chips=['Quelles chambres avez-vous ?','Combien coûte une chambre ?',"À quelle heure est l'arrivée ?",'Puis-je venir avec mon chien ?']),
'de':dict(title='Hostal Acuarela · Design-Hostal im Zentrum von Burgos',see_rooms='Zimmer ansehen',hero_k='Burgos · Zentrum',hero_t='Wir erfinden das Hostal neu',hero_s='Ein Design-Hostal im Geschäftszentrum von Burgos, ganz nah an der Altstadt.',
 intro_t='Emotionales Design',intro_p1='29 Außenzimmer und eine Studio-Suite mit feinem, mutigem Interieur, alle mit Hydromassage-Dusche und Musikanlage.',
 intro_p2='Im dritten Stock eine verglaste Terrasse mit kostenlosem Gemeinschaftsbereich: Tische, Stühle, Mikrowelle, Toaster, Kühlschrank und schöner Ausblick.',
 stats=['29 Zimmer + Studio-Suite','Hydromassage-Dusche','Kostenloses WLAN','Haustiere willkommen'],nav_rooms='Zimmer',rooms_t='Unsere Zimmer',rooms_s='Einzel-, Doppel-, Familienzimmer und ein Penthouse mit privater Terrasse.',
 svcs=['Verglaste Terrasse im dritten Stock','Gemeinschaftsbereich mit Mikrowelle und Kühlschrank','Laptop im Zimmer','Verkaufsautomat','Parken möglich im Parkhaus Virgen del Manzano','Haustiere willkommen'],
 around_s='Im Geschäftszentrum von Burgos und ganz nah an der Altstadt.',
 loc_p='Calle Guardia Civil 7 · Burgos, im Geschäftszentrum der Stadt.',
 chips=['Welche Zimmer gibt es?','Was kostet ein Zimmer?','Wann ist der Check-in?','Darf ich meinen Hund mitbringen?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
BOOK=dict(mode='mail',email='reservas@hostalacuarela.com')
D=dict(name='Hostal Acuarela',ac='#1e3550',ac2='#7a3e5a',ac2_a11y='#633149',book=BOOK,around=[],foot=FOOT,
 address='Calle Guardia Civil 7 · Burgos',phones=['+34 947 20 50 50'],emails=['reservas@hostalacuarela.com'],maps='Hostal Acuarela, Calle Guardia Civil 7, Burgos',t=T)
META=dict(repo='demo-hostal-acuarela-burgos',name='Hostal Acuarela',legal_name='HOSTAL ACUARELA, S.L.',registry_ids=['CIF B09497579'],
 url='https://hostalacuarela.com/',domain='hostalacuarela.com',municipality='Burgos',province='Burgos',sector='hostal de diseño de 29 habitaciones y un Estudio-Suite en el centro de Burgos',
 read_at='2026-10-30T07:12:46+01:00',created_at='2026-10-30T07:12:30+01:00',built_at='2026-10-30T07:25:00+01:00',audit_date='2026-10-30T06:52:00+01:00',
 rating=dict(value=4.1,coincide=['telefono','web'],date='2026-10-29T12:43:53+01:00',url='https://www.google.com/maps/place/Hostal+Acuarela/@42.3451614,-3.69491,17z/data=!4m9!3m8!1s0xd45fcda8eabec5d:0x360771483d799dbb!5m2!4m1!1i2!8m2!3d42.3451614!4d-3.69491!16s%2Fg%2F1vc_rp1w'),
 book=dict(mode='mail',url='mailto:reservas@hostalacuarela.com',note='Su web no tiene motor de reservas: la sección Reservas pide reservar por WhatsApp (638 968 116), correo (reservas@hostalacuarela.com) o teléfono (947 20 50 50). La demo enlaza el correo y el teléfono reales y no construye ningún motor.'),
 first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tenéis?','K01'),('¿Cuánto cuesta una habitación?','K02'),('¿A qué hora es el check-in?','K03'),('¿Puedo ir con mi perro?','K04'),('¿Hay parking?','K05'),('¿Hay wifi?','K06'),('¿Hay terraza?','K07'),('¿Dónde está el hostal?','K08'),('¿Cómo reservo?','K09'),('¿Podéis confirmarme disponibilidad para mañana?','K09'),('¿Hay restaurante?',None),('¿Tenéis piscina?',None)],
'en':[('Which rooms do you have?','K01'),('How much is a room?','K02'),('What time is check-in?','K03'),('Can I bring my dog?','K04'),('Is there parking?','K05'),('Is there wifi?','K06'),('Is there a terrace?','K07'),('Where is the hostel?','K08'),('How do I book?','K09'),('Can you confirm availability for tomorrow?','K09'),('Is there a restaurant?',None),('Do you have a swimming pool?',None)],
'fr':[('Quelles chambres avez-vous ?','K01'),('Combien coûte une chambre ?','K02'),("À quelle heure est l'arrivée ?",'K03'),('Puis-je venir avec mon chien ?','K04'),('Y a-t-il un parking ?','K05'),('Y a-t-il le wifi ?','K06'),('Y a-t-il une terrasse ?','K07'),("Où se trouve l'hostal ?",'K08'),('Comment réserver ?','K09'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K09'),('Y a-t-il un restaurant ?',None),('Avez-vous une piscine ?',None)],
'de':[('Welche Zimmer gibt es?','K01'),('Was kostet ein Zimmer?','K02'),('Wann ist der Check-in?','K03'),('Darf ich meinen Hund mitbringen?','K04'),('Gibt es einen Parkplatz?','K05'),('Gibt es WLAN?','K06'),('Gibt es eine Terrasse?','K07'),('Wo liegt das Hostal?','K08'),('Wie kann ich buchen?','K09'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K09'),('Gibt es ein Restaurant?',None),('Haben Sie ein Schwimmbad?',None)]}
