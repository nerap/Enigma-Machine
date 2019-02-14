import json

"""

    Emulation of enigma

    Take parameters by the user and the string to convert, return a string encoded as enigma would

"""


def rotor_roll(sequence, position):
    """This function simulate the rolling movement of a rotor
    Args:
        sequence: String, the actual rotor sequence
        position: Int, the number of movement the rotor as to do
    Return:
        string, the new sequence updated
    """
    sequence = sequence[position:] + sequence[0: position]
    return sequence


def move_plugboard(char, plug_list):
    """Check if the input of the user is plugged on the plugboard
    Args:
        char : the character to analyze in the plugboard
        plug_list : a list of list where each element is unique pair of letter,
            the actual plugs configuration of enigma
    Return:
        char, If the char is plugged return the actual char associated, else return the same character
    """
    #
    # plugboard_list as this form [[?, ?],[?, ?], ..., [?, ?]]
    # Iterate on each of those element(list so), and look for the char to be in that list and return the char
    # associated with, else return the same char
    #
    for element in plug_list:
        if char == element[0]:
            return element[1]
        elif char == element[1]:
            return element[0]

    return char


def encode_rotor(char, rotor_list):
    """Return the char in the actual sequence of the rotor
    Args :
        rotor_list : A list of 26 elements corresponding to the alphabet

        char : char, to encode
    Return :
        char, The actual new char in the rotor
    """
    #
    # alphabet.index(char) return the index of the actual char in the alphabet sequence
    #
    return rotor_list[alphabet.index(char)]


def encode_refractor(char, list_refractor):
    """Return the associated char in this static sequence of letter
    Args:
        list_refractor : A list of 26 letters in disorder
        char : the current character
    Return:
        char, The actual new char associated in the sequence
    """

    #
    # alphabet.index(char) return the index of the actual char in the alphabet sequence
    #
    return list_refractor[alphabet.index(char)]


def move_rotors_positions(_rotor_1, position_rotor_1,
                          _rotor_2, position_rotor_2,
                          _rotor_3, position_rotor_3):
    """Move the first rotor by 1, and check all potential revolution
    Args:
        _rotor_1 : string, current rotor_1 sequence
        position_rotor_1 : int, current state of the rotor
        _rotor_2 : string, current rotor_2 sequence
        position_rotor_2 : int, current state of the rotor
        _rotor_3 : string, current rotor_3 sequence
        position_rotor_3 : int, current state of the rotor
    Returns:
        _rotor_1 : string, updated rotor_1 sequence
        position_rotor_1 : int, current state of the rotor
        _rotor_2 : string, current rotor_2 sequence
        position_rotor_2 : int, current state of the rotor
        _rotor_3 : string, current rotor_3 sequence
        position_rotor_3 : int, current state of the rotor
    """

    position_rotor_1 += 1
    _rotor_1 = rotor_roll(_rotor_1, 1)

    if position_rotor_1 == 26:

        position_rotor_1 = 0

        position_rotor_2 += 1
        _rotor_2 = rotor_roll(_rotor_2, 1)
        if position_rotor_2 == 26:

            position_rotor_2 = 0

            position_rotor_3 += 1
            _rotor_3 = rotor_roll(_rotor_3, 1)

            if position_rotor_3 == 26:
                position_rotor_3 = 0

    return _rotor_1, position_rotor_1, _rotor_2, position_rotor_2, _rotor_3, position_rotor_3


def return_rotor(rotor):
    """The function returns the associated rotor from 1 to 5
    Args :
        rotor : int, rotor model use for this sequence
    Returns:
        string, this sequence in lower case
    """

    if rotor == 1:
        print("Loading the Rotor I")
        return "EKMFLGDQVZNTOWYHXUSPAIBRCJ".lower()
    if rotor == 2:
        print("Loading the Rotor II")
        return "AJDKSIRUXBLHWTMCQGZNPYFVOE".lower()
    if rotor == 3:
        print("Loading the Rotor III")
        return "BDFHJLCPRTXVZNYEIWGAKMUSQO".lower()
    if rotor == 4:
        print("Loading the Rotor IV")
        return "ESOVPZJAYQUIRHXLNFTGKDCMWB".lower()
    if rotor == 5:
        print("Loading the Rotor V")
        return "VZBRGITYUPSDNHLXAWMJQOFECK".lower()
    if rotor == 6:
        print("Loading the Rotor VI")
        return "JPGVOUMFYQBENHZRDKASXLICTW".lower()
    if rotor == 7:
        print("Loading the Rotor VII")
        return "NZJHGRCXMYSWBOUFAIVLPEKQDT".lower()
    else:
        print("Loading the Rotor VIII")
        return "FKQHTLXOCBJSPDZRAMEWNIUYGV".lower()


