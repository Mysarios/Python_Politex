All_Memory_volume = 1.44  # Mb
Count_pages = 100
String_per_page = 50
Count_Symbols = 25
Symbol_Memory = 4  # B

Bite_in_MB = 1048576

Memory_per_book = Count_pages * String_per_page * Count_Symbols * Symbol_Memory

print("Memory per book = ", Memory_per_book)
print("Bites in all memory = ", All_Memory_volume * Bite_in_MB)

Books_in_FloppyDisk = (All_Memory_volume * Bite_in_MB) // Memory_per_book

print("Count books = = ", Books_in_FloppyDisk)
