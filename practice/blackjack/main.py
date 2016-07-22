"""Blackjack playing game."""

import hand
import deck
import player
from hand import Hand
from deck import Deck
from player import Player
from card import Card


def draw_card(card_deck):
    """Draws card from top of deck and returns card.

    >>> draw_card(Deck([Card('2', 'C'), Card('3', 'D')]))
    Card('3', 'D')
    """
    card = card_deck.card_list.pop()
    return card


def play_round(card_deck, plyr):
    """Deal the cards to whomever wants them."""
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
        plyr.hand = hand.add_card_to_hand(card, plyr.hand)
        plyr.score = hand.return_score_of_hand(plyr.hand)
        if plyr.score > 21:
            print('{} busted!'.format(plyr.name))
            not_done = False
    return


def display_who_won(players):
    """

    >>> display_who_won([Player('Eric', Hand([]), 17),
    ...                  Player('Dealer', Hand([]), 18)])
    Dealer wins this round.
    >>> display_who_won([Player('Eric', Hand([]), 17),
    ...                  Player('Dealer', Hand([]), 22)])
    Eric wins this round.
    >>> display_who_won([Player('Eric', Hand([]), 17),
    ...                  Player('Dealer', Hand([]), 17)])
    Push.
    >>> display_who_won([Player('Eric', Hand([]), 22),
    ...                  Player('Dealer', Hand([]), 22)])
    Nobody wins.
    """
    winning_point_amt = max([p.score if p.score <= 21 else 0 for p in players])
    winners = [p.name for p in players if p.score == winning_point_amt]
    if len(winners) == 0:
        print('Nobody wins.')
    elif len(winners) > 1:
        print('Push.')
    else:
        print('{} wins this round.'.format(winners[0]))


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
    card_deck = deck.initialize_deck()
    deck.shuffle_deck(card_deck)
    players = player.initialize_players()
    for i in range(2):
        for plyr in players:
            card = draw_card(card_deck)
            plyr.hand = hand.add_card_to_hand(card, plyr.hand)
            plyr.score = hand.return_score_of_hand(plyr.hand)
    display_hands(players)
    for plyr in players:
        play_round(card_deck, plyr)
        display_player_hand(plyr)
    display_who_won(players)


if __name__ == '__main__':
    main()
