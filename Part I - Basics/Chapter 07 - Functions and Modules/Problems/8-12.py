def sandwich_summary(*ingredients):
    """Summarise the sandwich that is being made."""
    print("\nYou want to make a sandwich with the following ingredient(s):")

    for ingredient in ingredients:
        print("- " + ingredient.title())

    print("Your sandwich is ready.")


sandwich_summary('cheese')
sandwich_summary('pastrami', 'caramelised onions', 'pepper')
sandwich_summary('bacon', 'lettuce', 'tomatoes', 'jalapenos', 'mushrooms')
