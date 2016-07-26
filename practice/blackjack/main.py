"""Blackjack playing game."""

from hand import Hand, return_score_of_hand, add_card_to_hand
from deck import initialize_deck, shuffle_deck, draw_card
from player import Player, initialize_players
from card import Card


def play_round(card_deck, plyr):
    """Deal the cards to whomever wants them.

    Dealer:  automatically hits dealer until score is over 17
    Non-dealer:  hits until they stay or score is over 21
    """
    if plyr.score == 21:
        return
    not_done = True
    while not_done:
        if plyr.name == 'Dealer':
            if plyr.score >= 17:
                return
        else:
            display_player_hand(plyr)
            prompt_string = '{} hit or stay (h/s)? '.format(plyr.name)
            response = input(prompt_string)
            if response[0].lower() == 's':
                return
        card = draw_card(card_deck)
        add_card_to_hand(card, plyr.hand)
        plyr.score = return_score_of_hand(plyr.hand)
        if plyr.score > 21:
            print('{} busted!'.format(plyr.name))
            not_done = False
    return


def find_winners(players):
    """Find out who won and return list of their names.


    """
    winning_point_amt = max([p.score if p.score <= 21 else 0 for p in players])
    return [p.name for p in players if p.score == winning_point_amt]


def display_who_won(players):
    """Displays who won at the end of the game.

    >>> display_who_won([Player('Eric', Hand([]), 17),
    ...                  Player('Dealer', Hand([]), 18)])
    Dealer wins this hand.
    >>> display_who_won([Player('Eric', Hand([]), 17),
    ...                  Player('Dealer', Hand([]), 22)])
    Eric wins this hand.
    >>> display_who_won([Player('Eric', Hand([]), 17),
    ...                  Player('Dealer', Hand([]), 17)])
    Push.
    >>> display_who_won([Player('Eric', Hand([]), 22),
    ...                  Player('Dealer', Hand([]), 22)])
    Nobody wins.
    """
    winners = find_winners(players)
    if len(winners) == 0:
        print('Nobody wins.')
    elif len(winners) > 1:
        print('Push.')
    else:
        print('{} wins this hand.'.format(winners[0]))


def display_player_hand(plyr):
    """Display only one hand, after receiving a card.

    >>> display_player_hand(Player('Eric',
    ...                      Hand([Card('2', 'C'), Card('3', 'D')]), 5)
    ...                     )  # doctest: +NORMALIZE_WHITESPACE
    <BLANKLINE>
    Eric:  Hand:  2-C 3-D   Score:  5
    """
    hand_string = ''.join([c.rank + '-' + c.suit + ' '
                          for c in plyr.hand.card_list])
    print('\n{}:  Hand:  {}   Score:  {}'.format(plyr.name, hand_string,
                                                 plyr.score))


def display_hands(players):
    """Display the hands in a pleasant format.

    >>> display_hands([Player('Eric',
    ...                      Hand([Card('2', 'C'), Card('3', 'D')]), 5),
    ...                Player('Dealer',
    ...                      Hand([Card('A', 'C'), Card('10', 'D')]), 5)],
    ...                 ) # doctest: +NORMALIZE_WHITESPACE
    Eric                Dealer
    2-C 3-D             A-C
    """
    name_string = ''
    hand_string = ''
    for plyr in players:
        name_string += plyr.name.ljust(20)
        if plyr.name != 'Dealer':
            card_list_out = plyr.hand.card_list
        else:
            card_list_out = plyr.hand.card_list[:-1]  # Hide dealer's last card
        hand_string += ''.join([c.rank + '-' + c.suit + ' '
                                for c in card_list_out]).ljust(20)
    print(name_string)
    print(hand_string)


def main():
    card_deck = initialize_deck()
    shuffle_deck(card_deck)
    players = initialize_players()
    for i in range(2):  # Deal the first two cards to everyone.
        for plyr in players:
            card = draw_card(card_deck)
            add_card_to_hand(card, plyr.hand)
            plyr.score = return_score_of_hand(plyr.hand)
    display_hands(players)
    for plyr in players:
        play_round(card_deck, plyr)
        display_player_hand(plyr)
    display_who_won(players)


if __name__ == '__main__':
    main()
