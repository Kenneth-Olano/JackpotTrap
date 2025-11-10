# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define my_dissolve = Dissolve(0.3)  
define morale = 0
image thewinningstage = Movie(size=(1920, 1080), play="videos/test.webm", loop=False)

transform left_zoomed:
    xpos 0
    ypos 0
    xanchor 0.0
    yanchor 0.0
    zoom 5.0

transform right_zoomed:
    xpos 1920  # or config.screen_width
    ypos 0
    xanchor 1.0  # align right edge of image to xpos
    yanchor 0.0
    zoom 5.0

define kenneth = Character(
    window_style="window_ken",
    namebox_style="namebox_ken",
    what_style="ken_text",
)

define system = Character(
    window_style="window_system",
    namebox_style="namebox_system",
    what_style="system_text",
    # show_two_window=True
)

define mayeth = Character(
    window_style="window_mayeth",
    namebox_style="namebox_mayeth",
    what_style="mayeth_text",
)

define marco = Character(
    window_style="window_marco",
    namebox_style="namebox_marco",
    what_style="marco_text",
)

image Kenneth home neutral:
    "kenneth/ken_home_neutral.png"
    xalign 0
    zoom 0.25

image Kenneth home happy:
    "kenneth/ken_home_happy.png"
    xalign 0
    zoom 0.25

image Kenneth home frustrated:
    "kenneth/ken_home_frustrated.png"
    xalign 0
    zoom 0.25

image Kenneth home sad:
    "kenneth/ken_home_sad.png"
    xalign 0
    zoom 0.25

image Kenneth school neutral:
    "kenneth/ken_school_neutral.png"
    xalign 0
    zoom 0.25

image Kenneth school frustrated:
    "kenneth/ken_school_frustrated.png"
    xalign 0
    zoom 0.25

image Kenneth school happy:
    "kenneth/ken_school_happy.png"
    xalign 0
    zoom 0.25

image Mayeth:
    "mayeth/mayeth.png"
    xalign 1
    zoom 0.25

