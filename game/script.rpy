# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = DynamicCharacter("player")
define e = Character("Kruezenberg")
define a = Character("Léna")
define o = Character("Odium")
define w = Character("Diana")
define z = Character("???")
define v = Character("Veos", color="FF0000")
define c = Character("Walter")
define p = Character("Prodige")
define cat = Character("Jinx")
define b = Character("Brumen")
define s = Character("Syrianne", color="666666")
define slol = Character("Chyrianne", color="666666")
define ly = Character("Lyna", color="660099")
define inter = Character("Interface", color="3300FF")
define ten = Character("Tenworks", color="FF3300")
define ne = Character("Nekobi", color="00FF33")
define no = Character("Nodens", color="999999")
define lan = Character("Lanthinium", color="33fff0", what_font="CyberpunkWaifus.ttf")

screen battle1:
    frame:
        xalign 0.01 yalign 0.05
        xminimum 220 xmaximum 220
        vbox:
            text "Vous" size 22 xalign 0.5
            null height 5
            hbox:
                bar:
                    xmaximum 130
                    value player_hp
                    range player_max_hp
                    left_gutter 0
                    right_gutter 0
                    thumb None
                    thumb_shadow None
                    
                null width 5
                
                text "[player_hp] / [player_max_hp]" size 16
                
                
    frame:
        xalign 0.99 yalign 0.05
        xminimum 220 xmaximum 220
        vbox:
            text "Lanthinium" size 22 xalign 0.5
            null height 5
            hbox:
                bar:
                    xmaximum 130
                    value lanth_hp
                    range lanth_max_hp
                    left_gutter 0
                    right_gutter 0
                    thumb None
                    thumb_shadow None
                    
                null width 5
                
                text "[lanth_hp] / [lanth_max_hp]" size 16
                
    text "Joueur VS Lanthinium" xalign 0.5 yalign 0.05 size 30

# The game starts here.

label start:
    
    stop sound
    scene main_menu
    
    $ cravate = False
    $ albator = False
    $ jupever = False
    $ stylarchi = False
    
    $ romance_kruezenberg = 0
    $ romance_diana = 0
    $ romance_odium = 0
    $ romance_veos = 0
    $ romance_prodige = 0 
    $ romance_walter = 0
    $ romance_lanthinium = 0
    
    $ tarko1 = False
    $ tarko2 = False
    $ tarko3 = False
    $ tarko4 = False
    
    $ choicelyna = True
    $ pistol = False
    $ esquive = False
    $ paralysie = False
    
    $ PACEScore = 0
    
    "Avant de commencer, je vais prendre ton petit nom."
    "Je dois te dire, que dans ce jeu, tu incarnes une fille. Ça me paraît important à préciser. Bref, dis-moi tout !"

    $ player = renpy.input("Alors, qui es-tu ?")

    $ player = player.strip()

    if player == "":
        $ player="Pattycake"
        
    if player == "Veos":
       
        "Bravo, Vous avez trouvé l'easter egg 01/Nalya ! Souhaitez-vous le visiter ou continuer ?"
        
        menu:
            
            "Je veux !":
                jump PACES
                
            "Non merci.":
                jump debut
        
     
    if player == "Vatalite":
        
        "Bravo ! Vous avez trouvé l'easter egg 02/Nalya ! Souhaitez-vous le visiter ou continuer ?"
        
        menu:
            
            "Je veux !":
                jump Vatalite
                
            "Non merci.":
                jump debut
                
    if player == "Ficelle":
        
        "Bravo ! Vous avez trouvé l'easter egg 03/Nalya ! Souhaitez-vous le visiter ou continuer ?"
        
        menu:
            
            "Je veux !":
                jump Ficelle
                
            "Non merci.":
                jump debut
                                
    if player == "Kruezenberg":
        
        "Bravo ! Vous avez trouvé l'easter egg 04/Nalya ! Souhaitez-vous le visiter ou continuer ?"
        
        menu:
            
            "Je veux !":
                jump Krue
                
            "Je veux !":
                jump Krue
                
    if player == "Nash":
        
        "Bravo ! Vous avez trouvé l'easter egg 05/Nalya ! Souhaitez-vous le visiter ou continuer ?"
        
        menu:
            
            "Je veux !":
                jump Tarkoza
                
            "Non merci.":
                jump debut

    if player == "Lyna":
        
        "Bravo ! Vous avez trouvé l'easter egg 05/Nalya ! Souhaitez-vous le visiter ou continuer ?"
        
        menu:
            
            "Je veux !":
                jump Tarkoza
                
            "Non merci.":
                jump debut
                             
    if player == "Lurek":
        
        "Bravo ! Vous avez trouvé l'easter egg 05/Nalya ! Souhaitez-vous le visiter ou continuer ?"
        
        menu:
            
            "Je veux !":
                jump Tarkoza
                
            "Non merci.":
                jump debut
                            
    if player == "Jjur":
        $ romance_walter -= 100
    if player == "Gips":
        play sound "gipsinro.ogg"
        $renpy.pause()
        
 
        
     
    

    
    jump debut
    
label debut:
    
    stop music
    scene bg black
    with fade

    play sound "reveil.ogg" 
    
    $renpy.pause()
    
    m "Uuuuuuuhh ?"
    m "Grrmh..."
    
    scene bg bedroom
    
    play music "menu.ogg"

    m "Il est déjà cinq heures du matin..."
    
    "Aujourd'hui, c'est la rentrée ! J'entre en Terminale dans un nouveau lycée, à Sorea."
    
    "J'ai faim. Je me lève et me lave les mains, mais avant tout, je dis Bismillah."
    
    "Malgré la présence d'Allah à mes côtés, je ne me sens pas fraîche pour aller au lycée..."
    
    "Mais faut bien se préparer ! Je pars donc en direction de la douche."
    
    scene bg douche1
    with dissolve
    
    "Je me déshabille et je commence à me laver, afin de me préparer pour cette belle journée."
    
    play sound "douche.ogg"
    
    m "J'espère que je pourrais me faire des amis là-bas..."
    
    "Je n'ai jamais été populaire."
    
    "Mais j'ai pas vraiment le temps d'y réfléchir ! Je sors de la douche et je pars m'habiller sans hâte. Mon sac est fait, de toute façon."
    
    stop sound 
    
    "Je suis maintenant face à mon armoire. Je dois choisir quoi porter..."
    
menu:
    
    "Une jupe verte et un t-shirt bleu ; look classique, intemporel.":
        $ romance_odium += 1
        jump suite

    "Un t-shirt cravate, pour faire un peu hipster.":
        $ cravate = True
        jump suite
    
    "Mon cosplay de général venant d'Albator ; ça fait geek ":
        $ albator = True
        jump suite
    
    "Une chemise blanche à pois noirs, avec une salopette noire.":
        $ stylarchi = True
        jump suite
    
    "Je vais y aller nue. On s'en fout, de toute façon.":
        jump prison
        
label prison:
    
    scene bg prison
    with dissolve
    
    play music "caca.ogg"
    
    "Et voilà comment j'ai fini en prison... Comme quoi, à force de jouer à la conne..."
    
    " ... Si seulement c'était juste un jeu, je pourrais revenir en arrière et repenser à deux fois ma décision..."
    
    "Mais non, me voilà en prison pour exhibtionnisme. Mince."
    
    "C'est pas très 2K20..."
    
    return
    
        
label suite:
        
    
    "Je rejoins donc la salle à manger, afin de grignoter quelque chose avant de partir. Mon train part vers sept heures."
    
    scene bg miam
    with dissolve
    
    "Il me reste un croissant. Je l'avale rapidement, avec un bon verre de jus d'orange. Il est temps de partir."
    
    scene bg black
    with fade
    
    $renpy.pause()
     
    "Je marche jusqu'à la gare. Le soleil est déjà haut dans le ciel, en ces premiers jours d'été."
     
    scene bg rues
    with dissolve
    
    play music "lobby.ogg"
    
    "Il y a déjà plein de monde dans la rue."
    
    "Je prends donc mon train, en direction du lycée."

    show bg train
    with fade
    play sound "train.ogg"

    "Le train que j'emprunte est rempli de lycéens..."

    show bg train
    with hpunch

    "Dehors, la ville s'étend à l'horizon, dans de grandes étendues grises, sous le regard bienveillant du soleil."

    show bg train
    with hpunch

    "J'ouvre une énième fois le fascicule fourni par mon lycée."

    show bg train
    with hpunch

    " Lycée municipal de Sorea ! Faîtes de vos rêves une réalité ! "
                                                                                            
    show bg train
    with hpunch

    "J'espère qu'il y aura des beaux garçons dans ma classe..."

    show bg train
    with hpunch

    "Je me contente de regarder le paysage défiler, la tête posée contre la vitre, jusqu'à l'arrivée au quartier du lycée de Sorea."

    show bg black
    with Dissolve(10.0)

    stop sound fadeout 2.0
    
    $renpy.pause()
    
    "Finalement, au bout de 20 minutes, j'arrive à la gare..."
    
    show bg ville
    
    "... Problème, je n'ai aucune idée de par où se trouve le lycée..."
    
    "... Et la consultation du plan fourni par le fascicule ne fait que me perdre d'avantage."
    
    "Je vois au loin une épicerie et un garage. Peut-être pourraient-ils me renseigner ?"

    menu:
        
        "Aller dans le garage.":
            jump garage
        
        "Aller dans l'épicerie.":
            jump epicerie
        
        
