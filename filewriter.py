def write_to_file(input_list):
    """
    Checks if the last line of the file is the same as the given input,
    if it is it won't write to it
    """
    words = input_list[0].split()
    index_counter = 0
    for word in words:
        """
        if "<br>" in word:
            if word[-1] == ">":
                splitwords = word.split("<")
                words[index_counter] = splitwords[0]
            else:
                splitwords = word.split(">")
                words[index_counter] = splitwords[1]
        index_counter += 1
        """
        if "<br>" in word:
            words[index_counter] = word.replace("<br>", " ")
    
        index_counter += 1
    input_list[0] = " ".join(words)

    with open("./web_scraping/pure_shit.txt", 'r') as f:
        for line in f:
            pass

    with open("./web_scraping/pure_shit.txt", 'a') as f:
        string_to_be_written = f"{input_list[0]} -- {input_list[1]} \n"
        if string_to_be_written != line:
            #f.write(string_to_be_written)
            print(string_to_be_written)


write_to_file(["Orbán Viktor: <br>Kapcsolat van<br> a migráció és a koronavírus-járvány között", "kek"])