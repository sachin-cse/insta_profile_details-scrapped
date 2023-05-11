import csv
import instaloader
import datetime
import os

L = instaloader.Instaloader()

def get_profileinfo(keyword):
    folder = os.path.join(os.getcwd(), "insta_data")
    if not os.path.exists(folder):
        os.mkdir(folder)
    os.chdir(folder)

    profile = instaloader.Profile.from_username(L.context, keyword)
    heading = ["Username","User_Id","Profile Image","Followers","Following","Bio"]

    filename = keyword + ".csv"
    with open(filename, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(heading)

        # generate information about the profile
        username = profile.username
        user_id = profile.userid
        profile_image = profile.profile_pic_url
        followers = profile.followers
        following = profile.followees
        bio = profile.biography

        writer.writerow([username, user_id, profile_image, followers, following, bio])

    print(f'Profile information for {keyword} saved to {filename}.')









def main():
    with open('./input.txt', 'r') as f:
        keywords = f.readlines()
        keywords = [keyword.strip() for keyword in keywords]
        print(keywords)
    username = ""
    password = ""
    input_lines = []

    with open('./credentials/credentials_0.txt', 'r') as file:
        input_lines = [line.strip() for line in file]
    username = input_lines[0]
    password = input_lines[1]

    L.login(username, password)
    if len(keywords)>0:
        for keyword in keywords:
            get_profileinfo(keyword)
    else:
        print("Input is empty....")


if __name__ == "__main__":
    main()