label garage: #Prodige

    "je me dirige donc vers le garage, d'un pas rapide."
    
    show bg garage
    with fade
    
    "Au sein du garage des gens s'affairent, visiblement occupés à réparer une voiture."
    
    "Je ne sais pas trop comment aborder les gens, j'ai un peu peur de les ennuyer avec ma question."
    
    "Je tiens, un peu fébrile, le fasicule de mon lycée, comme pour mettre en évidence la raison de ma venue."
    
    "Soudain, une main se porte sur mon épaule."
    
    m "Eeeh ?"
    
    "Je me retourne pour faire face à un jeune homme, qui me regarde d'un air bieveillant."
    
    
    
    
    "aha"
    
    return


label epicerie: #ici on va mettre..en vrai je sais pas
    
    show bg magasin
    
    "oho"
    
    return
   
    # This ends the game.

    return
    
    
label PACES:
    
    stop music
    play music "kahoot.ogg"
    
    show bg paces
    
    "Choisissez une bonne réponse parmi ces propositions. Attention, plusieurs peuvent être valides, une seule est attendue."
    
    "UE 5 : tête et cou : à partir de quelle vertèbre l'artère vertébrale rejoint-elle le canal vertébral ?"
    
    menu:
        
        "C7":
            jump PACES2
        "C6":
            $ PACEScore += 1
            jump PACES2
        "C5":
            jump PACES2
            
label PACES2:
    
    "UE 5 : denture : choissez une des caractéristiques de la dent 23 ;"
    
    menu:
        
        "Se trouve sur l'hémi-arcade supérieure droite.":
            jump PACES3
        "Est une canine.":
            $ PACEScore += 1
            jump PACES3
        "Se trouve sur l'hémi-arcade supérieure gauche.":
            $ PACEScore += 1
            jump PACES3
        "Est la 1ère pré-molaire":
            jump PACES3
        "Peut avoir pour rôle de tirer les aliments vers l'arrière.":
            $ PACEScore += 1
            jump PACES3
            
label PACES3:

    "UE 5 : à propos du nerf IV : choisissez une bonne réponse."
    
    menu:
        
        "Il correspond au nerf abducens.":
            jump PACES4
        "Il correspond au nerf trochléaire.":
            $ PACEScore += 1
            jump PACES4
        "Il fait partie des nerfs crâniens, qui sont 12, et qui naissent tous du tronc cérébral.":
            jump PACES4
        "Il correspond au nerf occulo-moteur.":
            jump PACES4
        "Il participe à l'innervation du globe occulaire.":
            $ PACEScore += 1
            jump PACES4
            
label PACES4:
    
    "UE6 : histoire de la médecine : à propos de La Fabrica, quelle est la bonne réponse ?"
    
    menu:
        
        "Elle a été écrite par Gallien en 1543.":
            jump PACES5
        "Elle a été écrite par Vésale en 1643.":
            jump PACES5
        "Elle a été écrite par un belge en 1543.":
            $ PACEScore += 1
            jump PACES5
        "Elle a été écrite par Léonard de Vinci.":
            jump PACES5
        "La grande nouveauté de cette oeuvre est l'apparition de l'anatomie topographique.":
            jump PACES5
            
label PACES5:

    "UE5 : à propos du poignet : lesquel de ces os font partie du carpe ?"
    
    menu:
        
        "Le capitulum.":
            jump PACES6
        "L'os lunatum.":
            $ PACEScore += 1
            jump PACES6
        "Le talus.":
            jump PACES6
        "L'ulna.":
            jump PACES6
        "L'os trichétrum.":
            $ PACEScore += 1
            jump PACES6
            
label PACES6:
    
    "UE6 : Choisissez l'un des caractéristiques des essais cliniques ;"
    
    menu:
        
        "Les essais cliniques : les phases I et II sont obligatoires, le reste est facultatif.":
            jump PACES7
        "L'essai de phase I se fait sur des volontaires sains.":
            $ PACEScore += 1
            jump PACES7
        "L'essai de phase II se fait sur des milliers de patients.":
            jump PACES7
        "Il est possible d'utiliser des placebos pour évaluer l'efficacité d'un médicament.":
            $ PACEScore += 1
            jump PACES7
            
label PACES7:
    
    "UE6 : à propos de la pharmacocinétique : quelles sont les affirmations exactes ?"
    
    menu:
        
        "C'est l'étude de l'effet de l'organisme sur le médicament.":
            $ PACEScore += 1
            jump PACES8
        "Elle est composée de 3 phases.":
            jump PACES8
        "La plupart des médicaments sont hydrophiles.":
            jump PACES8
        "La plupart des médicaments sont lipophiles.":
            $ PACEScore += 1
            jump PACES8
            
label PACES8:
    
    "Encore UE5 : Où se situe le processus coracoïde ?"
    
    menu:
        
        "Se trouve en dedans par rapport à l'acromion.":
            $ PACEScore += 1
            jump PACES9
        "Est une partie de la scapula.":
            $ PACEScore += 1
            jump PACES9
        "Se trouve en dedans par rapport à l'humérus.":
            $ PACEScore += 1
            jump PACES9
        "Est une partie de la patella.":
            jump PACES9
        "Est une partie de l'omoplate.":
            $ PACEScore += 1
            jump PACES9
            
label PACES9:
    
    
    "UE1 : à propos des glucides : Une des bonnes réponses ?"
    
    menu:
        
        "Les glucides sont des biomolécules abondantes sur terre.":
            $ PACEScore += 1
            jump PACES10
        "Ils sont réputés comme très hydrophiles.":
            $ PACEScore += 1
            jump PACES10
        "Ils peuvent avoir un rôle : structural, métabolique, énergétique.":
            $ PACEScore += 1
            jump PACES10
        "Ils sont dépourvus de groupement hydroxyle":
            jump PACES10
        "Le saccharose, le lactose et le maltose sont des disaccharides.":
            $ PACEScore += 1
            jump PACES10
            
label PACES10:

    "UE7 : Science, société, humaine : à quelle date estime-t-on l'apparition de la peste, et qui en a découvert la bactérie ?"
    
    menu:
        
        "1347 et Koch.":
            jump PACESfin
        "1347 et les deux : Luc Montagnier et Françoise de Barré Sinussi.":
            jump PACESfin
        "1347 et Alexandre Yersin.":
            jump PACESfin
        "1348 et Koch.":
            jump PACESfin
        "1348 et Alexandre Yersin.":
            $ PACEScore += 1
            jump PACESfin
            
label PACESfin:
    
    "Bravo ! Voyons à présent les résultats de ton test ;"
    
    if PACEScore == 10:
        "Bravo ! Tu as eu un score parfait, tu es donc digne du nom choisi !"
        
        "Retiens-bien les bonnes réponses. Bientôt, cela te permettra d'accéder à un pan secret du jeu !"
        
        return
    else:
    
        "Tu as eu %(PACEScore)s bonne(s) réponse(s)."
    
        "Ce n'est pas assez pour avoir ton diplôme !"
    
        "Alors, que veux-tu faire à présent ?"
    
        menu:
        
            "Recommencer !":
                jump PACES
            "Mais, je voulais juste jouer au jeu...":
                jump debut
            "Sah, casse les couilles.":
                return
                
