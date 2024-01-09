def check_search_term(word, search_term):
    if search_term in word:
        print(f"Search term '{search_term}' do appear in word '{word}'")
    else:
        print(f"Search term '{search_term}' doesn't appears in word '{word}'")

def main():
    word = input("Insert word: ")
    search_term = input("Insert search term: ")
    check_search_term(word, search_term)

if __name__ == "__main__":
    main()          



#     Insert word: apple
# Insert search term: a
# Search term 'a' do appear in word 'apple'
# Program run - 2:

# Insert word: banana
# Insert search term: c
# Search term 'c' doesn't appears in word 'banana'