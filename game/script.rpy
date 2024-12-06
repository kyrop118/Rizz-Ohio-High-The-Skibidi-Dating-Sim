# fade in screen title here --> could just be a background highkey
define mc = Character("You", color="#c8ffc8", what_prefix='"', what_suffix='"')
define mci = Character("You", color="#c8ffc8", what_italic=True)
define mcn = Character(None, what_color="#ffee8c")
define nug = Character("???", color="#ffa500", what_prefix='"', what_suffix='"')
define chill = Character("???", color="#b0e0e6", what_prefix='"', what_suffix='"')
define gig = Character("???", color="#cbc3e3", what_prefix='"', what_suffix='"')
define amg = Character("Amongus Imposter", color="#c51111", what_prefix='"', what_suffix='"')
define emo = Character("Edgemund", color="1c1c84", what_prefix='"', what_suffix='"')
define tom = Character("Tomato Boy", color="#ffc0cb", what_prefix='"', what_suffix='"')
define ksi = Character("KSI", color="c8ffc8", what_prefix='"', what_suffix='"')
define quan = Character("Quandale Dingle Fairy", color="#1bfc06", what_prefix='"', what_suffix='"')
define ski = Character("Mr Skibidi Toilet", color="#cabd99", what_prefix='"', what_suffix='"')
define tate = Character("Andrew Tate", color="#d3d3d3", what_prefix='"', what_suffix='"')
define qd = Character("Turkish Quandale Dingle", color = "#ffc881ff", what_prefix='"', what_suffix='"')
define bt = Character("Blue Tie Kid", color="#242ec7", what_prefix='"', what_suffix='"')