label Vatalite:
    
    stop music
    scene bg black
    with fade
    
    play music "vataliteyes.ogg"
    
    "J’étais toute petite la première fois que je l’ai vu. Je devais sans doute avoir 8 ans."
    
    "C’était un grand homme noir dans l’obscurité de ma chambre. Il avait ensuite disparu comme il était apparu, dans un flash très rapide."
    
    "Le lendemain, je décidai d’aller dans la grande bibliothèque d’Opalues pour me documenter dessus."
    
    "C’était il y a neuf ans."

    stop music
    scene bg clock
    with fade
    
    play music "chopin.ogg"
    
    "Je prends ma tasse de thé sur ma table de chevet. Il est dix heures du matin."
    
    "Je lève douloureusement ma tête, encore un réveil difficile. Je n’aime pas les matins, c’est chiant les matins, il n’y a rien à faire."
    
    "Je préfère largement l’après midi. Je regarde par la fenêtre, les engrenages continuent de tourner, tout va bien."
    
    "Je descends donc dans la salle principale, munie toujours de ma tasse de thé. L’horloge tourne, vérification. Je regarde ma montre. Parfait."
    
    "Il ne me manque plus qu’un pain tournant, la spécialité d’Uppartenant, mon pays, et je me sentirai enfin à peu près fonctionnelle."
    
    "Hmm... Et peut-être changer d’habits, ça fait douze jours que j’ai les mêmes..."
    
    play sound "tictac.ogg"
    
    "Je descends dans le sous-sol, un fracas se fait de plus en plus fort, mais je l’aime bien. C'est la multitude de mécanismes complexes se déroulant sous plus d’un kilomètre en profondeur."

    
    "Et encore là ce n’est que le deuxième sous-sol, je ne vous parle pas des trois cents autres étages souterrains de cette gigantesque tour de l’enfer."
    
    "Me voici enfin à la cuisine, un pain tournant tout chaud m’y attend. J’adore les automatismes, j’adore les pains tournants, mais plus les pains tournants quand même, je ne vais pas manger la machine à bouffe."
    
    "Je remonte donc l’escalier, armée de ma tasse de thé et de mon magnifique pain."
    
    "Mon métabolisme se met enfin en marche, je suis prête pour une nouvelle journée."

    stop music
    stop sound
    play sound "dring.ogg"
    show bg clock
    with hpunch
    "DRIIING!!!"
    
    "Je sens que je vais démolir cette putain de sonnerie."
    
    "Qui a la témérité de me déranger à cette heure ? C’est vrai, les gens normaux démarrent à 4H, des fous, c’est insensé."
    
    "J’avale donc toute ma précieuse nourriture en vitesse, et arrive au panneau de contrôle."
    
    "Personne à l’écran. Étonnant."
    
    "Sans doute un farceur. Si je le trouve, je me sers de lui comme esclave pour 5 semaines."
    
    play music "vataliteyes.ogg"
    
    "J’ai un sentiment étrange. Je regarde ma montre, dix heures et 6 minutes."
    
    
    "Je regarde mes 7 panneaux de contrôle, rien. Je vérifie si la personne qui a sonné n’est pas dans la rue."
    
    "Juste 8 pigeons grignotant quelques graines. Pas un chat. Je réfléchis quelques minutes."
    
    "J’ai dit une bêtise, les gens ne se lèvent pas à quatre heures mais à 9H, pourquoi j’ai dit ça ?"
    
    "Et puis je n’ai pas sept panneaux de contrôle, et pourquoi aurais-je pris le temps de vérifier qu’il y avait huit pigeons ?"
    
    "Ça devient de plus en plus étrange. Je m’assois sur une pile d’une dizaine de livres."
    
    "Hmmm... J’ai un énorme pressentiment, comme si quelque chose me regardait. Je repense à mes 11 ans."
    
    "Pourquoi mes onze ans ? Ça n’a aucun rapport, je deviendrais folle comme le voisin de la douz-"
    
    play sound "onesegivepas.ogg"
    stop music
    scene bg black
    
    "Je reste figée. Je me retourne lentement."
    
    "Il est là."
    
    "Le grand être noir. Je suis tétanisée. Il me fixe intensément"
    
    "Serait-ce lui qui a sonné?"
    
    "Il a disparu."
    
    "La suite dans Vatalite, sur http://www.868games.fr/vatalite.php !"
    
    return
    
label Ficelle:
    
    stop music
    scene bg black
    with fade
    
    "Meow ?"
    
    play music "meows.ogg"
    
    scene bg foret
    
    "Meow."
    
    "Mii ?"
     
    "Meow Meow."
    
    m "Meow ?"
    
    show cat at truecenter
    
    cat "Meow !"
    
    m "Meow."
    
    cat "Miiii !"
    
    menu:
        
        "Meow.":
            cat "Meow !"
        
        "Meow.":
            cat "Meow"
    show cat at right
   
    m "Meow !"
    
    cat "Meeeoooow !"
    
    hide cat
    
    scene bg rues
    
    "Meow meow miii meow."
   
    m "Meow ?"
    
    show cat at left
    
    cat "Mii !"
    
    scene bg rues
    with hpunch
    
    show cat at center
    
    cat "Meow !"
    
    m "Meow."
    
    "Meow meow."
    
    return
    
