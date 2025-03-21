import os
import sys
from time import sleep

binary_codes = {
        ' ':  "00100000", '!':  "00100001", '"':  "00100010", '#':  "00100011",
        '$':  "00100100", '%':  "00100101", '&':  "00100110", "'":  "00100111",
        '(':  "00101000", ')':  "00101001", '*':  "00101010", '+':  "00101011",
        ',':  "00101100", '-':  "00101101", '.':  "00101110", '/':  "00101111",
        '0':  "00110000", '1':  "00110001", '2':  "00110010", '3':  "00110011",
        '4':  "00110100", '5':  "00110101", '6':  "00110110", '7':  "00110111",
        '8':  "00111000", '9':  "00111001", ':':  "00111010", ';':  "00111011",
        '<':  "00111100", '=':  "00111101", '>':  "00111110", '?':  "00111111",
        '@':  "01000000", 'A':  "01000001", 'B':  "01000010", 'C':  "01000011",
        'D':  "01000100", 'E':  "01000101", 'F':  "01000110", 'G':  "01000111",
        'H':  "01001000", 'I':  "01001001", 'J':  "01001010", 'K':  "01001011",
        'L':  "01001100", 'M':  "01001101", 'N':  "01001110", 'O':  "01001111",
        'P':  "01010000", 'Q':  "01010001", 'R':  "01010010", 'S':  "01010011",
        'T':  "01010100", 'U':  "01010101", 'V':  "01010110", 'W':  "01010111",
        'X':  "01011000", 'Y':  "01011001", 'Z':  "01011010", '[':  "01011011",
        '\\': "01011100", ']':  "01011101", '^':  "01011110", '_':  "01011111",
        '`':  "01100000", 'a':  "01100001", 'b':  "01100010", 'c':  "01100011",
        'd':  "01100100", 'e':  "01100101", 'f':  "01100110", 'g':  "01100111",
        'h':  "01101000", 'i':  "01101001", 'j':  "01101010", 'k':  "01101011",
        'l':  "01101100", 'm':  "01101101", 'n':  "01101110", 'o':  "01101111",
        'p':  "01110000", 'q':  "01110001", 'r':  "01110010", 's':  "01110011",
        't':  "01110100", 'u':  "01110101", 'v':  "01110110", 'w':  "01110111",
        'x':  "01111000", 'y':  "01111001", 'z':  "01111010", '{':  "01111011",
        '|':  "01111100", '}':  "01111101", '~':  "01111110", 
}

def show_title():
    for i in range(3):
        clear_terminal()
        print("""
        ########################
        #        BINARY        # 
        #    ENCODER/DECODER   #
        ########################
              
        """)
        sleep(0.5)
        clear_terminal()
        print("""
        ========================
        =        BINARY        = 
        =    ENCODER/DECODER   =
        ========================
              
        """)
        sleep(0.5)

def clear_terminal():
    clear_command = "cls" if sys.platform == "win32" else "clear"
    os.system(clear_command)

def text_to_binary(text):
    encoded_binary = ""
    for letter in text:
        for key in binary_codes.keys():
            if letter == key:
                value = f"{binary_codes[key]} "
                encoded_binary+=value
    return encoded_binary

def binary_to_text(binary):
    decoded_text = ""
    for word in binary.split():
        for key in binary_codes.keys():
            if word == binary_codes[key]:
                decoded_text+=key
    return decoded_text

if __name__ == "__main__":
    show_title()
    method = int(input("1. Encode a given text\n2. Decode a given binary code\nType the number of the option that you want:"))
    clear_terminal()
    match method:
        case 1:
            text = input("Type the text that you want to encode: ")
            result = text_to_binary(text)
            clear_terminal()
            print(f"Given text:\n{text}\n")
            print(f"Encoded text:\n{result}\n")

        case 2:
            binary = input("Type the binary code that you want to decode: ")
            result = binary_to_text(binary)
            clear_terminal()
            print(f"Given binary:\n{binary}\n")
            print(f"Encoded text:\n{result}\n")




