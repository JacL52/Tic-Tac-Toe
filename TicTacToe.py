game_loop = True
while game_loop == True:
    game_loop = False

    one = ""
    two = ""
    three = ""
    four = ""
    five = ""
    six = ""
    seven = ""
    eight = ""
    nine = ""

    repeat = True
    while repeat == True:
        repeat = False

        print("""
[1][2][3]
[4][5][6]
[7][8][9]
        """)

        game = True

        x_turn = True

        while x_turn == True:
            x_turn = False

            print(f"""
[{one}][{two}][{three}]
[{four}][{five}][{six}]
[{seven}][{eight}][{nine}]
            """)

            x = input("Where do you want to put your X? ")
            if x == "1":
                if one == "":
                    one = "x"
                else:
                    print("Please choose an empty spot")
                    x_turn = True
            elif x == "2":
                if two == "":
                    two = "x"
                else:
                    print("Please choose an empty spot")
                    x_turn = True
            elif x == "3":
                if three == "":
                    three = "x"
                else:
                    print("Please choose an empty spot")
                    x_turn = True
            elif x == "4":
                if four == "":
                    four = "x"
                else:
                    print("Please choose an empty spot")
                    x_turn = True
            elif x == "5":
                if five == "":
                    five = "x"
                else:
                    print("Please choose an empty spot")
                    x_turn = True
            elif x == "6":
                if six == "":
                    six = "x"
                else:
                    print("Please choose an empty spot")
                    x_turn = True
            elif x == "7":
                if seven == "":
                    seven = "x"
                else:
                    print("Please choose an empty spot")
                    x_turn = True
            elif x == "8":
                if eight == "":
                    eight = "x"
                else:
                    print("Please choose an empty spot")
                    x_turn = True
            elif x == "9":
                if nine == "":
                    nine = "x"
                else:
                    print("Please choose an empty spot")
                    x_turn = True


            if one == "x" and two == 'x' and three == "x":
                print("")
                print(f"""
[{one}][{two}][{three}]
[{four}][{five}][{six}]
[{seven}][{eight}][{nine}]
                        """)
                print("")
                print("X won")
                break
            elif four  == 'x' and five == 'x' and six == "x":
                print("")
                print(f"""
[{one}][{two}][{three}]
[{four}][{five}][{six}]
[{seven}][{eight}][{nine}]
                        """)
                print("")
                print("X won")
                break

            elif seven == 'x' and eight == 'x' and nine == "x":
                print("")
                print(f"""
[{one}][{two}][{three}]
[{four}][{five}][{six}]
[{seven}][{eight}][{nine}]
                                    """)
                print("")
                print("X won")
                break

            elif one == 'x' and four == 'x' and seven == "x":
                print("")
                print(f"""
[{one}][{two}][{three}]
[{four}][{five}][{six}]
[{seven}][{eight}][{nine}]
                                """)
                print("")
                print("X won")
                break

            elif two == 'x' and five == 'x' and eight == "x":
                print("")
                print(f"""
[{one}][{two}][{three}]
[{four}][{five}][{six}]
[{seven}][{eight}][{nine}]
                                    """)
                print("")
                print("X won")
                break

            elif three == 'x' and six == 'x' and nine == "x":
                print("")
                print(f"""
[{one}][{two}][{three}]
[{four}][{five}][{six}]
[{seven}][{eight}][{nine}]
                                    """)
                break

            elif one == 'x' and five == 'x' and nine == "x":
                print("")
                print(f"""
    [{one}][{two}][{three}]
    [{four}][{five}][{six}]
    [{seven}][{eight}][{nine}]
                               """)
                print("")
                print("X won")
                break
            elif three == 'x' and five == 'x' and seven == "x":
                print("")
                print(f"""
[{one}][{two}][{three}]
[{four}][{five}][{six}]
[{seven}][{eight}][{nine}]
                                    """)
                print("")
                print("X won")
                break

            if one == "" or two == "" or three == "" or four == "" or five == "" or six == "" or seven == "" or eight == "" or nine == "":
                o_turn = True
            else:
                print("Draw")
                break



        while o_turn == True:
            o_turn = False

            print(f"""
[{one}][{two}][{three}]
[{four}][{five}][{six}]
[{seven}][{eight}][{nine}]
                """)

            o = input("Where do you want to put your O? ")
            if o == "1":
                if one == "":
                    one = "o"
                else:
                    print("Please choose an empty spot")
                    o_turn = True
            elif o == "2":
                if two == "":
                    two = "o"
                else:
                    print("Please choose an empty spot")
                    o_turn = True
            elif o == "3":
                if three == "":
                    three = "o"
                else:
                    print("Please choose an empty spot")
                    o_turn = True
            elif o == "4":
                if four == "":
                    four = "o"
                else:
                    print("Please choose an empty spot")
                    o_turn = True
            elif o == "5":
                if five == "":
                    five = "o"
                else:
                    print("Please choose an empty spot")
                    o_turn = True
            elif o == "6":
                if six == "":
                    six = "o"
                else:
                    print("Please choose an empty spot")
                    o_turn = True
            elif o == "7":
                if seven == "":
                    seven = "o"
                else:
                    print("Please choose an empty spot")
                    o_turn = True
            elif o == "8":
                if eight == "":
                    eight = "o"
                else:
                    print("Please choose an empty spot")
                    o_turn = True
            elif o == "9":
                if nine == "":
                    nine = "o"
                else:
                    print("Please choose an empty spot")
                    o_turn = True


            if one == 'o' and two == 'o' and three == "o":
                print("")
                print(f"""
[{one}][{two}][{three}]
[{four}][{five}][{six}]
[{seven}][{eight}][{nine}]
                                    """)
                print("")
                print("O won")
                print("")
                play_again = input("Do you want to play again [Y/N]? ")
                print("")
                if play_again.lower() == "y" or play_again.lower() == "yes":
                    game_loop = True
                elif play_again.lower() == "n" or play_again.lower() == "no":
                    break
            elif four == 'o' and five == 'o' and six == "o":
                print("")
                print(f"""
[{one}][{two}][{three}]
[{four}][{five}][{six}]
[{seven}][{eight}][{nine}]
                                    """)
                print("")
                print("O won")
                print("")
                play_again = input("Do you want to play again [Y/N]? ")
                print("")
                if play_again.lower() == "y" or play_again.lower() == "yes":
                    game_loop = True
                elif play_again.lower() == "n" or play_again.lower() == "no":
                    break
            elif seven == 'o' and eight == 'o' and nine == "o":
                print("")
                print(f"""
[{one}][{two}][{three}]
[{four}][{five}][{six}]
[{seven}][{eight}][{nine}]
                                    """)
                print("")
                print("O won")
                print("")
                play_again = input("Do you want to play again [Y/N]? ")
                print("")
                if play_again.lower() == "y" or play_again.lower() == "yes":
                    game_loop = True
                elif play_again.lower() == "n" or play_again.lower() == "no":
                    break

            elif one == 'o' and four == 'o' and seven == "o":
                print("")
                print(f"""
[{one}][{two}][{three}]
[{four}][{five}][{six}]
[{seven}][{eight}][{nine}]
                                    """)
                print("")
                print("O won")
                print("")
                play_again = input("Do you want to play again [Y/N]? ")
                print("")
                if play_again.lower() == "y" or play_again.lower() == "yes":
                    game_loop = True
                elif play_again.lower() == "n" or play_again.lower() == "no":
                    break
            elif two == 'o' and five == 'o' and eight == "o":
                print("")
                print(f"""
[{one}][{two}][{three}]
[{four}][{five}][{six}]
[{seven}][{eight}][{nine}]
                                    """)
                print("")
                print("O won")
                print("")
                play_again = input("Do you want to play again [Y/N]? ")
                print("")
                if play_again.lower() == "y" or play_again.lower() == "yes":
                    game_loop = True
                elif play_again.lower() == "n" or play_again.lower() == "no":
                    break
            elif three == 'o' and six == 'o' and nine == "o":
                print("")
                print(f"""
[{one}][{two}][{three}]
[{four}][{five}][{six}]
[{seven}][{eight}][{nine}]
                                    """)
                print("")
                print("O won")
                print("")
                play_again = input("Do you want to play again [Y/N]? ")
                print("")
                if play_again.lower() == "y" or play_again.lower() == "yes":
                    game_loop = True
                elif play_again.lower() == "n" or play_again.lower() == "no":
                    break
            elif one == 'o' and five == 'o' and nine == "o":
                print("")
                print(f"""
[{one}][{two}][{three}]
[{four}][{five}][{six}]
[{seven}][{eight}][{nine}]
                                    """)
                print("")
                print("O won")
                print("")
                play_again = input("Do you want to play again [Y/N]? ")
                print("")
                if play_again.lower() == "y" or play_again.lower() == "yes":
                    game_loop = True
                elif play_again.lower() == "n" or play_again.lower() == "no":
                    break
            elif three == 'o' and five == 'o' and seven == "o":
                print("")
                print(f"""
[{one}][{two}][{three}]
[{four}][{five}][{six}]
[{seven}][{eight}][{nine}]
                                    """)
                print("")
                print("O won")
                print("")
                play_again = input("Do you want to play again [Y/N]? ")
                print("")
                if play_again.lower() == "y" or play_again.lower() == "yes":
                    game_loop = True
                elif play_again.lower() == "n" or play_again.lower() == "no":
                    break

            if one == "" or two == "" or three == "" or four == "" or five == "" or six == "" or seven == "" or eight == "" or nine == "":
                repeat = True
            else:
                print("")
                print("Draw")
                print("")
                play_again = input("Do you want to play again [Y/N]? ")
                print("")
                if play_again.lower() == "y" or play_again.lower() == "yes":
                    game_loop = True
                elif play_again.lower() == "n" or play_again.lower() == "no":
                    break
