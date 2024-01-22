def create_file(name_f, n):
    for i in range(n):
        my_file = open(f"data//{name_f+str(i)}.txt", "w")
        my_file.close()
