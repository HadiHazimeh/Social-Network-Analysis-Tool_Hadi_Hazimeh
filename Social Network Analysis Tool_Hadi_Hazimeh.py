
class Graph:
    def __init__(self):
        self.users = {} 

    def add_user(self, user_id, name):
        if user_id not in self.users:
            self.users[user_id] = User(user_id, name)

    def add_friendship(self, user_id1, user_id2):
        if user_id1 in self.users and user_id2 in self.users:
            self.users[user_id1].add_friend(user_id2)
            self.users[user_id2].add_friend(user_id1)

    def remove_user(self, user_id):
        if user_id in self.users:
            del self.users[user_id]

    def remove_friendship(self, user_id1, user_id2):
        if user_id1 in self.users and user_id2 in self.users:
            self.users[user_id1].friends.discard(user_id2)
            self.users[user_id2].friends.discard(user_id1)

    def bfs(self, start_user_id):
        visited = set()
        queue = [start_user_id]
        while queue:
            current_user_id = queue.pop(0)
            visited.add(current_user_id)
            print(f"Visited user {current_user_id}")
            for friend_id in self.users[current_user_id].friends:
                if friend_id not in visited:
                    queue.append(friend_id)

    def sort_users_by_name(self):
        sorted_users = sorted(self.users.values(), key=lambda user: user.name)
        return sorted_users

    def average_friends(self):
        total_friends = sum(len(user.friends) for user in self.users.values())
        return total_friends / len(self.users)


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.friends = set()

    def add_friend(self, friend_id):
        self.friends.add(friend_id)


# Example usage:
if __name__ == "__main__":
    social_network = Graph()
    social_network.add_user(1, "Alice")
    social_network.add_user(2, "Bob")
    social_network.add_user(3, "Charlie")
    social_network.add_friendship(1, 2)
    social_network.add_friendship(2, 3)
    social_network.add_friendship(3, 1)

    print(social_network.users[1].name)
    print(social_network.users[1].friends)
    print(social_network.users[2].name)
    print(social_network.users[2].friends) 
    print(social_network.users[3].name)
    print(social_network.users[3].friends)

    social_network.remove_user(1) 


    sorted_users = social_network.sort_users_by_name()
    for user in sorted_users:
        print(user.name)

    print(f"Average friends per user(after removing user 1 (alice)): {social_network.average_friends():.2f}")