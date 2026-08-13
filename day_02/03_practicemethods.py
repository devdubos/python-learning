user_input = " hello, pYthon! "
print(f"{user_input.strip().capitalize()}")

hobbies_str = "gaming, movies, books, sports"
hobbies_list = hobbies_str.split(", ")
hobbies_list.append("coding")
print(hobbies_list)

review = "This movie is terrible and bad"
review_new = review.replace("terrible", "awesome").replace("bad", "good")
print(review_new)