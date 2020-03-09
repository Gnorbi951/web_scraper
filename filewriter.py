def write_to_file(input_list):
    """
    Checks if the last line of the file is the same as the given input,
    if it is it won't write to it
    """
    with open("./web_scraping/pure_shit.txt", 'r') as f:
        for line in f:
            pass

    with open("./web_scraping/pure_shit.txt", 'a') as f:
        string_to_be_written = f"{input_list[0]} -- {input_list[1]} \n"
        if string_to_be_written != line:
            f.write(string_to_be_written)