image Marco:
    "marco/marco.png"
    xalign 1
    zoom 0.25



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene room day

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    # These display lines of dialogue.

    system "Alarm blares. Kenneth groans and reaches for his cracked phone." with my_dissolve

    show Kenneth home neutral at left_zoomed with my_dissolve

    kenneth "Ugh… gusto ko pang matulog." with my_dissolve

    kenneth "Ang bango ah… ano kayang niluluto ni Mama?"

    kenneth "Sige, prepare na nga ako para makakain na."

    scene kitchen day with my_dissolve

    show Mayeth at right_zoomed with my_dissolve

    mayeth "Kenneth, bumaba ka na. Kain na tayo." with my_dissolve

    show Kenneth school neutral at left_zoomed with my_dissolve

    kenneth "Opo, ma." with my_dissolve

    system "They sit together at the table." with my_dissolve

    mayeth "Kamusta naman ang school, anak? Anong mga ginawa niyo sa klase?" with my_dissolve

    kenneth "Okay lang naman po." with my_dissolve

    mayeth "Alam mo ba si Kirby, yung pinsan mo? Nakapagtapos na. Ang sipag talaga nun, proud na proud ang \nTita Joy mo sa kanya." with my_dissolve

    mayeth "Sana ganyan ka rin, anak. Mag-aral kang mabuti, ha? 'Wag ka na sanang sumama sa mga barkada mong baka manghila lang pababa."

    show Kenneth school frustrated at left_zoomed with my_dissolve

    kenneth "(Ito na naman si Mama, umagang-umaga sermon agad.)" with my_dissolve

    show Kenneth school neutral at left_zoomed with my_dissolve

    kenneth "Opo, ma."
    
    mayeth "Eh alam ko naman masipag ka. Mamayang pag-uwi mo, may surpresa ako sa'yo." with my_dissolve

    show Kenneth school happy at left_zoomed with my_dissolve

    kenneth "Talaga po? Ano yun?" with my_dissolve

    mayeth "Basta, mamayang gabi mo na lang malaman. Baka ma-late ka pa." with my_dissolve

    kenneth "Excited na ako… ano kaya yun?" with my_dissolve

    scene school with Fade(0.5, 2, 0.5)

    system "Paldo si Marco kanina, pre! Nanalo na naman sa Scatter ng 10k!" with my_dissolve

    system "Oo nga eh, manlilibre na raw yan!"

    system "Libre! Libre! Libre!"

    show Marco at right_zoomed with my_dissolve

    show Kenneth school neutral at left_zoomed with my_dissolve
    
    marco "Uy Ken, sama ka mamaya. Libre ko na 'to. Para naman 'di ka puro aral lang!" with my_dissolve

    kenneth "Pass muna. May gagawin pa tayo kay Ma'am Santos na video. Ayoko mag-cram eh." with my_dissolve

    marco "Grabe, ang sipag mo talaga. Pero kung magbago isip mo, sumama ka na. Sinuwerte ako kanina." with my_dissolve
  
    kenneth "Sige, pag-iisipan ko. Salamat pre." with my_dissolve

    scene kitchen night with Fade(0.5, 2, 0.5)

    show Mayeth at right_zoomed with my_dissolve

    show Kenneth home neutral at left_zoomed with my_dissolve

    system " Mayeth hands Kenneth a box." with my_dissolve

    mayeth "Ito, anak. Napansin ko kasing sira na yung screen ng phone mo. Baka nahihirapan ka \nnang gumawa ng assignment, baka makatulong 'to." with my_dissolve
   
    show Kenneth home happy at left_zoomed with my_dissolve

    kenneth "Salamat po, Ma! Ang laki ng tulong nito!" with my_dissolve

    mayeth "Pasensya ka na ha, di pa kita mabibilhan ng laptop. Masyadong mahal, gipit pa tayo." with my_dissolve

    kenneth "Okay lang po, Nay. Hindi ko naman po kailangan ngayon at magagawa ko lahat ng requirements ko nang\n maayos dito sa bagong phone ko." with my_dissolve

    kenneth "Thank you po. Iingatan ko 'to, promise."

    kenneth "(Ang bait ni mama, pero mas marami na kaming video editing na activities this semester.\n Kakayanin ko kayang sa phone lang gawin lahat…)"

    scene room night with Fade(0.5, 2, 0.5)

    show Kenneth home neutral at left_zoomed with my_dissolve

    system "\"Play to earn! Mabilis, makulay, masaya! Pwedeng laruin kahit saan!\"" with my_dissolve

    show Kenneth home frustrated at left_zoomed with my_dissolve

    kenneth "Ano ba yan, istorbo. Nag-eedit pa ako." with my_dissolve

    scene room night with Fade(0.5, 2, 0.5)

    show Kenneth home neutral at left_zoomed with my_dissolve

    system "After finishing the project, another ad pops up." with my_dissolve

    kenneth "Hay… wala nga laman GCash ko eh." with my_dissolve

    kenneth "Hmmm... Try lang, libangan lang."

    system "After installing the app, an endorsement appears." with my_dissolve

    system "Maine Dusa: \"Mag-Scatter na! Easy money, big prizes, anytime, anywhere! Approved by PAGCORAP!\"" with my_dissolve

    kenneth "Sige, libangan lang naman. Pa-cash in ako mamaya." with my_dissolve

    scene room night with Fade(0.2, 1, 0.2)

    show Kenneth home neutral at left_zoomed with my_dissolve

    system "JCash: \"You received ₱100 from 093728xxxx\"" with my_dissolve

    show Kenneth home happy at left_zoomed with my_dissolve

    kenneth "Hmmm… tignan nga natin." with my_dissolve

    scene room night with Fade(0.2, 1, 0.2, color="fff")

    show Kenneth home happy at left_zoomed with my_dissolve

    kenneth "Woooow! Grabe! Easy money nga — ₱100 naging ₱1,000?!" with my_dissolve

    system "JCash: \"You received ₱1,000 from Ace Star.\"" with my_dissolve

    # ...
    kenneth "Ayos! Mukhang yayaman ako dito!" with my_dissolve

    scene black with Fade(0.2, 1, 0.2, color="#000")

    $ renpy.movie_cutscene("videos/The Winning Stage.webm", delay=None, loops=0, stop_music=True)

    # 1. Clear the screen (optional, but clean)
    scene white with Fade(0.2, 1, 0.2, color="#fff")

    $ renpy.movie_cutscene("videos/test.webm", delay=None, loops=0, stop_music=True)


    scene room night with Fade(0.2, 1, 0.2, color="#fff")

    show Kenneth home happy at left_zoomed with my_dissolve
    
    kenneth "Grabe. Sino bang mag-aakala na yung ₱100 ko naging ₱30,000? \nMay laptop na ako, may mga bagong gamit pa." with my_dissolve

    ###LOSING STAGE STAGE 2 TITLE CARD HERE

    scene black with Fade(0.2, 1, 0.2, color="#000")

    $ renpy.movie_cutscene("videos/The Losing Stage.webm", delay=None, loops=0, stop_music=True)

    scene kitchen day with my_dissolve

    show Mayeth at right_zoomed with my_dissolve

    show Kenneth home neutral at left_zoomed with my_dissolve

    mayeth "Oh, anak. Kamusta ang school? Baka napapabayaan mo kaka-gala at kaka-cellphone ah." with my_dissolve

    menu:
        "Choose a response:"

        "Lie and say \"Maayos naman po.\"":
            $ morale += -1
            jump bad1

        "Be honest and say \"Medyo bumaba po grades ko, Ma… pero babawi ako.\"":
            show Kenneth home sad at left_zoomed with my_dissolve
            $ morale =+ 1
            jump good1
    
    label bad1:

        mayeth "Mabuti naman anak. Magfocus ka lang sa pag-aaral mo. Nag-aalala lang ako. Bawasan mo na rin ang paglalaro mo ng \nScatter, at baka mapabayaan mo ang pag-aaral mo.." with my_dissolve
        jump continue1

    label good1:
        
        mayeth "Naku, sabi ko na nga ba. Ang dalas mong wala dito sa bahay, at kung nandito ka man ay nakababad ka sa phone na yan." with my_dissolve

        mayeth "Puro ka kasi Scatter, sinasayang mo lang ang pera't oras mo 'dyan!."

        kenneth "Eh Ma, libangan lang naman. At least, hindi na ako nanghihingi ng pera sa'yo, 'di ba?" with my_dissolve

        mayeth "Alam ko. Malaking tulong nga yan… pero huwag mong hayaang lamunin ka niyan." with my_dissolve
        jump continue1

    label continue1:

        scene room night with Fade(0.5, 2, 0.5)

        show Kenneth home frustrated at left_zoomed with my_dissolve

        kenneth "Bwiset! Puro talo na naman ngayon. Dapat mabawi ko." with my_dissolve

        system "He bets again, focused. Then a chat notification pops up." with my_dissolve

        system "TING!" with my_dissolve

        system "Erika: \"Kenneth! Review tayo bukas sa library, ha?\""

    menu:
        "Choose a response:"

        "Swipe her chat notification and continue playing":
            $ morale += -1
            jump bad2

        "Reply and say \"Sige, sama ako bukas.\"":
            show Kenneth home neutral at left_zoomed with my_dissolve
            $ morale =+ 1
            jump continue2

    label bad2:
        system "TING!" with dissolve

        system "Erika: \"May ginagawa ka ba?\"" 

        system "Kenneth loses his bet."

        kenneth "Ughhh! Bwiset!" with my_dissolve

        system "TING!" with dissolve

        system "Erika: \"Huy! Sasama ka ba o hindi? Para makasama ka sa listahan ng reservation ng study room!\""

    menu:
        "Choose a response:"

        "Lash out and say \"Pwede ba, wag ngayon! Badtrip ako.\"":
            $ morale += -1
            jump continue2

        "Agree and say \"Sige, bukas, sasama ako.\"":
            show Kenneth home neutral at left_zoomed with my_dissolve
            $ morale += 1
            jump continue2

    label continue2: 
        scene school with Fade(0.5, 2, 0.5)

        show Marco at right_zoomed with my_dissolve

        show Kenneth school neutral at left_zoomed with my_dissolve

        marco "Ken, tara Scatter ulit, panalo ako kanina!" with my_dissolve

    menu:
        "Choose a response:"

        "Come along and say \"Sige, babawi rin ako. Bwiset kahapon eh, puro talo.\"":
            $ morale += -1
            jump bad3 #gambling animation

        "Decline and say \"Pass muna, kailangan ko mag-aral.\"":
            show Kenneth home neutral at left_zoomed with my_dissolve
            $ morale += 1
            jump good2 #studying animation

    label bad3:
        scene school with Fade(0.5, 2, 0.5)
        jump continue3

    label good2:
        scene school with Fade(0.5, 2, 0.5)
        jump continue3

    label continue3:
        scene kitchen night with Fade(0.5, 2, 0.5)

        show Kenneth home neutral at left_zoomed with my_dissolve

        system "Kenneth looked at his phone." with my_dissolve
    
    menu:
        "Choose a response:"

        "Play Scatter.":
            $ morale += -1
            jump bad4 #gambling animation

        "Study for finals.":
            show Kenneth home neutral at left_zoomed with my_dissolve
            $ morale += 1
            jump continue4 #studying animation

    label bad4:
        show Kenneth home sad at left_zoomed with my_dissolve

        kenneth "Try ko nga ulit… baka malas lang ako kanina at kahapon." with my_dissolve

        system "Kenneth bets 500 pesos..." with my_dissolve

        system "and loses."

        show Kenneth home frustrated at left_zoomed with my_dissolve

        kenneth "Bwiset… ugh, isa pa! Kaya pa 'yan." with my_dissolve

        system "Kenneth bets 2,000 pesos..." with my_dissolve

        system "...and wins it double."

        show Kenneth home happy at left_zoomed with my_dissolve

        kenneth "Ayun! Nabawi rin!" with my_dissolve

        system "Kenneth bets 10,000 pesos..." with my_dissolve

        system "...and loses it all."

        show Kenneth home frustrated at left_zoomed with my_dissolve

        kenneth "Ughhh!" with my_dissolve

        system "Kenneth bets 100 pesos..." with my_dissolve

        show Kenneth home sad at left_zoomed with my_dissolve

        kenneth "Please, please, please! Sana manalo!" with my_dissolve

        system "...and loses it all." with my_dissolve

        system "Scatter: \"! ! ! Insufficient Cash ! ! !\""

        kenneth "Sh*t, wala na akong pera." with my_dissolve

        scene black with Fade(0.2, 1, 0.2, color="#000")

        $ renpy.movie_cutscene("videos/The Desperation Stage.webm", delay=None, loops=0, stop_music=True)
        


        











    

    
    








    










    



    






    


    
    # This ends the game.

    return