label Krue:
    
    stop sound
    stop music
    scene bg kruze
    play music "vataliteyes.ogg"
    
    "#######??-!!KRUEZENBERG#CE&&MEME##@MORT######{nw}"
    play audio "rire.ogg"
    "AHAHA5466####____###AH_224########{nw}"
    "SJISFUISDFUI###Q4455#########6666############{nw}"
    play audio "rire.ogg"
    "AHAHA5466####____###AH_224########{nw}"
    "#######??-!!KRUEZENBERG#CE&&MEME##@MORT######{nw}"
    "######VOID24789***+++++++++++###########447{nw}"
    "SJISFUISDFUI###Q4455#########6666############{nw}"
    "SEHGFFUISDFUI###Q4455#########67466############{nw}"
    play audio "rire.ogg"
    "AHAHA5466####____###AH_224########{nw}"
    "#######??-!!KRUEZENBERG#CE&&MEME##@MORT######{nw}"
    play audio "rire.ogg"
    "AHAHA5466####____###AH_224########{nw}"
    "SJISFUISDFUI###Q4455#########6666############{nw}"
    play audio "rire.ogg"
    "AHAHA5466####____###AH_224########{nw}"
    "#######??-!!KRUEZENBERG#CE&&MEME##@MORT######{nw}"
    "######VOID24789***+++++++++++###########447{nw}"
    "SJISFUISDFUI###Q4455#########6666############{nw}"
    "SEHGFFUISDFUI###Q4455#########67466############{nw}"
    play audio "rire.ogg"
    "AHAHA5466####____###AH_224########{nw}"
    "#######??-!!KRUEZENBERG#CE&&MEME##@MORT######{nw}"
    "######VOID24789***+++++++++++###########447{nw}"
    "SJISFUISDFUI###Q4455#########6666############{nw}"
    "SEHGFFUISDFUI###Q4455#########67466############{nw}"
    play audio "rire.ogg"
    "AHAHA5466####____###AH_224########{nw}"
    "#######??-!!KRUEZENBERG#CE&&MEME##@MORT######{nw}"
    play audio "rire.ogg"
    "AHAHA5466####____###AH_224########{nw}"
    "SJISFUISDFUI###Q4455#########6666############{nw}"
    play audio "rire.ogg"
    "AHAHA5466####____###AH_224########{nw}"
    "#######??-!!KRUEZENBERG#CE&&MEME##@MORT######{nw}"
    "######VOID24789***+++++++++++###########447{nw}"
    "SJISFUISDFUI###Q4455#########6666############{nw}"
    "SEHGFFUISDFUI###Q4455#########67466############{nw}"
    play audio "rire.ogg"
    "AHAHA5466####____###AH_224########{nw}"
    "SEHGFFUISDFUI###Q4455#########67466############{nw}"
    play audio "rire.ogg"
    "AHAHA5466####____###AH_224########{nw}"
    "#######??-!!KRUEZENBERG#CE&&MEME##@MORT######{nw}"
    "######VOID24789***+++++++++++###########447{nw}"
    "SJISFUISDFUI###Q4455#########6666############{nw}"
    "SEHGFFUISDFUI###Q4455#########67466############{nw}"
    play audio "rire.ogg"
    "AHAHA5466####____###AH_224########{nw}"
    "#######??-!!KRUEZENBERG#CE&&MEME##@MORT######{nw}"
    play audio "rire.ogg"
    "AHAHA5466####____###AH_224########{nw}"
    "SJISFUISDFUI###Q4455#########6666############{nw}"
    play audio "rire.ogg"
    "AHAHA5466####____###AH_224########{nw}"
    "#######??-!!KRUEZENBERG#CE&&MEME##@MORT######{nw}"
    "######VOID24789***+++++++++++###########447{nw}"
    "SJISFUISDFUI###Q4455#########6666############{nw}"
    "SEHGFFUISDFUI###Q4455#########67466############{nw}"
    play audio "rire.ogg"
    "AHAHA5466####____###AH_224########{nw}"
    "SEHGFFUISDFUI###Q4455#########67466############{nw}"
    play audio "rire.ogg"
    "AHAHA5466####____###AH_224########{nw}"
    "#######??-!!KRUEZENBERG#CE&&MEME##@MORT######{nw}"
    play audio "rire.ogg"
    "AHAHA5466####____###AH_224########{nw}"
    "SJISFUISDFUI###Q4455#########6666############{nw}"
    play audio "rire.ogg"
    "AHAHA5466####____###AH_224########{nw}"
    "#######??-!!KRUEZENBERG#CE&&MEME##@MORT######{nw}"
    "######VOID24789***+++++++++++###########447{nw}"
    "SJISFUISDFUI###Q4455#########6666############{nw}"
    "SEHGFFUISDFUI###Q4455#########67466############{nw}"
    play audio "rire.ogg"
    "AHAHA5466####____###AH_224########{nw}"
    "SEHGFFUISDFUI###Q4455#########67466############{nw}"
    play audio "rire.ogg"
    "AHAHA5466####____###AH_224########{nw}"
    "#######??-!!KRUEZENBERG#CE&&MEME##@MORT######{nw}"
    "######VOID24789***+++++++++++###########447{nw}"
    "SJISFUISDFUI###Q4455#########6666############{nw}"
    "SEHGFFUISDFUI###Q4455#########67466############{nw}"
    play audio "rire.ogg"
    "AHAHA5466####____###AH_224########{nw}"
    "#######??-!!KRUEZENBERG#CE&&MEME##@MORT######{nw}"
    play audio "rire.ogg"
    "AHAHA5466####____###AH_224########{nw}"
    "SJISFUISDFUI###Q4455#########6666############{nw}"
    play audio "rire.ogg"
    "AHAHA5466####____###AH_224########{nw}"
    "#######??-!!KRUEZENBERG#CE&&MEME##@MORT######{nw}"
    "######VOID24789***+++++++++++###########447{nw}"
    "SJISFUISDFUI###Q4455#########6666############{nw}"
    "SEHGFFUISDFUI###Q4455#########67466############{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "#######??-!!KRUEZENBERG#CE&&MEME##@MORT######{nw}"
    "######VOID24789***+++++++++++###########447{nw}"
    "SJISFUISDFUI###Q4455#########6666############{nw}"
    "SEHGFFUISDFUI###Q4455#########67466############{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "#######??-!!KRUEZENBERG#CE&&MEME##@MORT######{nw}"
    "######VOID24789***+++++++++++###########447{nw}"
    "SJISFUISDFUI###Q4455#########6666############{nw}"
    "SEHGFFUISDFUI###Q4455#########67466############{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "#######??-!!KRUEZENBERG#CE&&MEME##@MORT######{nw}"
    "######VOID24789***+++++++++++###########447{nw}"
    "SJISFUISDFUI###Q4455#########6666############{nw}"
    "SEHGFFUISDFUI###Q4455#########67466############{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "#######??-!!KRUEZENBERG#CE&&MEME##@MORT######{nw}"
    "######VOID24789***+++++++++++###########447{nw}"
    "SJISFUISDFUI###Q4455#########6666############{nw}"
    "SEHGFFUISDFUI###Q4455#########67466############{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "#######??-!!KRUEZENBERG#CE&&MEME##@MORT######{nw}"
    "######VOID24789***+++++++++++###########447{nw}"
    "SJISFUISDFUI###Q4455#########6666############{nw}"
    "SEHGFFUISDFUI###Q4455#########67466############{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "#######??-!!KRUEZENBERG#CE&&MEME##@MORT######{nw}"
    "######VOID24789***+++++++++++###########447{nw}"
    "SJISFUISDFUI###Q4455#########6666############{nw}"
    "SEHGFFUISDFUI###Q4455#########67466############{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "#######??-!!KRUEZENBERG#CE&&MEME##@MORT######{nw}"
    "######VOID24789***+++++++++++###########447{nw}"
    "SJISFUISDFUI###Q4455#########6666############{nw}"
    "SEHGFFUISDFUI###Q4455#########67466############{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "#######??-!!KRUEZENBERG#CE&&MEME##@MORT######{nw}"
    "######VOID24789***+++++++++++###########447{nw}"
    "SJISFUISDFUI###Q4455#########6666############{nw}"
    "SEHGFFUISDFUI###Q4455#########67466############{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "#######??-!!KRUEZENBERG#CE&&MEME##@MORT######{nw}"
    "######VOID24789***+++++++++++###########447{nw}"
    "SJISFUISDFUI###Q4455#########6666############{nw}"
    "SEHGFFUISDFUI###Q4455#########67466############{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "#######??-!!KRUEZENBERG#CE&&MEME##@MORT######{nw}"
    "######VOID24789***+++++++++++###########447{nw}"
    "SJISFUISDFUI###Q4455#########6666############{nw}"
    "SEHGFFUISDFUI###Q4455#########67466############{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "#######??-!!KRUEZENBERG#CE&&MEME##@MORT######{nw}"
    "######VOID24789***+++++++++++###########447{nw}"
    "SJISFUISDFUI###Q4455#########6666############{nw}"
    "SEHGFFUISDFUI###Q4455#########67466############{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "#######??-!!KRUEZENBERG#CE&&MEME##@MORT######{nw}"
    play audio "rire.ogg"
    "AHAHA5466####____###AH_224########{nw}"
    "SJISFUISDFUI###Q4455#########6666############{nw}"
    play audio "rire.ogg"
    "AHAHA5466####____###AH_224########{nw}"
    "#######??-!!KRUEZENBERG#CE&&MEME##@MORT######{nw}"
    "######VOID24789***+++++++++++###########447{nw}"
    "SJISFUISDFUI###Q4455#########6666############{nw}"
    "SEHGFFUISDFUI###Q4455#########67466############{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "#######??-!!KRUEZENBERG#CE&&MEME##@MORT######{nw}"
    "######VOID24789***+++++++++++###########447{nw}"
    "SJISFUISDFUI###Q4455#########6666############{nw}"
    "SEHGFFUISDFUI###Q4455#########67466############{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "#######??-!!KRUEZENBERG#CE&&MEME##@MORT######{nw}"
    "######VOID24789***+++++++++++###########447{nw}"
    "SJISFUISDFUI###Q4455#########6666############{nw}"
    "SEHGFFUISDFUI###Q4455#########67466############{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "#######??-!!KRUEZENBERG#CE&&MEME##@MORT######{nw}"
    "######VOID24789***+++++++++++###########447{nw}"
    "SJISFUISDFUI###Q4455#########6666############{nw}"
    "SEHGFFUISDFUI###Q4455#########67466############{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "#######??-!!KRUEZENBERG#CE&&MEME##@MORT######{nw}"
    "######VOID24789***+++++++++++###########447{nw}"
    "SJISFUISDFUI###Q4455#########6666############{nw}"
    "SEHGFFUISDFUI###Q4455#########67466############{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "#######??-!!KRUEZENBERG#CE&&MEME##@MORT######{nw}"
    "######VOID24789***+++++++++++###########447{nw}"
    "SJISFUISDFUI###Q4455#########6666############{nw}"
    "SEHGFFUISDFUI###Q4455#########67466############{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "#######??-!!KRUEZENBERG#CE&&MEME##@MORT######{nw}"
    "######VOID24789***+++++++++++###########447{nw}"
    "SJISFUISDFUI###Q4455#########6666############{nw}"
    "SEHGFFUISDFUI###Q4455#########67466############{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "#######??-!!KRUEZENBERG#CE&&MEME##@MORT######{nw}"
    "######VOID24789***+++++++++++###########447{nw}"
    "SJISFUISDFUI###Q4455#########6666############{nw}"
    "SEHGFFUISDFUI###Q4455#########67466############{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "#######??-!!KRUEZENBERG#CE&&MEME##@MORT######{nw}"
    "######VOID24789***+++++++++++###########447{nw}"
    "SJISFUISDFUI###Q4455#########6666############{nw}"
    "SEHGFFUISDFUI###Q4455#########67466############{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "#######??-!!KRUEZENBERG#CE&&MEME##@MORT######{nw}"
    "######VOID24789***+++++++++++###########447{nw}"
    "SJISFUISDFUI###Q4455#########6666############{nw}"
    "SEHGFFUISDFUI###Q4455#########67466############{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "#######??-!!KRUEZENBERG#CE&&MEME##@MORT######{nw}"
    "######VOID24789***+++++++++++###########447{nw}"
    "SJISFUISDFUI###Q4455#########6666############{nw}"
    "SEHGFFUISDFUI###Q4455#########67466############{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "#######??-!!KRUEZENBERG#CE&&MEME##@MORT######{nw}"
    "######VOID24789***+++++++++++###########447{nw}"
    "SJISFUISDFUI###Q4455#########6666############{nw}"
    "SEHGFFUISDFUI###Q4455#########67466############{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "#######??-!!KRUEZENBERG#CE&&MEME##@MORT######{nw}"
    play audio "rire.ogg"
    "AHAHA5466####____###AH_224########{nw}"
    "SJISFUISDFUI###Q4455#########6666############{nw}"
    play audio "rire.ogg"
    "AHAHA5466####____###AH_224########{nw}"
    "#######??-!!KRUEZENBERG#CE&&MEME##@MORT######{nw}"
    "######VOID24789***+++++++++++###########447{nw}"
    "SJISFUISDFUI###Q4455#########6666############{nw}"
    "SEHGFFUISDFUI###Q4455#########67466############{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "#######??-!!KRUEZENBERG#CE&&MEME##@MORT######{nw}"
    "######VOID24789***+++++++++++###########447{nw}"
    "SJISFUISDFUI###Q4455#########6666############{nw}"
    "SEHGFFUISDFUI###Q4455#########67466############{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "#######??-!!KRUEZENBERG#CE&&MEME##@MORT######{nw}"
    "######VOID24789***+++++++++++###########447{nw}"
    "SJISFUISDFUI###Q4455#########6666############{nw}"
    "SEHGFFUISDFUI###Q4455#########67466############{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "#######??-!!KRUEZENBERG#CE&&MEME##@MORT######{nw}"
    "######VOID24789***+++++++++++###########447{nw}"
    "SJISFUISDFUI###Q4455#########6666############{nw}"
    "SEHGFFUISDFUI###Q4455#########67466############{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "#######??-!!KRUEZENBERG#CE&&MEME##@MORT######{nw}"
    "######VOID24789***+++++++++++###########447{nw}"
    "SJISFUISDFUI###Q4455#########6666############{nw}"
    "SEHGFFUISDFUI###Q4455#########67466############{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "#######??-!!KRUEZENBERG#CE&&MEME##@MORT######{nw}"
    "######VOID24789***+++++++++++###########447{nw}"
    "SJISFUISDFUI###Q4455#########6666############{nw}"
    "SEHGFFUISDFUI###Q4455#########67466############{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "#######??-!!KRUEZENBERG#CE&&MEME##@MORT######{nw}"
    "######VOID24789***+++++++++++###########447{nw}"
    "SJISFUISDFUI###Q4455#########6666############{nw}"
    "SEHGFFUISDFUI###Q4455#########67466############{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "#######??-!!KRUEZENBERG#CE&&MEME##@MORT######{nw}"
    "######VOID24789***+++++++++++###########447{nw}"
    "SJISFUISDFUI###Q4455#########6666############{nw}"
    "SEHGFFUISDFUI###Q4455#########67466############{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "#######??-!!KRUEZENBERG#CE&&MEME##@MORT######{nw}"
    "######VOID24789***+++++++++++###########447{nw}"
    "SJISFUISDFUI###Q4455#########6666############{nw}"
    "SEHGFFUISDFUI###Q4455#########67466############{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "#######??-!!KRUEZENBERG#CE&&MEME##@MORT######{nw}"
    "######VOID24789***+++++++++++###########447{nw}"
    "SJISFUISDFUI###Q4455#########6666############{nw}"
    "SEHGFFUISDFUI###Q4455#########67466############{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "#######??-!!KRUEZENBERG#CE&&MEME##@MORT######{nw}"
    "######VOID24789***+++++++++++###########447{nw}"
    "SJISFUISDFUI###Q4455#########6666############{nw}"
    "SEHGFFUISDFUI###Q4455#########67466############{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "AHAHA5466####____###AH_224########{nw}"
    "#######??-!!KRUEZENBERG#CE&&MEME##@MORT######{nw}"
    "######VOID24789***+++++++++++###########447{nw}"
    "SJISFUISDFUI###Q4455#########6666############{nw}"
    "SEHGFFUISDFUI###Q4455#########67466############{nw}"
    window hide
    play music "main-menu-theme.ogg"    
    show mainkmenu
    
    $renpy.pause()
    
    stop sound
    stop music
    stop audio
    play sound "brr.ogg"
    show maingmenu
    
    $renpy.pause()
    $renpy.pause()
    $renpy.pause()
   
    $ renpy.quit()
    
