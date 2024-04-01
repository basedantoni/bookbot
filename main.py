def sort_on(dict):
    return dict["count"]

def get_word_count(text):
  return len(text.split())

def get_letter_count(text):
  letters = {}

  for char in text.lower():
    if not char.isalpha():
      continue

    if char in letters:
      letters[char] += 1
    else:
      letters[char] = 1

  return letters

def main():
  with open("./books/frankenstein.txt") as f:
    file_contents = f.read()

    word_count = get_word_count(file_contents)
    letter_counts = get_letter_count(file_contents)

    letter_counts_list = []
    for letter in letter_counts:
      letter_counts_list.append({"letter": letter, "count": letter_counts[letter]})

    letter_counts_list.sort(reverse=True, key=sort_on)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")
    for letter in letter_counts_list:
      print(f"The '{letter["letter"]}' was found {letter["count"]} times")
    print("--- End report ---")

main()
