from datetime import datetime

class User:
    def __init__(self, user_id, username, password):
        self.__user_id = user_id
        self.__username = username
        self.__password = password
        self.__following = []
        self.__followers = []
        print(f"User registered: {self.__username}")

    def get_username(self):
        return self.__username

    def follow(self, other_user):
        self.__following.append(other_user)
        other_user.__followers.append(self)
        print(f"{self.__username} started following {other_user.get_username()}")
    
class Post:
    def __init__(self, post_id, user, caption, image_url):
        self.__post_id = post_id
        self.__user = user
        self.__caption = caption
        self.__image_url = image_url
        self.__likes = []
        self.__comments = []
        self.__created_at = datetime.now()
        print(f"\n{self.__user.get_username()} created a post: '{self.__caption}'")

    def add_like(self, user):
        self.__likes.append(user)
        print(f"{user.get_username()} liked {self.__user.get_username()}'s post")

    def add_comment(self, comment):
        self.__comments.append(comment)
        print(f"{comment.get_user().get_username()} commented on {self.__user.get_username()}'s post: '{comment.get_text()}'")

    def print_details(self):
        print("\n POST DETAILS")
        print(f"Author: {self.__user.get_username()}")
        print(f"Caption: {self.__caption}")
        print(f"Image: {self.__image_url}")
        print(f"Total Likes: {len(self.__likes)}")
        print("Comments:")
        for comment in self.__comments:
            print(f"  - {comment.get_user().get_username()}: {comment.get_text()}")


class Comment:
    def __init__(self, comment_id, user, text):
        self.__comment_id = comment_id
        self.__user = user
        self.__text = text
        self.__created_at = datetime.now()

    def get_user(self):
        return self.__user

    def get_text(self):
        return self.__text


class Message:
    def __init__(self, message_id, sender, receiver, content):
        self.__message_id = message_id
        self.__sender = sender
        self.__receiver = receiver
        self.__content = content
        self.__timestamp = datetime.now()
        print(f"Message sent from {self.__sender.get_username()} to {self.__receiver.get_username()}: '{self.__content}'")


# Creating instances
user1 = User(1, "Yami", "pass123")
user2 = User(2, "Eddy", "pass456")

# Performing actions
user2.follow(user1)

post1 = Post(101, user1, "I'm with this beautiful little cat!!", "https://imgamen.com/mishi.jpg")
post1.add_like(user2)

comment1 = Comment(201, user2, "It's so pretty!!")
post1.add_comment(comment1)

post1.print_details()

msg1 = Message(301, user2, user1, "Hey Yami, love u.")
 