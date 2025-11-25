import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_book_data():
    """
    Generate realistic book recommendation dataset with:
    - 100 books across multiple genres
    - 500 users with varying preferences
    - 6,299 ratings with 87.4% sparsity
    """
    
    # Set random seeds for reproducibility
    np.random.seed(42)
    random.seed(42)
    
    # Define book genres and their characteristics
    genres = {
        'Fiction': {'avg_pages': 320, 'popularity_weight': 1.2},
        'Mystery': {'avg_pages': 280, 'popularity_weight': 1.1},
        'Romance': {'avg_pages': 350, 'popularity_weight': 1.3},
        'Horror': {'avg_pages': 300, 'popularity_weight': 1.2},
        'Comedy': {'avg_pages': 280, 'popularity_weight': 1.3},
        'Science Fiction': {'avg_pages': 380, 'popularity_weight': 1.0},
        'Fantasy': {'avg_pages': 420, 'popularity_weight': 1.1},
        'Biography': {'avg_pages': 290, 'popularity_weight': 0.9},
        'History': {'avg_pages': 340, 'popularity_weight': 0.8},
        'Self-Help': {'avg_pages': 250, 'popularity_weight': 1.0},
        'Business': {'avg_pages': 260, 'popularity_weight': 0.9},
        'Technology': {'avg_pages': 300, 'popularity_weight': 0.8}
    }
    
    # Author names for realistic data
    authors = [
        'Sarah Johnson', 'Michael Chen', 'Emily Rodriguez', 'David Williams', 'Lisa Thompson',
        'James Miller', 'Maria Garcia', 'Robert Davis', 'Jennifer Brown', 'Christopher Wilson',
        'Amanda Taylor', 'Daniel Moore', 'Jessica Anderson', 'Matthew Thomas', 'Ashley Jackson',
        'Joshua White', 'Nicole Harris', 'Andrew Martin', 'Stephanie Lewis', 'Kevin Clark',
        'Rachel Green', 'Ryan Hall', 'Laura Allen', 'Brandon Young', 'Megan King',
        'Jonathan Wright', 'Samantha Lopez', 'Nicholas Hill', 'Brittany Scott', 'Tyler Adams',
        'Kayla Baker', 'Austin Gonzalez', 'Alexis Nelson', 'Cameron Carter', 'Hannah Mitchell',
        'Jordan Perez', 'Taylor Roberts', 'Morgan Turner', 'Sydney Phillips', 'Destiny Campbell',
        'Cody Parker', 'Sierra Evans', 'Bryce Edwards', 'Jasmine Collins', 'Devin Stewart',
        'Maya Sanchez', 'Tristan Morris', 'Paige Rogers', 'Garrett Reed', 'Mariah Cook'
    ]
    
    # Generate book titles by genre
    title_templates = {
        'Fiction': [
            'The Last {noun}', 'Beneath the {adjective} Sky', 'When {noun} Falls',
            'The {adjective} Truth', 'Beyond the {noun}', 'The Weight of {noun}',
            'Echoes of {noun}', 'The Forgotten {noun}', 'Dancing with {noun}',
            'The Color of {noun}'
        ],
        'Mystery': [
            'The {adjective} Detective', 'Murder in {place}', 'The Case of the {adjective} {noun}',
            'Death at {place}', 'The {noun} Conspiracy', 'Blood on {place}',
            'The {adjective} Witness', 'Secrets of {place}', 'The {noun} Files',
            'Shadow of {noun}'
        ],
        'Romance': [
            'Love in {place}', 'The {adjective} Heart', 'Passion at {place}',
            'My {adjective} Love', 'Hearts in {place}', 'The {noun} of Love',
            'Romance at {place}', 'The {adjective} Kiss', 'Love Beyond {noun}',
            'Forever in {place}'
        ],
        'Horror': [
            'The {adjective} Nightmare', 'Curse of {place}', 'The {noun} Haunting',
            'Terror at {place}', 'The {adjective} Shadow', 'Whispers of {noun}',
            'The {noun} Possession', 'Darkness in {place}', 'The {adjective} Fear',
            'Screams from {place}'
        ],
        'Comedy': [
            'The {adjective} Misadventure', 'Chaos in {place}', 'The {noun} Fiasco',
            'Laughing at {place}', 'The {adjective} Mishap', 'Jokes About {noun}',
            'Fun in {place}', 'The {adjective} Blunder', 'Comedy of {noun}',
            'Giggles from {place}'
        ],
        'Science Fiction': [
            'The {adjective} Galaxy', 'Beyond the {noun}', 'The {noun} Wars',
            'Journey to {place}', 'The {adjective} Planet', 'Stars of {noun}',
            'The {noun} Protocol', 'Empire of {noun}', 'The {adjective} Future',
            'Quantum {noun}'
        ],
        'Fantasy': [
            'The {adjective} Kingdom', 'Realm of {noun}', 'The {noun} Chronicles',
            'Magic of {place}', 'The {adjective} Dragon', 'Quest for {noun}',
            'The {noun} Prophecy', 'Legends of {place}', 'The {adjective} Sword',
            'Tales of {noun}'
        ],
        'Biography': [
            'The Life of {person}', '{person}: A Journey', 'My Story: {person}',
            'The {adjective} Life of {person}', '{person} Revealed', 'Inside {person}',
            'The {person} Chronicles', '{person}: The Truth', 'Becoming {person}',
            'The {adjective} {person}'
        ],
        'History': [
            'The {adjective} War', 'Rise of {place}', 'The Fall of {place}',
            'Secrets of {place}', 'The {noun} Era', 'Empire of {place}',
            'The {adjective} Revolution', 'Chronicles of {place}', 'The {noun} Age',
            'Legacy of {place}'
        ],
        'Self-Help': [
            'The {adjective} Mind', 'How to {verb} Your {noun}', 'The Art of {noun}',
            'Mastering {noun}', 'The {noun} Code', 'Unlock Your {noun}',
            'The {adjective} Way', 'Transform Your {noun}', 'The Power of {noun}',
            'Building {adjective} {noun}'
        ],
        'Business': [
            'The {adjective} Leader', 'Strategies for {noun}', 'The Art of {noun}',
            'Building {adjective} {noun}', 'The {noun} Advantage', 'Mastering {noun}',
            'The {adjective} Executive', 'Success Through {noun}', 'The {noun} Method',
            'Leading with {noun}'
        ],
        'Technology': [
            'The {adjective} Algorithm', 'Mastering {noun}', 'The Art of {noun}',
            'Programming {noun}', 'The {noun} Revolution', 'Understanding {noun}',
            'The {adjective} Code', 'Digital {noun}', 'The Future of {noun}',
            'Advanced {noun}'
        ]
    }
    
    # Word lists for title generation
    nouns = ['Dream', 'Shadow', 'Light', 'Storm', 'Fire', 'Moon', 'Star', 'Ocean', 'Mountain', 'River']
    adjectives = ['Silent', 'Golden', 'Dark', 'Bright', 'Hidden', 'Lost', 'Ancient', 'Modern', 'Wild', 'Gentle']
    places = ['Paris', 'London', 'Tokyo', 'New York', 'Rome', 'Cairo', 'Sydney', 'Berlin', 'Madrid', 'Moscow']
    people = ['Churchill', 'Einstein', 'Gandhi', 'Mozart', 'Tesla', 'da Vinci', 'Curie', 'Jobs', 'Mandela', 'Lincoln']
    verbs = ['Transform', 'Master', 'Improve', 'Build', 'Create', 'Develop', 'Enhance', 'Optimize', 'Achieve', 'Unlock']
    
    # Generate 100 books
    books_data = []
    for book_id in range(1, 101):
        genre = random.choice(list(genres.keys()))
        author = random.choice(authors)
        
        # Generate title
        template = random.choice(title_templates[genre])
        title = template.format(
            noun=random.choice(nouns),
            adjective=random.choice(adjectives),
            place=random.choice(places),
            person=random.choice(people),
            verb=random.choice(verbs)
        )
        
        # Generate other attributes
        base_pages = genres[genre]['avg_pages']
        pages = int(np.random.normal(base_pages, 50))
        pages = max(150, min(600, pages))  # Reasonable bounds
        
        publication_year = random.randint(1990, 2024)
        
        books_data.append({
            'book_id': book_id,
            'title': title,
            'author': author,
            'genre': genre,
            'publication_year': publication_year,
            'pages': pages
        })
    
    books_df = pd.DataFrame(books_data)
    
    # Generate 500 users with preferences
    users_data = []
    for user_id in range(1, 501):
        # Assign user preferences (favorite genres)
        num_preferred_genres = random.choices([1, 2, 3], weights=[0.4, 0.4, 0.2])[0]
        preferred_genres = random.sample(list(genres.keys()), num_preferred_genres)
        
        # User reading activity level
        activity_level = random.choices(['low', 'medium', 'high'], weights=[0.3, 0.5, 0.2])[0]
        
        users_data.append({
            'user_id': user_id,
            'preferred_genres': ','.join(preferred_genres),
            'activity_level': activity_level
        })
    
    users_df = pd.DataFrame(users_data)
    
    # Generate ratings with realistic patterns
    ratings_data = []
    target_ratings = 6299  # Target number of ratings for 87.4% sparsity
    
    # Calculate sparsity: (1 - ratings / (users * books)) * 100
    # 87.4% sparsity means 12.6% of user-book combinations have ratings
    # With 500 users and 100 books = 50,000 possible combinations
    # 12.6% of 50,000 = 6,300 ratings (close to our target)
    
    for user_id in range(1, 501):
        user_info = users_df[users_df['user_id'] == user_id].iloc[0]
        preferred_genres = user_info['preferred_genres'].split(',')
        activity_level = user_info['activity_level']
        
        # Determine number of ratings based on activity level
        if activity_level == 'low':
            num_ratings = random.randint(5, 15)
        elif activity_level == 'medium':
            num_ratings = random.randint(10, 25)
        else:  # high
            num_ratings = random.randint(20, 40)
        
        # Stop if we've reached target ratings
        if len(ratings_data) >= target_ratings:
            break
            
        # Limit ratings to avoid exceeding target
        remaining_ratings = target_ratings - len(ratings_data)
        num_ratings = min(num_ratings, remaining_ratings)
        
        # Select books to rate (bias towards preferred genres)
        available_books = books_df.copy()
        
        # Increase probability for preferred genres
        genre_weights = []
        for _, book in available_books.iterrows():
            if book['genre'] in preferred_genres:
                weight = 3.0  # 3x more likely to rate preferred genres
            else:
                weight = 1.0
            genre_weights.append(weight)
        
        # Sample books to rate
        if num_ratings > 0 and len(available_books) > 0:
            num_ratings = min(num_ratings, len(available_books))
            rated_books = np.random.choice(
                available_books.index,
                size=num_ratings,
                replace=False,
                p=np.array(genre_weights) / sum(genre_weights)
            )
            
            for book_idx in rated_books:
                book = available_books.iloc[book_idx]
                
                # Generate rating based on genre preference
                if book['genre'] in preferred_genres:
                    # Higher ratings for preferred genres
                    rating = np.random.choice([3, 4, 5], p=[0.2, 0.4, 0.4])
                else:
                    # More varied ratings for non-preferred genres
                    rating = np.random.choice([1, 2, 3, 4, 5], p=[0.1, 0.2, 0.4, 0.2, 0.1])
                
                # Add some noise to make ratings more realistic
                rating = rating + np.random.normal(0, 0.3)
                rating = max(1.0, min(5.0, rating))  # Clamp to valid range
                
                ratings_data.append({
                    'user_id': user_id,
                    'book_id': book['book_id'],
                    'rating': round(rating, 1)
                })
    
    ratings_df = pd.DataFrame(ratings_data)
    
    # Ensure we have exactly the target number of ratings
    if len(ratings_df) > target_ratings:
        ratings_df = ratings_df.sample(n=target_ratings, random_state=42).reset_index(drop=True)
    
    # Verify sparsity
    actual_sparsity = (1 - len(ratings_df) / (len(users_df) * len(books_df))) * 100
    print(f"Generated dataset with {actual_sparsity:.1f}% sparsity")
    print(f"Books: {len(books_df)}, Users: {len(users_df)}, Ratings: {len(ratings_df)}")
    
    return books_df, users_df, ratings_df

def generate_evaluation_data():
    """Generate additional data for system evaluation"""
    # This could include test sets, validation data, etc.
    # For now, we'll return the main dataset
    return generate_book_data()

if __name__ == "__main__":
    # Test data generation
    books, users, ratings = generate_book_data()
    print("Data generation completed successfully!")
    print(f"Generated {len(books)} books, {len(users)} users, and {len(ratings)} ratings")
