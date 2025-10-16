"{:10s} {:10s}".format("Name", "Total")
"{:10s} {:<10d}"


# def open_file():
#     file_exists = False
#
#     while not file_exists:
#         try:
#             file_name = input(":~Enter file name ~:")
#             fp = open(file_name, "r")
#             return fp
#
#         except FileNotFoundError:
#             print("\n*** unable to open file ***\n")

def add_word(word_map, word_list):
    # YOUR COMMENT
    if word_list[0] not in word_map:
        word_map[word_list[0]] = int(word_list[1])
    else:
        word_map[word_list[0]] = int(word_list[1]) + int(word_map[word_list[0]])




def build_map(in_file, word_map):
    next(in_file)
    for line in in_file:

        # YOUR COMMENT
        word_list = line.split()
        add_word(word_map, word_list)
        # for word in word_list:
        #     # YOUR COMMENT
        #     word = word.strip()
        #     add_word(word_map, word)



def main():
    word_map={}
    in_file = open("data1.txt", 'r')
    in_file_two = open("data2.txt", 'r')
    build_map(in_file, word_map)
    in_file.close()

    build_map(in_file_two, word_map)

    print("{:10s} {:10s}".format("Name", "Total"))
    for key in word_map:
        print("{:10s} {:<10d}".format(key, word_map[key]))
    in_file_two.close()




if __name__ == "__main__":
    main()