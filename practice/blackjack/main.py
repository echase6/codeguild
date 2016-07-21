"""Blackjack playing game."""

from card import Card
from deck import Deck
from hand import Hand
from player import Player
from random import shuffle

SUITS = ['S', 'D', 'C', 'H']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
PLAYER_NAMES = ['Eric', 'Joe', 'Dealer']


def initialize_players():
    """Set up players and return list of them.

    >>> initialize_players()
    [Player('Eric', Hand([]), 0, False), Player('Dealer', Hand([]), 0, False)]
    """
    players = []
    for player_name in PLAYER_NAMES:
        player = Player(player_name, Hand([]), 0, False)
        players += [player]
    return players


def add_card_to_hand(card, hand):
    """Adds a card to the hand.

    >>> add_card_to_hand(Card('A', 'H'), Hand([Card('2', 'C'), Card('3', 'D')]))
    Hand([Card('2', 'C'), Card('3', 'D'), Card('A', 'H')])
    """
    hand.card_list += [card]
    return hand


def return_score_of_hand(hand):
    """Calculates and returns the score of a hand.

    >>> return_score_of_hand(Hand([Card('2', 'C'), Card('3', 'D')]))
    5
    """
    point_total = 0
    num_aces_11 = 0
    for card in hand.card_list:
        if card.rank == 'A':
            point_total += 11
            num_aces_11 += 1
        elif card.rank == 'J' or card.rank == 'Q' or card.rank == 'K':
            point_total += 10
        else:
            point_total += int(card.rank)
    while num_aces_11 > 0 and point_total > 21:
        point_total -= 10
        num_aces_11 -= 1
    return point_total


def initialize_deck():
    """Loads and returns deck with cards in order. """
    deck = Deck([])
    for suit in SUITS:
        for rank in RANKS:
            deck.card_list += [Card(rank, suit)]
    return deck


def shuffle_deck(deck):
    """Shuffles deck.   """
    shuffle(deck.card_list)


def draw_card(deck):
    """Draws card from top of deck and returns card and lighter deck.

    >>> draw_card(Deck([Card('2', 'C'), Card('3', 'D')]))
    (Card('3', 'D'), Deck([Card('2', 'C')]))
    """
    card = deck.card_list.pop()
    return card, deck


def test_is_deck_empty(deck):
    """Tests whether deck is empty and returns True if empty.

    >>> test_is_deck_empty(Deck([Card('2', 'C'), Card('3', 'D')]))
    False
    >>> test_is_deck_empty(Deck([]))
    True
    """
    return len(deck.card_list) == 0


def check_if_skip_player(player):
    """Find out if the player needs to be skipped this round.

    >>> check_if_skip_player(Player('Eric',
    ...                      [Card('2', 'C'), Card('3', 'D')], 5, True))
    True
    >>> check_if_skip_player(Player('Eric',
    ...                      [Card('2', 'C'), Card('3', 'D')], 22, False))
    True
    >>> check_if_skip_player(Player('Dealer',
    ...                      [Card('2', 'C'), Card('3', 'D')], 5, True))
    True
    >>> check_if_skip_player(Player('Dealer',
    ...                      [Card('2', 'C'), Card('3', 'D')], 17, False))
    True
    >>> check_if_skip_player(Player('Dealer',
    ...                      [Card('2', 'C'), Card('3', 'D')], 15, False))
    False
    """
    if player.is_staying or player.score > 21:
        return True
    if player.name == 'Dealer':
        if player.score >= 17:
            return True
    else:
        prompt_string = '{} hit or stay (h/s)? '.format(player.name)
        response = input(prompt_string)
        if response[0].lower() == 's':
            return True
    return False


def play_round(deck, players, round_num):
    """Deal the cards to whomever wants them."""
    for player in players:
        if round_num > 1 and check_if_skip_player(player):
            player.is_staying = True
        else:
            card, deck = draw_card(deck)
            player.hand = add_card_to_hand(card, player.hand)
            player.score = return_score_of_hand(player.hand)
            if player.name == 'Dealer' and player.score >= 17:
                player.is_staying = True


def test_for_game_over(players):
    """Check if the game is over for any reason.

    >>> test_for_game_over([Player('Eric',[], 5, True),
    ...                    Player('Dealer', [], 22, False)])
    True
    >>> test_for_game_over([Player('Eric',[], 5, True),
    ...                    Player('Dealer', [], 12, True)])
    True
    >>> test_for_game_over([Player('Eric',[], 5, True),
    ...                    Player('Dealer', [], 12, False)])
    False
    """
    return(max([player.score for player in players]) >= 21 or
           all([player.is_staying for player in players]))


def display_who_won(players):
    """

    >>> display_who_won([Player('Eric', Hand([]), 17, False),
    ...                  Player('Dealer', Hand([]), 18, False)])
    Dealer wins this round.
    >>> display_who_won([Player('Eric', Hand([]), 17, False),
    ...                  Player('Dealer', Hand([]), 22, False)])
    Eric wins this round.
    >>> display_who_won([Player('Eric', Hand([]), 17, False),
    ...                  Player('Dealer', Hand([]), 17, False)])
    There was a tie.
    >>> display_who_won([Player('Eric', Hand([]), 22, False),
    ...                  Player('Dealer', Hand([]), 22, False)])
    Nobody wins.
    """
    winning_point_amt = max([p.score if p.score <= 21 else 0 for p in players])
    winners = [p.name for p in players if p.score == winning_point_amt]
    if len(winners) == 0:
        print('Nobody wins.')
    elif len(winners) > 1:
        print('There was a tie.')
    else:
        print('{} wins this round.'.format(winners[0]))


def display_hands(players, round_num):
    """Display the hands in a pleasant format.

    >>> display_hands([Player('Eric',
    ...                      Hand([Card('2', 'C'), Card('3', 'D')]), 5, True),
    ...                Player('Dealer',
    ...                      Hand([Card('A', 'C'), Card('10', 'D')]), 5, True)],
    ...                 2) # doctest: +NORMALIZE_WHITESPACE
              Round: 2
    Eric                Dealer
    2-C 3-D             A-C 10-D
    Points: 5           Points: 5
    """
    name_string = ''
    hand_string = ''
    points_string = ''
    for player in players:
        name_string += player.name.ljust(20)
        hand_string += ''.join([c.rank + '-' + c.suit + ' '
                                for c in player.hand.card_list]).ljust(20)
        points_string += 'Points: {}'.format(player.score).ljust(20)
    print(' '*10 + 'Round: {}'.format(round_num))
    print(name_string)
    print(hand_string)
    print(points_string, '\n')


def main():
    game_over = False
    deck = initialize_deck()
    shuffle_deck(deck)
    players = initialize_players()
    round_num = 0
    while round_num <= 2 or not game_over:
        play_round(deck, players, round_num)
        game_over = test_for_game_over(players)
        display_hands(players, round_num)
        round_num += 1
    display_who_won(players)


if __name__ == '__main__':
    main()
