def write_to_file(_input):
    """
    Checks if the last line of the file is the same as the given input,
    if it is it won't write to it
    """
    words = _input.split()
    index_counter = 0
    for word in words:
        if "<br>" in word:
            words[index_counter] = word.replace("<br>", " ")
    
        index_counter += 1
    _input = " ".join(words)

    with open("./collected.txt", 'r') as f:
        for line in f:
            pass

    with open("./collected.txt", 'a') as f:
        string_to_be_written = f"{_input} \n"
        if string_to_be_written != line:
            f.write(string_to_be_written)