def return_refractor(refractor):
    """Returns the associated string by the name of the relfector
    Args:
        refractor : string, the name of the reflector to chose
    Return:
        string, the correspond refractor
    """
    if refractor == "A":
        print("Loading the Refractor A")
        return "EJMZALYXVBWFCRQUONTSPIKHGD".lower()
    if refractor == "B":
        print("Loading the Refractor B")
        return "YRUHQSLDPXNGOKMIEBFZCWVJAT".lower()
    if refractor == "C":
        print("Loading the Refractor C")
        return "FVPJIAOYEDRZXWGCTKUQSBNMHL".lower()
    else:
        print("Loading the Refractor B Thin")
        return "RDOBJNTKVEHMLFCWZAXGYIPSUQ".lower()


def rotor_initialization(list_rotor_pos):
    """Assign to all rotors (3) the rotor itself and the sequence updated by the position
    Args:
     list_rotor_pos: list, with element, each element has 2 index, the first one is the rotor, the other one is position
     to set the sequence (rotors are unique)
    Return:
        _rotor_1: the current sequence of the rotor_1
        _rotor_2: the current sequence of the rotor_2
        _rotor_3: the current sequence of the rotor_3
    """

    _rotor_1 = rotor_roll(return_rotor(int(list_rotor_pos[0][0])), int(list_rotor_pos[0][1]))
    _rotor_2 = rotor_roll(return_rotor(int(list_rotor_pos[1][0])), int(list_rotor_pos[1][1]))
    _rotor_3 = rotor_roll(return_rotor(int(list_rotor_pos[2][0])), int(list_rotor_pos[2][1]))

    return _rotor_1, _rotor_2, _rotor_3


def get_input():
    """The function will get from the user the input need to for enigma to work
    Return :
        rotor_position : List, length of 3 with the rotor and the position on each element
        plugbard : list, length from 1 to 13 elements with unique letter on associated with unique letter
        refrector_list : string, the refractor sequence length 26 elements
        message_encode : string, the message to encode
    """

    rotor_position = json.loads(
        input(
            "Enter Rotor and Position with this exact format : [[R,P], [R,P], [R,P]] \nR from 1 to 8 (unique)"
            + "\nP from 0 to 25\nMax 3 elements\nInput : "))

    plugboard = json.loads(
        input("Enter plug board with this exact format : [[\"a\", \"c\"], [\"d\", \"e\"], ..., [\"v\", \"f\"]]"
              + "\nMax length 18, cannot be empty"))
    print("Plugboard loaded")
    print(plugboard)

    refractor_list = return_refractor(input("Chose one of those refrector [A, B, C, B Thin]").upper())

    message_encode = input("Enter the message to encode")

    return rotor_position, plugboard, refractor_list, message_encode


if __name__ == "__main__":

    """This function will encode a message from a user with the rules of enigma machine, 
    taking parameters from the user
    """

    #
    # Static wheel alphabet in order
    #

    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]

    #
    # Initialize the parameters needed for enigma to work
    #   Logic of enigma:
    #   char->PlugBoard->Rotor 1 ->Rotor 2 ->Rotor 3 ->Refractor ->Rotor 3 ->Rotor 2 ->Rotor 1 ->Plugboard ->char
    #
    #   Every time a key is pressed the rotor 1 move and after a revolution the second one will move, etc..
    #
    #   For good reason, we will take the final string to decode instead of get the answer of each character each time a
    #   key is pressed, it's the same, but easier to setup
    #
    #   We need from the user to chose a plugboard configuration, chose 3 rotor from 8 available and set a custom
    #   position on it, the refractor, and the message to decode
    #
    #

    rotor_position_list, plugboard_list, refrector_list, message = get_input()
    rotor_1, rotor_2, rotor_3 = rotor_initialization(rotor_position_list)

    #
    #   Set the current position of all rotor to 0
    #

    current_position_rotor_1 = 0
    current_position_rotor_2 = 0
    current_position_rotor_3 = 0

    result_encode = ""

    for i in range(0, len(message)):
        temp = message[i]
        temp = move_plugboard(temp, plugboard_list)

        rotor_1, current_position_rotor_1, rotor_2, current_position_rotor_2, rotor_3, current_position_rotor_3 =\
            move_rotors_positions(rotor_1, current_position_rotor_1,
                                  rotor_2, current_position_rotor_2,
                                  rotor_3, current_position_rotor_3)
        temp = encode_rotor(temp, rotor_1)

        temp = encode_rotor(temp, rotor_2)

        temp = encode_rotor(temp, rotor_3)

        temp = encode_refractor(temp, refrector_list)

        temp = encode_rotor(temp, rotor_3)

        temp = encode_rotor(temp, rotor_2)

        temp = encode_rotor(temp, rotor_1)

        temp = move_plugboard(temp, plugboard_list)

        result_encode += temp

    print("\nThe Encode : " + result_encode)
