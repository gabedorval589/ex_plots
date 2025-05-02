def get_user():
    user_name = input("What is your name? ")
    dob = input("What is your date of birth? (dd/mm/yyyy) ")
    fav_desert  = input("What is your favorite desert? ")
    return(user_name, dob, fav_desert)

# user_info = get_user()
# print(user_info)

def build_dict(user_info ):
    name, dob, desert = user_info
    my_dict = {
        'name': name,
        'dob': dob,
        'desert': desert
    }
    return my_dict

# response = build_dict(user_info)
# print(response)

if __name__ == "__main__":
    pass