label Tarkoza:
    
    stop music
    show bg black
    
    $ player = renpy.input("Tiens, dans cette partie tu peux changer ton nom, si tu veux.")

    $ player = player.strip()

    if player == "":
        $ player="Syrianne"
    
    if player == "Kruezenberg":
        
        "Bravo ! Vous avez trouvé l'easter egg 04/Nalya ! Souhaitez-vous le visiter ou continuer ?"
        
        menu:
            
            "Je veux !":
                jump Krue
                
            "Je veux !":
                jump Krue
    
    $renpy.pause()
    
    play sound "explosion1.mp3"
    
    $renpy.pause()

    show bg rea
    with hpunch
    play music "tark1.ogg"
    
    m "Urrrghhh...."
    
    "Je...me sens pas bien du tout..."
    
    "Je suis dans une drôle de salle, devant moi, un tas de composants informatiques parsèment une salle métalisée."
    
    "D'autre part, je possède une envie de vomir irrépressible. Je...."
    
    show bg rea
    with hpunch
    
    "Quand je relève la tête, une figure approche peu à peu, je n'arrive pas à la discerner."
    
    z "Réveillée ?"
    
    "Uurgghhh."
    
    show lyna at right
    with dissolve
    
    "Une jeune femme aux cheveux blonds très clairs s'approche de moi, avec un sourire aux lèvres, dans son autre main, une bouteille d'eau."
    
    z "Euh....coucou, tu viens juste de réaparaître."
    
    ly "Moi c'est Lyna, et euh.. Bienvenue au purgatoire."
    
    m "Au..purgatoire ?"
    
    ly "C'est...un peu compliqué, tu es morte disons. Et uh, tu as..revécu ?"
    
    m "Mais, ou suis je ?"
    
    ly "Toujours...sur le Saylent, oui. Disons juste, que les choses sont un peu plus compliquées."
    
    m "Comment ça ?"
    
    ly "Nous sommes...., enfin, complétement perdus dans l'espace. Aucune idée d'ou nous sommes."
    
    m "Attendez..."
    
    m "C'est pas possible..."
    
    "Tout cela est incohérent, il y a encore..10 minutes, je buvais un verre de Zalis avec mon amie Chloé..."
    
    m "Interface ?"
    
    play sound "Interface.mp3"
    
    inter "Oui ?"
    
    m "Ou sommes nous ?"
    
    play sound "Interface.mp3"
    
    inter "Donnée indisponible."
    
    m "Comment ça ?"
    
    play sound "Interface.mp3"
    
    inter "Donnée indisponible."
    
    "La jeune femme se prend d'un petit rire de moquerie."
    
    ly "Désolée...on a vraiment essayé."
    
    "Elle me tend une bouteille d'eau à présent."
    
    ly "Tu as peut être soif, les gens ont souvent soif en sortant de là..je crois."
    
    "Il était vrai. Je me saisis de la bouteille d'eau avant de la dévisser pour vider la moitié de son contenu, tandis que Lyna m'observe avec un air empathique."
    
    ly "Tu me diras quand tu sera prête. Je pourrais t'expliquer plus en détail si tu veux !"
    
    "J'observe autour de moi les câbles bleus et autres machines disparates avant d'acquiescer du regard."
    
    ly "Bien vient avec moi !"
    
    "Elle se met en route, je n'ai d'autre choix que de la suivre. Elle m'enmène ainsi, dans un premier ascensceur, puis un second, visiblement dans une sorte d'hopîtal abandonné, à moitié détruit."
    
    hide lyna
    show bg tark
    with fade
    "Nous arrivons cependant enfin au niveau d'un très large couloir, ou un homme blond semble nous attendre."
    hide lyna
    show veost at right
    with dissolve
    z "Ahahaha ! Une nouvelle ! Une scientifique pour Saytech ?"
    
    "L'homme en question est un blond d'un air hautain, portant une blouse de scientifique sur laquelle la lettre S est brodée au niveau de sa poîtrine. Il porte des petites lunettes de scientifiques."
    
    hide veost
    with dissolve
    show lyna at right
    with dissolve
    ly "Eh, attends un peu, Veos, elle vient seulement d'arriver...."
    
    hide lyna
    with dissolve
    show veost at right
    with dissolve
    
    v "Mais ma jolie, la science n'attends pas !"
    
    hide veost
    with dissolve
    show lyna at right
    with dissolve
    ly "Mais écoute, on va pas demander à... Ah mais, je t'ai même pas demandé ton nom !"
        
    m "%(player)s, moi c'est %(player)s..."
    
    ly "On va pas tout de suite demander à %(player)s de rejoindre Saytech, une chose après l'autre !"
    
    if player == "Lyna":
        ly "D'ailleurs c'est Marrant, tu portes le même prénom que moi !"
    
    hide lyna
    with dissolve
    show veost at right
    with dissolve
    
    "Veos semble soudainement prendre son menton en main, pris d'une hésitation visible."
    
    v "Mmhh Moui... disons."
    
    "Il semble alors reprendre sa route, un air un peu déçu."
    hide veost
    with dissolve
    
    v "Mais si tu es scientifique, hésite pas à rejoindre Saytech !"
    
    show lyna at right
    with dissolve
    
    "Lyna semble prise d'un petit rire."
    
    ly "Ahah, désolée, il changera jamais Veos, toujours et seulement la science en vue."
    
    "Elle joint ses main, semblant en train de préparer une explication."
    
    ly "Bon du coup comment dire.... Il y a ...quelques mois, le vaisseau a eu un problème."
    
    ly "Une très grande partie est détruite et nous survivons dans son épave, ce qu'il reste du vaisseau."
    
    ly "Par chance ou malchance, nous sommes devenus immortels...Et la mort..ne fait que nous ramener dans la salle de réapparition ou tu es arrivée."
    
    ly "Depuis disons qu'on cherche un moyen de revenir vers la Voie, mais surtout de survivre."
        
    ly "Ca va, tu as compris ou tu as des question ? Désolée si j'explique mal..."
    
    jump menutark1
    
label menutark1:
        
    menu:
        
        
        "Mais, ou se trouve le commandement ?" if tarko1 == False:
            jump tarkoo1
        
        
        "Et aucun signe des secours ?" if tarko2 == False:
            jump tarkoo2
            
        
        "Combien de survivants il y a t'il ?" if tarko3 == False:
            jump tarkoo3
            
         
        "Qu'est il arrivé aux Intelligences ?" if tarko4 == True:
            jump tarkoo4
            
        "Non, je pense que c'est bon.":
            jump Tarkoza2
            
label tarkoo1:
    
    m "Mais, ou se trouve le commandement ?"
    
    ly "A vrai dire, les rares humains du commandement sont soit introuvables, soient devenus inaptes. Et le commandement..des Intelligences..."
    
    ly "Disons pour le moment qu'il vaut mieux pas les croiser."
    $ tarko1= True
    $ tarko4 = True
    
    jump menutark1
    
label tarkoo2:
    
    m "Et aucun signe des secours ?" 
    
    ly "Absolument aucun. Désolée, on a essayé pourtant, mais on semble complétement hors de la voie."
    
    $ tarko2 = True
    
    jump menutark1
    
label tarkoo3:
    
    m "Combien de survivants il y a t'il ?"
    
    ly "Une centaine environ, mais on ne tient pas un registre correct, c'est assez compliqué disons."
    
    ly "Une part sort de nulle part, l'autre disparaît, c'est un enfer de tenir les comptes."
    
    $ tarko3 = True
    
    jump menutark1
    
