class Player:
    def __init__(self, player_data):
        self.id = player_data[0]
        self.name = player_data[1]
        self.current_pp = player_data[2]
        self.lockstate = player_data[3]
        self.pizeholder = player_data[4]
        self.total_dice = player_data[7]
        self.location = player_data[8]

    def save_player_data(self):
        # Overwrite the corresponding row in player-table
        # Maybe calls SQL class methods *OR* straight up SQL queries here
        pass


class Game:

    def __init__(self, id, name, players , round_counter, bag_city, searched):
        # call init from game_loader, proper startup sequence needed
        # players is a foreign key to player table
        self.id = id  # GET from DB
        self.name = name  # GET from DB
        self.round_counter = round_counter  # GET from DB
        self.bag_city = bag_city  # GET from DB
        self.searched = searched  # GET from DB
        self.player_list = []
        for player in players:
            self.player_list.append(Player(player))

    def save_game_data(self):
        for player in self.player_list:  # overwrite player-table
            player.save_player_data()
        # Overwrite the corresponding row in games-table

