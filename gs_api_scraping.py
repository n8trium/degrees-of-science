from scholarly import scholarly

# Search for an author by name
search_query = scholarly.search_author('Albert Einstein')
author = next(search_query)  # Get the first result

# Print author details
print(f"Author Name: {author['name']}")
print(f"Affiliation: {author['affiliation']}")
print(f"Number of Citations: {author['citedby']}")
print(f"Publications: {author['publications']}")

# To get more details about a specific publication
publication = scholarly.fill(author['publications'][0])  # Get the first publication
print(f"Title: {publication['bib']['title']}")