label tarkoo4:
    
    m "Qu'est il arrivé aux Intelligences ?"
    
    "Elle soupire visiblement d'un air effrayé."
    
    ly "C'est  compliqué, mais elles sont devenues toutes plus ou moins hostiles envers nous. Ce qui est évidemmment pas pratique.."
    
    ly "Si tu croises un KT8, fuis, c'est tout."
    
    $ tarko4 = False
    
    jump menutark1
    
label Tarkoza2:
    
    m "Non, je pense que c'est bon."
    
    ly "Soit, tu me diras si besoin alors."
    
    ly "Bon, il y a plus qu'à te faire visiter les lieux."
    
    ly "On va aller vers les cha-."
    
    "L'interphone de Lyna grésille soudainement, le peu de distance qui me sépare de Lyna me permet d'entendre le contenu du message."
    
    "{i}Hey Lyna ? Ici Tenworks, j'aurai besoin d'aide en bas au niveau des bas-fonds, tu peux venir ?{/i}"
    
    ly "Ah bien, ça te fera une introduction au final, vient avec moi !"
    
    ly "{i}Bien reçu Tenworks, j'ammène une nouvelle avec moi.{/i}"
    
    hide lyna
    
    "Nous parcourons donc plusieurs mètres. j'ai à peine le temps de voir une gare vers une autre zone du vaisseau, ainsi qu'une large place centrale ou des gens discutent de bon coeur."
    
    "Lyna m'entraîne enfin près d'un conduit de maintenance, disposant d'un large monte-charge que nous empruntons, en direction du bas."
    
    show bg usine
    with fade
    
    "Nous arrivons après quelques couloirs peu éclairés, au sein d'une large salle métallique comprenant diverses machines. Là, un nerfès en tenue de travail, un bandage sur le bras se dirige vers nous, pointant un tuyau au sol."
    
    show tenworks at right
    with dissolve
    
    ten "Hey salut, moi c'est Tenworks, vous pourriez pas m'aider ?"
    
    ten "C'est que mon bras est un peu foutu, vous voyez ?"
    
    hide tenworks
    with dissolve
    show lyna at right
    with dissolve
    
    ly "Bien sûr, qu'est ce que l'on peut faire ?"
    
    hide lyna
    with dissolve
    show tenworks at right
    with dissolve
    
    ten "Eh bien, il y a au sol, un tuyau de métal, ce serait pour le bouger et l'accrocher au système de ventilation, l'ancien est pété."
    
    "Effectivement, le tuyau semble cassé, il apparaît possible de le remplacer."
    
    hide tenworks
    with dissolve
    
    "Je m'approche donc du tuyau, que je soulève de mes deux bras, son poids est impossible à porter seule."
    show lyna at right
    with dissolve
    ly "Attends, je t'aide !"
    
    "Elle vient donc porter l'autre partie du tuyau avec une facilité déconcertante. Il apparaît clair que les passagers du vaisseaux ont du s'endurcir avec le temps."
    
    "Nous parvenons donc à installer le tuyeau, en le fixant à l'aide de barre métalliques et en le vissant au reste de la tuyauterie, avec l'aide de Tenworks."
    
    hide lyna
    with dissolve
    show tenworks at right
    with dissolve
    
    ten "Merci hein ! D'ailleurs la nouvelle, c'est quoi ton nom ?"
    
    m "Oh, moi c'est %(player)s !"
    
    if player == "Lyna":
        ten "Eh c'est marrant, on a deux chieuses maintenant."
        hide tenworks
        show lyna at right
        with dissolve
        
        ly "Très drôle.."
        
        hide lyna
        show tenworks at right 
        
    if player == "Tenworks":
         ten "Eh bien, c'est marrant, mon prénom est pas sensé être faire féminin !"
         
    if player == "Lurek":
         ten "Eh bien, une future révolutionnaire en herbe alors !"
        
    ten "En tout cas ravi de te rencontrer."

    m "De même !"
    
    ten "Mais je suppose que vous avez à faire non ?"
    
    hide tenworks
    with dissolve
    show lyna at right
    with dissolve
    
    ly "Pas spécifiquement, je cherche plus à l'intégrer un peu au vaisseau, tu vois ?"
    
    hide lyna
    with dissolve
    show tenworks at right
    with dissolve
    
    ten "Ouais je vois, à la rigueur, je crois que l'autre cherche de l'aide au niveau de la serre, vous pourriez aller voir ça ?"
    
    hide tenworks
    with dissolve
    show lyna at right
    with dissolve
    
    ly "Oui, puis bon, ce sera un coin plus joli que les bas fonds, sans nul doute."
    
    hide lyna
    with dissolve
    show tenworks at right
    with dissolve
    
    "Tenworks semble rire un peu, comme amusé par la remarque de Lyna."
    
    ten "On s'y fait en réalité, c'est juste vous en haut qui comprennez pas !"
    
    hide tenworks
    with dissolve
    show lyna at right
    with dissolve
    
    "Elle répond avec un rire visiblement moins franc."
    
    ly "Ouais c'est ça, allez, tardons pas trop, %(player)s !" 
    
    "Elle part donc prestante, dans la direction du monte charge."
    
    hide lyna
    with dissolve
    show bg tark
    with fade
    
    "Nous repartons donc à travers les couloirs du vaisseau, marchant pendant ce qui semble être une éternité."
    
    "Nous parvenons enfin, dans une grande salle très éclairée. Une rapide observation de Lyna me fait comprendre qu'elle ne semble pas à l'aise ici."
    
    show bg serre2
    with fade
    stop music
    play music "ss13title2.ogg"
    
    "l'endroit semble être un large parc, disposant de plantes, bancs, décorations et amménagements divers."
    
    "Au plafond, le géant ciel holographique baigne le lieu d'un soleil artificiel qui dans ce vaisseau, donne une couleur irréelle."
    
    "Non loin loin de là, un Harle semble attendre, dans ce qui ressemble à un champ ouvragé, vers lequel se dirige assurèment Lyna."
    
    "Je la suis donc, de peur de me perdre dans les couloirs gigantesques du vaisseau."
    
    show bg serre
    with fade
    
    "Le harle approche donc de nous deux, l'air joyeux."
     
    show nekobi at right
    with dissolve
    
    ne "Ah ! Des gens, vous pouvoir aider ?"
    
    "Il parle avec difficulté, semblant peu habitué à la langue commune. Il tend le bras vers une large brouette."
    
    ne "Apporter ça place centrale, Manger pour tout le monde."
    
    hide nekobi
    with dissolve
    show lyna at right
    with dissolve
    
    ly "Ah, c'est juste ça, tant mieux, ce sera rapide.."
    
    "Lyna se tourne vers moi, l'air interrogative, un peu implorante."
    
    ly "tu veux pas t'occuper de ça pour moi ? J'ai peut être à faire, et puis tu y trouveras des gens à rencontrer."
    
    menu:
        
        "Oui, je m'occupe de ça !":
            jump lynaOUI
        
        "Boah, j'ai assez aidé comme ça non ?":
            jump lynaNON
            $ choicelyna = False
            
label lynaOUI:
    
    m "Oui, je m'occupe de ça !"
    
    ly "Super, ça m'arrange pas mal je dois dire ! Faut juste aller à l'endroit central ou nous sommes passées plusieurs fois, tu te souviens ?"
    
    "J'acquiesce rapidement du chef."
    
    ly "Très bien alors, on se verra un de ces quatre !"
    
    hide lyna
    with dissolve
    
    "Je prends donc la brouette dans les mains, elle contient effectivement un ballot de pains de fortune."
    
    "Je la fais rouler ainsi pendant de longues minutes jusqu'à enfin atteindre la grande salle centrale."
    
    show bg sallecent
    with fade
    
    "Là de nombreuses personnes sont présentes, peu portant attention à mon arrivée, à l'exception d'une, habillée d'un air lègérement gothique."
    
    show syrianne at right
    with dissolve
    
    z "Heyyyyy ! Salut ! Je peux te piquer un morceau de pain ?"
    
    "Elle se tient les deux mains sur les pans de la brouette, m'observant de ses deux yeux manifestement non naturel, une opération ou des lentilles ? Je n'arrive pas à voir d'ici."
    
    m "Uuuh, je ne sais pas, je suppose, on m'a dit d'apporter ça ici."
    
    z "Cool !"
    
    "Sans plus attendre, elle penche la main dans la brouette, récupèrant un pain, qu'elle dévore immédiatement sans attendre."
    
    slol "Archmg...Au fait..Moi ch'est Chyrianne, et toi ?"
    
    m "Moi c'est... %(player)s-"
    
    slol "Cool, ouais t'es la nouvelle que l'on peut voir sur l'interphone."
    
    if player == "Syrianne":
        s "C'est marrant d'ailleurs que tu portes mon prénom."
        
        "Elle me tend une boîte noire bien fermée, que je prends avec hésitation avant de la mettre dans mon sac."
        
        s "Cadeau de la maison pour une soeur de prénom, utilise ça en cas de danger."
        
        $ pistol = True
    
    "Je regarde mon interphone, remarquant que je suis toujours connectée au réseau, qui me permet de voir les gens actuellement connectés dans cette section du vaisseau et actifs."
    
    "Une vingtaine-trentaine de nom apparaissent, celui de Lyna, Veos, Tenworks et enfin Syrianne, devant moi."
    
    s "Alors tu fais quoi dans la vie toi ?"
    
    m "Ah euh, j'étais vraiment juste là pour me reposer, prendre des vacances quoi !"
    
    s "Compréhensible, ouais, je faisais ça aussi en vrai."
    
    s "Mchai's du coup, tu as pu voir un peu le vaisseau ?"
    
    m "Oui, Lyna a pu me faire visiter, c'est sympa, enfin, ça a l'air."
    
    s "Oh, c'est que tu as juste pas encore eu d'emmerdes. Croit moi ça arrive, presque tout le temps, probablement encore aujourd'hui."
    
    "Je la regarde, elle ne semble pas particulièrement effrayée, les problèmes sont ils si fréquents ?"
    
    s "Pas besoin de me dévisager comme ça, à force, on s'y fait, tu t'y fera, comme tout le monde."
    
    if pistol == False:
        s "Avant de partir du coup, je vais jouer à un petit jeu avec toi."
        
        s "Quelle compagnie a construit le CT8 Saylent, mh ?"
        
        menu: 
        
             "La compagnie... Erena ?":
                 jump syrisuite
                        
             "la compagnie Saytech !":
                 jump syrisuite
             "La compagnie WhiteHole ?":
                 $ pistol = True
             "La compagnie CTcorp":
                 jump syrisuite
                
        label syrisuite:
                
            if pistol == True:
                s "Bravo ! c'est bien la compagnie WhiteHole ! tu as gagné ce truc !"
                    
                "Elle me tend un boîte noire, que je met rapidement dans mon sac."
            if pistol == False:
                "Eh non !!!! Désolée ma jolie, pas de cadeau pour toi !"
                

            
    
    s "Bon allez, c'était fun, merci pour le pain, on se croise plus tard !"
    
    hide syrianne
    with dissolve
    
    "Je me retrouve donc à rien devoir faire, je suppose que je peux partir explorer."
    
    show bg tark
    with fade
    
    "Je me balade dans les couloirs, jusqu'à trouver une gigantesque salle."
    
    show bg zone42
    with fade
    
    "La...Zone 4 ?"
    
    "je m'avance au sein de cette grande salle.."
    
    jump zone42

    
