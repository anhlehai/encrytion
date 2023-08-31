#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 12:42:28 2022

@author: haiph
"""

def read_file(file_name):
    """
    

    Parameters
    ----------
    file_name : string
        name of a file, should be put in quotation marks

    Returns
    -------
    byte_list : list
        a list with decimal numbers as elements after the file has been read in binary mode

    """
    file = open(file_name,'rb')     #file is onpened in binary mode
    file_content = file.read()
    byte_list = []
    for i in file_content:
        byte_list = byte_list + [((i))]     #create a list of bytes
    file.close()
    return byte_list

def write_file(file_name,content):
    """
    

    Parameters
    ----------
    file_name : string
        name of file, should be put in quotation marks
    content : list
        result from encrypt function can be used
    e.g: write_file('file_name',[14,72,71]) or write_file('file_name',encrypt('file','key')

    Returns
    -------
    None. This function is for writing file.

    """
    file = open(file_name,'wb')     #write the file in binary mode
    file.write((bytes(content)))
    file.close()
    return

def encrypt(plain_text,key):
    """
    

    Parameters
    ----------
    plain_text : string
        name of file, should be put in quotation marks
    key : string
        name of file, should be put in quotation marks

    Returns
    -------
    list_plain : list
        a list with decimal numbers as elements
        
    """
    list_key = read_file(key)
    list_plain = read_file(plain_text)
    for i in range(len(list_plain)):
        list_plain[i] = list_key[list_plain[i]]     #permute the bytes of the plain text by using the value of member in plain_text as the position of member in file key
    return list_plain

def decrypt(cipher_text,key):
    """
    

    Parameters
    ----------
    cipher_text : string
        name of a file, should be put in quotation marks
    key : string
        name of a file, should be put in quotation marks

    Returns
    -------
    list_cipher : list
        a list with decimal numbers as elements

    """
    list_key = read_file(key)
    list_cipher = read_file(cipher_text)
    for i in range(len(list_cipher)):
        for j in range(len(list_key)):
            if list_cipher[i] == list_key[j]:   #reverse the encyption by using the position of member in file key as value for member in decrypted file
                list_cipher[i] = j
                break
    return list_cipher

def test_encryption():
    encrypted = encrypt('plain_text','key')
    write_file('cipher_text',encrypted)
    decrypted = decrypt('cipher_text','key')
    write_file('plain_text1',decrypted)
    return (read_file('plain_text') == read_file('plain_text1'))




