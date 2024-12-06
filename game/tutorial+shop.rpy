screen button1():
    imagebutton:
        xalign 0.5
        yalign 0.5
        auto "button_%s.png" action [ToggleScreen("button1"), Jump("shop1")]

# The game starts here. 
label tut_start:
    label tutorial:
        scene black
        pause 5.0
        show text "Tutorial" with dissolve
        pause 1.0
        play music "audio/bgm_newdrop.mp3" fadein 1.0 volume 0.5
        hide text with fade
        scene bg brain
        # shop bg, shop bg music, tate sprite on screen
        #fade in mc sprite
        show tate at right with dissolve
        pause 1.0
        show tate as tate2 at left with dissolve 
        pause 1.0
        tate "If you want to learn how to rizz, you gotta know one thing."
        show tate as tate3 with dissolve:
            xalign 0.5
            pause 1.0
        tate "The way to a man's heart is . . ."
        show tate as tate4 with dissolve:
            xalign 0.75
            pause 1.0
        tate "FOOD."
        show tate as tate5 with dissolve:
            xalign 0.25
            pause 1.0
        mci "What kinda dream am I conjuring up rn?"
        tate "Also go make me a sandwich."
        show tate as tate6 with dissolve:
            xalign 0.4
            pause 1.0
        mc "Hell no."
        tate "Go buy one yourself then."
        show tate as tate7 with dissolve:
            xalign 0.6
            pause 1.0
        tate "Click here to go to the store, baka."
        stop music fadeout 1.0
        ## put a button to go shop here.
       
        scene black
        call screen button1
    
    label shop1:
        scene bg shop
        play music "audio/bgm_shop.mp3" fadein 1.0 volume 0.5
        show quandale at left
        with dissolve
        play sound "quandale_dingle.mp3"
        quan "Welcome to the Gyattalicious Store, can I help you with anything?"
        mcn "You snap out of your thoughts, cursing Andrew Tate."
        mc "Oh um in a moment."
        mci "Uhhhhh, what should I buy?"
        hide quandale 
        # tate sprite pops up
        show tate at right with dissolve
        pause 1.0
        show tate at left with dissolve
        pause 1.0
        tate "You can buy stuff to increase your Brainrot Gauge with the person you like . . ."
        show tate as tate3 with dissolve:
            xalign 0.5
            pause 1.0
        tate "These items are in your inventory after they're bought, and you can gift them any day."
        show tate as tate4 with dissolve:
            xalign 0.75
            pause 1.0
        show tate as tate5 with dissolve:
            xalign 0.25
            pause 1.0
        tate "But sometimes you may need an item to make certain choices!"
        show tate as tate6 with dissolve:
            xalign 0.4
            pause 1.0
        show tate as tate7 with dissolve:
            xalign 0.6
            pause 1.0
        tate "Be careful not to get cockblocked by being broke cuz."
        show tate as tate8 with dissolve:
            xalign 0.15
            pause 1.0
        show tate as tate9 with dissolve:
            xalign 0.85
            pause 1.0
        mc "Wait I'm kinda broke rn though."
        tate "I'll give you +100 gyatt coins, test it out."
        show tate as tate10 with dissolve:
            xalign 0.20
            pause 1.0
        show tate as tate11 with dissolve:
            xalign 0.80
            pause 1.0
        $ gyatt_coins = gyatt_coins +100
        tate "Don't fanum tax anything."
        mc "Thanks for the gyatt."
        stop music fadeout 1.0
        jump rizz_room
        label rizz_room:
            scene black
            pause 5.0
            play music "audio/bgm_rizz.mp3" fadein 1.0 volume 0.5
            show text "You have entered the rizz room." with dissolve
            pause 1.0
            hide text with fade
            scene bg heart
            show tate at left with dissolve
            tate "This is the rizz room, where you can later rizz up the senpai you like."
            hide tate
            show tate at right with dissolve
            tate "And your inventory is where your items are."
            hide tate
            tate "The things you buy can be used to increase Brainrot."
            show tate with dissolve:
                xalign 0.5
            mc "But how do I get more gyatt coins?"
            hide tate
            show tate with dissolve:
                xalign 0.25
            tate " Later on, every day, you'll earn gyatt coins if you say or do the thing with most aura."
            show tate with dissolve:
                xalign 0.75
            tate "Like complimenting the person you like."
            hide tate
            show tate with dissolve:
                xalign 0.4
            tate "Or mastering the Ohio rizzler life."
            hide tate
            show tate with dissolve:
                xalign 0.8
            tate "Or even saying something like 'I like your cut G.'"
            hide tate
            show tate with dissolve:
                xalign 0.2
            tate "Ok, now lets get back to the real world."
            hide tate
            show tate with dissolve:
                xalign 0.6
            tate "What do you think about women?"
            hide tate
            show tate with dissolve:
                xalign 0.3
            tate "I think they belong in the house, can't drive, and are a man's propert-"
            hide tate
            show tate with dissolve:
                xalign 0.7
            tate "HEY STOP- don't arrest me right now!!"
            hide tate with dissolve
            jump route_choose
            stop music fadeout 1.0

        label route_choose:
            mcn "Who would you like to rizz up?"
            menu:
                "Chill Guy":
                    jump shop2
                "Edgemund":
                    mcn "Unavailable in beta."
                    jump route_choose
                "Amongus Imposter":
                    mcn "Unavailable in beta."
                    jump route_choose
                "Gigachad":
                    mcn "Unavailable in beta."
                    jump route_choose
                "Tomato Man": 
                    mcn "Unavailable in beta."
                    jump route_choose
                "Secret Route": 
                    mcn "Rizz up all the characters to unlock this route."
                    jump route_choose

    label shop2:
        scene black
        pause 5.0
        show text "You are back in the shop." with dissolve
        pause 1.0
        hide text with fade
        scene bg shop
        play music "audio/bgm_shop.mp3" fadein 1.0 volume 0.5
        mc "I can't stop thinking about Chill Guy's gaze. . ."
        # BGM SHIMMY YA SHIMMY YUA
        # sfX ITS QUANDALE here
        show quandale at right
        quan "Welcome to the Gyattalicious Convenience Store!"
        quan "The more gyatt you got, the more goated you get."
        quan "Show me the gyatt coins!"
        hide quandale
        mcn "Should I buy something?"
        label back10:
            menu:
                "Fortnite Battle Pass (100 GYATT COINS)":
                    mcn "For a poggers gaming time."
                    mcn "+5 Brainrot All"
                    jump back10
                "John Pork Plushie (100 GYATT COINS)":
                    mcn "Would you answer though?"
                    mcn "+5 Brainrot All"
                    jump back10
                "Goated With The Sauce x2 (150 GYATT COINS)":
                    mcn "Fanum taxed, whopper flavored delicacy."
                    mcn "+10 Brainrot All"
                    jump back10
                "Sigma Meal Skibidi Slicers and Grimace Shake Meal (400 GYATT COINS)":
                    mcn "3AM midnight snack personally delivered by the smurf cat."
                    # sfx we live we love we lie
                    jump back10
                "Lunchly Poem (650 GYATT COINS)":
                    mcn "I like my cheese drippy. Become a rizzard of oz and serenade your favorite skibidi rizzler."
                    mcn "I saw a salmon fella\nwho was a monster yeller\nyelling about salmonella"
                    mcn "as he pooped into an umbrella\nafter eating the mozzarella\nfrom a lunchly."
                    mcn "+15 Brainrot All for next 5 mins (stackable)"
                    mcn "Successfully induced brain controlling mold to up your rizz points."
                    jump back10
                "Bing Chilling (300 GYATT COINS)":
                    mcn "A simply icy dessert made the ocky way."
                    mcn "+20 Brainrot All\n+30 Brainrot Chill Guy"
                    jump back10
                "Cherry Blossom Sprinkler (450 GYATT COINS)":
                    mcn "Call a meta meme cyclone to sprinkle flowers over your date."
                    mcn "+30 Brainrot All\n+45 Brainrot Chill Guy"
                    jump back10
                "Full-Black Ebony Hairbrush (200 GYATT COINS)":
                    mcn "Aggressively brush ur hair to cover your eyes, and woo your senpai wuth your sterling silver gaze."
                    mcn "+10 Brainrot All\n+20 Brainrot Edgemund"
                    jump back10
                "Emo Cross Y2K Silver Chain (450 GYATT COINS)":
                    mcn "Ward off any negative aura. Perfect for removing that aura debt and captivating passerbys with your sugar daddy energy. (Stackable)"
                    mcn "+30 BrainRot All\n+45 Brainrot Edgemund"
                    jump back10
                "I think that's enough shopping":
                    mci "I need to wake up for school."
                    stop music fadeout 1.0
                    jump day2

#finish copy here              