label lynaNON:
    
    m "Boah, j'ai assez aidé comme ça non ?"
    
    ly "Ah bon, bien, je m'occupe de ça, je suppose."
    
    "Elle semble partir avec un air un peu effrayé, semble t'il, fuyant rapidement la serre avec la charette, cependant."
    
    hide lyna
    with dissolve
    
    "Je me retrouve libre, au sein du vaisseau, laissant les champs à leur place."
    
    "Je m'approche d'une des grandes portes du parc, entrant dans le couloir s'y trouvant."
    
    show bg serrechambre
    
    "Il s'agit d'une grande antichambre, des salles ressemblant à des logements bordent celle ci."
    
    "Je m'avance donc, dans cette zone, quand un viel homme m'interpèle depuis un coin."
    
    show nodens at right
    with dissolve
    
    z "Bonjour ?"
    
    "Il me regarde avec un air intrigué."
    
    m "Bon..bonjour ?"
    
    "Il finit par me tendre la main, un air tendre"
    
    no "Moi c'est Nodens, enchanté. Et vous ?"
    
    m "Moi c'est.. %(player)s.."
    
    no "Enchanté, %(player)s."
    
    m "De même, je suppose ?"
    
    no "Nouvelle sur le vaisseau, je présume ?"
    
    m "Oui, enfin, je...-"
    
    "Il semble pris d'une pensée."
    
    no "Oh effectivement, vous avez été sur le vaisseau avant tout ça, oui, ma question n'avait pas de sens, excusez moi."
    
    m "Pas de souci, je suppose."
    
    no "Et du coup, on a pu vous présenter un peu le vaisseau ? Mh ?"
    
    m "Vaguement, j'avoue n'avoir eu qu'une présentation sommaire."
    
    no "Eh bien réglons ça. Ici nous sommes dans la Serre, c'est plus ou moins la zone de vie sympathique du vaisseau, ou se trouvent les chambres et le parc."
    
    no "Une autre aile comprend la zone médicale, dont tu viens probablement, ainsi qu'un accès vers Saytech, la zone scientifique."
    
    no "Une autre mène vers une zone commerciale, qui se termine par le poste du FSA, la securité du vaisseau."
    
    no "Enfin la dernière, comprend un accès vers la zone politique, une baie externe, une blibliothèque, un accès sous-terrain."
    
    no "Le mieux pour toi, c'est encore de faire un plan du vaisseau au fur et à mesure que tu te balades, même si, moi et un groupe que nous avosn formé travaille là dessus."
    
    m "Un groupe ?"
    
    no "Oui, une sorte de groupe d'entraide communautaire, qui se nomme le Coeur, enfin, je vais pas t'enbrigader aussi vite ahah, tu verras en temps voulu."
    
    m "Je vois, j'y réfléchirai !"
    
    no "Non puis enfin, il y a de nombreux accès vers une ventilation, principalement au niveau de la zone 42, c'est aussi une zone intéressante, surtout en cas de danger."
    
    m "Et ou je devrais aller pour commencer ?"
    
    no "Ca dépend vraiment de toi, de ce que tu veux faire, au début, promène toi, tu verras bien. Sur ce, je dois me rendre quelque part, à plus tard !"
    
    hide nodens
    with dissolve
    
    "Il repart donc, en direction d'une salle fermée par une porte à code, à l'arrière. Je retourne donc dans la serre."
    
    show bg serre2
    with fade
    
    "De là, je me redirige dans les couloirs principaux de sorte à me promener, allant depuis la salle centrale, me diriger vers une des ailes."
    
    show bg tark
    with fade
    
    "Je commence à me diriger dans un plus petit couloir, qui mène à une très grande salle..."
    
    show bg zone42
    with fade
    
    "Il s'agit d'une énorme salle de stockage, avec un texte zone 42 dont le 2 manque, qui se tient à l'arrière de la salle."
    
    "Il s'agit probablement de la grande salle de stockage dont Nodens avait parlé. Je commence alors, à m'avancer dans celle ci."
    
    jump zone42
    
label zone42:
    
    "Seul le vombrissement des machines m'accompagne, alors que je m'approche d'une grande tour métallisée."
    
    play sound "ambidanger.ogg"
    
    "Je commence à m'approcher du coin de celle ci."
    
    jump rea2
    
