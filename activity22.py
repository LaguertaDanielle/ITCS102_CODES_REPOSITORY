movie_type = ["horror", "thriller", "romance", "fantasy", "comedy", "action"]
title = []
while True:
    ans = input("Do you know about any movie genre? (Yes/No): ")

    if ans.lower() == "yes":
        print("Please select the list wwhat type of movie genre do you know")
        for x in movie_type:
            print(x)
        movie_type = input("Movie Type: ")

        title = input("The title of the move: ")
        title.append(title)
        continue

    else:
        print("Thank you! ")
        break
