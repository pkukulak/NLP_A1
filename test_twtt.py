import twtt



if __name__ == "__main__":
    #print(twtt.strip_urls("Hi my name Https://www.google.ca/search/asdfasdfas/asdfasdf is @Jesse, #name, #herpes Http://www.asdf.cin/asdfa </p>"))
    #print(twtt.strip_urls("Meet me today at tge FEC in DC at 4. Wear a carnation so I know it's you. <a href asdfasdf>Http://bit.ly/PACattack</a>."))
    #print(twtt.html_char_to_ascii("Hi my name www.google.ca/search/sdfasdf is &#64;Jesse, &#35;name, &amp;herpes "))
    #print(twtt.add_demarcation("I cant believe in the way Lebron shoots those 3s!!!! Go jays!!! #bluebirds!!", 4))
    #print(twtt.split_sentences('Hey you!! "God I love you!" Wanna get some coffee??? Freddy vs. Jason. vs.'))
    #print(twtt.tag_tokens("Meet me today at the FEC in DC at 4 ."))

    #print(twtt.space_clitics("Hi, I'll see you at it's house, and you're coming. And isn't it something. "))
    #print(twtt.space_tokens("Hi, I'll see you at it's house; and you're coming..!??.. And isn't!!! it something... Bring your dogs' leash."))
    print(twtt.normalize_tweet("Meet me today at tge FEC in DC at 4. Wear a carnation so I know it's you. <a href asdfasdf>Http://bit.ly/PACattack </a> Here <p> is another.", 4))


#"It is feb. first. It is cold.
#[9, 16, -1] # All possible candidates.