label rea2:
    
    hide screen battle1
    hide lanth
    stop music
    window hide
    show bg black
    play sound "explosion1.mp3"
    
    $renpy.pause()
    
    show bg rea
    play audio "bang.ogg"
    
    "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAH{nw}"
    
    show bg tark
    play audio "bang.ogg"
    
    "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAH{nw}"
    
    show bg usine
    play audio "bang.ogg"
    
    "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAH{nw}"
    
    show bg serre2
    play audio "bang.ogg"
    
    "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAH{nw}"
    
    show bg serre
    play audio "bang.ogg"
    
    "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAH{nw}"
    
    
    show bg rea
    with fade
    
    "Que..Que s'est il passé ?"
    
    show bg rea
    with hpunch
    play music "space.ogg"
    
    "Ma tête, ma tête est littéralement en feu, je ne comprends rien à ce qu'il m'arrive ?"
    
    show bg rea
    with hpunch
    
    "Autour de moi, la même salle de réaparition, en moi, le sentiment de ressenter des couteaux transperçer chaque part de mon corps."
    
    show bg rea
    with hpunch
    
    "Le monde est encore flou, des bruits stridents, des bruits de pas au loin, qui résonnent, qui résonnent, ça n'en finit pas."
    
    show bg rea
    with hpunch
    
    "Je...je...."
    
    show bg black
    $renpy.pause()
    show bg rea
    with fade
    
    "Quand je reviens à moi, je suis étalée au sol, j'ai du tomber dans le coma, je vais un peu mieux, mais la douleur lancinente est toujours présente, continuellement, inaltérable."
    
    "Je me lève et je descend lentement le montecharge."
    
    if pistol == True:
        "Je sors alors doucement la boîte que m'a donné l'autre fille."
        
        "A l'intérieur je trouve un pistolet, d'un noir mat, je le range immédiatement, bien qu'il puisse peut être m'être utile."
        
    show bg tark
    with fade
    
    "Je me retrouve dans les couloirs du vaisseau, personne à l'horizon ne semble se montrer."
    
    "Je décide de retourner vers la zone ou tout est devenu noir, comprendre ce qui est arrivé."
    
    if pistol == False:
        "Au sol, une barre de fer me fait de l'oeil, je la prend, afin d'assurer ma protection au cas ou."
        
    if pistol == True:
        "Je vois au sol une barre en fer, je ne la prends pas, j'ai toujours mon pistolet au cas ou."
        
    "Je continue d'avancer donc, jusqu'à trouver la zone ou tout avait disparu."
    
    show bg zone42
    with fade
    
    "Là, je contourne prudemment la tour en métal..."
    
    show lanth at right
    with fade
    
    "Là se trouve visiblement un KT8 que je ne peine pas à reconnaître, Lanthinium, l'un des officiers du vaisseau."
    
    "Au sol, le corps d'un officier du FSA semble geindre au sol."
    
    "Il se relève du corps, se mettant debout, me faisant face."
    
    lan "Oh, c'est point le meilleur moment pour venir, passager, mais soit."
    
    "Il se penche au sol pour ramasser une barre en métal.."
    
    $ combatmusic = renpy.random.randint(1, 4)
    
    if combatmusic == 1:
        play music "Grave.mp3"
    if combatmusic == 2:
        play music "comb1.ogg"
    if combatmusic == 3:
        play music "comb2.ogg"
    if combatmusic == 4:
        play music "comb3.ogg"

    
    $ lanth_max_hp = 50
    $ player_max_hp = 50
    $ lanth_hp = lanth_max_hp
    $ player_hp = player_max_hp
    
    show screen battle1
    
    while (lanth_hp > 0) and (player_hp > 0):
        
        menu:
            "Utiliser le pistolet pour tirer sur Lanthinium" if pistol == True and paralysie == False:
                $ esquive = False
                play sound "bang2.ogg"
                $ pistol_dam = renpy.random.randint(0, 6)
                if pistol_dam == 0:
                    "Mince j'ai loupé ma cible !"
                if pistol_dam == 1:
                    $ lanth_hp -= pistol_dam
                    hide lanth
                    show lanthred at right
                    with hpunch
                    play sound "cyborg.ogg"
                    $ landamage = renpy.random.randint(1, 3)
                    if landamage == 1:
                        lan "Vous aller regretter ca, vous en faites pas."
                    if landamage == 2:
                        lan "Bien tente, mais c'est pas ca qui va m'arreter."
                    if landamage == 3:
                        lan "Vous finirez par comprendre, que ca ne sert a rien de lutter, votre tombeau est ici."
                    hide lanthred
                    show lanth at right
                        
                if pistol_dam == 2:
                    $ lanth_hp -= pistol_dam
                    $ landamage = renpy.random.randint(1, 3)
                    hide lanth
                    show lanthred at right
                    with hpunch
                    play sound "cyborg.ogg"
                    if landamage == 1:
                        lan "Vous aller regretter ca, vous en faites pas."
                    if landamage == 2:
                        lan "Bien tente, mais c'est pas ca qui va m'arreter."
                    if landamage == 3:
                        lan "Vous finirez par comprendre, que ca ne sert a rien de lutter, votre tombeau est ici."
                    hide lanthred
                    show lanth at right
                if pistol_dam == 3:
                    $ lanth_hp -= pistol_dam
                    $ landamage = renpy.random.randint(1, 3)
                    hide lanth
                    show lanthred at right
                    with hpunch
                    play sound "cyborg.ogg"
                    if landamage == 1:
                        lan "Vous aller regretter ca, vous en faites pas."
                    if landamage == 2:
                        lan "Bien tente, mais c'est pas ca qui va m'arreter."
                    if landamage == 3:
                        lan "Vous finirez par comprendre, que ca ne sert a rien de lutter, votre tombeau est ici."
                    hide lanthred
                    show lanth at right
                if pistol_dam == 4:
                    $ lanth_hp -= pistol_dam
                    $ landamage = renpy.random.randint(1, 3)
                    hide lanth
                    show lanthred at right
                    with hpunch
                    play sound "cyborg.ogg"
                    if landamage == 1:
                        lan "Vous aller regretter ca, vous en faîtes pas."
                    if landamage == 2:
                        lan "Bien tente, mais c'est pas ca qui va m'arreter."
                    if landamage == 3:
                        lan "Vous finirez par comprendre, que ca ne sert a rien de lutter, votre tombeau est ici."
                    hide lanthred
                    show lanth at right
                if pistol_dam == 5:
                    $ lanth_hp -= pistol_dam
                    $ landamage = renpy.random.randint(1, 3)
                    hide lanth
                    show lanthred at right
                    with hpunch
                    play sound "cyborg.ogg"
                    if landamage == 1:
                        lan "Vous aller regretter ca, vous en faites pas."
                    if landamage == 2:
                        lan "Bien tente, mais c'est pas ca qui va m'arrêter."
                    if landamage == 3:
                        lan "Vous finirez par comprendre, que ca ne sert a rien de lutter, votre tombeau est ici."
                    hide lanthred
                    show lanth at right
                if pistol_dam == 6:
                    $ lanth_hp -= pistol_dam
                    $ landamage = renpy.random.randint(1, 3)
                    hide lanth
                    show lanthred at right
                    with hpunch
                    play sound "cyborg.ogg"
                    if landamage == 1:
                        lan "Vous aller regretter ca, vous en faites pas."
                    if landamage == 2:
                        lan "Bien tente, mais c'est pas ca qui va m'arreter."
                    if landamage == 3:
                        lan "Vous finirez par comprendre, que ca ne sert a rien de lutter, votre tombeau est ici."
                    hide lanthred
                    show lanth at right
                    
                    
                    
                    
                
            "Utiliser la barre de fer pour frapper Lanthinium" if pistol == False and paralysie == False:
                $ esquive = False
                play sound "bangmet.ogg"
                $ coup_dam = renpy.random.randint(1, 3)
                $ lanth_hp -= coup_dam
                $ landamage2 = renpy.random.randint(1, 3)
                hide lanth
                show lanthred at right
                with hpunch
                play sound "cyborg.ogg"
                if landamage2 == 1:
                    lan "Vous aller regretter ca, vous en faites pas."
                if landamage2 == 2:
                    lan "Bien tente, mais c'est pas ca qui va m'arreter."
                if landamage2 == 3:
                    lan "Vous finirez par comprendre, que ca ne sert a rien de lutter, votre tombeau est ici."
                hide lanthred
                show lanth at right
            "Reculer pour éviter une attaque de Lanthinium":
                $ esquive = True
                "Je me place en retrait."
                
            "Tenter de négocier avec Lanthinium":
                $ esquive = False
                $ hahaha = renpy.random.randint(1, 6)
                
                if hahaha == 1:
                    m "Attendez, on peut probablement trouver un compromis !"
                    
                    lan "Un compromis ? Je ne fais pas compromis."
                if hahaha == 2:
                    m "S'il vous plaît, ne me tuez pas !"
                    
                    lan "Je n'ai aucune raison de ne pas le faire."
                if hahaha == 3:
                    m "Je peux probablement vous aider, attendez !"
                    
                    lan "Eh bien, aidez moi en mourrant, c'est tout ce que je demande."
                if hahaha == 4:
                    m "Reculez, ou je vais devoir vous tuer !"
                    
                    lan "Comme si vous aviez une chance."
                if hahaha == 5:
                    m "Mais, attendez, en tant que KT8, vous devez aider le vaisseau !"
                    
                    lan "Votre mort entre dans un plan global pour aider le vaisseau."
                if hahaha == 6:
                    m "Qu'est ce que vous voulez au fond !!"
                    
                    lan "Votre mort immediate, rien de plus simple."
        if paralysie == True:
            "Mon bras commence tout juste à récupérer..."
            $ paralysie = False
        $ lanth_action = renpy.random.randint(1, 3)
        
        if lanth_action == 1:
            $ double_luck = renpy.random.randint(1, 2)
            
            if double_luck == 1:
                "Lanth tente d'attaquer, mince ! mais il rate !"
            if double_luck == 2:
                if esquive == True:
                    $ lanth_damage2 = renpy.random.randint(1, 3)
                    play sound "impact.mp3"
                    $ player_hp -= lanth_damage2
                    "Argh, il a anticipé mon esquive, et réussi à m'avoir avec sa barre, mais j'ai pu limiter les dégats ! (Dégats - [lanth_damage2] dégats"
                if esquive == False:
                    "Il prend son temps et me vise avec un blaster integré !"
                    $ chancedudestin = renpy.random.randint(1, 2)
                    
                    if chancedudestin == 1:
                        "Par chance, il rate, je n'ai rien !"
                    if chancedudestin == 2:
                        "Merde ! Il a touché mon bras, je ne peux plus le bouger !"
                        $ paralysie = True
                        
                    
            
                
        if lanth_action == 2:
            if esquive == True:
                "Ouais ! J'ai bien fait de me préparer à esquiver, il vient de me rater."
            if esquive == False:
                $ lanth_damage = renpy.random.randint(1, 8)
                play sound "impact.mp3"
                $ player_hp -= lanth_damage
                "Arrgh, il a réussi à me frapper avec sa barre en métal ! (Dégats - [lanth_damage] dégats"
        if lanth_action == 3:
            $ tauntlan = renpy.random.randint(1, 4)
            
            if tauntlan == 1:
                lan "Rendez vous tout de suite a la mort, ce sera plus rapide."
            if tauntlan == 2:
                lan "Pathetique."
            if tauntlan == 3:
                lan "Comprenez bien que je ressens pas la douleur, mais vous oui, c'est perdu d'avance."
            if tauntlan == 4:
                lan "Allez y, continuez, ca ne sert à rien."
                
    hide screen battle1
    
    if lanth_hp <= 0:
        if player_hp <= 0:
            "Double KO."
            jump rea2
            
        else:
            m "J'ai...réussi à le mettre au sol..."
            jump tark3
            
    if player_hp <=0:
        jump rea2
    
label tark3:
    
    "Ahahah win la suite plus tard les bébous !"
    
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
    
    
    
    
    
    
    
    
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
         
    
    
        
        
    
         
    

        
        
    
            
        
    
    

    
    
    
    
    
    return
    
    
    
    
    
    


     
return

        
    