label start:
    label prologue:
        stop music fadeout 1.0
        show text "Please be aware that this is a beta.\nThe beta currently only has two major routes." with fade
        pause 1.0
        show text "Please turn your volume on." with fade
        pause 1.0
        show text "Prologue - Day 1" with fade
        pause 1.0
        hide text with fade
        play music "audio/bgm_alarm.mp3" fadein 0.0 volume 0.5
        mcn "A loud alarm blares incessantly on your left, and you flip on your side to shut it off."
        stop music fadeout 1.0
        mci "New walls, a clean white ceiling. . ."
        scene bg bedroom
        with fade
        play music "audio/bgm_symphony.mp3" fadein 1.0 volume 0.5
        mci "It’s been almost a fortnight since I moved to Ohio but. . . I kinda miss Florida already."
        mci "Oh right!"
        mci "Today’s also my first day at Rizz Ohio High!"
        play sound "audio/sfx_blanket.mp3"
        scene bg kitchen
        with fade
        play sound "audio/sfx_stairs.mp3"
        mci "The kitchen hall is strangely empty huh. . ."
        mci "Oh right, Mom and Dad left early in the morning for their trip to Tomato Town. I wonder how they’re doing."
        scene bg breakfast
        with fade
        mci "This breakfast looks so skibidi, but I'm going to be late for school." 
        mcn "You instead just grab a piece of toast."
        stop music
        scene bg neighbourhood
        play music "audio/bgm_buckle.mp3" fadein 1.0 volume 0.5
        with fade
        mcn "You offhandedly check your watch only to find it’s. . . 7:69am??"
        mcn ". . ."
        mcn "Which means you have 11 minutes to make a 20 minute hike. What the sigma."
        mc "Oops kyaaaaaaaah! I'm gonna be late!!"
        mc "Gotta go sonic!"
        show running naruto
        stop music fadeout 1.0
        play music "audio/bgm_running_in_90s.mp3" fadein 1.0 volume 0.5
        mci "Shit shit. . ."
        mci "Shit shit shit shit shit."
        mci "I really hope I’m not late on my first day to-" 
        stop music
        scene black
        play sound "audio/sfx_bicycle_bell.mp3" fadein 0.5 volume 0.5 
        pause 2.0
        play sound "audio/sfx_bike_brake.mp3" fadein 0.5 volume 0.5 
        pause 3.0
        play sound "audio/sfx_fall.mp3" fadein 0.5 volume 0.5
        scene bg neighbourhood with hpunch
        with fade
        play music "audio/bgm_buckle.mp3" fadein 1.0 volume 0.5
        mc "Kyaaaa!!! Are you ok?"
        mci "This guy. . . He somehow braked 3.1415926535 nanoseconds before we collided?!"
        nug "Yuh!! All good vro. Are you okay?"
        mc "Yeah I’m good. I didn’t flinch at all."
        mci "I flinched so hard that my dawgs started gripping the cement lowkey but I’m not admitting that to a guy I just met."
        mc "Is your. . . bike ok?"
        nug "Naw ye don’t worry about my bike he bing chilling."
        nug "I once threw him off the National Museum of the US Air Force and he didn’t get a scratch!!"
        mci "Damn what a sigma."
        mci "That's like +1000 aura."
        mc "Ok. . ."
        nug ":)"
        mc "Do you know where Rizz Ohio High is btw?"
        mc "Today’s my first day."
        nug "Oh for sho vro, I’ll take you there."
        nug "I actually go there as well. Dap me up brother."
        mcn "You go in for a dap, feeling like an alpha."
        nug "Anyways, what's your name?"

    label name_and_addresses_choosing:
        menu:
            "P.Giddy":
                $ mcname = "P. Giddy"
                jump name_ested
            "Skibbitney":
                $ mcname = "Skibbitney"
                jump name_ested
            "Gronkxtron":
                $ mcname = "Gronkxtron"
                jump name_ested
            "Gyatlyn":
                $ mcname = "Gyatlyn"
                jump name_ested
            "Audrey":
                jump choiceaudrey   
            "I want to choose my own name":
                $ mcname = renpy.input("What's your name?", "Bob", length=30, exclude=" 0123456789+=,.?!<>{}[]()").strip() or "Bob" 
                jump name_ested

        label choiceaudrey:
            mcn "HI!! Is that you, Audrey Chen?"
            $ mcname = "Audrey"
            jump name_ested

    label name_ested:
        $ mc = Character("[mcname]", color="#c8ffc8", what_prefix='"', what_suffix='"')
        $ mci = Character("[mcname]", color="#c8ffc8", what_italic=True)
        mc "Call me [mcname]."
        mc "What's yours?"
        $ nug = Character("Dago", color="#ffa500", what_prefix='"', what_suffix='"')
        nug ". . . Dago."
        stop music
        play sound "audio/sfx_gegagedigedagedago.mp3" fadein 0.1 volume 0.5 
        show dago neutral
        nug "Gegagedigedage Dago."
        play music "audio/bgm_buckle.mp3" fadein 1.0 volume 0.5
        nug "But you can call me Dago."
        mc "Okay, Dago."
        mc "Nice to meet you."
        nug "Now just hop on, and be the booktok girl to my biker boy."
        hide dago neutral
        with dissolve
        mci "Omg why's he kinda kawaii."
        mcn "You Debby Ryan hair tuck and blush."
        mc "Do you think we can make 9 o’clock?"
        nug "Lol probs not but we can try."
        nug "I’m usually late anyways, but Sensei doesn’t mind."
        mci "Omg he's not into Wonyoungism. I can't be caught lacking with an academic victim lowkey."
        stop music
        scene black
        play sound "audio/sfx_pedalling.mp3" fadein 1.0 volume 0.5
        pause 5.0
        play sound "audio/sfx_door_slide.mp3"
        pause 4.0
        scene bg classroom 
        with fade
        play music "audio/bgm_skibidi.mp3" fadein 1.0 volume 0.5
        nug "Omatase shimashita Sensei!!! Sorry we late :P"
        mcn "Tf up with this weeb? People say {i}Okurete sumimasen{/i} normally anyways."
        mcn "You bow your head down in greeting."
        mcn "The teacher has a sinewy figure, sort of lanky but still maintains an air of proper authority somehow." 
        mcn "The toilet connected to his torso gives him a negative canthal tilt though."
        play sound "sfx_brr.mp3" fadein 1.0 volume 0.8
        show skibidi angry with dissolve
        ski "Skibidi toilet Ohio rizz. You both get to your seat- oh."
        ski "It’s the new kiddo!"
        show skibidi neutral with dissolve
        ski "Why don’t you introduce yourself to the class?"
        mcn "You scan the classroom tentatively as Dago sits himself at a seat in the centre of the room."
        mcn "There’s a figure at the corner of the room that catches your eye. . ."
        mci "Dark, goth, emo—"
        mci "Is that a hot alt chick wearing a fluffy jumpsuit. . ?"
        show edge neutralleft at left
        with dissolve
        ski "You’re [mcname], right? From Florida?"
        hide edge neutralleft
        with dissolve
        mc "Yes sir- I mean Sensei."
        ski "Well then, share three fun facts about yourself."
        mci ". . ."
        mci "Wtf are we in elementary school? Alright then."
        mci "Uhhh, well. . . "
        menu:
            "I touch grass everyday.":
                jump b
            "I fought doomscrolling-sama when I was 12 and won.": 
                jump b
    
    label b:
        mc "And. . ."
        menu:
            "I have the biggest gyatt of all of Ohio.":
                jump c
            "I have won the mogging championship three times.":
                jump c
    
    label c:
        mc "Lastly. . ."
        menu:
            "I came from Florida.":
                jump choice_c1
            "I have a pet cat named Mogster Mew Mew.":
                jump normal
        
    label choice_c1:
        ski "Well yeah, we already knew the last one. But thanks."
        jump normal
    
    label normal:
        ski "Ok cool stuff. Go sit. . . somewhere."
        ski "Just at the second row, over there."
        ski "And Gegagedigedage Dago, you might as well show them around the school at lunch since you guys came in together."
        mcn "Dago beams from his seat."
        show dago neutral at left 
        with dissolve
        nug ":)"
        hide dago neutral with dissolve
        mcn "Mr Skibidi resumes his teaching as if you both didn’t arrive late."
        mcn "He draws up complicated diagrams on the blackboard related to some new subject called Mewing 101."
        mci "I can't understand it much, but I reckon I’ll get it next lesson."
        scene black
        with fade
        pause 1.0
        scene bg classroom
        with fade
        play sound "audio/sfx_bell.mp3" fadein 1.0 volume 0.5
        show skibidi neutral
        ski "Skibidi toilet Ohio rizz!!"
        ski "Well that's the bell."
        ski "Get your gyatts out of my class. You’ll have Mrs. Sigmay next period."
        hide skibidi neutral with dissolve
        mci "That was actually quite a skibidi lesson."
        mci "Mr Skibidi seems nonchalant but. . . he really cares about these kids. I can tell through the way he teaches, huh."
        show dago neutral with dissolve
        nug "Sup vro."
        nug "Want me to give you a tour now?"
        mc "Yeah I’d like that, thanks."
        mcn "You look over your shoulder to the other side of the room where the hot goth chick was."
        show edge neutralleft at left
        with dissolve
        menu:
            "Can you introduce me to that person over there?":
                jump choice1
            "Don’t say anything bc you might lose 42069 aura.":
                jump choice2
    
    label choice1:
        nug "Oh, that’s Edgemund, he has generational aura debt."
        nug "He doesn’t really talk— like, to anyone."
        nug "Why do you ask?"
        mcn "You dodge his question."
        mc "Wait so that’s a dude?"
        mc "Not an emo chic- I mean, so, that’s not a girl wearing a fursuit?"
        nug "Naw vro. You blind ahh."
        nug "I’d recommend you just leave him alone tho. He’ll probably drag you to the backrooms if you talk to him."
        mc "???"
        mc "Okay. . ."
        mci "Damn I really thought that was a hot alt girl huh. Oh well, no big tiddy goth gf for me ig."
        jump choice2
    
    label choice2:
        hide edge neutralleft with dissolve
        mc "Let's do the tour."
        nug ":)"
        show bg cafeteria with fade
        stop music
        play music "audio/bgm_cafeteria.mp3" fadein 1.0 volume 0.1
        nug "This is the cafeteria!"
        nug "We all usually eat here for lunch, but some people go yap in any empty classrooms they find."
        hide dago neutral with dissolve
        mci "Woah this place looks like somewhere I could do the griddy in. It’s lowkey giving prison-core."
        show dago neutral with dissolve
        nug "So over there. . ."
        hide dago neutral with dissolve
        mcn "Dago points to a particularly congested group of Gen Z kids who are playing Brawl Stars and have their eyes glued to videos of Kai Cenat in a maid costume."
        show turkish qd:
            xalign 1.5
        play sound "audio/bgm_carnival.mp3" fadein 1.0 volume 0.5 loop
        qd "Yo Blue Tie Kid, what the sigma are you watching??"
        show tomato boy with dissolve
        tom "YOOOOOOOOOOOO!!!!"
        show blue tie with dissolve:
            xalign -0.5
        bt "Ain’t no way cuh. Did you pray today?"
        tom ". . ."
        tom "YOOOOOOOOOOOO!!!!!"
        show dago neutral with dissolve:
            xalign 0.25
            yalign 1.0
        nug ". . . is the Rizz Party gng. They’re the popular vros but on god they loud ahhh."
        mci "That dude’s face is so red..! He’s not even laughing or anything though. Get it white boi."
        mci "I wonder how red he can go."
        nug "And over at that table are 'the L-gamerz'."
        hide tomato boy 
        hide blue tie 
        hide turkish qd 
        with dissolve
        stop sound
        mcn "You narrow my eyes to try to figure out what they’re playing on their iPads. You think it’s Subway Surfers."
        nug "You see that imposter there with his back to the wall?"
        nug "That’s their biggest L. . . Uhh, L for leader."
        show among us neutral at right 
        with dissolve
        play sound "audio/sfx_sus.mp3" fadein 1.0 volume 1.0
        amg ". . ."
        mc "Wow he's so small and shiny"
        nug "Apparently his past girlfriends have all said he’s super buff. . ."
        nug "But vro just hides it all under his hardy exterior, y’know?"
        nug "No one knows if it’s true."
        mcn "Amongus looks up from his iPad for a split second, and you accidentally lock eyes."
        mcn "His gaze is deep—even if it lasted for just for a millisecond—and in that instant behind his goggles you see an immense profundity and aura in him."
        amg ". . . . . !!"
        hide among us neutral
        play sound "audio/sfx_sus.mp3" fadein 1.0 volume 1.0
        show among us buff at right
        mcn "Amon reverts his eyes as quickly as they joined yours."
        hide among us buff
        show among us neutral at right
        mci "What was that..?"
        mcn "You can feel your heart going dokidoki. . . But then you start to hearing him play Temple Run instead of Subway Surfers."
        mcn "That gives you the ick."
        hide among us neutral
        nug "And then over there. . ."
        scene black
        mcn "Dago continues to introduce almost every clique there is until lunch is over."
        show text "After School" with dissolve
        stop music
        pause 1.0
        hide text with fade
        scene bg school gates with fade
        play music "audio/sfx_bell.mp3" fadein 1.0 volume 0.5
        queue music "audio/bgm_skibidi.mp3" fadein 1.0 volume 0.5
        show dago neutral with dissolve
        mc "Well, see you tomorrow Dago. Thanks for everything today."
        mci "I’m tired asf from the first day already… its so bad on G."
        nug "No sweat vro."
        nug "We should walk home together cos we live in the same neighbourhood."
        mc "Nah all good I have to go buy some snacks at the konbini so. . ."
        nug ":("
        nug "Aw okay bet vro see you tomorrow."
        mci "Wait I lowkey feel bad for this mf? . . .whatever I just really want some alone-time rn though."
        mcn "Dago suddenly levitates into the sky, and shoots off like a rocket into the direction of our neighbourhood."
        play sound "sfx_rocket.mp3" fadein 1.0 volume 2.0
        hide dago neutral with moveouttop
        pause 5.0
        mci ". . .Wtf."
        stop music
        scene bg konbini
        with fade
        play sound "audio/sfx_store_bell.mp3" fadein 1.0 volume 0.5
        play music "audio/bgm_gigachad.mp3" fadein 1.0 volume 0.5
        mcn "Once you enter the store you feel an almost oppressive amount of aura."
        mcn "At the cashier, a man is casually curling 60 kilo weights."
        show gigachad with dissolve
        gig ". . ."
        mcn "But he isn’t just any man… you can feel it in your bones."
        mcn "This was an {i}alpha male{/i}."
        mcn "You stockpile on some Skyline Chilli and then timidly waddle up to the cashier."
        gig "Hey, first time at Gyattalicious? Haven’t seen you around before."
        mcn "He mogs you so hard you have to physically restabilise your balance without falling down on your knees like a rando in Walmart."
        mc "Uhh yeah! Just moved here and all."
        mc "Oh—I’m a junior. I go to the local high school. Ohio Rizz High."
        mcn "A glint of knowing passes his eyes."
        gig "You're a real one, king."
        mcn "You quake in your boots."
        gig "I graduated from there last year, and now I go to Mogging College."
        mc "Wow. . . That’s so skibidi!!"
        gig "If you ask around, I bet people will tell you I was a legend back in the old days."
        mcn "He appears to now possess the wisdom of a Boomer at age 18."
        mcn "Perchance he encountered some real struggles back in high school, you think, for him to developed such wisdom."
        gig "Anyways, lemme just ring up your snacks for you rn."
        play sound "audio/sfx_cashier_scanning.mp3" fadein 1.0 volume 0.5
        mci "Up close, his features seem even sharper."
        mci "His jawline looks like it could cut me if I ran my finger along it lolol."
        stop music
        scene bg nighttime streets with fade
        play music "audio/bgm_nighttime.mp3" fadein 1.0 volume 0.5
        mci "Damn, it’s so quiet here at night, it’s unnerving. Back in Florida we never had streets this still."
        play sound "audio/sfx_footsteps.mp3" fadein 1.0 volume 0.5
        mcn "You hear someone from behind."
        mcn "Not exactly behind behind, but somehow closing in on the distance between you and them."
        mci "I am fr getting chased rn??"
        play sound "audio/sfx_crash.mp3" fadein 1.0 volume 0.7
        mcn "You gather ur balls and speedily take a peek behind-"
        scene bg nighttime streets with hpunch
        chill "Ahh. . . my ass crack."
        show chill guy mystery with dissolve
        mc ". . . !"
        mcn "Under the streetlamp, you can finally distinguish his features from the dark surrounding you."
        mcn "You search his eyes for an awkwardly long amount of time."
        mcn "And that’s when it hits you."
        mc "Huh? Aren’t you. . ."
        mc "Chill Guy?!"
        $ chill = Character("Chill Guy", color="#b0e0e6", what_prefix='"', what_suffix='"')
        hide chill guy mystery with dissolve
        show chill guy neutral with fade
        stop music
        play music "audio/bgm_chillguy.mp3" fadein 1.0 volume 0.5
        chill "Oh, [mcname]? Is it really you?"
        chill "I can’t believe I met you here in Ohio, out of all places."
        mcn "Chill Guy gives you a lightskin stare."
        mcn "You clench your fists, the convenience store bags digging into you."
        mci "We haven’t seen each other in 7 years… And this dude has the nerve to be so chill about it. . . !!"
        mci "{b}He{/b} was the one who suddenly abandoned me all those years ago, when we were still children back in Florida."
        mci "Sigh… back in the old days. It’s so long ago I even remember the Bite of ‘87."
        mci "I won’t forgive him for that. . . " 
        mci "I still haven’t."
        mcn "A smile limps its way back on your face."
        mc "Yeah! Ahahah.a.ha. A."
        mc "Fancy seeing you here"
        mc "I need to griddy out of here. See ya!!!!"
        hide chill guy neutral
        show chill guy serious
        chill "Wait, [mcname]. . ."
        play sound "audio/sfx_running.mp3" fadein 1.0 volume 0.5
        mcn "You rush past him before you can regret the longing that colours his eyes. The pavement gives way to your feet, a loud heartbeat drumming in your skull."
        scene bg bedroom
        with fade
        stop music
        play music "audio/bgm_symphony.mp3" fadein 1.0 volume 0.5
        mci "Damn, today was so:"
        menu:
            "Skibidi":
                jump choiceskibidi
            "Unskibidi":
                jump choiceunskibidi
            
    
    label choiceskibidi:
        mci "Dago was super nice to me today for some reason."
        mci "I hope we can become closer friends."
        mci "Oh! And Edgemund, was it?"
        mci "He would be lowkey goated at crossdressing. . . hmm. . ."
        jump day1sleep
    
    label choiceunskibidi:
        mci "Fuck, I hope Chill Guy doesn’t go to the same school as me. I didn’t see him there today, but it’s the only possible school around here."
        jump day1sleep
    
    label day1sleep:
        mcn "And just like that you drift off to sleep."
        scene black
        tate "I’m a feminist."
        mci "Huh?? Why am I dreaming about Andrew Tate?!"
        jump tut_start
        

























        






















        
        












        




        



            
        












        

        







            

        
            
        




        




        











    
