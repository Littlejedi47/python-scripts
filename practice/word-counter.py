def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as file:
            contents = file.read()
            words = contents.split()
            num_words = len(words)
    except FileNotFoundError:
        print(f'Sorry the file "{filename}" does not exist!')
    else:
        if num_words == 1:
            print(f'The file "{filename}" has 1 word.')
        else:
            print(f'The file "{filename}" has about {num_words} words.')


filenames = ['learning-python.txt', 'lines.txt', 'sdgjkl;', 'pi.txt']
for i in filenames:
    count_words(i)