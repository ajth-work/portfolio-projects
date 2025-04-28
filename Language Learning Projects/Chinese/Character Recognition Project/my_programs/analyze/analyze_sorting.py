""" Direct the user towards data entry for new content or streamlined access to previously categorized content
    entry_type = input("""
        1. New Source (starting a new collection)\n
        2. Old Source (adding to a previous collection)\n
        """)
    if entry_type == 1:
        source_type = input("""
        What type of source?
        1. Book
        2. Internet
        3. User
        """)
        if source_type == 1:
            source_title = input("Enter the name of book: ")
        elif source_type == 2:
            source_link = input("Enter the link from the internet: ")
        elif source_type == 3:
            source_note = input("Enter note from user: ")

    elif entry_type == 2:
        # make a call to the existing source types section of the database
        #list what source types there are currently
        # for source_type in source_types, print source_type
        # source in source_type, print source

        # Define the major data points for the query
        source_id = ""  # database-defined

    source_link = input("Enter source link if from internet: ")
    source_count = ""  # Intially 0 by default, but if old source, then database-defined, ask databse how many times this source has been added to,
    source_method = input(
        "Enter source method: "
    )  #user-defined, list 1) Copied from OCR, 2) Copied from Internet, 3) Typed
    original_query = input("Enter original query: ")
    query_count = input("Enter query count: ")

    # Split the imported text into individual sentences using [ 。！？] as delimiters
    # Exclude delimiters that are within quotation marks
    sentences = re.split(r'(?<=[。！？])\s*(?![”])', text)
    # Filter out empty sentences
    sentences = [sentence for sentence in sentences if sentence.strip()]

    # Display the list of sentences before analysis
    print(f"{len(sentences)} sentences discovered:\n")
    for i, sentence in enumerate(sentences, start=1):
        print(f"{i}. {sentence.strip()}\n")
    """